---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 26 items, 15 important content pieces were selected

---

1. [OpenAI unveils Jalapeño, its first custom AI inference chip with Broadcom](#item-1) ⭐️ 9.0/10
2. [Qualcomm Acquires AI Startup Modular for $4 Billion](#item-2) ⭐️ 8.0/10
3. [Superhuman Generals.io Agent Trained with Self-Play RL and Vision Transformers](#item-3) ⭐️ 8.0/10
4. [Anthropic Accuses Alibaba of Illicitly Extracting Claude AI Capabilities](#item-4) ⭐️ 7.0/10
5. [Cloudflare launches self-managed OAuth for all developers](#item-5) ⭐️ 7.0/10
6. [Blogging can just be stating the obvious](#item-6) ⭐️ 7.0/10
7. [NVIDIA's 45°C liquid cooling cuts data center water consumption near zero](#item-7) ⭐️ 7.0/10
8. [RubyLLM: Unified Ruby framework for multiple AI providers](#item-8) ⭐️ 7.0/10
9. [Open-source PR spam mirrors early 2000s email spam crisis](#item-9) ⭐️ 7.0/10
10. [Google Introduces Computer Use Capabilities for Gemini 3.5 Flash](#item-10) ⭐️ 7.0/10
11. [Nub: A Bun-like all-in-one toolkit for Node.js](#item-11) ⭐️ 7.0/10
12. [Quoting Tom MacWright](#item-12) ⭐️ 7.0/10
13. [MuJoFil: GPU-Native Physics Simulator for Vision-Based RL Training](#item-13) ⭐️ 7.0/10
14. [High Dimensional Dynamic RoPE: Improved Positional Embeddings with Cumulative Matrix Products](#item-14) ⭐️ 7.0/10
15. [Comprehensive LLM inference pricing comparison reveals surprising caching cost variations](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI unveils Jalapeño, its first custom AI inference chip with Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI has unveiled Jalapeño, its first custom AI inference chip developed in partnership with Broadcom and manufactured by TSMC, completed in just nine months with the help of AI-assisted design optimization. The chip is specifically optimized for large language model inference workloads to improve performance, efficiency, and reduce computing costs at scale. This represents a major strategic shift for OpenAI into semiconductor design and manufacturing, reducing dependence on third-party chip suppliers and enabling tighter integration between AI models and hardware. The move signals the growing importance of custom silicon in the AI infrastructure landscape, following similar efforts by competitors like Google with their TPU generations. The nine-month development timeline was notably accelerated through the use of OpenAI's own AI models to optimize parts of the chip design and verification process, demonstrating AI's application in semiconductor design automation. The chip is manufactured by TSMC, a leading semiconductor foundry, ensuring access to cutting-edge fabrication technology.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference refers to the process of running trained machine learning models to generate predictions or outputs, which is computationally intensive and often requires specialized hardware. Custom silicon chips designed specifically for AI workloads can offer significant advantages in speed, power efficiency, and cost compared to general-purpose processors. Major tech companies like Google have invested heavily in custom AI chips (such as TPUs) to optimize their AI infrastructure and reduce operational costs.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://www.ltts.com/blog/ai-semiconductor-design">AI in Semiconductor Design: Toward Shorter Chip Cycles</a></li>
<li><a href="https://thetechportal.com/2026/06/24/openai-reveals-its-first-in-house-ai-inference-chip-jalapeno-developed-with-broadcom/">OpenAI reveals its first in-house AI inference chip ‘Jalapeño ...</a></li>

</ul>
</details>

**Discussion**: Community members expressed both enthusiasm and skepticism about the announcement. Some questioned whether the claimed AI-assisted design acceleration was genuinely significant or merely marketing language, while others highlighted that TSMC (not Intel) is the manufacturer. Technical discussions explored alternative approaches like burning model weights directly into silicon ROM for extreme efficiency, and comparisons were drawn to competing solutions like Taalas and Google's established TPU generations.

**Tags**: `#AI Hardware`, `#Custom Chips`, `#Infrastructure`, `#OpenAI`, `#Semiconductor Design`

---

<a id="item-2"></a>
## [Qualcomm Acquires AI Startup Modular for $4 Billion](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm announced an all-stock acquisition of AI startup Modular Inc. valued at approximately $4 billion, gaining access to Modular's AI compiler and inference software stack. The deal was announced on June 24, 2026, and represents Qualcomm's strategic push to develop competitive AI software capabilities beyond its traditional mobile chip business. This acquisition signals Qualcomm's ambition to compete with Nvidia in AI infrastructure and positions the company to support its broader strategy of transitioning from ARM architecture toward RISC-V, while building a complete AI software stack for data center and edge computing applications. The deal reflects growing recognition that semiconductor companies need integrated software solutions to succeed in the AI market. Modular's core technology includes MLIR (Multi-Level Intermediate Representation) compiler infrastructure and the Mojo programming language, which enable AI models to run efficiently across different hardware platforms without requiring platform-specific rewrites. The acquisition is part of Qualcomm's broader portfolio expansion that includes investments in RISC-V ecosystem companies like Tenstorrent, Ventana, and Alphawave.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Modular was founded by Chris Lattner, a renowned compiler expert known for his work on LLVM and Swift, and developed software tools designed to optimize AI inference across diverse hardware platforms. RISC-V is an open-source processor instruction set architecture that offers an alternative to ARM's proprietary architecture, providing vendors with greater flexibility and independence. The AI software stack has become increasingly critical as companies recognize that hardware alone is insufficient to compete in AI—software optimization, compiler technology, and cross-platform compatibility are essential for efficient AI deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/">Qualcomm to buy startup Modular for $4 billion in AI software push</a></li>
<li><a href="https://startupfortune.com/qualcomm-is-buying-modular-for-4-billion-to-take-on-nvidia-where-it-actually-counts/">Qualcomm is buying Modular for $4 billion to take on Nvidia where it ...</a></li>
<li><a href="https://www.modular.com/blog/democratizing-ai-compute-part-8-what-about-the-mlir-compiler-infrastructure">Modular: What about the MLIR compiler infrastructure? (Democratizing AI ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed but substantive: some commenters express concern that Mojo may not achieve broad cross-platform adoption under Qualcomm ownership, noting a pattern of failed cross-platform AI languages (SYCL, OpenCL, One API); others view the acquisition positively as part of Qualcomm's strategic portfolio-building in RISC-V and AI infrastructure; one commenter notes the irony that Modular's founder has previously criticized hardware companies for failing to build effective AI stacks, yet is now being acquired by one.

**Tags**: `#acquisitions`, `#AI infrastructure`, `#Qualcomm`, `#RISC-V`, `#edge computing`

---

<a id="item-3"></a>
## [Superhuman Generals.io Agent Trained with Self-Play RL and Vision Transformers](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A researcher successfully trained a self-play reinforcement learning agent for Generals.io that achieved superhuman performance and ranked #1 on the human 1v1 leaderboard. The agent was developed using Vision Transformers and JAX, with the entire pipeline reimplemented from NumPy/Torch to improve scalability, and the work includes a comprehensive guide, open-source simulator, and agent code. This achievement demonstrates significant progress in competitive game AI by combining self-play reinforcement learning with modern deep learning architectures, showing that scaling and architectural improvements can overcome limitations of hand-crafted heuristics. The open-source tools and comprehensive documentation provide valuable resources for the game AI and reinforcement learning community. The agent evolved from an initial master's thesis project using behavior cloning and reward shaping that was still beaten by top human players; the breakthrough came from reimplementing in JAX for better performance and replacing CNNs with Vision Transformers to leverage scaling rather than domain-specific priors. The work includes a fast JAX-based simulator for Generals.io that can be used independently as an imperfect-information real-time strategy environment.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is a fast-paced multiplayer strategy game where players expand territory, command armies, and protect their general (a key unit whose capture means defeat). Self-play reinforcement learning is a training technique where an agent plays against copies of itself at different skill levels, allowing it to gradually improve by facing opponents of comparable strength. Vision Transformers are a neural network architecture that divides input images into patches and processes them with transformer layers, offering an alternative to convolutional neural networks that can scale more effectively with data.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.generals.io/1v1guide.html">Generals.io 1v1 Guide | Generals.io-Wiki</a></li>
<li><a href="https://huggingface.co/learn/deep-rl-course/unit7/self-play">Self-Play: a classic technique to train competitive agents in ...</a></li>
<li><a href="https://arxiv.org/abs/2408.01072">A Survey on Self-play Methods in Reinforcement Learning Self-Play: a classic technique to train competitive agents in ... A Survey on Self-play Methods in Reinforcement Learning Self-play reinforcement learning with comprehensive critic in ... Self-Play Meta-Reinforcement Learning in Multi-Agent Games Self-Play Reinforcement Learning for Strategic Games A Survey on Self-Play Methods in Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#game-ai`, `#self-play`, `#vision-transformers`, `#systems-engineering`

---

<a id="item-4"></a>
## [Anthropic Accuses Alibaba of Illicitly Extracting Claude AI Capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 7.0/10

Anthropic has alleged that Alibaba illicitly extracted capabilities from its Claude AI model through model distillation techniques. The accusation centers on Alibaba's use of Claude's outputs to train and improve competing AI systems without authorization. This dispute highlights critical questions about intellectual property protection in the AI industry and sets a precedent for how companies can legally use AI model outputs for training purposes. The case could significantly impact how AI companies protect their proprietary models and establish boundaries around model distillation practices. Model distillation is a legitimate machine learning technique where knowledge from a larger, more capable model (teacher) is transferred to a smaller model (student) to reduce computational costs while maintaining performance. The technical distinction between authorized fine-tuning and unauthorized distillation remains contested, with commenters noting that thousands of businesses perform similar distillation operations daily.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Model distillation, also known as knowledge distillation, is a standard machine learning technique where a smaller, more efficient model learns to replicate the behavior and outputs of a larger, more complex model. This process allows companies to deploy capable AI systems on less powerful hardware or reduce computational costs while maintaining performance on specific tasks. The technique has been widely adopted across the industry and is used by major AI companies including OpenAI for optimizing their models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>
<li><a href="https://www.ibm.com/think/topics/knowledge-distillation">What is Knowledge distillation? | IBM</a></li>

</ul>
</details>

**Discussion**: Community discussion reveals significant skepticism about Anthropic's complaint, with commenters pointing out apparent hypocrisy: Anthropic itself downloaded millions of copyrighted books from pirate sites like LibGen for training, a practice a judge ruled as infringement. Commenters also distinguish between different distillation methods and note that Chinese resellers are offering Claude API access at 70-90% below official prices through account pooling and fraud, then selling the model outputs as training data. The broader sentiment questions whether Anthropic has standing to complain about unauthorized model use given its own training data sourcing practices.

**Tags**: `#AI-Security`, `#Intellectual-Property`, `#Model-Distillation`, `#AI-Ethics`, `#Industry-Dispute`

---

<a id="item-5"></a>
## [Cloudflare launches self-managed OAuth for all developers](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 7.0/10

Cloudflare has launched self-managed OAuth clients, enabling developers to build third-party applications that integrate with Cloudflare accounts using OAuth authentication. This provides a more secure and user-friendly alternative to traditional API tokens for accessing Cloudflare services. This capability simplifies authentication for third-party integrations while improving security by enabling user delegation and reducing the need to share API tokens directly. It aligns with modern authentication standards and makes Cloudflare's platform more accessible to developers building agent-ready and AI-integrated applications. The implementation uses Cloudflare's infrastructure and is designed to work with standard OAuth 2.0 flows, including support for agent-ready applications that comply with RFC 9728. The feature addresses a gap where Cloudflare previously exposed OAuth capabilities only through its API as an MCP server, but now provides direct OAuth client management for developers.

hackernews · terryds · Jun 25, 02:18 · [Discussion](https://news.ycombinator.com/item?id=48668033)

**Background**: OAuth is an industry-standard authentication protocol that allows users to grant third-party applications access to their accounts without sharing passwords. It enables secure delegation of permissions and is widely used for integrations between services. Cloudflare Access is Cloudflare's identity and access management solution that protects internal applications and resources.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/">Introducing self - managed OAuth clients · Changelog</a></li>
<li><a href="https://blog.cloudflare.com/managed-oauth-for-access/">Managed OAuth for Access: make internal apps agent-ready in one click</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">Managed OAuth · Cloudflare One docs</a></li>

</ul>
</details>

**Discussion**: Community discussion reveals mixed perspectives on OAuth's complexity: while some developers find OAuth and enterprise authentication frustrating and confusing, particularly for headless systems, others recognize its value for user delegation scenarios. The Ory Hydra author praised the implementation's performance, and commenters noted that simpler alternatives like scoped API keys with rotation and audit logs may provide better developer experience for server-to-server authentication, suggesting Cloudflare's offering addresses a specific use case rather than being universally optimal.

**Tags**: `#OAuth`, `#Authentication`, `#Cloudflare`, `#Cloud Infrastructure`, `#Identity Management`

---

<a id="item-6"></a>
## [Blogging can just be stating the obvious](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/) ⭐️ 7.0/10

An exploration of why blogging about seemingly obvious topics remains valuable, challenging the assumption that well-known ideas shouldn't be written about.

hackernews · Curiositry · Jun 24, 23:46 · [Discussion](https://news.ycombinator.com/item?id=48666927)

**Tags**: `#blogging`, `#knowledge-sharing`, `#writing`, `#meta-commentary`, `#learning`

---

<a id="item-7"></a>
## [NVIDIA's 45°C liquid cooling cuts data center water consumption near zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 7.0/10

NVIDIA has unveiled a 45°C liquid-cooling architecture for AI data centers that dramatically reduces water consumption while enabling waste heat recovery for district heating systems. This approach operates at higher coolant temperatures than conventional liquid cooling, allowing data centers to repurpose thermal output for community heating applications. This development addresses two critical challenges in data center operations: excessive water consumption (currently up to 40% of total power goes to cooling) and environmental waste of thermal energy. The ability to recover waste heat for district heating creates significant economic and environmental value, potentially worth millions of dollars annually to local communities while reducing the overall carbon footprint of AI infrastructure. The 45°C coolant temperature is warm enough to be viable for district heating systems but requires favorable climate conditions to be most effective; the approach's efficiency and cost-effectiveness vary significantly based on ambient temperature and proximity to district heating infrastructure. Community comments note that similar concepts have been demonstrated elsewhere, such as NASA's Ames Research Center using water cooling at approximately 90°F (32°C), and Microsoft's data center in Finland already providing free heating to a city.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Modern AI data centers face extreme thermal challenges because high-performance processors generate enormous amounts of heat; traditional air cooling is increasingly insufficient and consumes massive amounts of water through evaporative cooling towers. Liquid cooling systems circulate coolant directly through or near processors to remove heat more efficiently, but conventional designs operate at lower temperatures that waste the thermal energy. District heating systems are networks that distribute heat from centralized sources to multiple buildings in a community, and waste heat recovery involves capturing thermal energy that would otherwise be discarded and repurposing it for useful applications.

<details><summary>References</summary>
<ul>
<li><a href="https://techstory.in/the-45c-breakthrough-nvidias-liquid-cooling-architecture-solves-data-center-water-crisis/">The 45°C Breakthrough NVIDIA’s Liquid Cooling Architecture ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1364032125005362">Data center waste heat for district heating networks: A review - ScienceDirect</a></li>
<li><a href="https://www.danfoss.com/en/about-danfoss/our-businesses/climate-solutions/waste-heat/">Turn waste heat into clean heat with District Energy | Danfoss</a></li>

</ul>
</details>

**Discussion**: Community discussion reveals strong interest in the district heating synergy, with commenters noting that 45°C waste heat is viable for heating systems and could provide millions in annual value to communities. However, skepticism exists about the technical novelty—some question why higher-temperature liquid cooling wasn't adopted previously and note that similar concepts already exist (NASA's Ames facility, Microsoft's Finland data center). Key concerns include the requirement for favorable climates and the practical challenge that data centers and district heating grids rarely locate near each other by accident, suggesting implementation barriers beyond pure technology.

**Tags**: `#data-center-infrastructure`, `#liquid-cooling`, `#sustainability`, `#thermal-management`, `#AI-infrastructure`

---

<a id="item-8"></a>
## [RubyLLM: Unified Ruby framework for multiple AI providers](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM is a Ruby framework that provides a single, unified API interface for accessing multiple AI providers including GPT, Claude, and local Ollama instances. The framework emphasizes developer experience with an opinionated, productive design philosophy similar to Rails' approach to web development. RubyLLM addresses the fragmentation problem where each AI provider ships its own client library, reducing developer friction and engineering time for Ruby teams building AI applications. This unified abstraction layer enables faster development and easier switching between providers without rewriting application code. Community feedback highlights strong API design and developer experience comparable to Vercel's AI framework, but reveals maintenance concerns including slow PR responsiveness and edge case handling issues (such as caching problems with xAI's completions API). The framework has inspired derivative projects like Raix, which builds on top of RubyLLM's abstractions.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: AI providers like OpenAI, Anthropic, and others each maintain separate client libraries with different APIs, creating complexity for developers who want to use multiple providers or switch between them. A unified API layer abstracts away these differences, allowing developers to write code once and use it with any supported provider. This approach mirrors how Rails simplified web development by providing opinionated conventions and abstractions.

<details><summary>References</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI providers.</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ ruby _ llm : One delightful Ruby framework for every...</a></li>
<li><a href="https://medium.com/airtribe/rubyllm-and-the-return-of-rails-superpower-notes-from-euruko-2025-b72eeeb6b185">RubyLLM and the Return of Rails’ Superpower — Notes... | Medium</a></li>

</ul>
</details>

**Discussion**: Community members praise RubyLLM's API design and usability, with users reporting successful real-world implementations and appreciation for its balance between out-of-the-box functionality and flexibility. However, concerns emerge around maintainer engagement, with reports of slow PR responses and inconsistent code quality in merged contributions, leading some to suggest that a minimal, API-compatible alternative might be valuable.

**Tags**: `#Ruby`, `#LLM-Framework`, `#AI-Integration`, `#Developer-Tools`, `#Open-Source`

---

<a id="item-9"></a>
## [Open-source PR spam mirrors early 2000s email spam crisis](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 7.0/10

Open-source projects are increasingly overwhelmed by low-quality pull requests and issues, drawing parallels to the email spam epidemic of the early 2000s. The discussion highlights how traditional spam-fighting mechanisms like sender reputation systems and organizational accountability don't translate effectively to GitHub's decentralized contributor model. This problem directly impacts open-source maintainers' ability to manage projects effectively, as legitimate contributions get buried under noise and maintainers spend time filtering spam instead of reviewing quality code. The lack of effective solutions threatens the sustainability of open-source development and could discourage both maintainers and genuine contributors. Unlike email spam where organizational reputation (IP addresses and domains) creates accountability for thousands of users, GitHub's individual contributor model lacks equivalent organizational pressure to maintain sender reputation. GitHub has recently introduced configurable PR limits for maintainers as a partial mitigation, though some projects are experimenting with alternative approaches like requiring non-textual meetings between maintainers and new contributors before first PR merges.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: Pull requests are GitHub's foundational collaboration feature that allow developers to propose, discuss, and review code changes before merging them into a project. Open-source projects rely on community contributions, but the low barrier to entry and lack of organizational accountability mechanisms make them vulnerable to spam—unsolicited, low-quality, or malicious contributions that waste maintainers' time. Email spam in the early 2000s faced similar challenges until reputation systems and organizational controls (like ISP blacklisting) created consequences for bulk senders.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">About pull requests - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: Community members highlight a key structural difference: email spam relied on organizational accountability (ISPs could blacklist servers affecting thousands of users), whereas GitHub's individual contributor model lacks equivalent organizational pressure. Genuine contributors express frustration that legitimate contributions are increasingly ignored or auto-closed by bots, while some projects are experimenting with solutions like requiring non-textual verification between maintainers and new contributors. GitHub's recent introduction of configurable PR limits is seen as a partial step toward addressing the problem.

**Tags**: `#open-source`, `#community`, `#maintainability`, `#spam-prevention`, `#github`

---

<a id="item-10"></a>
## [Google Introduces Computer Use Capabilities for Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google has announced built-in computer use capabilities for Gemini 3.5 Flash, enabling the model to see, reason, and take action across browser, mobile, and desktop environments by observing screenshots and executing mouse and keyboard actions. This feature allows developers to build custom agents that can interact with computer interfaces without requiring separate integrations. Computer use capabilities represent a significant step toward autonomous AI agents that can perform real-world tasks on behalf of users, expanding Gemini's applicability beyond text and function calling to full GUI automation. This capability is particularly valuable for developers building agentic systems that need to interact with legacy applications, web interfaces, and desktop tools without custom API integrations. Gemini 3.5 Flash's computer use feature leverages vision-language model capabilities to process visual information from screenshots and translate user commands into GUI interactions, though community feedback indicates reliability issues such as hallucinated data, incorrect command execution (like running destructive git commands), and limitations compared to competitors like Claude's Opus 4.8 and OpenAI's GPT-4. The feature also lacks MCP (Model Context Protocol) support in the Gemini app, which users note is available in competing solutions.

hackernews · swolpers · Jun 24, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48662999)

**Background**: Computer use in AI refers to the ability of large language models augmented with vision capabilities to interact with graphical user interfaces by interpreting screenshots and executing commands like mouse clicks and keyboard input. This represents an evolution from traditional function calling, where models invoke predefined APIs, to a more general-purpose approach where models can work with any application or interface. Vision-language models process both visual and textual information from screens to understand context and determine appropriate actions, similar to how a human user would navigate a computer.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/">Introducing computer use in Gemini 3 . 5 Flash</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://arxiv.org/abs/2402.07945">[2402.07945] ScreenAgent: A Vision Language Model-driven Computer Control Agent</a></li>

</ul>
</details>

**Discussion**: Community feedback reveals significant practical concerns about the implementation: users report that Gemini 3.5 Flash struggles with basic tasks like data extraction and reformatting, sometimes giving up after multiple errors; it has executed dangerous commands (like `git reset --hard`) contrary to user intent; and it lacks important features like MCP support that competitors offer. Users also express frustration with the model's instruction-following capabilities and prefer alternative solutions like Claude or free OpenAI plans, with some noting that Google's own performance graphs show Gemini 3.5 Flash underperforming compared to Claude Opus 4.8 and GPT-4.5.

**Tags**: `#AI/ML`, `#Gemini`, `#LLM-Agents`, `#Computer-Vision`, `#Tool-Use`

---

<a id="item-11"></a>
## [Nub: A Bun-like all-in-one toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 7.0/10

Colin McDonnell, creator of Zod, has released Nub, a lightweight Node.js toolkit that augments stock Node with transpilation (powered by oxc), module resolution hooks, and polyfills through a --require preload approach. The toolkit adds features like Worker and Temporal API polyfills while keeping code execution on Node's actual engine and standard library. Nub provides a lighter-weight alternative to Bun that improves Node.js developer experience (DX) without requiring a runtime switch, making it appealing for teams wanting better tooling while staying within the Node.js ecosystem. Early adoption signals show real-world value, with teams successfully migrating entire monorepos to Nub with zero issues and significant performance gains. Nub uses the oxc JavaScript transpiler (written in Rust) packaged as a Node-API add-on for fast transpilation, and leverages Node's native module resolution hooks API rather than --import for ESM support. The toolkit is purely additive—it doesn't replace Node's engine or stdlib, only augments them through hooks and preloading.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Bun is a modern JavaScript runtime that offers an all-in-one toolkit including a package manager, bundler, and test runner alongside runtime capabilities, providing superior developer experience but requiring users to switch from Node.js. Node.js module resolution hooks allow developers to customize how modules are found and loaded, while Node-API add-ons enable native code integration. The oxc project is a high-performance JavaScript toolchain written in Rust, offering significantly faster transpilation than alternatives like SWC and Biome.

<details><summary>References</summary>
<ul>
<li><a href="https://oxc.rs/">The JavaScript Oxidation Compiler</a></li>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://nodejs.org/api/module.html">Modules: `node:module` API | Node.js v26.3.1 Documentation</a></li>

</ul>
</details>

**Discussion**: Community response is highly positive, with commenters praising the idea as sensible and noting McDonnell's credibility (creator of Zod, former Bun employee). A monorepo team reported zero issues and exceptional speed after migration. Some technical discussion emerged around ESM support implementation details and whether Node's native TypeScript support makes the transpiler necessary, though these appear to be clarifying questions rather than criticisms.

**Tags**: `#Node.js`, `#Developer Tools`, `#TypeScript`, `#Build Systems`, `#Runtime`

---

<a id="item-12"></a>
## [Quoting Tom MacWright](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright observes that fully LLM-generated job applications, portfolios, and projects create 'accidental anonymity' by being generic and impersonal, revealing nothing authentic about candidates beyond their tool usage.

rss · Simon Willison · Jun 24, 18:13

**Tags**: `#AI`, `#careers`, `#hiring`, `#authenticity`, `#LLM-generated-content`

---

<a id="item-13"></a>
## [MuJoFil: GPU-Native Physics Simulator for Vision-Based RL Training](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 7.0/10

MuJoFil is a new open-source physics simulator that combines NVIDIA's Newton physics engine with Google's Filament renderer to enable high-fidelity, GPU-native vision-based reinforcement learning training. The project addresses MuJoCo's CPU bottleneck by leveraging GPU acceleration and supports flexible environment formats (GLB, OpenUSD) from online sources like Sketchfab and Polyhaven, with both CPU and GPU-accelerated variants available on PyPI. This addresses a critical pain point in RL research by enabling scalable, parallelizable vision-based RL training without MuJoCo's CPU limitations or the accessibility barriers of proprietary solutions like NVIDIA Isaac (which requires expensive hardware and licensing). The GPU-native approach with high visual fidelity and open-source availability makes advanced RL training more accessible to researchers with limited resources. MuJoFil offers physically-based rendering (PBR) texture support and plug-and-play functionality for importing environments from online sources, significantly expanding beyond MuJoCo's native environment limitations. The project is still in early development with acknowledged bugs, and the creator plans to make the code repository public on GitHub while currently offering installation via pip (mujofil for CPU variant, mujofil-warp for GPU variant, with potential renaming to mujofil-cuda).

reddit · r/MachineLearning · /u/MT1699 · Jun 24, 19:07

**Background**: MuJoCo is a widely-used physics simulator for robotics and RL research, but its CPU-based architecture limits parallelization. While MJX (MuJoCo XLA) provides GPU acceleration, it is not optimized for vision-based RL pipelines. NVIDIA's Newton is a newer GPU-accelerated physics engine developed jointly by NVIDIA, Google DeepMind, and Disney Research. Google's Filament is an open-source physically-based rendering engine that provides high-quality 3D graphics capabilities across multiple platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>
<li><a href="https://github.com/google/filament">google / filament : Filament is a real-time physically based rendering ...</a></li>
<li><a href="https://mujoco.readthedocs.io/en/stable/mjx.html">MuJoCo XLA (MJX) - MuJoCo Documentation</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#physics-simulation`, `#gpu-computing`, `#computer-vision`, `#open-source`

---

<a id="item-14"></a>
## [High Dimensional Dynamic RoPE: Improved Positional Embeddings with Cumulative Matrix Products](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 7.0/10

A researcher has proposed High Dimensional Dynamic RoPE (HDD-RoPE), a novel positional embedding method that extends standard RoPE by breaking token embeddings into larger chunks (e.g., 4-dimensional instead of 2-dimensional) and making rotation amounts data-dependent based on layer activations. When trained on the TinyStories dataset with a GPT-2-like model, HDD-RoPE achieves faster validation loss convergence compared to the baseline transformer using xPos, with reproducible code and detailed mathematical exposition available on GitHub. This work addresses a fundamental aspect of transformer architecture by proposing that positional information is inherently multidimensional rather than linear, which could improve how models understand hierarchical structures like paragraphs and sentences. The demonstrated faster convergence on TinyStories suggests potential efficiency gains in training, though broader validation on larger-scale experiments would strengthen the impact claim. HDD-RoPE uses 4-dimensional chunks instead of the standard 2-dimensional pairs, creating 6 axes of rotation (from 4 choose 2 combinations) to represent 6-dimensional position information, and employs data-dependent rotation rates that the model learns during training. The method was validated on a GPT-2-like architecture with 4 blocks and 768-dimensional embeddings, but the evaluation is limited to the relatively small TinyStories benchmark rather than larger language modeling tasks.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 24, 18:16

**Background**: Rotary Positional Embeddings (RoPE) are a modern technique for encoding position information in transformer models by rotating token embeddings in a multi-dimensional space, allowing models to naturally learn relative positions between tokens. Standard RoPE processes embeddings in pairs of two dimensions, with each pair rotated at a fixed rate determined by position in the sequence. xPos is an alternative positional encoding method designed for better extrapolation beyond training sequence lengths. The cumulative matrix product is a mathematical operation that sequentially multiplies matrices together, which the researcher repurposed as the foundation for HDD-RoPE's rotation mechanism.

<details><summary>References</summary>
<ul>
<li><a href="https://nn.labml.ai/transformers/rope/index.html">Rotary Positional Embeddings ( RoPE )</a></li>
<li><a href="https://medium.com/@DataDry/decoding-rotary-positional-embeddings-rope-the-secret-sauce-for-smarter-transformers-193cbc01e4ed">Decoding Rotary Positional Embeddings ( RoPE ): The... | Medium</a></li>

</ul>
</details>

**Tags**: `#positional-embeddings`, `#transformers`, `#RoPE`, `#machine-learning`, `#deep-learning`

---

<a id="item-15"></a>
## [Comprehensive LLM inference pricing comparison reveals surprising caching cost variations](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 7.0/10

A developer compiled public pricing data from seven major LLM providers (OpenRouter, DeepSeek, Together AI, Fireworks, Groq, and others) into a single spreadsheet, comparing input/output token costs, context windows, and cached input pricing across supported models. The analysis revealed that cached input token costs vary dramatically across providers—sometimes by tens of times—making caching policy potentially more important than headline token prices for common workloads. This resource directly addresses a critical pain point for engineers selecting LLM providers: the lack of centralized, comparable pricing information across vendors. For applications using agents with large system prompts, RAG pipelines, multi-turn conversations, or repeated prompt templates, understanding caching costs can dramatically reduce total cost of ownership and influence provider selection decisions. The spreadsheet does not include benchmark data such as latency tests or throughput measurements; it relies entirely on public pricing pages and APIs. The analysis identifies several gaps in provider transparency: some providers clearly expose caching policies while others barely document them, and the same model can vary in cost by multiple times depending on the provider, with additional variables like precision variants (FP16, FP8, quantized) and network egress costs not yet systematized.

reddit · r/MachineLearning · /u/Technomadlyf · Jun 24, 11:28

**Background**: Prompt caching (also called prefix caching or context caching) is a technique that reuses attention states across different LLM prompts, significantly reducing both latency and inference costs—particularly valuable for production workloads with repeated prompt structures. RAG (Retrieval-Augmented Generation) pipelines enhance AI model accuracy by fetching facts from external sources, often involving repeated context that benefits from caching. Tokens are the fundamental units of data that LLMs process; pricing models typically charge separately for input tokens (the prompt) and output tokens (the model's response), with cached tokens often priced at a discount.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bentoml.com/llm/inference-optimization/prefix-caching">Prefix caching | LLM Inference Handbook</a></li>
<li><a href="https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/">What Is Retrieval - Augmented Generation aka RAG | NVIDIA Blogs</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#LLM-pricing`, `#cost-optimization`, `#inference`, `#provider-comparison`, `#prompt-caching`

---