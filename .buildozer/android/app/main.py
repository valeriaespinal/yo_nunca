from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import random

class YoNuncaApp(App):
    def build(self):
        self.prompts_normal = [
            "Yo nunca he robado en una tienda.",
            "Yo nunca he perdido el trabajo por haber salido de fiesta y bebido demasiado la noche anterior.",
            "Yo nunca pensé que un personaje de dibujos animados fuera atractivo.",
            "Yo nunca he estado esposado por la policía.",
            "Yo nunca he tenido diarrea en la casa de un amigo.",
            "Yo nunca me he vestido con ropa del sexo opuesto.",
            "Yo nunca he culpado a un amigo por algo que hice.",
            "Yo nunca he jugado a la Ouija.",
            "Yo nunca he bebido antes de cumplir 18.",
            "Yo nunca me he enamorado de un profesor.",
            "Yo nunca he dudado de mi orientación sexual.",
            "Yo nunca he creado una cuenta falsa en las redes sociales.",
            "Yo nunca he despertado en un lugar extraño porque iba muy borracho.",
            "Yo nunca he perdido la parte de abajo de mi traje de baño mientras estaba en la playa.",
            "Yo nunca he ido en pijama y zapatillas por la calle.",
            "Yo nunca lloré ni supliqué para librarme de una multa o de un castigo.",
            "Yo nunca he perdido el conocimiento.",
            "Yo nunca he hecho que alguien tenga que ir al hospital.",
            "Yo nunca me he hecho un piercing en una zona innombrable.",
            "Yo nunca me he bañado en la playa totalmente desnudo.",
            "Yo nunca he estado esposado.",
            "Yo nunca he fantaseado con alguien que está hoy aquí.",
            "Yo nunca he mentido sobre cuánto mido para ligar.",
            "Yo nunca he pasado más de una semana sin ducharme.",
            "Yo nunca he tenido una experiencia paranormal.",
            "Yo nunca he llevado la ropa interior al revés durante todo un día.",
            "Yo nunca he fingido encontrarme mal para no ir al trabajo.",
            "Yo nunca he quedado muy en ridículo al intentar ligar con alguien.",
            "Yo nunca he recibido una bofetada en público.",
            "Yo nunca he deseado la muerte a alguien que esté hoy aquí.",
            "Yo nunca he robado dinero.",
            "Yo nunca he exagerado mis logros para intentar ligar.",
            "Yo nunca he dado un nombre falso.",
            "Yo nunca he trabajado borracho.",
            "Yo nunca he olido mi propia ropa interior para ver si está limpia o sucia.",
            "Yo nunca he dejado plantado a alguien en una cita.",
            "Yo nunca he devuelto algo después de habérmelo puesto.",
            "Yo nunca he soltado sin querer el teléfono en el baño.",
            "Yo nunca he llorado de mentira para conseguir algo.",
            "Yo nunca he gastado más de 200 euros en una noche de fiesta.",
            "Yo nunca he enviado un mensaje a un ex sin venir a cuento.",
            "Yo nunca he salido corriendo haciendo un simpa.",
            "Yo nunca he buscado mi propio nombre en Google.",
            "Yo nunca he editado mis selfies.",
            "Yo nunca me han negado la entrada a un club.",
            "Yo nunca he mandado mensajes privados a un famoso.",
            "Yo nunca he mentido jugando a 'Yo nunca'.",
            "Yo nunca he dicho que me gustaba mucho un regalo y luego lo he devuelto.",
            "Yo nunca he borrado una foto de una red social por no gustarme cómo salgo.",
            "Yo nunca he dicho una mentira a mis amigos.",
            "Yo nunca he entrado a una fiesta sin que me hayan invitado.",
            "Yo nunca he recibido una bofetada en público.",
            "Yo nunca he escuchado reggaetón en sesión privada en Spotify para que nadie me descubriera.",
            "Yo nunca he tenido una época vegetariana o vegana.",
            "Yo nunca he ido a que me echaran las cartas.",
            "Yo nunca he hecho trampas en un juego de mesa.",
            "Yo nunca he vomitado encima de alguien.",
            "Yo nunca he mentido diciendo que me gustaba lo que había cocinado una amistad o mi pareja.",
            "Yo nunca le he hecho ghosting a nadie.",
            "Yo nunca he pillado a mis padres teniendo sexo.",
            "Yo nunca he usado apodos estúpidos para referirme a mi pareja.",
            "Yo nunca me he comido algo del suelo.",
            "Yo nunca he sido rechazado amorosamente por alguien.",
            "Yo nunca he tenido una pelea en público.",
            "Yo nunca he llegado tarde al trabajo.",
            "Yo nunca he cogido manía a una amiga o a otra persona.",
            "Yo nunca me he tirado un pedo y luego le he echado la culpa a otra persona.",
            "Yo nunca he hecho nada ilegal.",
            "Yo nunca he mentido a alguien de esta habitación.",
            "Yo nunca he besado al hermano de un amigo.",
            "Yo nunca he estropeado una prenda de vestir que me prestó una amiga.",
            "Yo nunca me he quedado a dormir en la casa de un extraño una noche entera.",
            "Yo nunca he orinado en la ducha.",
            "Yo nunca he ignorado a un conocido en público.",
            "Yo nunca he comido las sobras de otra mesa en un restaurante.",
            "Yo nunca he mentido al besar a alguien.",
            "Yo nunca he mirado el teléfono de mi pareja.",
            "Yo nunca he contado el secreto de alguien.",
            "Yo nunca me he encaprichado con el padre de un amigo.",
            "Yo nunca he mentido a nadie de este grupo.",
            "Yo nunca he intentado seducir a un profesor.",
            "Yo nunca he estado más de una semana sin ducharme.",
            "Yo nunca he usado la misma ropa interior dos días seguidos.",
            "Nunca me ha caído mal alguien de este grupo.",
            "Nunca he puesto una excusa para no verme con alguien que está aquí.",
            "Nunca he visto las 'stories' de alguien de este grupo en modo avión.",
            "Nunca he 'stalkeado' las fotos más antiguas del Instagram de gente de este grupo."
            ]
        self.prompts_funny = [
            "Yo nunca he tenido sexo en el lugar de trabajo.",
            "Yo nunca he tenido cibersexo.",
            "Yo nunca he llevado una máscara o antifaz en la cama.",
            "Yo nunca he participado en una orgía.",
            "Yo nunca le he hecho un baile erótico a alguien.",
            "Yo nunca he tenido sexo en la cama de mis padres.",
            "Yo nunca he grabado con el móvil una relación íntima.",
            "Yo nunca me he lesionado mientras tenía relaciones íntimas.",
            "Yo nunca he mantenido relaciones con alguien 5 años mayor que yo.",
            "Yo nunca he mantenido relaciones con alguien 10 años mayor que yo.",
            "Yo nunca he vomitado durante el sexo.",
            "Yo nunca me he disfrazado para satisfacer una fantasía.",
            "Yo nunca he estado con nadie de mi familia.",
            "Yo nunca quise tener relaciones con una persona del mismo sexo.",
            "Yo nunca he sido infiel.",
            "Yo nunca me he liado con el ex de un amigo o amiga.",
            "Yo nunca he pasado la noche con alguien este grupo.",
            "Yo nunca le he visto el trasero a un profesor/a.",
            "Yo nunca he fingido un orgasmo.",
            "Yo nunca he estado con un primo o prima.",
            "Yo nunca he dicho el nombre equivocado durante una relación.",
            "Yo nunca he tenido una relación sexual con un compañero de trabajo.",
            "Yo nunca le he sido infiel a ninguna de mis parejas.",
            "Yo nunca he tenido una relación abierta.",
            "Yo nunca lo he hecho al aire libre.",
            "Yo nunca he usado una comida como juguete.",
            "Yo nunca he enviado un desnudo a la persona equivocada.",
            "Yo nunca he intentado ligar con el rollo de un amigo.",
            "Yo nunca he mandado un audio subido de tono a un familiar por error.",
            "Yo nunca he tenido sexo en el coche.",
            "Yo nunca he usado una aplicación de citas.",
            "Yo nunca me he enamorado de un profe.",
            "Yo nunca he comprado nada en un sex shop.",
            "Yo nunca he tomado una fotografía de mis partes íntimas.",
            "Yo nunca he vomitado mientras tenía relaciones sexuales.",
            "Yo nunca he tomado la pastilla del día después.",
            "Yo nunca me he sentido atraído por el padre o la madre de un amigo.",
            "Yo nunca he tenido sexo por teléfono.",
            "Yo nunca he pagado una suscripción a una página porno.",
            "Yo nunca he escondido un chupetón a mis padres.",
            "Yo nunca he pensado en otra persona durante el sexo.",
            "Yo nunca me he hecho la paja viendo hentai.",
            "Yo nunca me he hecho la paja más de tres veces en un día.",
            "Yo nunca me he hecho la paja más de cinco veces en un día.",
            "Yo nunca me he hecho la paja más de diez veces en un día.",
            "Yo nunca he pasado más de seis meses sin tener sexo.",
            "Yo nunca he hecho una cobra (o me la han hecho).",
            "Yo nunca le he enviado a alguien una foto polla o un nude.",
            "Yo nunca he recibido un baile erótico.",
            "Yo nunca he dado un baile erótico.",
            "Yo nunca me he hecho un selfie sexy.",
            "Yo nunca he fingido un orgasmo.",
            "Yo nunca he hecho un trío.",
            "Yo nunca me he besado con alguien del mismo sexo.",
            "Yo nunca he hecho sexting.",
            "Yo nunca he estado en una playa nudista.",
            "Yo nunca he visto porno.",
            "Yo nunca he estado enamorado de un compañero de trabajo.",
            "Yo nunca he estado en un sex shop.",
            "Yo nunca he tenido una aventura de una noche.",
            "Yo nunca me he enamorado a primera vista.",
            "Yo nunca he salido con más de una persona a la vez.",
            "Yo nunca me he acostado con alguien que me dobla la edad.",
            "Yo nunca he salido con alguien durante más de un año.",
            "Yo nunca he traído a alguien a casa para que conozca a mis padres.",
            "Yo nunca he hecho sexo tántrico.",
            "Yo nunca he usado afrodisíacos.",
            "Yo nunca he probado posturas del kamasutra.",
            "Yo nunca me he masturbado delante de alguien.",
            "Yo nunca he tenido una cita a ciegas.",
            "Nunca he tenido sexo en un avión.",
            "Yo nunca he fantaseado con un famoso.",
            "Yo nunca he tenido relaciones por dinero o por favores.",
            "Yo nunca he tenido sexo en el mar/piscina.",
            "Yo nunca me he acostado con un compañero de oficina.",
            "Yo nunca he vuelto con un ex.",
            "Yo nunca he sido infiel.",
            "Yo nunca me he acostado con dos personas distintas el mismo día.",
            "Yo nunca me he acostado con alguien en la primera cita.",
            "Yo nunca he tenido sexo en un avión.",
            "Yo nunca he chupado los dedos de los pies de mi pareja.",
            "Yo nunca he buscado en Google las posiciones sexuales del Kamasutra.",
            "Yo nunca he tenido una fantasía sexual con otra persona cuando estaba en una relación.",
            "Yo nunca he fingido un orgasmo.",
            "Nunca he pensado en alguien de este grupo como 'algo más'.",
            "Nunca he querido besar a quien está ahora a mi derecha.",
            "Nunca he tenido una fantasía sexual con una persona que está aquí.",
            "Nunca he imaginado a alguien de aquí desnudo/a.",
            "Nunca he deseado que una persona que está aquí me bese por todo el cuerpo.",
            "Nunca me he sentido atraída sexualmente por alguien de la sala.",
            "Nunca he anhelado una relación superlarga con alguien que está aquí.",
            "Nunca he fantaseado con quien tengo a la izquierda.",
            "Nunca he soñado con besar a alguien de esta sala.",
            "Nunca he hecho un trío con alguien de la sala.",
            "Nunca he pensado en hacer un trío con alguien que está aquí.",
            "Nunca he 'stalkeado' en Instagram a alguien de esta sala.",
            "Nunca me he tocado pensando en alguien que está aquí.",
            "Nunca me he imaginado teniendo hijos con alguien que tengo cerca ahora mismo.",
            "Nunca he querido que me bese quien tengo ahora enfrente.",
            "Nunca he imaginado que le gusto a alguien de esta habitación.",
            "Nunca he sentido nada por alguien de aquí cuando me escribió un mensaje.",
            "Nunca he escrito el nombre de alguien de aquí con un corazoncito al lado.",
            "Nunca me he imaginado casándome con alguien que está presente.",
            "Nunca he querido hacer 'love bombing' a alguien de esta sala.",
            "Nunca he pensado en alguien de esta sala e imaginado que protagonizamos una serie.",
            "Nunca he comparado a nadie de aquí con mi persona ideal.",
            "Nunca he querido hacer un regalo especial a alguien de esta sala.",
            "Nunca he manifestado a alguien de esta habitación.",
            "Nunca he querido salir de fiesta con alguien de esta sala.",
            "Nunca he pensado en declararme a alguien que está aquí mismo.",
            "Nunca he considerado que alguien que está aquí debería estar conmigo.",
            "Nunca he sentido mariposas con quien está mirándome ahora mismo.",
            "Nunca he querido liarme en una discoteca con alguien de aquí.",
            "Nunca he querido chupar la oreja a alguien de aquí.",
            "Nunca he sentido que una persona que está aquí es 'mi persona'.",
            "Nunca he imaginado cosas subidas de tono con quien está dos puestos a mi izquierda.",
            "Nunca he mirado fotos de alguien de aquí con nostalgia.",
            "Nunca me he imaginado en mis vacaciones soñadas con alguien que está en este grupo.",
            "Nunca he pensado en un 'y si' con quien está dos puestos a mi derecha.",
            "Nunca he sentido que no es el momento con alguien de aquí, pero que lo será.",
            "Nunca he pensado en alguien de aquí escuchando canciones románticas.",
            "Nunca se ha colado alguien de aquí en un sueño sexual.",
            "Nunca me he imaginado en un concierto superguay con alguien de aquí.",
            "Nunca he sobrepensado en una persona aquí presente.",
            "Nunca he querido presentar a mis amigos a alguien de aquí como mi pareja.",
            "Nunca he extrañado de manera diferente a alguien de aquí.",
            "Nunca me he tocado pensando en alguien de este grupo.",
            "Nunca he querido saber si le molo a alguien de aquí.",
            "Nunca he pensado de más en quien tengo justo delante.",
            "Nunca he tenido un 'crush'.",
            "Nunca me he masturbado en un lugar público.",
            "Nunca he hecho un trío entre colegas.",
            "Nunca me he besado con la expareja de una amiga.",
            "Nunca he sentido algo diferente por alguien que está aquí.",
            "Nunca me ha gustado el ex de alguien de este grupo.",
            "Nunca me ha gustado la pareja de alguien de este grupo.",
            "Nunca he tenido ganas de besar a una persona que está aquí ahora mismo.",
            "Nunca he querido acostarme con alguien de aquí y/o su pareja.",
            "Nunca he pensado en cambiar de amigos."
            ]
        self.prompts_mixed = self.prompts_normal + self.prompts_funny
        self.current_prompt_index = -1

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(1, 1))
        layout.canvas.before.add(Color(1, 1, 1, 1))
        layout.canvas.before.add(Rectangle(size=layout.size, pos=layout.pos))

        title = Label(text="Yo nunca", font_size='24sp', size_hint=(1, None), height=50)
        layout.add_widget(title)

        buttons_layout = BoxLayout(spacing=10, size_hint=(1, None), height=100)

        normal_button = Button(text="Normal", on_press=self.show_normal_prompt, background_color=(1, 0.75, 0.8, 1))
        buttons_layout.add_widget(normal_button)

        funny_button = Button(text="Chistoso", on_press=self.show_funny_prompt, background_color=(1, 0.75, 0.8, 1))
        buttons_layout.add_widget(funny_button)

        mixed_button = Button(text="Mixto", on_press=self.show_mixed_prompt, background_color=(1, 0.75, 0.8, 1))
        buttons_layout.add_widget(mixed_button)

        layout.add_widget(buttons_layout)

        self.prompt_label = Label(text="", font_size='18sp', halign='center', size_hint=(1, None), height=50)
        layout.add_widget(self.prompt_label)

        return layout

    def show_normal_prompt(self, instance):
        self.show_prompt(self.prompts_normal)

    def show_funny_prompt(self, instance):
        self.show_prompt(self.prompts_funny)

    def show_mixed_prompt(self, instance):
        self.show_prompt(self.prompts_mixed)

    def show_prompt(self, prompts):
        index = random.randint(0, len(prompts) - 1)
        self.current_prompt_index = index
        self.prompt_label.text = prompts[index]

if __name__ == '__main__':
    YoNuncaApp().run()
