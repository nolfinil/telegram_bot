from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    constants,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ──────────────────────────────
# Клавиатуры
# ──────────────────────────────
def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💸 КУПИТЬ ДОСТУП В ПРИВАТКУ", callback_data="buy")],
            [InlineKeyboardButton("📦 ЧТО ВНУТРИ ПРИВАТКИ?", callback_data="inside")],
            [InlineKeyboardButton("💼 НАСТАВНИЧЕСТВО И КОНСУЛЬТАЦИИ", callback_data="services")],
            [InlineKeyboardButton("❓ ЗАДАТЬ ВОПРОС ИЛЬЕ", url="https://t.me/nolfinil")],
        ]
    )


def buy_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ ОПЛАТИТЬ ВХОД", callback_data="payment")],
            [InlineKeyboardButton("🔙 Назад", callback_data="menu")],
        ]
    )


def inside_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ ОПЛАТИТЬ ВХОД", callback_data="payment")],
            [InlineKeyboardButton("🔙 Назад", callback_data="menu")],
        ]
    )


def services_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ ОПЛАТА", callback_data="payment")],
            [InlineKeyboardButton("❓ ЗАДАТЬ ВОПРОС", url="https://t.me/nolfinil")],
            [InlineKeyboardButton("🔙 Назад", callback_data="menu")],
        ]
    )


def payment_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📤 Скинуть чек об оплате", url="https://t.me/nolfinil")],
            [InlineKeyboardButton("🔙 Назад", callback_data="menu")],
        ]
    )


# ──────────────────────────────
# Хэндлеры
# ──────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption = (
        "👋 Привет! Добро пожаловать!\n\n"
        "Выбери, что тебя интересует ниже:"
    )
    with open("avavava.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=caption,
            parse_mode=constants.ParseMode.MARKDOWN,
            reply_markup=main_menu_keyboard(),
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # 1) Главное меню
    if query.data == "menu":
        await query.delete_message()
        caption = (
            "👋 Готов помочь снова!\n\n"
            "Что вас интересует?"
        )
        with open("avavava.jpg", "rb") as photo:
            await query.message.chat.send_photo(
                photo=photo,
                caption=caption,
                parse_mode=constants.ParseMode.MARKDOWN,
                reply_markup=main_menu_keyboard(),
            )

    # 2) Стоимость приватки
    elif query.data == "buy":
        text = (
            "💸 *Стоимость доступа (навсегда):*\n\n"
            "🇺🇸 20 USD\n"
            "🇰🇿 10 000 ₸\n"
            "🇷🇺 1 800 ₽\n"
            "🇺🇿 250 000 сум\n"
            "🇰🇬 1 700 сом\n\n"
            "❗❗ *ДОСТУП ДАЁТСЯ НАВСЕГДА*\n\n"
            "Нажмите «ОПЛАТИТЬ ВХОД» для реквизитов."
        )
        await query.edit_message_caption(
            caption=text,
            parse_mode=constants.ParseMode.MARKDOWN,
            reply_markup=buy_keyboard(),
        )

    # 3) Что внутри приватки
    elif query.data == "inside":
        text = (
            "📌 *Нужна информация про приватку?*\n\n"
            "💰 *Стоимость доступа: 20 $ (навсегда)*\n"
            "🇰🇬 Кыргызстан — 1 700 сом\n"
            "🇰🇿 Казахстан — 10 000 ₸\n"
            "🇺🇿 Узбекистан — 250 000 сум\n"
            "🇷🇺 Россия — 1 800 ₽\n\n"
            "🔍 *Что внутри?*\n"
            "— Мини-курсы и видеоуроки по зарубежному YouTube\n"
            "— Подбор прибыльных ниш и стратегий\n"
            "— Полезные фишки, шаблоны и скрипты\n"
            "— Только проверенные методы без воды\n"
            "— Бесплатные созвоны со мной\n"
            "— Поддержка и ответы на вопросы\n\n"
            "📦 *+ Внутри есть курс по YouTube с нуля*\n\n"
            "👥 Приватка — твой быстрый старт в YouTube без хаоса.\n\n"
            "Готов(а) стартовать? Жми «ОПЛАТИТЬ ВХОД»."
        )
        with open("5454203047233319344.jpg", "rb") as photo:
            await query.message.chat.send_photo(
                photo=photo,
                caption=text,
                parse_mode=constants.ParseMode.MARKDOWN,
                reply_markup=inside_keyboard(),
            )
        await query.delete_message()

    # 4) Услуги (консультация и наставничество)
    elif query.data == "services":
        message = (
            "🚀 *МОИ УСЛУГИ — ДЛЯ ТЕХ, КТО ХОЧЕТ ЗАПУСТИТЬСЯ И ЗАРАБАТЫВАТЬ НА YOUTUBE*\n\n"
            "📦 *Приватный Telegram-канал* — 20 $ (навсегда)\n"
            "— Готовые мини-курсы по зарубежному YouTube\n"
            "— Подбор прибыльных ниш и стратегии роста\n"
            "— Только рабочие фишки без воды\n"
            "— Созвоны и поддержка внутри сообщества\n\n"
            "🧠 *Индивидуальная консультация* — 20 $/час\n"
            "_Если у тебя уже есть канал или идеи._\n"
            "— Разбор твоего канала и ошибок\n"
            "— Выбор ниши под твои сильные стороны\n"
            "— Чёткая стратегия продвижения\n"
            "— Ответы на все твои вопросы\n\n"
            "🎯 *Наставничество* — 200 $/месяц\n"
            "_Если хочешь с нуля дойти до монетизации._\n"
            "— Помощь с нишей, контентом, оформлением\n"
            "— Поддержка на каждом этапе\n"
            "— Полный контроль и разбор результатов\n"
            "— Вместе доведём до цели"
        )
        await query.edit_message_caption(
            caption=message,
            parse_mode=constants.ParseMode.MARKDOWN,
            reply_markup=services_keyboard(),
        )

    # 5) Реквизиты
    elif query.data == "payment":
        text = (
            "💳 *Реквизиты для перевода:*\n\n"
            "⬇️ *Kaspi банк:*\n"
            "4400430296140327\n"
            "ILYA NOLFIN\n\n"
            "⬇️ *Альтернатива карта:*\n"
            "4405639843389055\n"
            "ILYA NOLFIN\n\n"
            "⬇️ *Криптокошелёк (USDT, TRC20):*\n"
            "`THcXbiQF28w6dctrFwJKfvHG2vAgV1CFQz`\n\n"
            "⬇️ *Если ничего не подошло:*\n"
            "[Оплатить через Telegram](https://t.me/tribute/app?startapp=sxvQ)\n\n"
            "⚠️ *После оплаты нажми кнопку ниже, чтобы скинуть чек об оплате* 💬\n"
            "и я пришлю ссылку на канал 🔗"
        )
        await query.edit_message_caption(
            caption=text,
            parse_mode=constants.ParseMode.MARKDOWN,
            reply_markup=payment_keyboard(),
        )


# ──────────────────────────────
# Запуск приложения
# ──────────────────────────────
if __name__ == "__main__":
    TOKEN = "7753398742:AAFaN-kDseix7hgQ_SnI9JUfRZAHxBSAbMQ"  # ← ваш токен

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Бот запущен")
    app.run_polling()
