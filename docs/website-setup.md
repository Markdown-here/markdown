---
type: Guide
---

# Website setup

One-time steps to put [the website](website.md) online at `markdown.here`. Do them in order. Each part ends with a check, so you know it worked before you move on.

| Part | What | Time |
|---|---|---|
| [1. Turn on GitHub Pages](#1-turn-on-github-pages) | The site goes live at a `github.io` address | 5 minutes |
| [2. Move the repo to the organization](#2-move-the-repo-to-the-organization) | `thephm/markdown` becomes `Markdown-here/markdown` | 10 minutes |
| [3. Connect markdown.here](#3-connect-markdownhere) | DNS at Namecheap, then the domain in GitHub | 20 minutes, plus up to a day for DNS |

Everything here is free: GitHub Pages costs nothing for public repos, on personal accounts and free organizations.

## 1. Turn on GitHub Pages

1. Open the repo on GitHub and go to **Settings › Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**. There's no Save button; it saves right away.
3. Go to **Actions › Website** and click **Run workflow**, then **Run workflow** again.
4. Wait for the run to turn green, about 2 minutes **(verify)**.

**Check:** **Settings › Pages** now says "Your site is live at …", with an address like `https://thephm.github.io/markdown/`. Open it. The home page should say **Learn Markdown here**.

## 2. Move the repo to the organization

The organization `Markdown-here` is the long-term home. Moving the repo keeps every commit, branch, tag, release, issue, workflow, and setting. GitHub also redirects the old address, so old links and clones keep working.

GitHub organization names can't contain a dot, so the organization's address is `github.com/Markdown-here`, even though the site is `markdown.here`.

### Move it

1. In the repo, go to **Settings › General** and scroll to the bottom, **Danger Zone**.
2. Click **Transfer**.
3. Choose **Select one of my organizations**, then **Markdown-here**.
4. Type `thephm/markdown` to confirm, and click **I understand, transfer this repository**.

**Check:** the repo opens at <https://github.com/Markdown-here/markdown>, and <https://github.com/thephm/markdown> sends you there.

### Afterwards

1. **Organization settings:** in the organization, go to **Settings › Actions › General**. Under **Policies**, make sure actions are allowed, at least **Allow actions created by GitHub** plus the two the workflows use: `lycheeverse/lychee-action` and `softprops/action-gh-release`. **(verify)** these are allowed by default.
2. **Pages after the move:** open **Settings › Pages** in the moved repo. If **Source** isn't **GitHub Actions** anymore, set it again. **(verify)** whether it carries over.
3. **Your phone:** the clone on your phone still works through the redirect. To point it at the new address:

   ```bash
   git remote set-url origin https://github.com/Markdown-here/markdown.git
   ```

   Your fine-grained token is for `thephm/markdown` only. Make a new one for `Markdown-here/markdown` (see [Release a version](../RELEASING.md#2-make-a-github-token)). If the organization asks to approve tokens, approve it under the organization's **Settings › Personal access tokens › Pending requests**.
4. **Update the links in the repo:** about a dozen files still say `github.com/thephm/markdown`, including the slide footers and two places in `hugo.yaml` (`repo` and the GitHub menu item). Ask Claude to change them, or search the repo for `thephm/markdown`.

## 3. Connect markdown.here

Three steps: prove to GitHub that you own the domain, point the domain at GitHub, then tell the repo to use it. The DNS steps use **Namecheap**, where the domain is registered.

### 3a. Verify the domain with GitHub

This stops anyone else from using `markdown.here` with their own GitHub Pages site.

1. In GitHub, open the **organization** (not the repo): **Settings › Pages**.
2. Click **Add a domain**, type `markdown.here`, and click **Add domain**.
3. GitHub shows a **TXT record**: a host name that starts with `_github-pages-challenge-` and a long value. Keep this page open.
4. In a new tab, sign in to [Namecheap](https://www.namecheap.com/), go to **Domain List**, and click **Manage** next to `markdown.here`.
5. Open the **Advanced DNS** tab. Under **Host Records**, click **Add New Record**:

   | Type | Host | Value | TTL |
   |---|---|---|---|
   | TXT Record | `_github-pages-challenge-Markdown-here` (copy it from GitHub) | The value from GitHub | Automatic |

   Namecheap adds `.markdown.here` to the host by itself, so don't type it.
6. Click the green ✓ to save the row.
7. Back on GitHub, click **Verify**. If it says it can't find the record yet, wait 10 minutes and try again. It can take up to a day.

**Check:** the domain shows as **Verified** under the organization's **Settings › Pages**.

### 3b. Point the domain at GitHub

Still in Namecheap, on **Advanced DNS**:

1. **Remove Namecheap's parking records.** A new domain usually has a **CNAME Record** for `www` pointing to `parkingpage.namecheap.com`, and a **URL Redirect Record** for `@`. Delete both with the 🗑 icon. Leave the TXT record from 3a.
2. **Add these records**, one row each, with **Add New Record**:

   | Type | Host | Value |
   |---|---|---|
   | A Record | `@` | `185.199.108.153` |
   | A Record | `@` | `185.199.109.153` |
   | A Record | `@` | `185.199.110.153` |
   | A Record | `@` | `185.199.111.153` |
   | AAAA Record | `@` | `2606:50c0:8000::153` |
   | AAAA Record | `@` | `2606:50c0:8001::153` |
   | AAAA Record | `@` | `2606:50c0:8002::153` |
   | AAAA Record | `@` | `2606:50c0:8003::153` |
   | CNAME Record | `www` | `markdown-here.github.io.` |

   Leave TTL on **Automatic**. `@` means the domain itself. The addresses are GitHub's, from [Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site); check there if they've changed.
3. Save each row with the green ✓.

**Check:** wait 30 minutes, then look the domain up at <https://dnschecker.org/#A/markdown.here>. Most places should show the four `185.199.…` addresses. DNS can take up to a day to reach everywhere.

### 3c. Tell the repo to use the domain

1. In the repo, go to **Settings › Pages**.
2. Under **Custom domain**, type `markdown.here` and click **Save**. GitHub checks the DNS, which takes a minute or two.
3. When the check passes, tick **Enforce HTTPS**. If it's greyed out, GitHub is still getting a certificate. Come back in an hour; it can take up to a day.

You don't need a `CNAME` file in the repo. Sites published by a workflow keep the custom domain in settings only.

**Check:** open <https://markdown.here/>. You see the home page, with a padlock in the address bar. <https://www.markdown.here/> goes to the same place.

## Something went wrong

| Symptom | Cause | Fix |
|---|---|---|
| **Website** run fails at **Get the site address** | Pages isn't on, or is set to "Deploy from a branch" | Part 1: set Source to **GitHub Actions** |
| Run fails at **deploy** with a permissions error | The organization blocks the Pages actions | Organization **Settings › Actions › General**: allow actions created by GitHub |
| Run fails at **deploy** with "Branch is not allowed to deploy" | The `github-pages` environment only allows some branches | Repo **Settings › Environments › github-pages**: allow `main` |
| **Verify** says the TXT record isn't there | DNS hasn't spread yet, or the host has `.markdown.here` twice | Wait, then check the host in Namecheap is only `_github-pages-challenge-Markdown-here` |
| GitHub says "DNS check unsuccessful" | Records not there yet, or the parking records are still in place | Wait up to a day; delete the parking records (3b) |
| Enforce HTTPS stays greyed out | The certificate isn't ready | Wait up to a day. Remove and re-add the custom domain if it's still stuck |
| Browser shows a Namecheap parking page | Old records still cached | Wait, or try another network. Check the records at dnschecker.org |
| The site works but has no styles | The site was built for a different address | Run **Actions › Website › Run workflow** again after changing the domain |
