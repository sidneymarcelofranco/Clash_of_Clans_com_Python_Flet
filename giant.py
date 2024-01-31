import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_height = 500
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.GREY, ft.colors.SURFACE]
        ),
        content=ft.Image(
            src='img\\giant.png',
            scale=1.4)
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 5', color=ft.colors.ORANGE, weight=ft.FontWeight.BOLD,size=12),
                ft.Text(value='The Giant',
                        weight=ft.FontWeight.BOLD,
                        size=30,
                        color=ft.colors.BLACK),
                ft.Text(value="Slow, steady and powerful, Giants are massive warriors that soak up huge amounts of damage. Show them a turret or cannon and you'll see their fury unleashed!",
                        color=ft.colors.GREY,
                        text_align=ft.TextAlign.CENTER)

            ]

        )
    )
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value='2M',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20,
                                ),
                        ft.Text(value='TRAINNING', 
                                color=ft.colors.WHITE,
                                size=10
                                ),                        
                    ]
                ),
                ft.VerticalDivider(opacity=0.5),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value='12',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20,
                                ),
                        ft.Text(value='SPEED',
                                color=ft.colors.WHITE,
                                size=10
                                ),                        
                    ]
                ),
                ft.VerticalDivider(opacity=0.5),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value='2250',
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20,
                                ),
                        ft.Text(value='COST',
                                color=ft.colors.WHITE,
                                size=10
                                ),                        
                    ]
                )                
            ]
        ))

    layout = ft.Container(
        height=600,
        width=300,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.BROWN),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,

        content=ft.Column(

            spacing=0,
            controls=[
                image,
                info,
                skills,
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
