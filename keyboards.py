from telegram import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup([
    ["🚀 ابدأ"],
    ["🖥️ الرندر", "🤖 الذكاء الاصطناعي"],
    ["💰 الرصيد", "💳 شحن الرصيد"],
    ["💬 الدعم"]
], resize_keyboard=True)


render_menu = ReplyKeyboardMarkup([
    ["V-Ray", "Corona"],
    ["Lumion", "D5 Render"],
    ["⬅️ رجوع"]
], resize_keyboard=True)


vray_menu = ReplyKeyboardMarkup([
    ["3ds Max", "SketchUp"],
    ["⬅️ رجوع"]
], resize_keyboard=True)


ai_menu = ReplyKeyboardMarkup([
    ["✍️ نص → صورة", "🖼️ تعديل صورة"],
    ["⬅️ رجوع"]
], resize_keyboard=True)
