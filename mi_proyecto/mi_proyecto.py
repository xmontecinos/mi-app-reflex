import reflex as rx

class State(rx.State):
    # Aquí guardas tus datos para que no se recarguen siempre
    archivos_procesados: list[str] = []

    def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            # Tu lógica pesada aquí
            self.archivos_procesados.append(file.filename)

def index():
    return rx.vstack(
        rx.upload(
            rx.text("Arrastra tus archivos aquí"),
            id="upload1",
        ),
        rx.button("Procesar", on_click=State.handle_upload(rx.upload_files(upload_id="upload1"))),
        rx.foreach(State.archivos_procesados, rx.text)
    )

app = rx.App()
app.add_page(index)
