import flet as ft

from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Text, Colors, View
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Atividade 1 Navegação'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Home'), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text='Enviar',
                                   width=page.window.width,
                                   on_click=lambda _: page.go('/exibir'))
                ]
            )
        )
        if page.route == '/exibir':
            page.views.append(
                View(
                    '/exibir',
                    [
                        AppBar(title=Text('Exibir'), bgcolor=Colors.PRIMARY_CONTAINER),
                        ft.Text(value=f'Olá {input_nome.value}, tudo bem?', size=14)
                    ]
                )
            )
        page.update()

    def volta(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.go(page.route)
    page.on_view_pop = volta

    #     Criação de componentes
    input_nome = ft.TextField(label='Nome:', hint_text='Digite seu nome')


ft.app(main)
