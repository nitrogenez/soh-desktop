# Copyright (C) 2022 nitrogenez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


label soh_chapter1_prologue_uk_UA:

    window hide

    scene bg default_background with dissolve
    stop music fadeout 1.0
    play ambience silence fadein 6
    stop sound_loop fadeout 1.0

    $ renpy.pause(2)
    play music soh_theme
    show soh_noise with dissolve2
    $ renpy.pause(6)

    "Не кожна людина зможе уникнути появи страху білого листа.{w} Це дуже сильний страх, який може не тільки відвести людину у режим прокрастинації, але також вбити."
    "Колись я теж була наївною, задерикуватою дівчинкою. Думала, що “ось зараз закінчу школу і буду жити гарно”, але у результаті моє життя вирішило зіграти зі мною жарт.{w} Злий жарт."
    "Десь у 14 років я почала цікавитись технологіями...{w} Адже це так круто.{w} Ти можеш буквально спілкуватись зі своїм комп'ютером, й прямо казати йому, що робити..."
    "Я почала вчитись прогамувати.{w} Читала різні книги за структурами мов, за їх парадигмами, за тим, як вони працюють та чим відрізняються...{w} Але після цього в мене з'явились сумніви щодо того, чи хочу я займатись цим усе своє життя..."

    window hide
    $ renpy.pause(2)
    window show

    "Я вирішила розібратись у собі.{w} Я перестала нормально вчитися, я перестала мріяти про майбутнє, у тому числі про своє, але у результаті я... Побачила одну статтю у інтернеті...{w} Про таку річ як “кібербезпека”..."
    "Звісно, я одразу побіжала дивиться, що це таке, й, звісно ж, скільки за це платять...{w} Зрозуміла справа, що нічого складного перед собою я бачити не хотіла, та й не було це потрібно. Адже головне для мене було - навчитись."
    "…"

    window hide
    $ renpy.pause(2)
    window show

    "Час йшов.{w} Я вивчала мережі, системи, безпеку систем...{w} Мене це усе дуже сильно залучило, я майже повністю перестала цікавитись школою, спілкуванням, та іншим."
    "Я знищила свої акаунти у соціальних мережах, стерла інформацію про моє життя звідти, звідки змогла, і повністю стала...{w} {glitch=50.0}{b}Анонімна.{/b}{/glitch}{w} Кумедне слово."
    "У наш час слово “Анонімність” більшь асоціюється з якимись жирними дохлими задротами, що ставлять собі на профіль дівчин з аніме й що кажуть {i}“я дівчина, доказів не буде”{/i}"
    "Сучасні люди оцінюють анонімність як щось, до чого люди вдаються у той час, коли їм щось потрібно отримати...{w} Наприклад увагу, якої їм дуже не вистачає."
    "…"

    window hide
    $ renpy.pause(2)
    window show

    "Я ніколи не була такою.{w} Мені потрібна анонімність, щоб забеспечити власну безпеку й безпеку дорогих мені людей...{w} {glitch=50.0}Адже я хакер.{/glitch}"
    "І з цим словом у сучасному світі відбуваються цікави метаморфози.{w} Усі вважають, що хакери - то люди, які можуть за секунди зламати якусь компанію і красти звідти щось."
    "Частково вони праві.{w} Такі люди є.{w} І їх дуже багато, щоб створити стереотип про їх професію.{w} Але жодна людина розуміє, що хакером може бути хто завгодно, і ви про це ніколи не дізнаєтесь."
    "Наприклад.{w} Ви хоч раз бачили, як якась людина показувала вам за своїм бажанням свою історію браузеру? Чи показував хтось вам свої особисі повідомлення від користувача з ніком “Киця”? Сумніваюся."
    "…"

    window hide
    $ renpy.pause(2)
    window show

    "До чого я все це?{w} Я сама не знаю.{w} Але я люблю довгі та насичені монологи, адже вони допомагають мені уникнути реальності і втекти в моє минуле, якого мені так не вистачає, і в яке я так сильно хочу повернутись."
    "…"

    window hide
    $ renpy.pause(2)
    window show

    "Моє ім'я Аліса.{w} Вітаю, друг."

    window hide
    stop music fadeout 6
    $ renpy.pause(6)
    play music music_list['sunny_day'] fadein 2
    window show

    # TODO: Make art slideshow
    "Насправді зрозуміти світоустрій дуже просто, якщо ти здатна помічати дрібні деталі.{w} Деталі, які ты не хочеш бачити.{w} Деталі, які ты не хочеш помічати.{w} Деталі на куточку твого ока."
    "Диявол таїться у дрібницях…{w} Ці дрібниці заважають мені жити."
    "Наприклад..."

    window hide
    pause 2
    window show

    "Я знайомлюся з якимсь хлопцем, мені в ньому все подобається, прекрасна зовнішність, він хоч і курить, але небагато, і взагалі не п'є. І ось він запрошує мене до себе."
    "Заходячи до нього додому, я бачу бардак, купу розкиданих кам'яних шкарпеток і серветок, і на куточку свого ока помічаю, що в нього починає стискатися кулак."
    "Відразу стає зрозуміло, що далі буде, хто він, і чим весь час займався.{w} І це той самий момент, від якого мене могла б уберегти моя уважність. Принаймні я могла б відчути, як людина занадто сильно намагається здатися вам ідеальним і беззаперечним."
    "…"

    window hide
    $ renpy.pause(1)
    window show

    "Зовнішність завжди дуже оманлива."

    window hide
    stop music fadeout 6
    scene bg semen_room with Dissolve(4)
    $ renpy.pause(6)
    window show

    th "Кімната.{w} Така рідна.{w} Я вже навіть не пам'ятаю, як я купила цю квартиру, і як вона на той момент виглядала.{w} Все так перемішалося...{w} Я вже настільки звикла, що я навіть не можу уявити, як моя кімната могла б виглядати...{w} Чистою."
    th "Я не дуже багато і не дуже часто прибираю...{w} Можна сказати, взагалі.{w} Я не маю ні бажання, ні часу.{w} Я завжди або сиджу за комп'ютером і марную час на напівмертвих даркбордах, або заробляю на життя, виконуючи нехитрі замовники на фріланс-біржах."
    th "Я, звичайно, не вибаглива.{w} Тому мені вистачає $60-80 на місяць.{w} Це не так багато.{w} Враховуючи ціни та інфляцію."
    th "...{w}Ех.{w} Люблю монологи…{w} Але у будь-якому випадку, вже час за роботу…"

    window hide
    scene bg default_background with dissolve2
    show soh_title_text '{}'.format(persistent.soh_locale['ingame']['*-hours-later'] % (4)) at truecenter

    $ renpy.pause(4)
    scene bg semen_room with dissolve2
    window show

    dv "{i}*позіхання*{/i}.{w} Ну, от і все…{w} На сьогодні достатно…"

    window hide
    scene bg default_background with dissolve2
    play music blow_with_the_fires_lofi fadein 0.8
    $ renpy.pause(4)
    window show

    "Я пішла на кухню."

    window hide
    scene bg default_background with Dissolve(4)
    $ renpy.pause(2)
    window show

    "Прийшовши на кухню я поставила чайник, сіла за стіл, і почала дивитися у вікно.{w} Вигляд був такий, який у мене завжди вигляд з вікна.{w} Нічого особливого."
    "Тільки ось сьогодні був якийсь, мабуть, особливий день, коли мене душило сильне почуття образи і прокрастинація.{w} Таких днів не буває дуже багато, але все ж таки прокрастинація в моєму житті зустрічається дуже часто.{w} З урахуванням того, де живу."
    "…"

    window hide
    scene bg default_background with dissolve
    $ renpy.pause(6)
    window show

    "Через час чайник закипів.{w} Я налила собі гарячий кенійський чай і знову сіла за стіл, знову втупившись у вікно."
    th "Куди я гойдаюся...{w} Хоча, ясна річ...{w} У прірву."

    "У голові тихо грав мій улюблений witch house, в очах миготіли психоделічні образи.{w} Все натякало на те, що я просто їду з глузду.{w} Хоча, правду кажучи, це і на краще.{w} Можливо, я зможу позбутися свого прокляття."
    "…"
    "Я зможу…"
    "…"

    window hide
    show soh_title_text '{}'.format(persistent.soh_locale['ingame']['*-hours-later'] % (2)) at truecenter
    $ renpy.pause(4)

    scene anim prolog_3 with dissolve2
    scene anim prolog_4 with dissolve
    scene anim prolog_5 with dissolve
    scene anim prolog_10 with dissolve
    scene anim prolog_11 with dissolve

    $ renpy.pause(4)
    scene bg black with dissolve
    $ renpy.pause(2)
    scene anim prolog_14 with dissolve2
    scene anim prolog_15 with dissolve2
    $ renpy.pause(4)

    window show

    th "Я лежу на ліжку.{w} Наді мною стеля.{w} А ще наді мною сусіди, яким я одного разу зламала телевізор і почала крутити перший сезон “Доктор Хто”…{w} Хех…"
    th "І не для себе ж я це розповідаю.{w} Певно, мій мовчазний друже?"

    window hide
    show soh_noise with dissolve2
    stop music fadeout 1
    pause 1
    play music controlisanillusion
    $ renpy.pause(3)
    window show

    th "{glitch=50.0}...Чому ти ніколи не відповідаєш мені?{/glitch}"

    window hide
    $ renpy.pause(2)
    window show

    th "{glitch=50.0}Чому ти завжди мовчиш?{/glitch}"

    window hide
    $ renpy.pause(2)
    window show

    th "{glitch=50.0}Я тобі неприємна?{/glitch}"

    window hide
    $ renpy.pause(2)
    window show

    th "{glitch=50.0}Чи ти намагаєшся зі мною заговорити, але не можеш?{w} Може, я не справжня для тебе рівно настільки...{/glitch}"
    th "{glitch=50.0}Наскільки справжній для мене ти?{/glitch}"
    th "{glitch=50.0}...{w}Чи впевнений ти у своєму існуванні?{w} Чи впевнений ти у його корисності?{w} І чи впевнений ти у своїх переконаннях щодо того...{/glitch}"
    th "{glitch=50.0}Що робить тебе людиною?{w} Що робить тебе особистістю?{/glitch}"
    th "{glitch=50.0}...{w}Я є реальною.{w} Питання в тому: чи реальний ти, друже?{/glitch}"

    window hide
    $ renpy.pause(4)
    scene bg black with dissolve2

    $ soh_Achievement(persistent.soh_locale['achievements']['ach-demo'])
    $ renpy.pause(4)

    jump soh_main_menu