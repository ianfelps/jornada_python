# imporat biblioteca
import flet as ft

# função principal do app
def main(pagina):
    # criar texto
    texto = ft.Text("Chat AO VIVO!")

    # criar coluna de chat
    chat = ft.Column()

    # criar caxia de texto para popup
    nome_usuario = ft.TextField(label="Escreva seu nome de usuário")

    # função para processar as mensagens recebidas
    def enviar_mensagem_tunel(mensagem):
        # tipo de mensagem
        tipo = mensagem["tipo"]
        # verificar qual o tipo de mensagem
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            # adicionar aviso de quando um usuário entrar no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat!", size=12, italic=True, color=ft.colors.ORANGE_500))
        # atualizar página
        pagina.update()

    # chamar a função "enviar_mensagem_tunel" para processar as mensagens
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # função para enviar mensagens
    def enviar_mensagem(evento):
        # publicar entrada do usuário no sistema
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        # atualizar página
        pagina.update()

    # criar campo de mensagem
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)

    # criar botão de enviar mensagem (ao clicar, chamar a função "enviar_mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        # publicar mensagem e nome do usuário no sistema
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # remover elementos anteriores
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campo de mensagem e botao de enviar mensagem
        pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))
        # atualizar página
        pagina.update()

    # configurações do popup de entrada no chat
    popup = ft.AlertDialog(
        # parâmetros do popup
        open=False, 
        modal=True,
        # titulo do popup
        title=ft.Text("Bem-vindo ao Chat"),
        # conteúdo do popup
        content=nome_usuario,
        # botão para iniciar o chat (chamar a função "entrar_popup")
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    # função para entrar no chat (criar o popup)
    def entrar_chat(evento):
        # abrir o popup
        pagina.dialog = popup
        popup.open = True
        # atualizar página
        pagina.update()

    # criar botão para iniciar o chat (ao clicar, chama a função "entrar_chat")
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    # adicionar elementos
    pagina.add(texto)
    pagina.add(botao_iniciar)

# iniciar app (no navegador)
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)