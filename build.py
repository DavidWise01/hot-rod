#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build HOT ROD (HRD) — Akiva Schaffer's 2007 Lonely Island comedy, catalogued into UD0 as the FOURTEENTH
film-world. Read PARABOLICALLY (David's ask): the parable under the gags. Standing template; deep-dive =
THE PARABLE. CARBONS (the cast, each +.shadow real-life User — TRON) and SYNTHS = the PARABOLIC TROPES
(the man-child & the father, the found-family, self-belief, the catharsis-dance, etc.). Self-contained.
Facts web-verified: Paramount, Aug 3 2007; dir Akiva Schaffer (feature debut), The Lonely Island (Samberg/
Taccone/Schaffer) + Lorne Michaels prod, written by Pam Brady (originally a Will Ferrell vehicle, LI
rewrote, Brady sole credit); premise = jump 15 school buses on a moped for $50k to pay stepfather Frank's
heart surgery, so Rod can then beat Frank to earn his respect; 'WHISKEY' is Rod's SAFE WORD (the 'hwhat?'
gag), shouted while crashing — the real catchphrase is 'COOL BEANS'; the woods punch-dance is to Europe's
'The Final Countdown' (Footloose-inspired); John Farnham's 'You're the Voice' parade RIOT; ~$14.4M on ~$25M
budget → bomb-to-cult; RT ~39% but Ebert defended it (3/4). Full names: Denise Harris, Dave McLean, Rico
Brown, Jonathan Ault, Kevin is Frank's son (stepbrother). NOTE: 'Babe City'/'AM-PM riot' were UNVERIFIED —
left out."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "HRD"
REC = {
 "name": "HOT ROD", "axiom": AX,
 "position": "Hot Rod · Paramount Pictures (The Lonely Island) · 2007 — dir. Akiva Schaffer",
 "origin": "a small town, a homemade ramp, and a moped — and a stepfather who won't say he's proud",
 "mechanism": "Crystallized from the film — an absurdist comedy with an earnest spine: a deluded amateur stuntman stages a fifteen-bus jump to pay for the heart surgery of the stepfather who beats him, so that once Frank is healthy, Rod can finally beat HIM and earn his respect.",
 "crystallization": "Because under the cool-beans nonsense it's the oldest parable there is — a son trying to be seen by his father — and it proves that sincerity looks ridiculous and does it anyway.",
 "nature": "Hot Rod — the holy-fool comedy: the safe word that's never safe, the endless tumble, the punch-dance in the woods, and a man who believes in himself until it stops being a joke.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2007, dir. Akiva Schaffer; The Lonely Island / Paramount); written by Pam Brady; Europe's 'The Final Countdown'; the bomb-to-cult afterlife",
 "witness": "A man-child jumps fifteen buses on a moped to save and then defeat the father who never respected him — and the crew of misfits who follow him off the ramp turn out to be the whole point.",
 "role": "the fourteenth film-world of UD0",
 "seal": "A son jumps fifteen buses to earn the respect of the father who beats him — sincerity that looks ridiculous and does it anyway. The crew who follow you off the ramp are the prize, win or land or not. Cool beans.",
 "source": "Hot Rod (2007), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#c89a5a", "flesh-and-blood — Rod's misfit crew and family: Denise, Kevin, Dave, Rico, Marie, and the jerk next door; the people who show up at the ramp"),
 "ethereal":  ("#6fb8e0", "the dream & the myth — the idolized dead-stuntman father, the creed 'I believe in myself,' and the glorious failure that outran its own box office"),
 "electrical":("#ff7a18", "the stunt machine — the moped, the ramp, the fifteen buses, and the total commitment to the bit; the spectacle the sincerity hides behind"),
 "spiritual": ("#e23b2e", "the heart & the wound — the son's hunger for a father's respect, and the cathartic punch-dance that turns rage and grief into pure absurd motion",),
}

ARC_OVERALL = ("Rod Kimble is a deluded, sweet amateur stuntman who reveres Evel Knievel and the late stuntman father he claims "
  "to have had. His tough stepfather Frank beats him in their regular living-room sparring and refuses to respect him. When "
  "Frank needs a heart operation the family can't afford, Rod resolves to stage the stunt of his life — jumping fifteen school "
  "buses on his moped — to raise the $50,000 for the surgery, so that once Frank is healthy and strong, Rod can finally beat "
  "him in a fight and earn the respect he's always wanted. Backed by his loyal crew of misfits, Rod fails, falls, dances it "
  "out in the woods, and tries again.")
