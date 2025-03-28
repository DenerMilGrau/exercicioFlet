import flet as ft

from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Text, Colors, View
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Atividade 2 Navegação'
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
                    AppBar(title=Text('Cadastro de livro'), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_categoria,
                    input_autor,
                    input_descricao,

                    ElevatedButton(text='Enviar',
                                   width=page.window.width,
                                   on_click=lambda _: page.go('/exibir_info'))
                ]
            )
        )
        if page.route == '/exibir_info':
            page.views.append(
                View(
                    '/exibir_info',
                    [
                        AppBar(title=Text('Exibir'), bgcolor=Colors.PRIMARY_CONTAINER),
                        Text(value='Título:', size=20),
                        Text(value=f'{input_titulo.value}', size=14),
                        Text(value='Categoria:', size=20),
                        Text(value=f'{input_categoria.value}', size=14),
                        Text(value='Autor:', size=20),
                        Text(value=f'{input_autor.value}', size=14),
                        Text(value=f'Descrição:', size=20),
                        Text(value=f'{input_descricao.value}', size=14),
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

    input_titulo = ft.TextField(label='Título:', hint_text='insira o título')
    input_categoria = ft.TextField(label='Categoria:', hint_text='insira a categoria')
    input_autor = ft.TextField(label='Autor:', hint_text='insira o autor')
    input_descricao = ft.TextField(label='Descrição:', hint_text='insira a descrição')

ft.app(main)