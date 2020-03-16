from ControleAcervo.ctrl.dialogs.messageAlert  import Message

class MessageSingleton:

    message = None

    @staticmethod
    def getInstance():
        if not MessageSingleton.message:
            MessageSingleton.message = Message()
        return MessageSingleton.message