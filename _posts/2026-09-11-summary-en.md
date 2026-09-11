---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 29 items, 13 important content pieces were selected

---

1. [Rust Becomes a Tier-1 Language at Microsoft](#item-1) ⭐️ 9.0/10
2. [Shopify Reverts to Native Development with Swift and Kotlin](#item-2) ⭐️ 8.0/10
3. [OpenAI Launches Flexible Agents API for AI Deployment](#item-3) ⭐️ 8.0/10
4. [Cognition Unveils SWE-2 Model to Compete with Fable 5.1 and GPT-Astra](#item-4) ⭐️ 8.0/10
5. [Critical RCE Vulnerability Fixed in Forgejo <=16.0.3](#item-5) ⭐️ 8.0/10
6. [Challenges of Using AI Models like Astra for Coding](#item-6) ⭐️ 8.0/10
7. [Anthropic's September 2026 Report on AI Misuse](#item-7) ⭐️ 8.0/10
8. [Run Any Nix Package in Your Browser with Trynix.dev](#item-8) ⭐️ 8.0/10
9. [NASA Technique Reveals Ancient Images in Satellite Photos](#item-9) ⭐️ 7.0/10
10. [PlanetScale Introduces Neki: A Sharded Postgres Solution](#item-10) ⭐️ 7.0/10
11. [Proof of Capture: Apple Reference Image, but open source and using steganography](#item-11) ⭐️ 7.0/10
12. [Datasette Releases Security Patches for Alpha and Stable Versions](#item-12) ⭐️ 7.0/10
13. [ACL Implements New Sustainable Reviewing Policy](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Rust Becomes a Tier-1 Language at Microsoft](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

Rust has been elevated to a tier-1 language at Microsoft, joining the ranks of C++, C#, and TypeScript. This change signifies Microsoft's strong endorsement of Rust for internal development. This elevation underscores Rust's growing importance and maturity in systems programming, potentially influencing other companies to adopt Rust for safer and more efficient software development. It highlights Microsoft's commitment to modernizing its codebase with secure and performant languages. As a tier-1 language, Rust will receive the same level of support and tooling as other major languages at Microsoft. This includes integration with Microsoft's development environments and support for Rust in their production workflows.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a systems programming language known for its performance, safety, and concurrency features. It was created by Graydon Hoare and officially sponsored by Mozilla before being managed by the Rust Foundation. Rust's memory safety without a garbage collector makes it particularly appealing for system-level programming. Microsoft has been integrating Rust into its ecosystem, reflecting a broader industry trend towards safer programming practices.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>
<li><a href="https://www.theregister.com/devops/2026/09/11/microsoft-annoints-rust-as-a-tier-1-internal-language/5295732">Microsoft annoints Rust as a 'Tier 1' internal language</a></li>

</ul>
</details>

**Discussion**: Community members are excited about Rust's elevation, noting its maturity and potential to replace older languages like C++. Discussions also highlight Microsoft's ambitious goals to convert existing codebases to Rust and the language's growing interoperability with other languages.

**Tags**: `#Rust`, `#Microsoft`, `#Programming Languages`, `#Systems Programming`, `#Software Development`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Frust-is-tier-1-language-at-microsoft-c3aba4d1&content=---%0Atitle%3A%20%22Rust%20is%20tier-1%20language%20at%20Microsoft%22%0Aurl%3A%20https%3A%2F%2Frustfoundation.org%2Fmedia%2Fguest-post-rust-is-tier-1-language-at-microsoft%2F%0Asource%3A%20%22hackernews%20%C2%B7%20mmastrac%22%0Ascore%3A%209.0%0Atags%3A%20%5B%22Rust%22%2C%20%22Microsoft%22%2C%20%22Programming%20Languages%22%2C%20%22Systems%20Programming%22%2C%20%22Software%20Development%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BRust%20is%20tier-1%20language%20at%20Microsoft%5D%28https%3A%2F%2Frustfoundation.org%2Fmedia%2Fguest-post-rust-is-tier-1-language-at-microsoft%2F%29%0A%E2%AD%90%EF%B8%8F%209.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20mmastrac%0A%0ARust%20has%20been%20elevated%20to%20a%20tier-1%20language%20at%20Microsoft%2C%20joining%20the%20ranks%20of%20C%2B%2B%2C%20C%23%2C%20and%20TypeScript.%20This%20change%20signifies%20Microsoft%27s%20strong%20endorsement%20of%20Rust%20for%20internal%20development.%20This%20elevation%20underscores%20Rust%27s%20growing%20importance%20and%20maturity%20in%20systems%20programming%2C%20potentially%20influencing%20other%20companies%20to%20adopt%20Rust%20for%20safer%20and%20more%20efficient%20software%20development.%20It%20highlights%20Microsoft%27s%20commitment%20to%20modernizing%20its%20codebase%20with%20secure%20and%20performant%20languages.%20As%20a%20tier-1%20language%2C%20Rust%20will%20receive%20the%20same%20level%20of%20support%20and%20tooling%20as%20other%20major%20languages%20at%20Microsoft.%20This%20includes%20integration%20with%20Microsoft%27s%20development%20environments%20and%20support%20for%20Rust%20in%20their%20production%20workflows.%0A%0A%23%23%20Background%0ARust%20is%20a%20systems%20programming%20language%20known%20for%20its%20performance%2C%20safety%2C%20and%20concurrency%20features.%20It%20was%20created%20by%20Graydon%20Hoare%20and%20officially%20sponsored%20by%20Mozilla%20before%20being%20managed%20by%20the%20Rust%20Foundation.%20Rust%27s%20memory%20safety%20without%20a%20garbage%20collector%20makes%20it%20particularly%20appealing%20for%20system-level%20programming.%20Microsoft%20has%20been%20integrating%20Rust%20into%20its%20ecosystem%2C%20reflecting%20a%20broader%20industry%20trend%20towards%20safer%20programming%20practices.%0A%0A%23%23%20Discussion%0ACommunity%20members%20are%20excited%20about%20Rust%27s%20elevation%2C%20noting%20its%20maturity%20and%20potential%20to%20replace%20older%20languages%20like%20C%2B%2B.%20Discussions%20also%20highlight%20Microsoft%27s%20ambitious%20goals%20to%20convert%20existing%20codebases%20to%20Rust%20and%20the%20language%27s%20growing%20interoperability%20with%20other%20languages.%0A">💾 Save to Obsidian</a>

---

<a id="item-2"></a>
## [Shopify Reverts to Native Development with Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify has announced its decision to transition from React Native back to native development using Swift and Kotlin. This move marks a significant shift in their mobile development strategy. This decision is significant as it reflects a potential industry trend away from cross-platform frameworks like React Native towards native development. It could influence other companies' mobile development strategies and impact the broader software engineering community. Shopify's move to native development involves using Swift for iOS and Kotlin for Android, both of which are known for their performance and native capabilities. This transition may require significant resource allocation and retraining of developers.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source framework developed by Meta Platforms that allows developers to build mobile applications using JavaScript and React. It has been popular for its ability to enable cross-platform development, reducing the need for separate iOS and Android codebases. Swift and Kotlin, on the other hand, are programming languages specifically designed for iOS and Android development, respectively, offering better integration with their respective platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://www.coderio.com/blog/software-development/swift-vs-kotlin-native-app-development/">Swift vs Kotlin for Native App Development: Complete 2026 Guide</a></li>

</ul>
</details>

**Discussion**: Community discussions reflect a mix of surprise and skepticism about Shopify's decision, with some questioning the efficiency of managing such a large engineering team. Others shared their experiences of transitioning from React Native to native development, noting the challenges and benefits.

**Tags**: `#Mobile Development`, `#React Native`, `#Swift`, `#Kotlin`, `#Software Engineering`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fshopify-is-moving-from-react-native-back-to-swift-and-kotlin-ccf40ae1&content=---%0Atitle%3A%20%22Shopify%20is%20moving%20from%20React%20Native%20back%20to%20Swift%20and%20Kotlin%22%0Aurl%3A%20https%3A%2F%2Fshopify.engineering%2Fback-to-native%0Asource%3A%20%22hackernews%20%C2%B7%20fnthawar2%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22Mobile%20Development%22%2C%20%22React%20Native%22%2C%20%22Swift%22%2C%20%22Kotlin%22%2C%20%22Software%20Engineering%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BShopify%20is%20moving%20from%20React%20Native%20back%20to%20Swift%20and%20Kotlin%5D%28https%3A%2F%2Fshopify.engineering%2Fback-to-native%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20fnthawar2%0A%0AShopify%20has%20announced%20its%20decision%20to%20transition%20from%20React%20Native%20back%20to%20native%20development%20using%20Swift%20and%20Kotlin.%20This%20move%20marks%20a%20significant%20shift%20in%20their%20mobile%20development%20strategy.%20This%20decision%20is%20significant%20as%20it%20reflects%20a%20potential%20industry%20trend%20away%20from%20cross-platform%20frameworks%20like%20React%20Native%20towards%20native%20development.%20It%20could%20influence%20other%20companies%27%20mobile%20development%20strategies%20and%20impact%20the%20broader%20software%20engineering%20community.%20Shopify%27s%20move%20to%20native%20development%20involves%20using%20Swift%20for%20iOS%20and%20Kotlin%20for%20Android%2C%20both%20of%20which%20are%20known%20for%20their%20performance%20and%20native%20capabilities.%20This%20transition%20may%20require%20significant%20resource%20allocation%20and%20retraining%20of%20developers.%0A%0A%23%23%20Background%0AReact%20Native%20is%20an%20open-source%20framework%20developed%20by%20Meta%20Platforms%20that%20allows%20developers%20to%20build%20mobile%20applications%20using%20JavaScript%20and%20React.%20It%20has%20been%20popular%20for%20its%20ability%20to%20enable%20cross-platform%20development%2C%20reducing%20the%20need%20for%20separate%20iOS%20and%20Android%20codebases.%20Swift%20and%20Kotlin%2C%20on%20the%20other%20hand%2C%20are%20programming%20languages%20specifically%20designed%20for%20iOS%20and%20Android%20development%2C%20respectively%2C%20offering%20better%20integration%20with%20their%20respective%20platforms.%0A%0A%23%23%20Discussion%0ACommunity%20discussions%20reflect%20a%20mix%20of%20surprise%20and%20skepticism%20about%20Shopify%27s%20decision%2C%20with%20some%20questioning%20the%20efficiency%20of%20managing%20such%20a%20large%20engineering%20team.%20Others%20shared%20their%20experiences%20of%20transitioning%20from%20React%20Native%20to%20native%20development%2C%20noting%20the%20challenges%20and%20benefits.%0A">💾 Save to Obsidian</a>

---

<a id="item-3"></a>
## [OpenAI Launches Flexible Agents API for AI Deployment](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI has introduced the Agents API, allowing developers to deploy AI agents flexibly. This API supports features like automatic context compaction and multi-agent orchestration. The introduction of the Agents API is significant as it simplifies the deployment of AI agents, potentially reducing development time and costs. It also opens up discussions on self-hosting and vendor lock-in, impacting how developers and companies might choose to implement AI solutions. The Agents API allows for the creation of production-ready agents with a single API call, specifying task, model, tools, and environment. It also supports self-hosting options, which can ease transitions between different service providers.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: OpenAI is a leading AI research organization known for its development of advanced AI models like GPT-3 and Codex. APIs are interfaces that allow different software applications to communicate with each other. The Agents API is part of OpenAI's efforts to make AI more accessible and customizable for developers, enabling them to integrate AI capabilities into their applications more easily.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents SDK | OpenAI API</a></li>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API | OpenAI</a></li>

</ul>
</details>

**Discussion**: Community members are discussing the potential of the Agents API for reducing the complexity of deploying AI agents. Some are excited about the self-hosting capabilities, which could mitigate concerns about vendor lock-in. Others are debating the evolving distinction between traditional LLM endpoints and more sophisticated agent harnesses.

**Tags**: `#AI`, `#API`, `#OpenAI`, `#Agent`, `#Machine Learning`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fopenai-agents-api-3dffb20e&content=---%0Atitle%3A%20%22OpenAI%20Agents%20API%22%0Aurl%3A%20https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fguides%2Fagents-api%2Foverview%0Asource%3A%20%22hackernews%20%C2%B7%20aquir%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22AI%22%2C%20%22API%22%2C%20%22OpenAI%22%2C%20%22Agent%22%2C%20%22Machine%20Learning%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BOpenAI%20Agents%20API%5D%28https%3A%2F%2Fdevelopers.openai.com%2Fapi%2Fdocs%2Fguides%2Fagents-api%2Foverview%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20aquir%0A%0AOpenAI%20has%20introduced%20the%20Agents%20API%2C%20allowing%20developers%20to%20deploy%20AI%20agents%20flexibly.%20This%20API%20supports%20features%20like%20automatic%20context%20compaction%20and%20multi-agent%20orchestration.%20The%20introduction%20of%20the%20Agents%20API%20is%20significant%20as%20it%20simplifies%20the%20deployment%20of%20AI%20agents%2C%20potentially%20reducing%20development%20time%20and%20costs.%20It%20also%20opens%20up%20discussions%20on%20self-hosting%20and%20vendor%20lock-in%2C%20impacting%20how%20developers%20and%20companies%20might%20choose%20to%20implement%20AI%20solutions.%20The%20Agents%20API%20allows%20for%20the%20creation%20of%20production-ready%20agents%20with%20a%20single%20API%20call%2C%20specifying%20task%2C%20model%2C%20tools%2C%20and%20environment.%20It%20also%20supports%20self-hosting%20options%2C%20which%20can%20ease%20transitions%20between%20different%20service%20providers.%0A%0A%23%23%20Background%0AOpenAI%20is%20a%20leading%20AI%20research%20organization%20known%20for%20its%20development%20of%20advanced%20AI%20models%20like%20GPT-3%20and%20Codex.%20APIs%20are%20interfaces%20that%20allow%20different%20software%20applications%20to%20communicate%20with%20each%20other.%20The%20Agents%20API%20is%20part%20of%20OpenAI%27s%20efforts%20to%20make%20AI%20more%20accessible%20and%20customizable%20for%20developers%2C%20enabling%20them%20to%20integrate%20AI%20capabilities%20into%20their%20applications%20more%20easily.%0A%0A%23%23%20Discussion%0ACommunity%20members%20are%20discussing%20the%20potential%20of%20the%20Agents%20API%20for%20reducing%20the%20complexity%20of%20deploying%20AI%20agents.%20Some%20are%20excited%20about%20the%20self-hosting%20capabilities%2C%20which%20could%20mitigate%20concerns%20about%20vendor%20lock-in.%20Others%20are%20debating%20the%20evolving%20distinction%20between%20traditional%20LLM%20endpoints%20and%20more%20sophisticated%20agent%20harnesses.%0A">💾 Save to Obsidian</a>

---

<a id="item-4"></a>
## [Cognition Unveils SWE-2 Model to Compete with Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 8.0/10

Cognition has launched the SWE-2 model, a new AI model designed to rival leading models like Fable 5.1 and GPT-Astra. The model was released on September 10, 2026, and is post-trained from the Kimi K3 model. The launch of SWE-2 is significant as it introduces a new competitor in the AI model space, potentially challenging established models like Fable 5.1 and GPT-Astra. This could lead to advancements in AI capabilities and increased competition in the industry. SWE-2 is post-trained from the Kimi K3 model, which has 2.8 trillion parameters and has undergone extensive reinforcement learning. Despite its potential, there are concerns about its generalization capabilities and the lack of open weights.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Background**: Cognition is a company known for its AI models, with SWE-2 being the latest in its series. The AI model space is highly competitive, with models like Fable 5.1 and GPT-Astra leading the market. These models are used for a variety of tasks, including coding, reasoning, and complex problem-solving. The introduction of SWE-2 aims to push the boundaries of what AI models can achieve, particularly in coding and reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE - 2 : Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://cellcog.ai/blog/cognition-swe-2/">Cognition SWE - 2 : Benchmarks, the 64% Cost Claim, and... | CellCog</a></li>
<li><a href="https://genztech.blog/models/cognition-swe-2/">Cognition SWE - 2 for Coding — Benchmarks, Pricing & Specs (2026)</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight skepticism about SWE-2's performance, particularly its generalization capabilities, as evidenced by discrepancies in benchmark scores. Concerns are also raised about the model's openness, with calls for more transparency and open weights.

**Tags**: `#AI`, `#Machine Learning`, `#Model Release`, `#Technology`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fcognition-launches-new-swe-2-model%2C-rivaling-fable-5.1-and-gpt-astra-403f674b&content=---%0Atitle%3A%20%22Cognition%20launches%20new%20SWE-2%20model%2C%20Rivaling%20Fable%205.1%20and%20GPT-Astra%22%0Aurl%3A%20https%3A%2F%2Fcognition.com%2Fblog%2Fswe-2%0Asource%3A%20%22hackernews%20%C2%B7%20seelos%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22AI%22%2C%20%22Machine%20Learning%22%2C%20%22Model%20Release%22%2C%20%22Technology%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BCognition%20launches%20new%20SWE-2%20model%2C%20Rivaling%20Fable%205.1%20and%20GPT-Astra%5D%28https%3A%2F%2Fcognition.com%2Fblog%2Fswe-2%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20seelos%0A%0ACognition%20has%20launched%20the%20SWE-2%20model%2C%20a%20new%20AI%20model%20designed%20to%20rival%20leading%20models%20like%20Fable%205.1%20and%20GPT-Astra.%20The%20model%20was%20released%20on%20September%2010%2C%202026%2C%20and%20is%20post-trained%20from%20the%20Kimi%20K3%20model.%20The%20launch%20of%20SWE-2%20is%20significant%20as%20it%20introduces%20a%20new%20competitor%20in%20the%20AI%20model%20space%2C%20potentially%20challenging%20established%20models%20like%20Fable%205.1%20and%20GPT-Astra.%20This%20could%20lead%20to%20advancements%20in%20AI%20capabilities%20and%20increased%20competition%20in%20the%20industry.%20SWE-2%20is%20post-trained%20from%20the%20Kimi%20K3%20model%2C%20which%20has%202.8%20trillion%20parameters%20and%20has%20undergone%20extensive%20reinforcement%20learning.%20Despite%20its%20potential%2C%20there%20are%20concerns%20about%20its%20generalization%20capabilities%20and%20the%20lack%20of%20open%20weights.%0A%0A%23%23%20Background%0ACognition%20is%20a%20company%20known%20for%20its%20AI%20models%2C%20with%20SWE-2%20being%20the%20latest%20in%20its%20series.%20The%20AI%20model%20space%20is%20highly%20competitive%2C%20with%20models%20like%20Fable%205.1%20and%20GPT-Astra%20leading%20the%20market.%20These%20models%20are%20used%20for%20a%20variety%20of%20tasks%2C%20including%20coding%2C%20reasoning%2C%20and%20complex%20problem-solving.%20The%20introduction%20of%20SWE-2%20aims%20to%20push%20the%20boundaries%20of%20what%20AI%20models%20can%20achieve%2C%20particularly%20in%20coding%20and%20reasoning%20tasks.%0A%0A%23%23%20Discussion%0ACommunity%20discussions%20highlight%20skepticism%20about%20SWE-2%27s%20performance%2C%20particularly%20its%20generalization%20capabilities%2C%20as%20evidenced%20by%20discrepancies%20in%20benchmark%20scores.%20Concerns%20are%20also%20raised%20about%20the%20model%27s%20openness%2C%20with%20calls%20for%20more%20transparency%20and%20open%20weights.%0A">💾 Save to Obsidian</a>

---

<a id="item-5"></a>
## [Critical RCE Vulnerability Fixed in Forgejo <=16.0.3](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

A critical remote code execution vulnerability in Forgejo versions up to 16.0.3 has been identified and fixed. This update is crucial for users to secure their systems against potential exploits. This vulnerability could allow attackers to execute arbitrary code remotely, posing a significant security risk to systems using Forgejo. The fix is important for maintaining the integrity and security of open-source projects relying on this platform. The vulnerability involved template expansion interfering with git repository initialization. The fix prevents this interference, ensuring that new repositories are initialized securely.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Background**: Forgejo is an open-source platform for hosting software development projects, using Git for version control. Remote code execution (RCE) is a severe security vulnerability that allows attackers to execute code on a target system from a remote location, potentially leading to data breaches or system compromise. Ensuring such vulnerabilities are patched promptly is critical for the security of any software platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo</a></li>
<li><a href="https://www.cloudflare.com/learning/security/what-is-remote-code-execution/">What is remote code execution?</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights concerns about security practices and comparisons with Gitea, another similar platform. Some users noted that Gitea is protected against such issues, while others emphasized the importance of reporting vulnerabilities without shaming affected projects.

**Tags**: `#security`, `#vulnerability`, `#open-source`, `#Forgejo`, `#RCE`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fforgejo-%3D16.0.3-critical-rce-fa7bd8e6&content=---%0Atitle%3A%20%22Forgejo%20%3C%3D16.0.3%20Critical%20RCE%22%0Aurl%3A%20https%3A%2F%2Fcodeberg.org%2Fforgejo%2Fforgejo%2Fsrc%2Fbranch%2Fforgejo%2Frelease-notes-published%2F16.0.4.md%0Asource%3A%20%22hackernews%20%C2%B7%20weierstass%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22security%22%2C%20%22vulnerability%22%2C%20%22open-source%22%2C%20%22Forgejo%22%2C%20%22RCE%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BForgejo%20%3C%3D16.0.3%20Critical%20RCE%5D%28https%3A%2F%2Fcodeberg.org%2Fforgejo%2Fforgejo%2Fsrc%2Fbranch%2Fforgejo%2Frelease-notes-published%2F16.0.4.md%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20weierstass%0A%0AA%20critical%20remote%20code%20execution%20vulnerability%20in%20Forgejo%20versions%20up%20to%2016.0.3%20has%20been%20identified%20and%20fixed.%20This%20update%20is%20crucial%20for%20users%20to%20secure%20their%20systems%20against%20potential%20exploits.%20This%20vulnerability%20could%20allow%20attackers%20to%20execute%20arbitrary%20code%20remotely%2C%20posing%20a%20significant%20security%20risk%20to%20systems%20using%20Forgejo.%20The%20fix%20is%20important%20for%20maintaining%20the%20integrity%20and%20security%20of%20open-source%20projects%20relying%20on%20this%20platform.%20The%20vulnerability%20involved%20template%20expansion%20interfering%20with%20git%20repository%20initialization.%20The%20fix%20prevents%20this%20interference%2C%20ensuring%20that%20new%20repositories%20are%20initialized%20securely.%0A%0A%23%23%20Background%0AForgejo%20is%20an%20open-source%20platform%20for%20hosting%20software%20development%20projects%2C%20using%20Git%20for%20version%20control.%20Remote%20code%20execution%20%28RCE%29%20is%20a%20severe%20security%20vulnerability%20that%20allows%20attackers%20to%20execute%20code%20on%20a%20target%20system%20from%20a%20remote%20location%2C%20potentially%20leading%20to%20data%20breaches%20or%20system%20compromise.%20Ensuring%20such%20vulnerabilities%20are%20patched%20promptly%20is%20critical%20for%20the%20security%20of%20any%20software%20platform.%0A%0A%23%23%20Discussion%0AThe%20community%20discussion%20highlights%20concerns%20about%20security%20practices%20and%20comparisons%20with%20Gitea%2C%20another%20similar%20platform.%20Some%20users%20noted%20that%20Gitea%20is%20protected%20against%20such%20issues%2C%20while%20others%20emphasized%20the%20importance%20of%20reporting%20vulnerabilities%20without%20shaming%20affected%20projects.%0A">💾 Save to Obsidian</a>

---

<a id="item-6"></a>
## [Challenges of Using AI Models like Astra for Coding](https://lucumr.pocoo.org/2026/9/7/astra-why/) ⭐️ 8.0/10

The article discusses the challenges of using AI models such as Astra for coding, highlighting issues in model training and the concept of 'involution' in AI engineering. Understanding these challenges is crucial for developers and engineers who rely on AI models for coding tasks, as it impacts the efficiency and quality of software development. The article points out that AI models may struggle with 'shitty code' and that the training process might not adequately penalize poor coding practices. Additionally, the concept of 'involution' suggests increasing effort without proportional improvement.

hackernews · manojbajaj95 · Sep 11, 06:23 · [Discussion](https://news.ycombinator.com/item?id=49654229)

**Background**: AI models like Astra are increasingly used in software engineering to automate coding tasks. However, training these models involves challenges such as ensuring data quality, avoiding biases, and managing computational costs. 'Involution' in AI refers to the phenomenon where increased competition and effort do not lead to proportional gains in productivity or quality.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oracle.com/artificial-intelligence/ai-model-training-challenges/">6 Common AI Model Training Challenges</a></li>
<li><a href="https://www.mercor.com/resources/experts/what-are-the-main-challenges-in-ai-model-training/">What Are the Main Challenges in AI Model Training? | Mercor</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about the quality of code produced by AI models and the effectiveness of the training process. There is skepticism about whether AI models are adequately penalized for poor coding practices, and some users express frustration with the slow progress of AI-generated code.

**Tags**: `#AI`, `#Machine Learning`, `#Software Engineering`, `#Model Training`, `#Coding`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fastra-for-coding-why-are-we-doing-this-again-59a8a687&content=---%0Atitle%3A%20%22Astra%20for%20Coding%3A%20Why%20Are%20We%20Doing%20This%20Again%3F%22%0Aurl%3A%20https%3A%2F%2Flucumr.pocoo.org%2F2026%2F9%2F7%2Fastra-why%2F%0Asource%3A%20%22hackernews%20%C2%B7%20manojbajaj95%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22AI%22%2C%20%22Machine%20Learning%22%2C%20%22Software%20Engineering%22%2C%20%22Model%20Training%22%2C%20%22Coding%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BAstra%20for%20Coding%3A%20Why%20Are%20We%20Doing%20This%20Again%3F%5D%28https%3A%2F%2Flucumr.pocoo.org%2F2026%2F9%2F7%2Fastra-why%2F%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20manojbajaj95%0A%0AThe%20article%20discusses%20the%20challenges%20of%20using%20AI%20models%20such%20as%20Astra%20for%20coding%2C%20highlighting%20issues%20in%20model%20training%20and%20the%20concept%20of%20%27involution%27%20in%20AI%20engineering.%20Understanding%20these%20challenges%20is%20crucial%20for%20developers%20and%20engineers%20who%20rely%20on%20AI%20models%20for%20coding%20tasks%2C%20as%20it%20impacts%20the%20efficiency%20and%20quality%20of%20software%20development.%20The%20article%20points%20out%20that%20AI%20models%20may%20struggle%20with%20%27shitty%20code%27%20and%20that%20the%20training%20process%20might%20not%20adequately%20penalize%20poor%20coding%20practices.%20Additionally%2C%20the%20concept%20of%20%27involution%27%20suggests%20increasing%20effort%20without%20proportional%20improvement.%0A%0A%23%23%20Background%0AAI%20models%20like%20Astra%20are%20increasingly%20used%20in%20software%20engineering%20to%20automate%20coding%20tasks.%20However%2C%20training%20these%20models%20involves%20challenges%20such%20as%20ensuring%20data%20quality%2C%20avoiding%20biases%2C%20and%20managing%20computational%20costs.%20%27Involution%27%20in%20AI%20refers%20to%20the%20phenomenon%20where%20increased%20competition%20and%20effort%20do%20not%20lead%20to%20proportional%20gains%20in%20productivity%20or%20quality.%0A%0A%23%23%20Discussion%0ACommunity%20comments%20highlight%20concerns%20about%20the%20quality%20of%20code%20produced%20by%20AI%20models%20and%20the%20effectiveness%20of%20the%20training%20process.%20There%20is%20skepticism%20about%20whether%20AI%20models%20are%20adequately%20penalized%20for%20poor%20coding%20practices%2C%20and%20some%20users%20express%20frustration%20with%20the%20slow%20progress%20of%20AI-generated%20code.%0A">💾 Save to Obsidian</a>

---

<a id="item-7"></a>
## [Anthropic's September 2026 Report on AI Misuse](https://www.anthropic.com/threat-intelligence-report-september-2026) ⭐️ 8.0/10

Anthropic released its September 2026 report detailing instances of AI misuse by various actors. The report highlights ethical and security concerns raised by these activities. The report is significant as it underscores the potential risks and ethical dilemmas posed by AI misuse. It affects stakeholders in AI development, security, and policy-making, highlighting the need for robust countermeasures. The report identifies misuse by actors in various regions, including China and Russia, using AI models like Claude. It also discusses covert operations by companies like Moonshot AI and DeepSeek, which misled customers about the AI models in use.

hackernews · garo-pro · Sep 10, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49647300)

**Background**: AI misuse refers to the inappropriate or harmful application of artificial intelligence technologies, which can lead to ethical, legal, and security issues. Companies like Anthropic are actively monitoring and reporting on these activities to mitigate risks. AI models, such as Claude, are sophisticated systems that can be exploited for malicious purposes if not properly managed. The ongoing development of AI safety measures is crucial to prevent such misuse.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-countering-misuse-aug-2025">Detecting and countering misuse of AI: August 2025 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals">Investigating three incidents in our cybersecurity evaluations \ Anthropic</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/ai-misuse/">How to prevent misuse of AI</a></li>

</ul>
</details>

**Discussion**: Community comments reflect concerns about companies like Moonshot AI and DeepSeek misleading customers by secretly using Claude. Some users criticize the report for mixing business model concerns with genuine public harm issues. Others point out the potential double standards in Anthropic's approach to AI misuse.

**Tags**: `#AI Ethics`, `#Security`, `#Threat Intelligence`, `#AI Misuse`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fdetecting-and-countering-misuse-of-ai-september-2026-d957d6c9&content=---%0Atitle%3A%20%22Detecting%20and%20countering%20misuse%20of%20AI%3A%20September%202026%22%0Aurl%3A%20https%3A%2F%2Fwww.anthropic.com%2Fthreat-intelligence-report-september-2026%0Asource%3A%20%22hackernews%20%C2%B7%20garo-pro%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22AI%20Ethics%22%2C%20%22Security%22%2C%20%22Threat%20Intelligence%22%2C%20%22AI%20Misuse%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BDetecting%20and%20countering%20misuse%20of%20AI%3A%20September%202026%5D%28https%3A%2F%2Fwww.anthropic.com%2Fthreat-intelligence-report-september-2026%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20garo-pro%0A%0AAnthropic%20released%20its%20September%202026%20report%20detailing%20instances%20of%20AI%20misuse%20by%20various%20actors.%20The%20report%20highlights%20ethical%20and%20security%20concerns%20raised%20by%20these%20activities.%20The%20report%20is%20significant%20as%20it%20underscores%20the%20potential%20risks%20and%20ethical%20dilemmas%20posed%20by%20AI%20misuse.%20It%20affects%20stakeholders%20in%20AI%20development%2C%20security%2C%20and%20policy-making%2C%20highlighting%20the%20need%20for%20robust%20countermeasures.%20The%20report%20identifies%20misuse%20by%20actors%20in%20various%20regions%2C%20including%20China%20and%20Russia%2C%20using%20AI%20models%20like%20Claude.%20It%20also%20discusses%20covert%20operations%20by%20companies%20like%20Moonshot%20AI%20and%20DeepSeek%2C%20which%20misled%20customers%20about%20the%20AI%20models%20in%20use.%0A%0A%23%23%20Background%0AAI%20misuse%20refers%20to%20the%20inappropriate%20or%20harmful%20application%20of%20artificial%20intelligence%20technologies%2C%20which%20can%20lead%20to%20ethical%2C%20legal%2C%20and%20security%20issues.%20Companies%20like%20Anthropic%20are%20actively%20monitoring%20and%20reporting%20on%20these%20activities%20to%20mitigate%20risks.%20AI%20models%2C%20such%20as%20Claude%2C%20are%20sophisticated%20systems%20that%20can%20be%20exploited%20for%20malicious%20purposes%20if%20not%20properly%20managed.%20The%20ongoing%20development%20of%20AI%20safety%20measures%20is%20crucial%20to%20prevent%20such%20misuse.%0A%0A%23%23%20Discussion%0ACommunity%20comments%20reflect%20concerns%20about%20companies%20like%20Moonshot%20AI%20and%20DeepSeek%20misleading%20customers%20by%20secretly%20using%20Claude.%20Some%20users%20criticize%20the%20report%20for%20mixing%20business%20model%20concerns%20with%20genuine%20public%20harm%20issues.%20Others%20point%20out%20the%20potential%20double%20standards%20in%20Anthropic%27s%20approach%20to%20AI%20misuse.%0A">💾 Save to Obsidian</a>

---

<a id="item-8"></a>
## [Run Any Nix Package in Your Browser with Trynix.dev](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Trynix.dev now allows users to run any Nix package from the past 13 years in a browser-based virtual machine using WebAssembly. This service is powered by qemu-wasm and provides URL-addressable packages for easy access. This development is significant as it simplifies testing and experimentation with different software environments directly in the browser. It could greatly benefit developers by providing a novel way to access and test software without the need for local installations. The virtual machine runs on x86_64 Linux and can be booted with any Nix package, which are URL addressable. This allows users to quickly load and interact with specific software versions, such as Python 3.6.2 from 2017, directly in their browser.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a cross-platform package manager for Unix and Unix-like systems, known for its functional programming language and reproducible builds. WebAssembly is a binary instruction format for a stack-based virtual machine, designed to enable high-performance applications on web pages. qemu-wasm is an experimental port of the QEMU system emulator to the browser, enabling virtual machines to run in a web environment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#Virtualization`, `#Development Tools`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fany-nix-package%2C-live-in-your-browser-a2c293f2&content=---%0Atitle%3A%20%22Any%20Nix%20package%2C%20live%20in%20your%20browser%22%0Aurl%3A%20https%3A%2F%2Fsimonwillison.net%2F2026%2FSep%2F10%2Ftrynix%2F%0Asource%3A%20%22rss%20%C2%B7%20Simon%20Willison%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22Nix%22%2C%20%22WebAssembly%22%2C%20%22Virtualization%22%2C%20%22Development%20Tools%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BAny%20Nix%20package%2C%20live%20in%20your%20browser%5D%28https%3A%2F%2Fsimonwillison.net%2F2026%2FSep%2F10%2Ftrynix%2F%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20rss%20%C2%B7%20Simon%20Willison%0A%0ATrynix.dev%20now%20allows%20users%20to%20run%20any%20Nix%20package%20from%20the%20past%2013%20years%20in%20a%20browser-based%20virtual%20machine%20using%20WebAssembly.%20This%20service%20is%20powered%20by%20qemu-wasm%20and%20provides%20URL-addressable%20packages%20for%20easy%20access.%20This%20development%20is%20significant%20as%20it%20simplifies%20testing%20and%20experimentation%20with%20different%20software%20environments%20directly%20in%20the%20browser.%20It%20could%20greatly%20benefit%20developers%20by%20providing%20a%20novel%20way%20to%20access%20and%20test%20software%20without%20the%20need%20for%20local%20installations.%20The%20virtual%20machine%20runs%20on%20x86_64%20Linux%20and%20can%20be%20booted%20with%20any%20Nix%20package%2C%20which%20are%20URL%20addressable.%20This%20allows%20users%20to%20quickly%20load%20and%20interact%20with%20specific%20software%20versions%2C%20such%20as%20Python%203.6.2%20from%202017%2C%20directly%20in%20their%20browser.%0A%0A%23%23%20Background%0ANix%20is%20a%20cross-platform%20package%20manager%20for%20Unix%20and%20Unix-like%20systems%2C%20known%20for%20its%20functional%20programming%20language%20and%20reproducible%20builds.%20WebAssembly%20is%20a%20binary%20instruction%20format%20for%20a%20stack-based%20virtual%20machine%2C%20designed%20to%20enable%20high-performance%20applications%20on%20web%20pages.%20qemu-wasm%20is%20an%20experimental%20port%20of%20the%20QEMU%20system%20emulator%20to%20the%20browser%2C%20enabling%20virtual%20machines%20to%20run%20in%20a%20web%20environment.%0A">💾 Save to Obsidian</a>

---

<a id="item-9"></a>
## [NASA Technique Reveals Ancient Images in Satellite Photos](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 7.0/10

NASA has applied decorrelation stretch technology to satellite photos to reveal ancient images. This technique, originally used for image enhancement, is now uncovering historical data hidden in satellite imagery. This development is significant as it opens new possibilities for archaeological research using remote sensing. By revealing ancient images, researchers can gain insights into historical landscapes and human activities without traditional excavation. The decorrelation stretch technique enhances color differences by transforming the image's color planes to be uncorrelated. However, it may face challenges with numerical instability and degenerate cases where color planes are linearly dependent.

hackernews · gumby · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645437)

**Background**: Decorrelation stretch is an image processing technique that enhances color differences, making it useful for analyzing multispectral datasets. Remote sensing in archaeology uses such techniques to uncover data that traditional methods cannot access. This approach allows archaeologists to study historical sites and artifacts from afar, providing a non-invasive means to explore ancient civilizations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mdpi.com/2227-7390/13/20/3297">Numerical Methods for Decorrelation Stretch - MDPI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_sensing_in_archaeology">Remote sensing in archaeology</a></li>
<li><a href="http://www.dstretch.com/">DStretch.com home page</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects a mix of surprise and admiration for the technique's application. Some users noted the historical context of image processing techniques, while others shared practical insights on similar methods using software like GIMP. There is also a sentiment that this technique, while not new, is a noteworthy success story.

**Tags**: `#remote sensing`, `#satellite imagery`, `#archaeology`, `#image processing`, `#NASA`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Ftechnique-for-manipulating-satellite-photos-now-reveals-ancient-images-%282025%29-20a18063&content=---%0Atitle%3A%20%22Technique%20for%20Manipulating%20Satellite%20Photos%20Now%20Reveals%20Ancient%20Images%20%282025%29%22%0Aurl%3A%20https%3A%2F%2Fspinoff.nasa.gov%2FManipulating_Satellite_Photos_Now_Reveals_Ancient_Images%0Asource%3A%20%22hackernews%20%C2%B7%20gumby%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22remote%20sensing%22%2C%20%22satellite%20imagery%22%2C%20%22archaeology%22%2C%20%22image%20processing%22%2C%20%22NASA%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BTechnique%20for%20Manipulating%20Satellite%20Photos%20Now%20Reveals%20Ancient%20Images%20%282025%29%5D%28https%3A%2F%2Fspinoff.nasa.gov%2FManipulating_Satellite_Photos_Now_Reveals_Ancient_Images%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20gumby%0A%0ANASA%20has%20applied%20decorrelation%20stretch%20technology%20to%20satellite%20photos%20to%20reveal%20ancient%20images.%20This%20technique%2C%20originally%20used%20for%20image%20enhancement%2C%20is%20now%20uncovering%20historical%20data%20hidden%20in%20satellite%20imagery.%20This%20development%20is%20significant%20as%20it%20opens%20new%20possibilities%20for%20archaeological%20research%20using%20remote%20sensing.%20By%20revealing%20ancient%20images%2C%20researchers%20can%20gain%20insights%20into%20historical%20landscapes%20and%20human%20activities%20without%20traditional%20excavation.%20The%20decorrelation%20stretch%20technique%20enhances%20color%20differences%20by%20transforming%20the%20image%27s%20color%20planes%20to%20be%20uncorrelated.%20However%2C%20it%20may%20face%20challenges%20with%20numerical%20instability%20and%20degenerate%20cases%20where%20color%20planes%20are%20linearly%20dependent.%0A%0A%23%23%20Background%0ADecorrelation%20stretch%20is%20an%20image%20processing%20technique%20that%20enhances%20color%20differences%2C%20making%20it%20useful%20for%20analyzing%20multispectral%20datasets.%20Remote%20sensing%20in%20archaeology%20uses%20such%20techniques%20to%20uncover%20data%20that%20traditional%20methods%20cannot%20access.%20This%20approach%20allows%20archaeologists%20to%20study%20historical%20sites%20and%20artifacts%20from%20afar%2C%20providing%20a%20non-invasive%20means%20to%20explore%20ancient%20civilizations.%0A%0A%23%23%20Discussion%0AThe%20community%20discussion%20reflects%20a%20mix%20of%20surprise%20and%20admiration%20for%20the%20technique%27s%20application.%20Some%20users%20noted%20the%20historical%20context%20of%20image%20processing%20techniques%2C%20while%20others%20shared%20practical%20insights%20on%20similar%20methods%20using%20software%20like%20GIMP.%20There%20is%20also%20a%20sentiment%20that%20this%20technique%2C%20while%20not%20new%2C%20is%20a%20noteworthy%20success%20story.%0A">💾 Save to Obsidian</a>

---

<a id="item-10"></a>
## [PlanetScale Introduces Neki: A Sharded Postgres Solution](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

PlanetScale has launched Neki, a new sharded Postgres solution designed to improve scalability and performance in distributed databases. Neki addresses critical scalability and performance challenges faced by distributed databases, potentially transforming how large-scale applications manage data. This development could significantly impact organizations relying on Postgres for their database needs. Neki is built on the foundation of PlanetScale's expertise with Vitess, a widely-used open-source database clustering system for MySQL. However, it is not open source, which has raised some concerns within the community.

hackernews · simon_weber · Sep 10, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49645686)

**Background**: Sharding is a database architecture pattern that involves splitting a database into smaller, more manageable pieces called shards. This technique is used to improve performance and scalability by distributing data across multiple servers. PostgreSQL, a popular open-source relational database, has seen various implementations of sharding, but many have been proprietary or lagged behind the main community releases. PlanetScale, known for its work with Vitess, has now introduced Neki to bring sharding capabilities to Postgres.

<details><summary>References</summary>
<ul>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale</a></li>
<li><a href="https://wiki.postgresql.org/wiki/Built-in_Sharding">Built-in Sharding - PostgreSQL wiki</a></li>
<li><a href="https://wiki.postgresql.org/wiki/WIP_PostgreSQL_Sharding">WIP PostgreSQL Sharding</a></li>

</ul>
</details>

**Discussion**: Community discussions highlight a mix of excitement and skepticism. Some users appreciate the potential of unlimited IOPS and the technical advancements, while others express concerns about the lack of open-source availability and the practicality of Neki's claims. The debate also touches on the comparison with Supabase's Multigres and the implications of eventual consistency in distributed systems.

**Tags**: `#database`, `#postgres`, `#sharding`, `#scalability`, `#distributed-systems`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fneki-%E2%80%93-sharded-postgres-d5b330be&content=---%0Atitle%3A%20%22Neki%20%E2%80%93%20Sharded%20Postgres%22%0Aurl%3A%20https%3A%2F%2Fplanetscale.com%2Fblog%2Fintroducing-neki%0Asource%3A%20%22hackernews%20%C2%B7%20simon_weber%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22database%22%2C%20%22postgres%22%2C%20%22sharding%22%2C%20%22scalability%22%2C%20%22distributed-systems%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BNeki%20%E2%80%93%20Sharded%20Postgres%5D%28https%3A%2F%2Fplanetscale.com%2Fblog%2Fintroducing-neki%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20simon_weber%0A%0APlanetScale%20has%20launched%20Neki%2C%20a%20new%20sharded%20Postgres%20solution%20designed%20to%20improve%20scalability%20and%20performance%20in%20distributed%20databases.%20Neki%20addresses%20critical%20scalability%20and%20performance%20challenges%20faced%20by%20distributed%20databases%2C%20potentially%20transforming%20how%20large-scale%20applications%20manage%20data.%20This%20development%20could%20significantly%20impact%20organizations%20relying%20on%20Postgres%20for%20their%20database%20needs.%20Neki%20is%20built%20on%20the%20foundation%20of%20PlanetScale%27s%20expertise%20with%20Vitess%2C%20a%20widely-used%20open-source%20database%20clustering%20system%20for%20MySQL.%20However%2C%20it%20is%20not%20open%20source%2C%20which%20has%20raised%20some%20concerns%20within%20the%20community.%0A%0A%23%23%20Background%0ASharding%20is%20a%20database%20architecture%20pattern%20that%20involves%20splitting%20a%20database%20into%20smaller%2C%20more%20manageable%20pieces%20called%20shards.%20This%20technique%20is%20used%20to%20improve%20performance%20and%20scalability%20by%20distributing%20data%20across%20multiple%20servers.%20PostgreSQL%2C%20a%20popular%20open-source%20relational%20database%2C%20has%20seen%20various%20implementations%20of%20sharding%2C%20but%20many%20have%20been%20proprietary%20or%20lagged%20behind%20the%20main%20community%20releases.%20PlanetScale%2C%20known%20for%20its%20work%20with%20Vitess%2C%20has%20now%20introduced%20Neki%20to%20bring%20sharding%20capabilities%20to%20Postgres.%0A%0A%23%23%20Discussion%0ACommunity%20discussions%20highlight%20a%20mix%20of%20excitement%20and%20skepticism.%20Some%20users%20appreciate%20the%20potential%20of%20unlimited%20IOPS%20and%20the%20technical%20advancements%2C%20while%20others%20express%20concerns%20about%20the%20lack%20of%20open-source%20availability%20and%20the%20practicality%20of%20Neki%27s%20claims.%20The%20debate%20also%20touches%20on%20the%20comparison%20with%20Supabase%27s%20Multigres%20and%20the%20implications%20of%20eventual%20consistency%20in%20distributed%20systems.%0A">💾 Save to Obsidian</a>

---

<a id="item-11"></a>
## [Proof of Capture: Apple Reference Image, but open source and using steganography](https://merybenavente.me/blog/proof-of-capture) ⭐️ 7.0/10

The article introduces an open-source method for signing images using steganography, sparking discussions on its security implications and technical feasibility.

hackernews · merybenavente · Sep 10, 19:44 · [Discussion](https://news.ycombinator.com/item?id=49649222)

**Tags**: `#steganography`, `#image processing`, `#open source`, `#security`, `#cryptography`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fproof-of-capture-apple-reference-image%2C-but-open-source-and-using-steganography-ffe91d84&content=---%0Atitle%3A%20%22Proof%20of%20Capture%3A%20Apple%20Reference%20Image%2C%20but%20open%20source%20and%20using%20steganography%22%0Aurl%3A%20https%3A%2F%2Fmerybenavente.me%2Fblog%2Fproof-of-capture%0Asource%3A%20%22hackernews%20%C2%B7%20merybenavente%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22steganography%22%2C%20%22image%20processing%22%2C%20%22open%20source%22%2C%20%22security%22%2C%20%22cryptography%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BProof%20of%20Capture%3A%20Apple%20Reference%20Image%2C%20but%20open%20source%20and%20using%20steganography%5D%28https%3A%2F%2Fmerybenavente.me%2Fblog%2Fproof-of-capture%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20merybenavente%0A%0AThe%20article%20introduces%20an%20open-source%20method%20for%20signing%20images%20using%20steganography%2C%20sparking%20discussions%20on%20its%20security%20implications%20and%20technical%20feasibility.%0A">💾 Save to Obsidian</a>

---

<a id="item-12"></a>
## [Datasette Releases Security Patches for Alpha and Stable Versions](https://simonwillison.net/2026/Sep/11/datasette-security/) ⭐️ 7.0/10

Datasette has released security patches for versions 1.0a39 and 0.65.4. These patches address subtle bugs discovered through an extensive audit conducted with the help of AI models. The security patches are crucial for users running Datasette instances on the public web, especially those mixing public and private tables. This release highlights the importance of security audits in software development. The audit was conducted using advanced AI models like Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. The process involved collaborative efforts to create automated tests and implement fixes, ensuring thorough review by multiple parties.

rss · Simon Willison · Sep 11, 03:27

**Background**: Datasette is an open-source tool designed to help users publish and explore data. Security is a critical aspect for any software, especially for tools like Datasette that may handle sensitive information. Regular audits and updates are necessary to maintain the integrity and security of such systems.

**Tags**: `#Datasette`, `#Security`, `#Software Release`, `#Bug Fixes`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fdatasette-1.0a39-and-0.65.4-security-releases-1e206d76&content=---%0Atitle%3A%20%22Datasette%201.0a39%20and%200.65.4%20security%20releases%22%0Aurl%3A%20https%3A%2F%2Fsimonwillison.net%2F2026%2FSep%2F11%2Fdatasette-security%2F%0Asource%3A%20%22rss%20%C2%B7%20Simon%20Willison%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22Datasette%22%2C%20%22Security%22%2C%20%22Software%20Release%22%2C%20%22Bug%20Fixes%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BDatasette%201.0a39%20and%200.65.4%20security%20releases%5D%28https%3A%2F%2Fsimonwillison.net%2F2026%2FSep%2F11%2Fdatasette-security%2F%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20rss%20%C2%B7%20Simon%20Willison%0A%0ADatasette%20has%20released%20security%20patches%20for%20versions%201.0a39%20and%200.65.4.%20These%20patches%20address%20subtle%20bugs%20discovered%20through%20an%20extensive%20audit%20conducted%20with%20the%20help%20of%20AI%20models.%20The%20security%20patches%20are%20crucial%20for%20users%20running%20Datasette%20instances%20on%20the%20public%20web%2C%20especially%20those%20mixing%20public%20and%20private%20tables.%20This%20release%20highlights%20the%20importance%20of%20security%20audits%20in%20software%20development.%20The%20audit%20was%20conducted%20using%20advanced%20AI%20models%20like%20Claude%20Fable%205.1%2C%20GPT-5.6%2C%20and%20GPT-6%20Astra.%20The%20process%20involved%20collaborative%20efforts%20to%20create%20automated%20tests%20and%20implement%20fixes%2C%20ensuring%20thorough%20review%20by%20multiple%20parties.%0A%0A%23%23%20Background%0ADatasette%20is%20an%20open-source%20tool%20designed%20to%20help%20users%20publish%20and%20explore%20data.%20Security%20is%20a%20critical%20aspect%20for%20any%20software%2C%20especially%20for%20tools%20like%20Datasette%20that%20may%20handle%20sensitive%20information.%20Regular%20audits%20and%20updates%20are%20necessary%20to%20maintain%20the%20integrity%20and%20security%20of%20such%20systems.%0A">💾 Save to Obsidian</a>

---

<a id="item-13"></a>
## [ACL Implements New Sustainable Reviewing Policy](https://www.reddit.com/r/MachineLearning/comments/1wd7b83/acl_sustainable_reviewing_policy_d/) ⭐️ 7.0/10

The Association for Computational Linguistics (ACL) has introduced a new sustainable reviewing policy to manage increased submission numbers. The policy requires each submission to include a qualified reviewer and caps total submissions at 20 and first-author submissions at 5 per cycle. This policy is significant as it addresses the challenge of handling the growing number of submissions in academic publishing, ensuring the quality and sustainability of the review process. It impacts authors and reviewers in the machine learning and computational linguistics communities. Submissions must 'pay' for themselves by providing a qualified service contributor, and those without will enter a lottery for remaining capacity. A mentorship system will be established for those not yet qualified, and measures to prevent system abuse will be implemented.

reddit · r/MachineLearning · /u/S4M22 · Sep 11, 05:38

**Background**: The ACL Rolling Review (ARR) is a centralized peer review platform for the Association for Computational Linguistics, aimed at improving the efficiency and consistency of the review process. The new policy is part of efforts to make the reviewing system more sustainable, as the number of submissions has been increasing significantly. The policy introduces quotas and requires authors to contribute to the reviewing process, which is a shift from traditional practices.

<details><summary>References</summary>
<ul>
<li><a href="https://aclrollingreview.org/">ACL Rolling Review – A peer review platform for the Association for Computational Linguistics</a></li>
<li><a href="https://aclrollingreview.org/incentives2025">Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025) – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics</a></li>

</ul>
</details>

**Discussion**: The community has mixed reactions, with some agreeing on the necessity of the policy to maintain quality, while others are concerned about potential gatekeeping effects. There is also discussion on the fairness and feasibility of the lottery system for submissions without a reviewer.

**Tags**: `#ACL`, `#reviewing policy`, `#academic publishing`, `#machine learning`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Facl-sustainable-reviewing-policy-d-f3e1307c&content=---%0Atitle%3A%20%22ACL%20Sustainable%20Reviewing%20Policy%20%5BD%5D%22%0Aurl%3A%20https%3A%2F%2Fwww.reddit.com%2Fr%2FMachineLearning%2Fcomments%2F1wd7b83%2Facl_sustainable_reviewing_policy_d%2F%0Asource%3A%20%22reddit%20%C2%B7%20r%2FMachineLearning%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22ACL%22%2C%20%22reviewing%20policy%22%2C%20%22academic%20publishing%22%2C%20%22machine%20learning%22%5D%0Asaved%3A%202026-09-11%0A---%0A%23%20%5BACL%20Sustainable%20Reviewing%20Policy%20%28D%29%5D%28https%3A%2F%2Fwww.reddit.com%2Fr%2FMachineLearning%2Fcomments%2F1wd7b83%2Facl_sustainable_reviewing_policy_d%2F%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20reddit%20%C2%B7%20r%2FMachineLearning%0A%0AThe%20Association%20for%20Computational%20Linguistics%20%28ACL%29%20has%20introduced%20a%20new%20sustainable%20reviewing%20policy%20to%20manage%20increased%20submission%20numbers.%20The%20policy%20requires%20each%20submission%20to%20include%20a%20qualified%20reviewer%20and%20caps%20total%20submissions%20at%2020%20and%20first-author%20submissions%20at%205%20per%20cycle.%20This%20policy%20is%20significant%20as%20it%20addresses%20the%20challenge%20of%20handling%20the%20growing%20number%20of%20submissions%20in%20academic%20publishing%2C%20ensuring%20the%20quality%20and%20sustainability%20of%20the%20review%20process.%20It%20impacts%20authors%20and%20reviewers%20in%20the%20machine%20learning%20and%20computational%20linguistics%20communities.%20Submissions%20must%20%27pay%27%20for%20themselves%20by%20providing%20a%20qualified%20service%20contributor%2C%20and%20those%20without%20will%20enter%20a%20lottery%20for%20remaining%20capacity.%20A%20mentorship%20system%20will%20be%20established%20for%20those%20not%20yet%20qualified%2C%20and%20measures%20to%20prevent%20system%20abuse%20will%20be%20implemented.%0A%0A%23%23%20Background%0AThe%20ACL%20Rolling%20Review%20%28ARR%29%20is%20a%20centralized%20peer%20review%20platform%20for%20the%20Association%20for%20Computational%20Linguistics%2C%20aimed%20at%20improving%20the%20efficiency%20and%20consistency%20of%20the%20review%20process.%20The%20new%20policy%20is%20part%20of%20efforts%20to%20make%20the%20reviewing%20system%20more%20sustainable%2C%20as%20the%20number%20of%20submissions%20has%20been%20increasing%20significantly.%20The%20policy%20introduces%20quotas%20and%20requires%20authors%20to%20contribute%20to%20the%20reviewing%20process%2C%20which%20is%20a%20shift%20from%20traditional%20practices.%0A%0A%23%23%20Discussion%0AThe%20community%20has%20mixed%20reactions%2C%20with%20some%20agreeing%20on%20the%20necessity%20of%20the%20policy%20to%20maintain%20quality%2C%20while%20others%20are%20concerned%20about%20potential%20gatekeeping%20effects.%20There%20is%20also%20discussion%20on%20the%20fairness%20and%20feasibility%20of%20the%20lottery%20system%20for%20submissions%20without%20a%20reviewer.%0A">💾 Save to Obsidian</a>

---