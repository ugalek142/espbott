from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

TOKEN = 'TU_TOKEN_AQUI'  # ¡Usa variables de entorno en producción!

keyboard = ReplyKeyboardMarkup(
    [['Записаться', 'Тарифы'], ['Оставить отзыв']],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я — бот разговорного испанского. Выбери действие ниже:",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'записаться' in text:
        await update.message.reply_text("📝 Форма для записи 👉 https://your-form-link")
    elif 'тарифы' in text:
        await update.message.reply_text("💸 Тарифы:\n— 30 мин: 500 ₽\n— 5 уроков: 2000 ₽")
    elif 'отзыв' in text:
        await update.message.reply_text("🙏 Отзыв можно оставить здесь или по ссылке 👉 https://your-review-form")
    else:
        await update.message.reply_text("Пожалуйста, выбери одну из кнопок ниже ⬇️")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Бот с кнопками запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
