from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from bot.config_reader import config


async def set_bot_commands(bot: Bot):
    admin_commands = [
        BotCommand(command="who", description="Получение информации о пользователе"),
        BotCommand(command="ban", description="Заблокировать пользователя"),
        BotCommand(command="shadowban", description="Скрытно заблокировать пользователя"),
        BotCommand(command="unban", description="Разблокировать пользователя"),
        BotCommand(command="list_banned", description="Список заблокированных"),
    ]
    await bot.set_my_commands(
        admin_commands,
        scope=BotCommandScopeChat(chat_id=config.admin_chat_id)
    )
