def classify(message):
    text = message.lower()

    reference_words = [
        "справк",
    ]

    complaint_words = [
        "холодная",
        "очередь",
        "пропал",
        "не работает",
        "сломался",
        "проблем",
    ]

    if any(word in text for word in reference_words):
        return "справка"

    if any(word in text for word in complaint_words):
        return "жалоба"

    return "другое"


def make_reply(category, message):
    if category == "справка":
        return (
            "Здравствуйте! Для получения справки о месте учёбы "
            "обратитесь в деканат или учебный офис вашего факультета."
        )

    if category == "жалоба":
        if "wi-fi" in message.lower() or "wifi" in message.lower():
            return (
                "Здравствуйте! Спасибо за сообщение. "
                "Информацию о проблеме с Wi-Fi передадим технической службе."
            )

        return (
            "Здравствуйте! Спасибо за обратную связь. "
            "Мы передадим информацию ответственным сотрудникам."
        )

    if "консультац" in message.lower():
        return (
            "Здравствуйте! Для записи на консультацию уточните, "
            "пожалуйста, преподавателя и удобное время."
        )

    if "парков" in message.lower():
        return (
            "Здравствуйте! Парковка для гостей находится рядом с территорией корпуса. "
            "Точное расположение можно уточнить у администрации или охраны."
        )

    return "Здравствуйте! Уточните, пожалуйста, ваш вопрос."


def main():
    with open("messages.txt", "r", encoding="utf-8") as file:
        messages = [line.strip() for line in file if line.strip()]

    for number, message in enumerate(messages, start=1):
        category = classify(message)
        reply = make_reply(category, message)

        print(f"{number}. {message}")
        print(f"Категория: {category}")
        print(f"Черновик ответа: {reply}")
        print()


if __name__ == "__main__":
    main()
