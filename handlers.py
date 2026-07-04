from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from keyboards import main_menu, render_menu, vray_menu, ai_menu

# حالات مؤقتة
PHOTO = 1
TEXT = 2

user_data = {}


# /start (يرجع كل الأزرار)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 أهلاً بك في بوت الخدمات",
        reply_markup=main_menu
    )


# كل الرسائل (الأزرار القديمة)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🖥️ الرندر":
        await update.message.reply_text("اختر نوع الرندر", reply_markup=render_menu)

    elif text == "V-Ray":
        await update.message.reply_text("اختر البرنامج", reply_markup=vray_menu)

    elif text == "Corona":
        await update.message.reply_text("📂 أرسل ملف المشروع")

    elif text == "🤖 الذكاء الاصطناعي":
        await update.message.reply_text("اختر خدمة AI", reply_markup=ai_menu)

    elif text == "✍️ نص → صورة":
        await update.message.reply_text("✍️ أرسل وصف الصورة")

    elif text == "🖼️ تعديل صورة":
        await update.message.reply_text("📷 أرسل الصورة")

    else:
        await update.message.reply_text("اختر من القائمة 👇")


# 📷 استقبال الصورة
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    photo = update.message.photo[-1]

    user_data[user_id] = {"photo": photo.file_id}

    await update.message.reply_text("✍️ الآن أرسل وصف الصورة")
    return TEXT


# 📝 استقبال الوصف
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    data = user_data.get(user_id, {})
    photo = data.get("photo")

    if photo:
        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=photo,
            caption=f"📩 طلب جديد\n\n👤 ID: {user_id}\n\n📝 الوصف:\n{text}"
        )

        await update.message.reply_text("✅ تم استلام طلبك بنجاح")

        user_data.pop(user_id, None)


# تسجيل الهاندلرز
def register_handlers(app):
    from telegram.ext import CommandHandler, MessageHandler, filters

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))