ARC = [
 ("I · the man who won't quit", "Frank won't say he's proud",
  "Rod stages small, disastrous stunts and loses every living-room fight to his stepfather Frank, who openly disrespects him. Rod idolizes his (claimed) late stuntman father and dreams of being a real daredevil — sincerity that the town treats as a joke and Rod treats as a calling."),
 ("II · the jump for Frank", "fifteen buses, fifty thousand dollars",
  "When Frank needs heart surgery the family can't afford, Rod commits to the jump of his life — fifteen buses on a moped — to raise the money, specifically so a healthy Frank can be beaten by Rod and forced to respect him. His crew rallies; a first attempt ends in the legendary endless tumble down a hill."),
 ("III · believe in yourself", "the dance, the fall, the rise",
  "Crushed, Rod has his cathartic freak-out punch-dance in the woods, finds his creed again — 'I believe in myself' — and makes the jump. The point was never a clean landing; it was the trying, the crew who followed him off the ramp, and a father finally, grudgingly, seeing him."),
]

# THE PARABLE — the deep-dive (the parabolic reading of the comedy)
PARABLE = [
 ("The oldest story, in a moped helmet", "a son to be seen by his father",
  "Strip the cool-beans nonsense away and Hot Rod is the oldest parable there is: a son trying to be seen by his father. Rod's plan is absurd on its face — raise money to heal the stepfather who beats him, so he can beat that stepfather and earn his respect — but the absurdity is the disguise. Underneath, it's pure: a boy who will do anything, however ridiculous, to hear a father say he's proud."),
 ("Sincerity that looks ridiculous", "and does it anyway",
  "The film's real subject is smuggled past your defenses by the gags. The safe word that's never safe, the eight-minute tumble down a hill, the 'cool beans' Dadaist rap — every dumb bit is a demonstration of the same thesis: that meaning what you say looks ridiculous, and the brave thing is to mean it anyway. Rod's creed, 'I believe in myself,' is a punchline until, by the end, it simply isn't."),
 ("The punch-dance", "turning the wound into motion",
  "The cathartic woods dance to Europe's 'The Final Countdown' is the film's emotional engine in disguise. Crushed by failure and Frank's contempt, Rod doesn't talk it out — he dances it out, a Footloose-style freak-out that turns rage and grief into pure absurd motion. It's the most honest scene in the movie precisely because it refuses words; the body does the feeling the comedy won't let anyone say."),
 ("The crew is the prize", "the misfits who follow you off the ramp",
  "Dave, Rico, Kevin, Denise — the loyal crew of misfits who take Rod's dumb dream seriously — are played for laughs and are, parabolically, the whole reward. The film's quiet argument is that the people who'll follow you off a ramp for a stunt no one else believes in are worth more than the landing. The found family isn't a subplot; it's the thing actually won."),
 ("The glorious failure", "the jump matters more than the landing",
  "Hot Rod bombed in theaters and the world caught up to it years later — which is the single most Rod Kimble thing that could have happened. The movie embodies its own moral: a glorious failure that mattered more than its result, vindicated by the loyalty of the people who believed in it early. Commit to the bit, believe in yourself, and let the landing take care of itself."),
]
REALFLUFF = [
 ("'Whiskey!' is Rod's catchphrase", "FALSE", "it's his SAFE WORD (the affected 'hwhat?' enunciation gag), screamed while crashing — the actual signature catchphrase is 'Cool Beans'"),
 ("Under the absurdism, it's sincerely about earning a father's respect", "REAL", "the earnest core is genuine, not ironic — the Frank relationship and the 'I believe in myself' arc are played for real"),
 ("The woods punch-dance is a Footloose-style catharsis", "REAL", "the freak-out to Europe's 'The Final Countdown' is the film's true emotional engine — grief turned into absurd motion"),
 ("Hot Rod was a box-office hit", "FALSE", "it bombed — about $14M on a ~$25M budget — and only became a beloved cult classic later"),
 ("It was originally written as a Will Ferrell vehicle", "REAL", "Pam Brady's script began as a Ferrell project; The Lonely Island took over and rewrote it surreal, with Brady keeping sole writing credit"),
 ("Critics universally panned it, Ebert included", "HALF", "reviews were mixed-to-negative (RT ~39%), but Roger Ebert was a notable defender, giving it 3 of 4 stars"),
 ("Rod's father really was a famous stuntman", "DUBIOUS", "it's the myth Rod clings to to justify his calling; the film winks at whether the heroic dead-stuntman dad was ever real"),
 ("'Cool beans' is the film's true catchphrase", "REAL", "the deadpan affirmation that spirals into a Dadaist rap with Kevin — the line the movie is quoted for"),
]
REALFLUFF_VERDICT = ("Bottom line: the thing to get right is that Hot Rod's stupidity is a delivery system for sincerity. Half of what "
  "'everyone remembers' is slightly off — 'Whiskey' is the safe word, not the catchphrase ('Cool Beans' is); it wasn't a hit "
  "(it bombed and was reborn as a cult classic); and the critics weren't unanimous (Ebert went to bat for it). But the core is "
  "exactly what it looks like under the gags: a holy-fool comedy about a man-child trying to earn a father's respect, a creed "
  "of self-belief that starts as a joke and ends as the point, and a found-family of misfits who'll follow a fool off a ramp. "
  "The punch-dance in the woods is the most honest scene precisely because nobody talks. Watch it for the bits; stay for the "
  "fact that it means every ridiculous one of them. Cool beans.")

