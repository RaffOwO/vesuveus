# Vesuveus - *Small*, yet *Mighty*, Mechanical Keyboard

<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="./files/media/iconwide.png" alt="vesuveus keyboard" width="500" style="border-radius: 10px;" />
</p>

Hey there! I present to you the Vesuveus, a small, ergonomic mechanical keyboard! 

This little wonder is heavily inspired by many amazing works of the community of the ergomech keyboard enthusiasts.

- [reddit](reddit.com/r/ErgoMechKeyboards) is a great place to start if you want to learn more about the world of ergonomic mechanical keyboards.

## What *is* the Vesuveus?
Vesuveus is a compact, pocketable keyboard with 40 keys that packs-a-punch! 

It's carefully designed to be your trusty sidekick for every task, whether you're coding, designing, gaming or just having some typing fun.

<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="./files/media/project.png" alt="vesuveus project" width="400" style="border-radius: 10px;" />
</p>
It's name /*vɛˈsuːviuəs*/ is derived by the volcano ___Vesuvius___ at Naples 🍕🤏.
<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="./files/media/vesuvius.jpg" alt="Mt. Vesuvius" width="400" style="border-radius:10px;" />
</p>

## The Design Philosophy

I've been admiring the world of mechanical keyboards for a while now, and I've wanted to make this project as an entry point for many that are scared to buy some expensive keyboard with the fear to not like it. I've been there, and I know how it feels. So, I wanted to make a keyboard that is:

- Affordable, so you can try it without breaking the bank.
- Ergonomic, so you can try the ergonomic world.
- Easy to build, so you can have fun while building it.
- Adaptable, so you can customize it to your needs.

Let's dive into the details of the design and see how I've achieved these goals!

## Why 40 Keys?

You might wonder why I settled on 40 keys, right? Well, I tried everything from 34 to 48 keys, and this magical 40-key layout is the sweet spot for me! Let me break it down for you:

- **34 or 36 layouts** are great for programmers and have a minimal footprint. But they drive me crazy when I switch to *mouse-centric* apps like Inkscape or PowerPoint. I need those modifier keys and an arrow cluster, man! That's why keyboards like the [bgkeeb](https://github.com/sadekbaroudi/bgkeeb) from sadekbaroudi and the [Sweep](https://github.com/davidphilipbarr/Sweep) by davidphilipbarr couldn't fully satisfy my needs.

<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="./files/media/34KeysLayout.jpg" alt="34-KeysLayout" width="400" style="border-radius:10px;"/>
</p>

- On the other hand, **46 or 48 layouts** feel like chaos and totally ignore the whole ergonomic idea. I mean, making my pinky press 4 to 6 keys? That's madness! Even with some cheats like using my ring finger for the top row, my pinky still ends up responsible for 4 keys. It just doesn't feel right and isn't ergonomic at all. I designed some keyboards with this layout, but I never felt comfortable using them; if you would like something the [Frame-48](https://github.com/gregsqueeb/Frame-48) by gregsqueeb is a great option.

<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="./files/media/48KeysLayout.png" alt="48-KeysLayout" width="400"/>
</p>

So, the **40-key layout** gives me the best of both worlds - it's usable, comfortable, and doesn't take up too much space. I believe it achieves the perfect balance between _usability_, _comfort_, and _dimensions_.

<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="./files/media/layout.svg" alt="Layout" width="400"/>
</p>

