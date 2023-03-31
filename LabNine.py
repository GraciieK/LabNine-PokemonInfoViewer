from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info


root = Tk()
root.title("Pokémon Information Viewer")
root.resizable(False, False)

#ADD Frames To Window.

frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20, 10))

frm_btm_left = ttk.LabelFrame(root, text='Pokémon Information')
frm_btm_left.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='Pokémon Stats')
frm_btm_right.grid(row=1, column=1, padx=(20, 10), pady=(10, 20), sticky=N)

#ADD Widgets To Window.

lbl_name = ttk.Label(frm_top, text='Pokémon Name:')
lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    #Get The Pokemon Name Entered By The User
    poke_name = ent_name.get().strip()
    if len(poke_name) ==-0:
        return

    #Get The Pokemon Information From The PokeAPI.
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
        err_msg = f'Unable to fetch information for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
        return

    #Populate The Information Values.

    poke_height = poke_info['height'] * 10
    lbl_height_value['text'] = f"{poke_height} cm"

    poke_weight = poke_info['weight'] / 10
    lbl_weight_value['text'] = f"{poke_weight} kg"
    
    poke_type = [n['type']['name'] for n in poke_info['types']]
    poke_type_list = ', '.join(poke_type).title()
    lbl_type_value['text'] = poke_type_list

    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defence['value'] = poke_info['stats'][2]['base_stat']
    bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_special_defence['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']

    bar_hp_text['text'] = f"{poke_info['stats'][0]['base_stat']}/255"
    bar_attack_text['text'] = f"{poke_info['stats'][1]['base_stat']}/255"
    bar_defence_text['text'] = f"{poke_info['stats'][2]['base_stat']}/255"
    bar_special_attack_text['text'] = f"{poke_info['stats'][3]['base_stat']}/255"
    bar_special_defence_text['text'] = f"{poke_info['stats'][4]['base_stat']}/255"
    bar_speed_text['text'] = f"{poke_info['stats'][5]['base_stat']}/255"

    return

btn_get_info = ttk.Button(frm_top, text='Get Information', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)


#Populate widget in the Information Box.

#Height
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=(10, 5), pady=10, sticky=E)

lbl_height_value = ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=1, padx=(10, 5), pady=10, sticky=W)


#Weight
lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=(10, 5), pady=10, sticky=E)

lbl_weight_value = ttk.Label(frm_btm_left, text='TBD')
lbl_weight_value.grid(row=1, column=1, padx=(10, 5), pady=10, sticky=W)

#Type
lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=(10, 5), pady=10, sticky=E)

lbl_type_value = ttk.Label(frm_btm_left, text='TBD')
lbl_type_value.grid(row=2, column=1, padx=(10, 5), pady=10, sticky=W)




#Populate Wighet In The Stats Frame

lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx=(10, 5), pady=10, sticky=E)
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1, padx=(10, 5), pady=10)

bar_hp_text = ttk.Label(frm_btm_right, text='TBD/255')
bar_hp_text.grid(row=0, column=3, padx=(10, 5), pady=10, sticky=E, )
#transparent = root.wm_attributes('-transparent', True)

#Attack
lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, padx=(10, 5), pady=10, sticky=E)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1, padx=(10, 5), pady=10)

bar_attack_text = ttk.Label(frm_btm_right, text='TBD/255')
bar_attack_text.grid(row=1, column=3, padx=(10, 5), pady=10, sticky=E)

#Defence
lbl_defence = ttk.Label(frm_btm_right, text='Defence:')
lbl_defence.grid(row=2, column=0, padx=(10, 5), pady=10, sticky=E)
bar_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defence.grid(row=2, column=1, padx=(10, 5), pady=10)

bar_defence_text = ttk.Label(frm_btm_right, text='TBD/255')
bar_defence_text.grid(row=2, column=3, padx=(10, 5), pady=10, sticky=E)

#Special Attack
lbl_special_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_special_attack.grid(row=3, column=0, padx=(10, 5), pady=10, sticky=E)
bar_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_attack.grid(row=3, column=1, padx=(10, 5), pady=10)

bar_special_attack_text = ttk.Label(frm_btm_right, text='TBD/255')
bar_special_attack_text.grid(row=3, column=3, padx=(10, 5), pady=10, sticky=E)

#Special Defence
lbl_special_defence = ttk.Label(frm_btm_right, text='Special Defence:')
lbl_special_defence.grid(row=4, column=0, padx=(10, 5), pady=10, sticky=E)
bar_special_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_defence.grid(row=4, column=1, padx=(10, 5), pady=10)

bar_special_defence_text = ttk.Label(frm_btm_right, text='TBD/255')
bar_special_defence_text.grid(row=4, column=3, padx=(10, 5), pady=10, sticky=E)

#Speed
lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, padx=(10, 5), pady=10, sticky=E)
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1, padx=(10, 5), pady=10)

bar_speed_text = ttk.Label(frm_btm_right, text='TBD/255')
bar_speed_text.grid(row=5, column=3, padx=(10, 5), pady=10, sticky=E)


#Look Until Window Is Closed.
root.mainloop()