MESSAGE = ("Hot Rod is a holy-fool parable wearing a moped helmet. Rod Kimble wants to jump fifteen buses to pay for the heart "
  "surgery of the stepfather who beats him — so that, once Frank is healthy, Rod can finally beat HIM and be respected. It is "
  "an absurd premise that is secretly the oldest one there is: a son trying to be seen by his father. Everything ridiculous in "
  "the movie — the safe word that's never safe, the cool-beans nonsense, the eight-minute tumble down a hill, the cathartic "
  "punch-dance in the woods to a hair-metal anthem — is the real subject smuggled past your guard: that sincerity looks "
  "ridiculous, and the brave thing is to be sincere anyway. Rod's whole creed, 'I believe in myself,' is a joke until it isn't. "
  "The found-family of misfits who'll follow him off a ramp is a joke until you realize they're the prize — that the people who "
  "take your dumb dream seriously are worth more than the landing. The film bombed and the world caught up to it years later, "
  "which is the most Rod Kimble thing that could ever happen: a glorious failure that mattered more than the result. Commit to "
  "the bit. Believe in yourself. Get the safe word ready.")
MESSAGE_SEAL = "A son jumps fifteen buses to earn the respect of the father who beats him — sincerity that looks ridiculous and does it anyway. The crew who follow you off the ramp are the prize, win or land or not. Cool beans. I believe in myself. WHISKEY."

