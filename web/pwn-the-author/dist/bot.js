const { chromium } = require("playwright");

function sleep(s) {
  return new Promise((resolve) => setTimeout(resolve, s));
}

const browserArgs = {
  headless: (() => {
    return true;
  })(),
  args: [
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-gpu",
    "--no-gpu",
    "--disable-default-apps",
    "--disable-translate",
    "--disable-device-discovery-notifications",
    "--disable-software-rasterizer",
    "--disable-xss-auditor",
  ],
  ignoreHTTPSErrors: true,
};

let initBrowser = null;

async function getContext() {
  let context = null;
  if (initBrowser == null) initBrowser = await chromium.launch(browserArgs);
  context = await initBrowser.newContext();
  return context;
}

console.log("Bot started");

module.exports = {
  validateURL: async (url) => {
    if (!url) {
      return { success: false, error: "URL is required" };
    }

    try {
      const parsedUrl = new URL(url);
      if (parsedUrl.protocol !== "http:" && parsedUrl.protocol !== "https:") {
        return { success: false, error: "Invalid URL protocol" };
      }
      return { success: true };
    } catch {
      return { success: false, error: "Invalid URL format" };
    }
  },

  visit: async (urlToVisit) => {
    const context = await getContext();
    try {
      const page = await context.newPage();
      await context.addCookies([
        {
          name: "flag",
          value: process.env.FLAG,
          url: process.env.HOST,
          sameSite: "None",
          secure: true,
          httpOnly: false,
        },
      ]);

      console.log(`Bot visiting ${urlToVisit}`);
      await page.goto(urlToVisit, {
        waitUntil: "load",
        timeout: 10 * 1000,
      });
      await sleep(15000);

      await context.close();
      console.log("Browser closed");
      return { success: true };
    } catch (e) {
      console.error(e);
      return { success: false, error: e.message };
    } finally {
      await context.close();
    }
  },
};
