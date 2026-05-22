"""Helpers for fetching and polling messages from a Telegram chat."""

from __future__ import annotations

import asyncio
import logging
import time

import telegram

# Suppress noisy logs from telegram/httpx internals.
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Token for the bot.
token: str | None = None

# Chat identifier used as fallback.
chat_id: int | str | None = None


async def _fetch_messages(
    *,
    target_chat_id: int | str,
    bot_token: str,
    offset: int | None = None,
    limit: int = 100,
    request_timeout: int = 10,
    allowed_updates: list[str] | tuple[str, ...] | None = ("message",),
) -> tuple[list[telegram.Message], int | None]:
    """
    Fetch messages for a specific chat from Telegram updates.

    Args:
        target_chat_id: Chat ID whose messages should be returned.
        bot_token: Telegram bot token.
        offset: First update ID to return. Use the returned `next_offset`
            in subsequent calls to avoid re-reading old updates.
        limit: Maximum number of updates to request in one call.
        request_timeout: Long-poll timeout (seconds) used by `get_updates`.
        allowed_updates: Update types requested from Telegram.

    Returns:
        A tuple of `(messages, next_offset)` where:
        - `messages` contains messages belonging to `target_chat_id`.
        - `next_offset` should be reused in the next call.

    Raises:
        ValueError: If `bot_token` is empty.
    """
    if not bot_token:
        raise ValueError("A valid bot_token is required.")

    updates: list[telegram.Update] | tuple[telegram.Update, ...]
    bot = telegram.Bot(token=bot_token)
    async with bot:
        updates = await bot.get_updates(
            offset=offset,
            limit=limit,
            timeout=request_timeout,
            allowed_updates=list(allowed_updates) if allowed_updates is not None else None,
        )

    messages: list[telegram.Message] = []
    next_offset = offset
    target_chat_id_str = str(target_chat_id)

    for update in updates:
        next_offset = update.update_id + 1
        message = update.effective_message
        if message is None or message.chat is None:
            continue
        if str(message.chat.id) == target_chat_id_str:
            messages.append(message)

    return messages, next_offset


async def _fetch_answer_with_retry(
    *,
    target_chat_id: int | str,
    bot_token: str,
    offset: int | None = None,
    timeout_seconds: float | None = None,
    poll_interval_seconds: float = 2.0,
    limit: int = 100,
    request_timeout: int = 10,
    allowed_updates: list[str] | tuple[str, ...] | None = ("message",),
) -> telegram.Message | None:
    """
    Poll Telegram until at least one message is found or timeout is reached.

    Args:
        target_chat_id: Chat ID to monitor for incoming messages.
        bot_token: Telegram bot token.
        offset: First update ID to request.
        timeout_seconds: Maximum total wait time. If `None`, polling does not
            time out.
        poll_interval_seconds: Sleep time between poll attempts.
        limit: Maximum number of updates to request in one call.
        request_timeout: Long-poll timeout (seconds) used by `get_updates`.
        allowed_updates: Update types requested from Telegram.

    Returns:
        The most recent message from the target chat, or `None` when timeout
        expires before any message is received.
    """
    if poll_interval_seconds <= 0:
        raise ValueError("poll_interval_seconds must be > 0.")

    start_time = time.monotonic()
    next_offset = offset

    while True:
        messages, next_offset = await _fetch_messages(
            target_chat_id=target_chat_id,
            bot_token=bot_token,
            offset=next_offset,
            limit=limit,
            request_timeout=request_timeout,
            allowed_updates=allowed_updates,
        )
        if messages:
            return messages[-1]

        if timeout_seconds is not None:
            elapsed = time.monotonic() - start_time
            if elapsed >= timeout_seconds:
                return None

        await asyncio.sleep(poll_interval_seconds)


def fetch_messages(
    *,
    target_chat_id: int | str | None = chat_id,
    bot_token: str | None = token,
    offset: int | None = None,
    limit: int = 100,
    request_timeout: int = 10,
    allowed_updates: list[str] | tuple[str, ...] | None = ("message",),
) -> tuple[list[telegram.Message], int | None]:
    """
    Synchronous wrapper for fetching messages from a Telegram chat.

    Args:
        target_chat_id: Chat ID whose messages should be returned.
        bot_token: Telegram bot token.
        offset: First update ID to return.
        limit: Maximum number of updates to request in one call.
        request_timeout: Long-poll timeout (seconds) used by `get_updates`.
        allowed_updates: Update types requested from Telegram.

    Returns:
        A tuple `(messages, next_offset)`.

    Raises:
        ValueError: If `target_chat_id` or `bot_token` is missing.
    """
    if target_chat_id is None:
        raise ValueError("A target_chat_id is required.")
    if bot_token is None:
        raise ValueError("A bot_token is required.")

    return asyncio.run(
        _fetch_messages(
            target_chat_id=target_chat_id,
            bot_token=bot_token,
            offset=offset,
            limit=limit,
            request_timeout=request_timeout,
            allowed_updates=allowed_updates,
        )
    )


def fetch_answer_with_retry(
    *,
    target_chat_id: int | str | None = chat_id,
    bot_token: str | None = token,
    offset: int | None = None,
    timeout_seconds: float | None = None,
    poll_interval_seconds: float = 2.0,
    limit: int = 100,
    request_timeout: int = 10,
    allowed_updates: list[str] | tuple[str, ...] | None = ("message",),
) -> telegram.Message | None:
    """
    Synchronous wrapper that retries until a chat answer arrives or times out.

    Args:
        target_chat_id: Chat ID to monitor for incoming messages.
        bot_token: Telegram bot token.
        offset: First update ID to request.
        timeout_seconds: Maximum total wait time. If `None`, polling does not
            time out.
        poll_interval_seconds: Sleep time between poll attempts.
        limit: Maximum number of updates to request in one call.
        request_timeout: Long-poll timeout (seconds) used by `get_updates`.
        allowed_updates: Update types requested from Telegram.

    Returns:
        The most recent message from the target chat, or `None` if timeout is
        reached before any message is received.

    Raises:
        ValueError: If `target_chat_id` or `bot_token` is missing.
    """
    if target_chat_id is None:
        raise ValueError("A target_chat_id is required.")
    if bot_token is None:
        raise ValueError("A bot_token is required.")

    return asyncio.run(
        _fetch_answer_with_retry(
            target_chat_id=target_chat_id,
            bot_token=bot_token,
            offset=offset,
            timeout_seconds=timeout_seconds,
            poll_interval_seconds=poll_interval_seconds,
            limit=limit,
            request_timeout=request_timeout,
            allowed_updates=allowed_updates,
        )
    )