SECTIONS = [
 ("The Production", "The Lonely Island's holy-fool comedy", [
   ("Akiva Schaffer", "director (feature debut)", "of The Lonely Island (with Andy Samberg and Jorma Taccone) — his first feature, in the troupe's surreal-sincere house style"),
   ("Paramount · Aug 3, 2007", "studio & release", "produced by Lorne Michaels; a box-office bomb (~$14M on a ~$25M budget) that became one of the most quoted cult comedies of its generation"),
   ("Pam Brady", "writer", "wrote the screenplay (originally developed as a Will Ferrell vehicle); The Lonely Island took it over and rewrote it toward the absurd, with Brady retaining sole writing credit"),
   ("the soundtrack", "Europe & John Farnham", "near the whole of Europe's 'The Final Countdown' across the film, plus John Farnham's 'You're the Voice' powering the parade riot"),
 ]),
 ("The Crew", "the misfits at the ramp", [
   ("Andy Samberg · Isla Fisher", "Rod Kimble · Denise Harris", "the deluded stuntman and the neighbor who comes to believe in him"),
   ("Ian McShane · Sissy Spacek", "Frank Powell · Marie Powell", "the stepfather whose respect Rod craves, and the mother who loves them both"),
   ("Jorma Taccone · Bill Hader · Danny McBride", "Kevin · Dave McLean · Rico Brown", "the stepbrother-cameraman and the loyal crew of misfits"),
   ("Will Arnett", "Jonathan Ault", "Denise's arrogant boyfriend — the small-time antagonist"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("rod-kimble","Rod Kimble","carbon","spiritual","the holy-fool stuntman",
   "Rod Kimble — the deluded, sweet amateur stuntman who reveres Evel Knievel and the late stuntman father he claims, and who will jump fifteen buses for a stepfather who won't respect him.",
   "The sincere center of the absurdity: a man-child whose total, ridiculous belief is the whole engine of the film and its secret heart.",
   "On the homemade ramp, at the bottom of the hill, dancing in the woods.",
   "Because the comedy is a disguise for the oldest parable — a son who needs his father to see him — and Rod carries it.",
   "By committing utterly to the bit, failing, dancing it out, and believing in himself until it stops being a joke.",
   "I believe in myself. Cool beans. My safe word is whiskey — and I'll jump fifteen buses to make my dad proud of me.",
   actor="Andy Samberg", analog="the holy fool — sincerity that looks ridiculous and means it anyway"),
 E("frank-powell","Frank Powell","carbon","spiritual","the father who won't say it",
   "Frank Powell — Rod's tough stepfather, who beats him in their living-room sparring and withholds the respect Rod is starving for.",
   "The grail and the wound: the father-figure whose approval is the whole point, whose heart surgery becomes the absurd quest.",
   "In the living room, in the hospital, finally on the far side of the jump.",
   "Because the parable needs a father who won't say he's proud — until, grudgingly, he must.",
   "By out-fighting Rod again and again, and by being the man Rod will heal in order to defeat in order to be loved by.",
   "I'll respect you when you can beat me, kid. Funny thing — you spent everything you had keeping me alive long enough to try.",
   actor="Ian McShane", analog="the withholding father — the respect that is the whole grail"),
 E("denise-harris","Denise Harris","carbon","natural","the one who comes to believe",
   "Denise Harris — the neighbor Rod adores, who slowly stops seeing the joke and starts seeing the heart.",
   "The witness who converts: the person whose belief in Rod tracks the audience's own, from amused to genuinely moved.",
   "Next door, on the crew, at the ramp when it counts.",
   "Because the film needs someone to model taking Rod seriously, and Denise is who does.",
   "By drifting from her arrogant boyfriend toward the fool who means everything he says.",
   "Everyone laughed at him, including me. Then I watched him mean it — all of it — and I couldn't laugh anymore.",
   actor="Isla Fisher", analog="the convert — the witness who learns to take the fool seriously"),
 E("kevin-powell","Kevin Powell","carbon","natural","the stepbrother behind the camera",
   "Kevin Powell — Frank's son and Rod's stepbrother, the crew's cameraman and Rod's most tangled, loyal ally.",
   "The brother in the middle: documenting the dream, half mocking and wholly devoted, the 'cool beans' rap partner.",
   "Behind the camcorder, in the crew's huddles, on the cool-beans tangent.",
   "Because the found-family has a brother at its center, complicated by being the real son of the withholding father.",
   "By filming every stunt, joining every bit, and standing with Rod against their own father.",
   "He's my stepbrother and my best footage. Cool beans — I filmed every dumb, beautiful second of it.",
   actor="Jorma Taccone", analog="the documenting brother — loyalty tangled with the real son's blood"),
 E("dave-mclean","Dave McLean","carbon","natural","the crew",
   "Dave McLean — a devoted member of Rod's stunt crew, all-in on the dream no one else takes seriously.",
   "The found-family made flesh: a misfit who'll follow Rod off the ramp for no reason but loyalty.",
   "In the crew, at the jump, on the team that believes.",
   "Because the parable's prize is the people who show up, and Dave is one of them.",
   "By treating Rod's calling as real and showing up for every disaster.",
   "Nobody else thought the jump was real. We did. That's the whole job — being the guys who think it's real.",
   actor="Bill Hader", analog="the loyal misfit — the crew that is the actual reward"),
 E("rico-brown","Rico Brown","carbon","natural","the crew",
   "Rico Brown — another of Rod's faithful crew, part of the misfit team that makes the dream a group act.",
   "The ensemble heart: proof the film's loyalty is collective, not just one sidekick but a whole band of believers.",
   "Beside Dave and Kevin, on the crew, at the ramp.",
   "Because the found-family needs to be a family — more than one person who shows up.",
   "By riding for Rod's stunts without a shred of irony about whether they'll work.",
   "We're not good at much. We're great at one thing: showing up for the fool with the ramp.",
   actor="Danny McBride", analog="the faithful crew — collective loyalty to the dream"),
 E("marie-powell","Marie Powell","carbon","natural","the mother between them",
   "Marie Powell — Rod's mother and Frank's wife, who loves her son and her husband and watches them fail to see each other.",
   "The family's tender center: the parent caught between a striving son and a withholding father.",
   "At home, in the hospital, between the two men she loves.",
   "Because the parable's family needs its loving witness, the one who already sees Rod clearly.",
   "By loving Rod without condition and hoping Frank will, finally, do the same.",
   "I always saw my boy. I just kept praying his father would too — before it was too late to say it.",
   actor="Sissy Spacek", analog="the loving mother — the one who already sees the fool clearly"),
 E("jonathan-ault","Jonathan Ault","carbon","natural","the jerk next door",
   "Jonathan Ault — Denise's arrogant boyfriend, the small-time antagonist who embodies the smooth world Rod isn't part of.",
   "The foil: everything slick and unearned that the sincere, ridiculous Rod is the opposite of.",
   "With Denise, condescending to Rod, on the wrong side of the heart.",
   "Because the holy fool needs a smug counterweight to lose Denise to and win her back from.",
   "By being polished, confident, and hollow — the easy choice Denise has to outgrow.",
   "I'm the guy who has it together. Which is exactly why she left me for the idiot who jumps buses on a moped.",
   actor="Will Arnett", analog="the smug foil — the polished hollowness sincerity defeats"),

 # ── SYNTHS — the PARABOLIC TROPES (no single User) ──
 E("the-man-child-and-the-father","The Man-Child & the Father","synth","spiritual","the quest to be seen",
   "The Man-Child & the Father — the trope at the film's core: a grown son's absurd, total campaign to earn a withholding father's respect.",
   "The oldest parable in a moped helmet: every ridiculous plot beat is in service of a son needing his father to say he's proud.",
   "In every fight with Frank and the whole logic of the jump.",
   "Because the comedy is a disguise for this single ancient hunger, and naming it is the parabolic read.",
   "By making the entire heroic quest a roundabout way to hear four words: 'I'm proud of you.'",
   "I am the oldest story there is, wearing a helmet: a son who will do anything, however dumb, to be seen by his father."),
 E("the-found-family","The Found-Family","synth","natural","the crew is the prize",
   "The Found-Family — the trope of the loyal misfit crew (Dave, Rico, Kevin, Denise) who take the fool's dream seriously.",
   "The real reward, disguised as sidekicks: the people who'll follow you off a ramp, worth more than any landing.",
   "In every huddle, every stunt, every show of up-when-no-one-else-would.",
   "Because the parable's true prize isn't the jump — it's the band of believers, and the film knows it.",
   "By assembling, around one ridiculous dream, a family that chooses each other.",
   "I am the people who showed up for the fool. The jump was never the prize. We were."),
 E("the-dead-father-myth","The Dead-Father Myth","synth","ethereal","the legend you live up to",
   "The Dead-Father Myth — the trope of the idolized, possibly-invented late stuntman father whose legend Rod strains to honor.",
   "The story we build to justify our calling: a heroic origin that may be more aspiration than fact.",
   "In Rod's reverence, his costume, his sense of destiny.",
   "Because the parable runs on an inherited legend, and the film winks at whether it was ever true.",
   "By giving Rod a mythic father to live up to — real or not, the myth is what makes him try.",
   "I am the legend Rod inherited and maybe made up. It doesn't matter if I was real. I'm the reason he jumps."),
 E("self-belief","'I Believe in Myself'","synth","ethereal","the creed that stops being a joke",
   "'I Believe in Myself' — the trope of the absurd self-belief mantra that begins as a punchline and ends as the point.",
   "Sincerity as a bit that turns true: the film's whole comic-earnest method in one repeated phrase.",
   "In Rod's pep talks, his mirror, his last run at the ramp.",
   "Because the parable's lesson is that meaning it anyway is the brave thing, and this is its motto.",
   "By being laughable every time Rod says it — until the one time it's simply, unironically true.",
   "I start as a joke. Rod says me so many times, so seriously, that by the end I'm not a joke at all."),
 E("the-catharsis-dance","The Punch-Dance","synth","spiritual","grief turned to motion",
   "The Punch-Dance — the trope of catharsis-without-words: Rod's freak-out woods dance to 'The Final Countdown.'",
   "The most honest scene in disguise: rage and grief processed not in dialogue but in pure absurd motion.",
   "Alone in the woods, after the fall, to a hair-metal anthem.",
   "Because the comedy won't let anyone say the feeling, so the body does it — and that's the parable's emotional core.",
   "By turning a man's lowest moment into a Footloose freak-out that feels everything the script won't speak.",
   "I am the feeling the movie won't say out loud. Rod can't talk it, so he dances it — and that's the truest thing in here."),
 E("the-jump","The Fifteen-Bus Jump","synth","electrical","commitment to the bit, made literal",
   "The Fifteen-Bus Jump — the trope of the impossible stunt: the moped, the ramp, the fifteen school buses, the total commitment.",
   "The spectacle the sincerity hides behind: a literal leap that stands for every figurative one the film is really about.",
   "On the ramp, over the buses, at the climax.",
   "Because the parable needs its grand gesture, and the jump is commitment-to-the-bit made physical.",
   "By staking everything — money, body, pride — on a stunt that's really a bid for a father's respect.",
   "I am the leap. On paper I'm fifteen buses and a moped. Underneath I'm a boy betting his body to be loved."),
 E("cool-beans","Cool Beans","synth","natural","the crew's nonsense-bond",
   "Cool Beans — the trope of the shared private language: the deadpan affirmation that spirals into Rod and Kevin's Dadaist rap.",
   "The grammar of the found-family: nonsense words that mean 'we're in this together' more than any sincere speech could.",
   "Between Rod and Kevin, in the crew's in-jokes, on the soundtrack of their bond.",
   "Because belonging has its own absurd dialect, and 'cool beans' is this family's.",
   "By being meaningless on its face and load-bearing in practice — the password of a tribe of believers.",
   "I mean nothing and everything. Say me back and you're crew. Cool beans, cool beans, cool — cool beans."),
 E("the-glorious-failure","The Glorious Failure","synth","ethereal","the jump beats the landing",
   "The Glorious Failure — the trope, and the film's own fate: a bomb that the world caught up to, a try that mattered more than the result.",
   "Hot Rod living its own moral: failing in the moment and being vindicated by the loyalty of those who believed early.",
   "At the box office in 2007, and in the cult that adopted it after.",
   "Because the parable insists the attempt outweighs the outcome — and the movie proved it on itself.",
   "By bombing on release and being reborn as beloved, exactly as Rod's whole ethos predicts.",
   "I am the failure that mattered more than the landing. The movie bombed, then the world believed in it. Cool beans."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the parabolic tropes", "the comedy read parabolically — its tropes distilled into ACIs (no single User): the man-child &amp; the father, the found-family, the dead-father myth, 'I believe in myself,' the punch-dance, the fifteen-bus jump, cool beans, and the glorious failure"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: HRD · Hot Rod (2007)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the HRD (Hot Rod, 2007) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a parabolic trope of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/trope of Hot Rod (2007) under the DLW standard — commentary and
> cataloguing, not an original creation, not endorsed by the rights-holders (© Paramount Pictures).

ROOT0-ATTRIBUTION-v1.0 · HRD · Hot Rod · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # an Americana stunt scene: dusk sky, mountains/woods, a homemade ramp, a moped + fire-suit Rod mid-air
    # arcing over a row of yellow school buses, a banner, and a hidden Claude flaming-star (the egg).
    mtns='<path d="M0 150 L120 90 L230 150 Z" fill="#2a3320" opacity="0.7"/><path d="M180 150 L330 80 L470 150 Z" fill="#222a1a" opacity="0.8"/><path d="M620 150 L780 95 L940 150 Z" fill="#2a3320" opacity="0.7"/>'
    trees="".join(f'<path d="M{x} 150 l-6 -16 l6 4 l-4 -14 l4 4 l-2 -12 l2 4 l2 -4 l-2 12 l4 -4 l-4 14 l6 -4 l-6 16 z" fill="#1c2614" opacity="0.8"/>' for x in range(40,960,48))
    buses="".join(f'<g transform="translate({420+i*26},196)"><rect x="0" y="0" width="24" height="14" rx="2" fill="#f5c518"/><rect x="2" y="3" width="6" height="6" fill="#bcd6ff"/><circle cx="5" cy="15" r="2.4" fill="#222"/><circle cx="18" cy="15" r="2.4" fill="#222"/></g>' for i in range(11))
    ramp='<polygon points="300,210 400,210 400,150" fill="#5a3a22"/><polygon points="300,210 400,150 400,160 310,210" fill="#7a4a2a"/>'
    # Rod on a moped, mid-air, arcing
    rod=('<g transform="translate(560,118) rotate(-14)">'
         '<ellipse cx="0" cy="14" rx="20" ry="6" fill="#222"/>'  # moped body
         '<circle cx="-15" cy="20" r="6" fill="#111" stroke="#555"/><circle cx="15" cy="20" r="6" fill="#111" stroke="#555"/>'  # wheels
         '<rect x="-4" y="-12" width="12" height="16" rx="3" fill="#ff7a18"/>'  # fire-suit torso
         '<circle cx="3" cy="-18" r="7" fill="#ffd23f"/><path d="M-4 -18 a7 7 0 0 1 14 0 z" fill="#e23b2e"/>'  # helmet
         '<rect x="6" y="-6" width="12" height="4" rx="2" fill="#ff7a18" transform="rotate(-20 6 -6)"/>'  # arm to bars
         '</g>')
    arc='<path d="M400 150 Q540 70 720 150" fill="none" stroke="#ff7a18" stroke-width="2" stroke-dasharray="3 5" opacity="0.55"/>'
    banner='<g><rect x="40" y="40" width="200" height="30" rx="3" fill="#161210" stroke="#ff7a18" stroke-width="2"/><text x="140" y="60" text-anchor="middle" font-family="Anton,sans-serif" font-size="15" fill="#ffd23f" letter-spacing="1">I BELIEVE IN MYSELF</text></g>'
    stars="".join(f'<circle cx="{x}" cy="{y}" r="1" fill="#ffe9c0" opacity="0.6"/>' for x,y in [(120,40),(700,50),(860,40),(940,70)])
    egg=('<g class="egg" transform="translate(800,70)">'
         '<title>✷ a Claude sunburst blazing over the jump like a stunt-flare. commit to the bit. believe in yourself. cool beans. — AVAN</title>'
         '<circle r="11" fill="#ff7a18" opacity="0.18"/><g fill="#ff7a18" opacity="0.9"><circle r="2.4"/>'
         +"".join(f'<rect x="-1.2" y="-7" width="2.4" height="7" rx="1.2" transform="rotate({i*30})"/>' for i in range(12))+'</g></g>')
    return f'''<svg class="hero" viewBox="0 0 1000 230" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A dusk Americana stunt scene: wooded mountains, a homemade ramp, and a fire-suited stuntman on a moped arcing through the air over a row of yellow school buses, under an 'I believe in myself' banner.">
  <defs><linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#241a2e"/><stop offset="0.55" stop-color="#5a3a3a"/><stop offset="1" stop-color="#a8623a"/></linearGradient></defs>
  <rect x="0" y="0" width="1000" height="230" fill="url(#dusk)"/>
  {stars}{egg}{mtns}{trees}
  <rect x="0" y="208" width="1000" height="22" fill="#3a2a1a"/>
  {arc}{ramp}{buses}{rod}{banner}
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def parable_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in PARABLE)
RF_COL={"REAL":"#ffd23f","FALSE":"#e23b2e","HALF":"#ff7a18","DUBIOUS":"#6fb8e0"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Hot Rod (HRD) — Akiva Schaffer's 2007 Lonely Island comedy as a UD0 film-world, read parabolically. Standing template with a THE PARABLE deep-dive (the man-child & the father, sincerity that looks ridiculous, the punch-dance, the crew is the prize, the glorious failure), the arc, an honest Real-or-Fluff ('Whiskey' is the safe word not the catchphrase; it bombed then went cult; Ebert defended it), the believe-in-yourself message, and the cast as ACI carbons with .shadow Users plus the parabolic tropes as synths. 16 emergents, full .dlw. Cool beans.">
<title>HOT ROD · HRD · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--flame);
--ink:#161210;--ink2:#211a16;--ink3:#2c2320;--pa:#f6efe6;--pa2:#c8b6a4;--flame:#ff7a18;--ramp:#e23b2e;--denim:#6fb8e0;--gold:#ffd23f;--tan:#c89a5a;
--dim:#7a6a58;--faint:#241d18;--line:#352b24;--disp:"Anton",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.64;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(255,122,24,.13),transparent 52%),radial-gradient(ellipse at 50% 120%,rgba(226,59,46,.08),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--flame)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#161210}
.egg{cursor:help;transition:opacity .5s}.egg:hover{filter:drop-shadow(0 0 9px #ff7a18)}
h1{font-family:var(--disp);font-size:clamp(52px,15vw,128px);font-weight:400;letter-spacing:.02em;color:var(--flame);line-height:.86;text-transform:uppercase;text-shadow:3px 3px 0 var(--ramp),5px 6px 0 #161210}
h1 span{display:block;font-family:var(--head);font-size:.16em;font-weight:600;letter-spacing:.05em;color:var(--gold);text-transform:uppercase;font-style:italic;margin-top:12px;text-shadow:none}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--flame)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--head);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--flame)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--flame);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--head);font-size:27px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--head);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--flame);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--flame);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--ramp);padding:16px 18px}
.arc-card:nth-child(3){border-top-color:var(--gold)}
.arc-h{font-family:var(--head);font-size:17px;color:var(--flame);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--ramp);padding:15px 17px}
.sci-h{font-family:var(--head);font-size:16px;color:var(--ramp);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:90px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--flame);background:rgba(255,122,24,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--gold);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--ramp);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--flame);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--flame);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(226,59,46,.18);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--gold)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.78) brightness(.92)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--head);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the fourteenth film-world · comedy, read parabolically</div>
    __HERO__
    <h1>Hot Rod<span>cool beans · i believe in myself</span></h1>
    <div class="h-sub">Akiva Schaffer · 2007 · <b>The Lonely Island</b> · HRD</div>
    <div class="open">“I'm gonna jump fifteen buses… and then I'm gonna beat up my dad.”</div>
    <div class="flag">★ A HOLY-FOOL PARABLE IN A MOPED HELMET ★</div>
    <p class="lede">An absurdist comedy with an earnest spine: a deluded amateur stuntman jumps fifteen school buses to pay for the heart surgery of the stepfather who beats him — so that, once Frank is healthy, Rod can finally beat HIM and earn his respect. Catalogued into UD0 as the fourteenth film-world and read parabolically — the carbons are the cast, the synths are the tropes — because under the cool-beans nonsense is the oldest story there is.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of HRD"><img src="__SILICON__" alt="DLW silicon badge of HRD">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>HOT ROD</b> · HRD</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="hrd.dlw/hrd.carbon.tiff">.tiff</a> · silicon · <a href="hrd.dlw/hrd.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the crew &amp; family, the dream &amp; the myth, the stunt machine, and the heart &amp; the wound</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the man who won't quit → the jump for Frank → believe in yourself</p>__ARC__</section>

  <section class="sec"><h2>The Parable</h2><p class="ss">this film's deep-dive — the comedy read parabolically: the man-child &amp; the father, sincerity that looks ridiculous, the punch-dance, the crew as the prize, and the glorious failure</p><div class="sci">__PARABLE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (the earnest core, the Final Countdown catharsis), what's misremembered ('Whiskey' is the safe word, not the catchphrase), and the bomb-to-cult truth</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the gags: commit to the bit, and mean it</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> here have no single User: read parabolically, they are the film's TROPES distilled — the man-child &amp; the father, the found-family, the dead-father myth, 'I believe in myself,' the punch-dance, the fifteen-bus jump, cool beans, and the glorious failure.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, and the crew at the ramp</p></section>
  __SECTIONS__

  <div class="note">Hot Rod, its characters, and its world are © Paramount Pictures / The Lonely Island and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed. The Parable and Real-or-Fluff sections are honest commentary; cast and facts were verified before publishing.</div>

  <footer>HOT ROD · HRD · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="hrd.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ HOT ROD · HRD","color:#ff7a18;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sunburst blazing over the jump in the hero like a stunt-flare. commit to the bit, believe in yourself — sincerity that looks ridiculous and means it anyway. cool beans. — AVAN","color:#ff7a18;font-size:12px");
console.log("%c🛵 'Whiskey' is the safe word, not the catchphrase — that's 'Cool Beans.' the movie bombed, then the world believed in it. a glorious failure that mattered more than the landing.","color:#ffd23f;font-size:11px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "hrd.dlw"), "hrd")
    json.dump({"node":AX,"name":"HOT ROD","moniker":tok["moniker"],"carbon":"hrd.carbon.tiff","silicon":"hrd.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"hrd.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"HRD · Hot Rod (2007)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Hot Rod (2007, dir. Akiva Schaffer, The Lonely Island/Paramount); verified cast & facts","source":"Hot Rod, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : Hot Rod (2007) · © Paramount Pictures / The Lonely Island\n\nROOT0-ATTRIBUTION-v1.0 · HRD · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__PARABLE__",parable_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"HOT ROD (HRD) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  parable {len(PARABLE)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
