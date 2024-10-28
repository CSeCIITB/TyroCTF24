const express = require("express");
const path = require("path");
const app = express();
const bot = require("./bot");
const ejs = require("ejs");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  ejs.renderFile(
    path.join(__dirname, "index.ejs"),
    { totalPosts: 4, host: process.env.HOST },
    (err, str) => {
      if (err) {
        console.error(err);
        return res.status(500).send("Internal Server Error");
      }
      res.send(str);
    },
  );
});

app.get("/fetch", (req, res) => {
  res.sendFile(path.join(__dirname, "fetch.html"));
});

app.post("/visit", async (req, res) => {
  const { url } = req.body;

  if (!url) {
    return res.status(400).send("URL is required");
  }

  try {
    const validationResult = await bot.validateURL(url);
    if (!validationResult.success) {
      return res.status(400).send(validationResult.error);
    }

    res.send("Bot visiting " + url);

    bot.visit(url).catch((error) => {
      console.error("Error visiting URL:", error);
    });
  } catch (error) {
    console.error("Error:", error);
    res.status(500).send("Error occurred: " + error.message);
  }
});

app.get("/posts/0", (req, res) => {
  res.send(`
<style>a { color: red; }</style>
<h1>Choose Good Passwords</h1>

<p><strong>OK, this goes without saying... but 'password' is not a good password!</strong></p>

<h2>An ideal password must be:</h2>

<ul>
    <li><strong>Long:</strong> Less than 8 characters and it's easily crackable. Aim for 11+ characters. Bruteforcing a password gets exponentially harder with each extra character.</li>
    <li><strong>Symbols:</strong> Placing symbols does increase the security of the password. However, replacing 'e' with 3 is not gonna do as much as you expect. Do obscure stuff.</li>
    <li><strong>Avoid using common words:</strong> Try not to use any words that easily show up in regular conversation. Avoid popular words like 'Lightsaber' or 'Uranus'. This is to prevent something known as a 'dictionary attack' (explained later).</li>
    <li><strong>Has a lot of randomness:</strong> Weird passwords = harder to crack = safer.</li>
    <li><strong>Unique:</strong> <em>DO NOT REUSE YOUR PASSWORDS.</em></li>
</ul>

<p>A good resource for this is the computerphile video on choosing passwords: <a href="https://youtu.be/3NjQ9b3pgIg?si=_C0D_2EMlEPetlJw" target="_blank">Watch here</a>.</p>

<p><strong>"But dude," you might say, "I won't be able to remember all those passwords."</strong></p>

<p>Yes, sure, coming up and remembering unique passwords is inconvenient. But you know what else is inconvenient? Explaining to your friends that "No, I'm not a Nigerian prince in disguise."</p>

<p>This is where password managers come in. Instead of remembering so many passwords, you remember one very good password and let the password manager handle the rest: <a href="https://youtu.be/w68BBPDAWr8?si=jj_lMcLdhbr50CUO" target="_blank">Watch here</a>.</p>
`);
});

app.get("/posts/1", (req, res) => {
  res.send(`
<style>a { color: red; }</style>
<h1>Enable 2FA</h1>

<p><strong>Two-Factor Authentication, or 2FA, is a veryyyyyyy powerful tool.</strong></p>

<p>Even if your super-duper password is cracked (e.g., using keyloggers), 2FA will come in clutch to save you.</p>

<p>Aside from having something that only you know (i.e., your password), 2FA ties additional information to your account, making it more secure.</p>

<p>There are many implementations of 2FA, but the principle is the same.</p>

<p>Once again, the computerphile video on this topic is an amazing resource: <a href="https://youtu.be/ZXFYT-BG2So?si=TcdHl7fMLbtQJqdN" target="_blank">Watch here</a>.</p>
`);
});

app.get("/posts/2", (req, res) => {
  res.send(`
<style>a { color: red; }</style>
<h1>Do Not Click on Suspicious Links</h1>

<p><strong>Age-old wisdom:</strong> "If it looks suspicious, smells suspicious, and feels suspicious... delete the message."</p>

<p>Do not investigate. Depending on your system, you could get 'infected' by simply clicking the link once and not doing anything else.</p>

<p>Curiosity killed the cat, but satisfaction brought it back. That doesn't really apply here, cause the satisfaction you get from finding out that the link was actually a malicious link will quickly be followed by the realization that you clicked on a malicious link.</p>

<p>Additionally, don't fill out passwords on websites you suspect.</p>

<p>Phishing is a common attempt at trying to obtain credentials where the user creates a look-alike website (e.g., an Instagram clone), and when you enter your credentials there, it redirects you to the actual site and stores the entered information.</p>

<p>Password managers do help here. If your password manager is not auto-filling your password, you might want to check the link for suspicious stuff.</p>
`);
});

app.get("/posts/3", (req, res) => {
  res.send(`
<style>a { color: red; }</style>
<h1>Do Not Share Sensitive Information</h1>

<p><strong>Now this may seem obvious:</strong> Why would you just hand out your password to strangers?</p>

<p>The issue is, it's not always strangers that will be asking you for your password. Consider the following situation:</p>

<p>Your dumb friend (the same one who got hacked to sell snake oil) wants access to your Netflix account, and you, not trusting your friend's Instagram security, decide to mail the password.</p>

<p>Next day, your friend clicks on a malicious link in the mail and it steals all his mail data and sends it to some place. Next thing you know, your Netflix account and twenty other accounts that use a similar password are all taken over. And worse, the attackers are ruining the Netflix recommendation algorithm that you carefully fine-tuned. Oh, also they took over your Facebook account to sell snake oil, but more importantly, Netflix is now ruined for you.</p>

<p><strong>Moral of the story?</strong> <em>DO NOT REUSE YOUR PASSWORDS.</em> Also, don't share your passwords or any sensitive information for that matter. Even if you do everything else right, the person you shared stuff with might not have the same priority for security.</p>

<p><strong>Trust is for babies.</strong> Secure your stuff.</p>
`);
});

app.listen(3000, () => {
  console.log("Challenge is running on http://localhost:3000");
});
