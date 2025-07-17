from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Главное меню
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📌 Приватный канал", callback_data='private'),
            InlineKeyboardButton("💼 Услуги", callback_data='services'),
        ],
        [
            InlineKeyboardButton("💳 Реквизиты", callback_data='payment'),
        ]
    ])

# Кнопка назад
def back_button_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Назад в меню", callback_data='menu')]
    ])

# /start (без фото)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Добро пожаловать!\n\nЧто тебя интересует?",
        reply_markup=main_menu_keyboard()
    )

# обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # если нажал "Назад в меню", просто отправляем новое сообщение
    if query.data == 'menu':
        await update.effective_chat.send_message(
            text="👋 Привет! Добро пожаловать обратно в меню!\n\nЧто тебя интересует?",
            reply_markup=main_menu_keyboard()
        )
        await query.delete_message()

    elif query.data == 'private':
        message = (
            "📌 *Нужна информация про приватку?*\n\n"
            "💰 *Стоимость доступа: 20$ (доступ навсегда)*\n"
            "🇰🇬 Кыргызстан — 1700 сом\n"
            "🇰🇿 Казахстан — 10 000 тенге\n\n"
            "🇺🇿 Узбекистан — 250 000 сум\n"
            "🇷🇺 Россия — 1 800 рублей\n\n"
            "Зайди на мой профиль в Instagram:\n"
            "[кликни](https://www.instagram.com/nolfinil/)\n"
            "и кликни по *Актуальному* 🔥\n\n"
            "*Приватка по зарубежному YouTube* — это:\n\n"
            "🎓 *Обучение по нишам и YouTube:*\n"
            "— Мини-курсы и видеоуроки\n"
            "— Разбор прибыльных ниш\n"
            "— Полезные фишки и стратегии\n"
            "— Бесплатные созвоны со мной\n\n"
            "📦 *+ внутри есть курс по YouTube с нуля*"
        )
        await query.delete_message()
        await update.effective_chat.send_photo(
            photo=open("telegram_bot/5454203047233319344.jpg", "rb"),
            
            caption=message,
            parse_mode="Markdown",
            reply_markup=back_button_keyboard()
        )

    elif query.data == 'services':
        message = (
            "🚀 *МОИ УСЛУГИ — ДЛЯ ТЕХ, КТО ХОЧЕТ ЗАПУСТИТЬСЯ И ЗАРАБАТЫВАТЬ НА YOUTUBE*\n\n"

            "📦 *Приватный Telegram-канал* — $20 (доступ навсегда)\n"
            "— Готовые мини-курсы по зарубежному YouTube\n"
            "— Подбор прибыльных ниш и стратегии роста\n"
            "— Только рабочие фишки без воды\n"
            "— Созвоны и поддержка внутри сообщества\n\n"

            "🧠 *Индивидуальная консультация* — $20/час\n"
            "_Если у тебя уже есть канал или идеи._\n"
            "— Разбор твоего канала и ошибок\n"
            "— Выбор ниши под твои сильные стороны\n"
            "— Чёткая стратегия продвижения\n"
            "— Ответы на все твои вопросы\n\n"

            "🎯 *Наставничество* — $200/месяц\n"
            "_Если хочешь с нуля дойти до монетизации._\n"
            "— Помощь с нишей, контентом, оформлением\n"
            "— Поддержка на каждом этапе\n"
            "— Полный контроль и разбор результатов\n"
            "— Вместе доведём до цели"
        )
        await query.edit_message_text(
            message,
            parse_mode="Markdown",
            reply_markup=back_button_keyboard()
        )

    elif query.data == 'payment':
        message = (
            "💳 *Реквизиты для перевода:*\n\n"
            "⬇️ *Kaspi банк:*\n"
            "4400430296140327\n"
            "ILYA NOLFIN\n\n"
            "⬇️ *Альтернатива карта:*\n"
            "4405639843389055\n"
            "ILYA NOLFIN\n\n"
            "⬇️ *Криптокошелёк (USDT, TRC20):*\n"
            "THcXbiQF28w6dctrFwJKfvHG2vAgV1CFQz\n\n"
            "⬇️ *Если ничего не подошло:*\n"
            "[Оплатить через Telegram](https://t.me/tribute/app?startapp=sxvQ)\n\n"
            "⚠️ *После оплаты нажми кнопку ниже, чтобы скинуть чек об оплате в личку* 💬"
        )

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("📤 Скинуть чек об оплате", url="https://t.me/nolfinil")],
            [InlineKeyboardButton("🔙 Назад в меню", callback_data='menu')]
        ])

        await query.edit_message_text(
            message,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=buttons
        )


# запуск
if __name__ == '__main__':
    TOKEN = '7753398742:AAFaN-kDseix7hgQ_SnI9JUfRZAHxBSAbMQ'

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Бот запущен")
    app.run_polling()
