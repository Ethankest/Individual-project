class Room:

  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.exits = {}

  def add_exit(self, direction, room):
    self.exits[direction] = room

  def get_exit(self, direction):
    return self.exits.get(direction)


class Player:

  def __init__(self, starting_location):
    self.current_location = starting_location

  def move(self, direction):
    next_location = self.current_location.get_exit(direction)
    if next_location:
      self.current_location = next_location
      print("\n" + self.current_location.description)
    else:
      print("You can't go that way!")


def main():
  # Define rooms
  dimly_lit_room = Room(
      "Dimly Lit Room",
      "You awake in a dimly lit room. You don’t remember much about your life except for a specific orb of light. For some reason, you know it had a name, ‘Zulpidel.’ You don’t understand the significance of this orb and its name, but you do know it has great power."
      "\nAfter thinking about the orb, you look around the room and see a doorway, a potion, and a dagger floating above a pedestal with ornate markings adorning the sides of both the pedestal and dagger."
      "\nWill you go to the doorway, potion, or dagger?")

  dagger_room = Room(
      "Dagger Room",
      "You slowly walk towards the dagger in caution. You don’t know what will"
      "\nhappen if you take the dagger, but you assume it’s trapped.")
  doorway_room = Room(
      "Doorway",
      "You walk towards the doorway and open it. Suddenly a vicous, bloodthirsty, beast lunges at you and gobbles you up. You die."
      "\nGAME OVER"
      "\n"
      "\n Ending 6 out of 6"
  )
  potion_room = Room(
      "Potion Room",
      "You walk towards the potion. Your body moves of its own accord. You pick it up. Your body forces you to drink it. You die."
      "\nGAME OVER"
      "\n"
      "\nEnding 2 out of 6")

  let_it_take_room = Room(
      "Let It Take Room",
      "You continue to float up into the sky. You float for hours until finally, you see the source of the light. An orb that looks slightly familiar. And then you realize that it’s the same orb from your memory ‘Zulpidel.’ Do you reach out to touch the orb or continue to float?"
  )

  touch_orb_room = Room(
      "Touch Orb Room",
      "You reach out to touch the orb, once your finger collides with the orb you are bathed in a swath of light. You start to hear a sound. You strain your ears to hear, and slowly, the sound becomes more clear, “Jake, Jake, Jake, wake up! Please wake up! Come on Jake!” Is that my name? You"
      "\nwonder. But before you have time to rack your brain for any memory of a past life, You wake up."
      "\n"
      "\nThe end"
      "\n"
      "\n ")

  goofy_secret_ending_room = Room(
      "Goofy Secret Ending Room",
      "Ok, you dont want to do anything? Fine. You sit in the exact same spot for 5 days before dying of starvation. You die."
      "\nGAME OVER"
      "\n"
      "\nSecret Ending 2 out of 4")

  take_dagger_room = Room(
      "Take Dagger Room",
      "\nYou pick up the dagger and nothing happens for a moment. Suddenly a vibrant"
      "\nlight comes from the top of the room onto you. You don’t seem to understand what is"
      "\nhappening... After the light has been on you for what seems like an eternity, you begin to float. You cry out in surprise as you’re whisked off your feet towards the"
      "\nlight. You fly through a hole in the ceiling. You didn’t think there was a hole there"
      "\nbefore, but you might have missed it. After gaining your bearings slightly, you"
      "\nrealize that the dagger has disappeared. You look down towards the pedestal and it"
      "\nisn’t there, it isn’t in your hand, and it isn’t floating next to you."
      "\nYou look around and see nothing, you see the room that you were previously in, but"
      "\nnothing else. The light is still bringing you up, but more slowly now."
  )

  struggle_room = Room(
      "Struggle Room",
      "You struggle to get out of the light. You feel yourself slipping out of the light. However you vastly miscalculated the distance to the top of the room. You fall and splat dead on the ground."
      "\n"
      "\n GAME OVER"
      "\n"
      "\n Ending 3 out of 6")

  walk_away_room = Room(
      "Walk Away Room",
      "You walk away from the dagger and fall into a spiked pit that opened up a second before. You die."
      "\nGAME OVER"
      "\n"
      "\nEnding 4 out of 6")

  stab_room = Room("stab room","You stab yourself in the chest multiple times. you watch your blood and innards spill out from the many incisions you have placed upon yourself until the light fades from your eyes. You die.""\nGAME OVER""\n""\nSecret Ending 4 out of 4")
  
  continue_to_float_room = Room("continue to float room" , "The light continues to bring you up until it suddenly disappears, you fall. You fall past the room and into the void below. You fall for days until. You starve to death. You die.""\n""\nGAME OVER""\n""\nEnding 5 out of 6")
  secret_secret_endong = Room(
      "Secret Secret Endong Room" , "18 years later…"
"\n""\n""\nMom! Dad! I’m driving myself to school!” you yell. “Ok honey!” Your mom yells back from the living room. Your mom and dad have been married for 17 years. You are the oldest of two. You and your brother who is 15. You get into your car. You start driving towards your school. You drive to the coffee shop to get a coffee for both you and your boyfriend. You start driving when suddenly a semi-truck comes and hits your car hard. Your parents, your brother, and your boyfriend rush to the hospital to see how you’re doing. They get there and find you in a coma. You can still hear though. You hear your dad say in defeat. “Same as m-” Your mind fades to black."



"\n""\n""\nYou awake in a dark room. You don’t remember much about your li-")
  secret_ending_room = Room(
      "Secret Ending Room",
      "You wake up and see many doctors. You realize that your name is, in fact, Jake. You begin to remember your life. You remember your parents, your dog, going to college, becoming an A-class"
      "\nengineer. You remember meeting your girlfriend, Elle. You remember buying your new dog (you named him Omelet) with Elle. You remember driving, you remember screaming as a semi-truck crashed headfirst into your little car. Then after that, nothing. Until now. “Where’s Elle?” you ask the doctors. You hear a small little voice to your right that breaks as it speaks. “Right here” You see Elle, she looks a little bit older than when you last saw her. She’s crying. You speak, “Hey hey, hey, what’s wrong?” Elle wipes away her tears and says, “Nothing. I’m just so happy you’re back after so long.” You then realize you’ve been in a coma. You turn and ask the doctors, “How long was I under?” One of the doctors looks at a clipboard and then says, “Two years, almost exactly” That explains why Elle looked a little bit older. Elle speaks, “I have been by this bed every day since the crash. I never gave up on you. And now,” her voice breaks “you’re back.” Elle wipes her eyes again, “The doctors gave you some drug to wake you up, it took them two years to track it down, I’m not angry with them, in fact, I'm quite happy. They brought you back to me."
      "\n"
      "\nYou stay in the hospital for another week as the doctors wrap up their tests. You luckily didn’t sustain any lasting injuries from the crash. You find Elle. You ask her, “You ready?” She turns around with a smile, kisses you, and says, “Let's go home.”"
      "\n"
      "\nThe End"
      "\n"
      "\n ")

  # Connect rooms
  dimly_lit_room.add_exit("dagger", dagger_room)
  dimly_lit_room.add_exit("doorway", doorway_room)
  dimly_lit_room.add_exit("potion", potion_room)
  dimly_lit_room.add_exit("No", goofy_secret_ending_room)
  dagger_room.add_exit("take", take_dagger_room)
  dagger_room.add_exit("walk away", walk_away_room)

  take_dagger_room.add_exit("let it take", let_it_take_room)
  take_dagger_room.add_exit("continue", let_it_take_room)
  take_dagger_room.add_exit("struggle", struggle_room)
  take_dagger_room.add_exit("stab", stab_room)
  let_it_take_room.add_exit("continue" , continue_to_float_room)

  # Create player
  player = Player(dimly_lit_room)

  # Game loop
  while True:
    command = input(
        "You awake in a dimly lit room. You don’t remember much about your life"
        "\nexcept for a specific orb of light. For some reason, you know it had a"
        "\nname, ‘Zulpidel.’ You don’t understand the significance of this orb and"
        "\nits name, but you do know it has great power."
        "\nAfter thinking about the orb, you look around the room and see a doorway, a potion, and a dagger floating above a pedestal with ornate markings"
        "\nadorning the sides of both the pedestal and dagger."
        "\nWill you go to the doorway, potion, or dagger? ")

    if command == "dagger":
      print(dagger_room.description)
      command = input("Do you take the dagger or walk away? " )
      if command == "walk away":
        print(exit(walk_away_room.description))
      if command == "take":
        print(take_dagger_room.description)
        command = input(
            "You can either struggle to get out of the light or let it continue to take you. "
         )
        if command == "stab":
          print(exit(stab_room.description))
        if command == "struggle":
          print(exit(struggle_room.description))
        if command == "let it take" or command == "continue" or command == "take":
          print(let_it_take_room.description)
          command = input(
              "You can either reach out to touch the orb or continue to float. "
           )
          if command == "continue":
            print(exit(continue_to_float_room.description))
          if command == "reach out" or command == "touch":
            print(touch_orb_room.description)
            command = input("Ending 1 out of 6 ")
            if command == "Zulpidel":
              print(secret_ending_room.description)
              command = input("Secret Ending 1 out of 4 ")
              if command == "18 years":
                print(secret_secret_endong.description)
            break
    if command == "doorway":
      print(doorway_room.description)
      break
    if command == "potion":
      print(exit(potion_room.description))
      
    if command == "No":
      print(exit(goofy_secret_ending_room.description))
    if command == "quit":
      print("Goodbye!"
            "\nGAME OVER""\n""\nSecret Ending 3 out of 4" )
      break

    player.move(command)



if __name__ == "__main__":
  main()