**Note**: I think that adding a extra side key for the pinky could be great (see the [TOTEM](https://github.com/GEIGEIGEIST/TOTEM) by GEIGEIGEIST layout) because we are accustomed to stretching the pinky sideways, but this would occupy more space on the desk and on the 3D printer, so I didn't feel to include that in this version. Maybe, in the future there will be a 42 keys version.

**Another Note**: When it comes to gaming, I've traditionally used the WASD keys for movement. However, due to the compact layout of Vesuveus, I've opted for the ESDF configuration instead. This tweak allows me to retain my muscle memory, one potential drawback is the intial configuration that i have to do when I install a new game. I did experiment with introducing a separate gaming layer, but found that it disrupted my workflow, especially when switching between gaming and other tasks. This decision was based on maintaining usability and minimizing the learning curve, making Vesuveus versatile for various uses. Feel free to customize your layout as needed!

## No Split? Hear Me Out!

Yep, Vesuveus is a **unibody design**, and I know you might be thinking, "Why not go split?" Well, here's the deal:

- **Split keyboards** have their perks, no doubt! I appreciate the adjustable positions that open your shoulders even more; it's all about that ergonomic goodness. But they come with their own set of drawbacks too - like dealing with multiple MCUs or tangled cables. Plus, when you're on the go like me, a unibody is a lifesaver! It's easy to carry around, and the angled configuration still keeps my shoulders happy. Oh, and it plays nice with the mouse too! The last thing I want is a twist game on my desk trying to reach my mouse.

### Atreus? Nah, I Got This!

Some folks might ask, "Why didn't you just get an Atreus?" Well, let me tell you:

- I like my **pinky stagger strong**, so Atreus's weaker stagger wouldn't be comfy for me.

- Gotta have that **classic arrow cluster** for my work, and Atreus didn't quite cut it for that. It's an essential part of my workflow, and I don't want to miss it.

- Also I wanted to make my tribute for the community challenging myself to design a keyboard from scratch.

So, I put my quirky preferences and design philosophies to work and created this perfect balance - ***Vesuveus***!
<p align="center" style="box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="./files/media//1stBuildRaffOwO.jpg" alt="vesuveus keyboard" width="400" style="border-radius: 10px;" />
</p>


## Why Handwired? Ain't Got Time for PCBs!

Now, I know some of you might wonder why I went handwired. Truth is, I'd love to make a PCB, but hey, learning Kicad takes time, and I'm busy creating magic with Vesuveus! Besides, there's a certain charm to handwiring - it's like crafting something special with your own hands.

**Note**: If you're interested in collaborating and working on PCBs or creating revisions with a tented nature, I'd be more than thrilled to team up! Let's improve Vesuveus together and explore new possibilities.

Still, once I have the knowledge and skill to manage Kicad, I would love to release a PCB version with some good-looking silkscreens!

## Tall and Proud: My Preference for Non-Low Profile

Ah, the low-profile trend! While it's true that low-profile keyboards are all the rage these days, I have to admit that I'm not a fan. I'm a sucker for that satisfying key travel, and low-profile switches just don't cut it for me. Sure, I love the sleekness of laptop keyboards, but I haven't found a low-profile switch with a smooth travel that feels great to me. Maybe I'm just picky, but hey, we all have our preferences!

Don't get me wrong; I understand the appeal of low-profile keyboards, especially when it comes to portability. And, yes, I've entertained the idea of creating a low-profile version of Vesuveus for the sake of being travel-friendly. But for now, it's not a priority in my design process.

Mathematically speaking, using low-profile switches could reduce the height of the keyboard by 0.7cm to 1cm, which might seem tempting. However, I believe that the sacrifice in key travel and typing experience isn't worth it for me. I want Vesuveus to be a powerhorse of comfort and usability, and that includes preserving that delightful key travel I cherish.

That being said, if you happen to come across a smooth af low-profile switch that could change my mind, please let me know! I'm always open to exploring new possibilities and refining Vesuveus to make it even better for the community of keyboard enthusiasts. So, for now, Vesuveus stands proud with its classic key switches, and I hope you'll still find it to be an amazing companion for your travels and everyday use! 😄

# Vesuveus in Action
In this video, you can witness the silent and satisfying keystrokes of the Vesuveus mechanical keyboard. Please note that the video was recorded with a smartphone, so the quality might not be top-notch, but the typing experience is!

[![Vesuveus in Action](https://img.youtube.com/vi/LMMimb1wSFk/0.jpg)](https://www.youtube.com/watch?v=LMMimb1wSFk)

Stay tuned for more videos and pictures of the Vesuveus in action as I continue to explore and improve this little wonder!

# Should You Try Vesuveus?

Hey, if my madness intrigues you, why not give Vesuveus a try? I'd be more than happy to include your contributions or ideas in this project! Feel free to get in touch, and let's make some keyboard magic together! 😄

You can find the build guide in the [files/README.md](./files/README.md) file.
