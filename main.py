import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = tk.Tk()
root.title("the store")
root.geometry("350x350")

total = 0
money = 900000


def update_total(cost):
        global total, money
        cost_int = int(cost.strip("$"))
        if money >= cost_int:
            total += cost_int
            money -= cost_int
            cost_output.config(text=f"Total cost: ${total}")
            wallet_balance.config(text=f"Wallet balance: ${money}")
        else:
            cost_output.config(text="Not enough money!")



# Images and costs
items = [{"image": "gravy.jpg", "cost": "$4"},
         {"image": "mama.jpg", "cost": "$6"},
         {"image": "shin.jpg", "cost": "$7"}]

title_label = tk.Label(root, text = "good store", font = ("Helvetica", 16))
title_label.pack(pady = 5)

frame = tk.Frame(root)
frame.pack(pady = 1)

for item in items:
  item_frame = tk.Frame(frame)
  item_frame.pack(side = tk.LEFT)

  # Open and resize the image
  img = Image.open(item["image"])
  img = img.resize((100, 100))
  img = ImageTk.PhotoImage(img)
  img_label = tk.Label(item_frame, image=img)
  img_label.image = img
  img_label.pack()

  # Add cost below each image
  cost_label = tk.Label(item_frame, text="Cost: " + item["cost"])
  cost_label.pack()

  # Add a Buy button
  buy_button = tk.Button(item_frame, text="Buy This Now", command=lambda cost=item["cost"]: update_total(cost))
  buy_button.pack()

cost_output = tk.Label(root, text = "")
cost_output.pack(pady=40)

wallet_balance = tk.Label(root, text=f"Wallet balance: ${money}")
wallet_balance.pack()



root.mainloop()