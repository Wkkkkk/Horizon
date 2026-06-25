---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 26 items, 15 important content pieces were selected

---

1. [OpenAI unveils Jalapeno, its first custom AI inference chip](#item-1) ⭐️ 9.0/10
2. [Qualcomm Acquires AI Infrastructure Startup Modular for $4 Billion](#item-2) ⭐️ 8.0/10
3. [Superhuman Generals.io Agent Achieved via Self-Play RL and Vision Transformers](#item-3) ⭐️ 8.0/10
4. [Anthropic alleges Alibaba illicitly extracted Claude AI capabilities](#item-4) ⭐️ 7.0/10
5. [Cloudflare launches self-managed OAuth for all users](#item-5) ⭐️ 7.0/10
6. [NVIDIA's 45°C liquid cooling cuts data center water consumption to near zero](#item-6) ⭐️ 7.0/10
7. [RubyLLM: Unified Ruby framework for multiple AI providers](#item-7) ⭐️ 7.0/10
8. [PR spam in open-source projects mirrors early 2000s email spam crisis](#item-8) ⭐️ 7.0/10
9. [Google Introduces Computer Use for Gemini 3.5 Flash](#item-9) ⭐️ 7.0/10
10. [Show HN: Nub – A Bun-like all-in-one toolkit for Node.js](#item-10) ⭐️ 7.0/10
11. [Quoting Tom MacWright](#item-11) ⭐️ 7.0/10
12. [Papers with Code launches curated open-source OCR models benchmark](#item-12) ⭐️ 7.0/10
13. [MuJoFil: GPU-Native Physics Simulator for Vision-Based RL Training](#item-13) ⭐️ 7.0/10
14. [HDD-RoPE: High-Dimensional Dynamic Rotary Positional Embeddings](#item-14) ⭐️ 7.0/10
15. [Comprehensive LLM inference pricing comparison reveals surprising caching cost variations](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI unveils Jalapeno, its first custom AI inference chip](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI has announced Jalapeno, its first custom AI inference chip developed in partnership with Broadcom and manufactured by TSMC, designed to accelerate inference for products like ChatGPT and the OpenAI API. The chip was developed from design to production in nine months, with OpenAI's own models used to accelerate parts of the design and optimization process. This move signals OpenAI's commitment to controlling its AI infrastructure and reducing dependency on third-party hardware providers, while also demonstrating the competitive pressure in the AI inference hardware market where companies like Google, Cerebras, and Groq are developing specialized silicon. Custom inference chips can significantly reduce latency and cost for large-scale AI deployments, making AI services more economically viable at scale. The chip is manufactured by TSMC and specifically optimized for large language model inference workloads. Community discussion reveals skepticism about OpenAI's claims regarding AI-assisted design acceleration, with some questioning whether the nine-month timeline represents a genuine breakthrough or standard marketing language.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference refers to the process of running trained machine learning models to generate predictions or outputs, as opposed to training which involves learning from data. Custom silicon chips designed specifically for AI workloads can provide significant performance and efficiency advantages over general-purpose processors. The AI chip market has become increasingly competitive, with major cloud providers like AWS (Inferentia), Google (TPU), and specialized startups developing their own hardware to optimize inference performance and reduce costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalcitizen.life/openai-unveils-jalapeno-its-first-custom-ai-chip-built-with-broadcom/">OpenAI Unveils Jalapeño, Its First Custom AI Chip Built With Broadcom</a></li>
<li><a href="https://www.braiviq.com/blog/ai-inference-hardware-war-2026-cerebras-groq-tesla-dojo-nvidia-uk-enterprise">The 2026 AI Inference Hardware War: Cerebras, Groq, Tesla Dojo...</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>

</ul>
</details>

**Discussion**: Community members expressed mixed reactions: some praised the move as significant infrastructure progress, while others questioned whether the AI-assisted design acceleration claim was genuine or marketing hype. Discussion also highlighted alternative approaches to inference optimization, such as burning model weights directly into silicon ROM (as proposed by Taals), and noted that competitors like Google with their TPU generations and other specialized chip makers (Cerebras, Groq) have been pursuing similar strategies longer.

**Tags**: `#AI Hardware`, `#Custom Chips`, `#Infrastructure`, `#LLM Inference`, `#Semiconductor Design`

---

<a id="item-2"></a>
## [Qualcomm Acquires AI Infrastructure Startup Modular for $4 Billion](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm has announced the acquisition of Modular, an AI infrastructure startup, for $4 billion. This deal brings Modular's Mojo programming language and AI/ML tooling capabilities under Qualcomm's portfolio, marking a significant strategic investment in AI infrastructure beyond traditional chip manufacturing. This acquisition signals Qualcomm's strategic pivot toward building a comprehensive AI/ML infrastructure stack and potentially reducing dependence on ARM architecture by investing in RISC-V and cross-platform AI tooling. The move reflects broader industry trends where chip makers are expanding beyond hardware into software ecosystems to remain competitive in the AI era. Modular is known for developing Mojo, a Python-like systems programming language built on the MLIR compiler framework that targets multiple hardware accelerators including GPUs, TPUs, and ASICs. The company has committed to open-sourcing Mojo in fall 2026, though as of June 2026 the compiler remains closed-source with an open-source standard library.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Modular was founded by Chris Lattner, a renowned compiler expert known for his work on LLVM and Swift. The company developed Mojo as a high-performance programming language designed to bridge the gap between Python's ease of use and the performance requirements of AI/ML workloads on heterogeneous hardware. Edge AI inference—running AI models on edge devices rather than cloud servers—has become increasingly important for latency-sensitive applications, and Qualcomm's acquisition reflects the industry's focus on optimizing AI compute across diverse hardware platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed, with some viewing the acquisition positively for Modular's employees and Qualcomm's AI ambitions, while others express disappointment about Mojo's prospects as a cross-platform language—comparing it to previous failed initiatives like SYCL and OpenCL. A key concern is whether a hardware company can successfully execute on AI software infrastructure, given founder Chris Lattner's previous public statements about hardware companies' struggles with AI stacks, creating an ironic tension in the deal.

**Tags**: `#M&A`, `#AI/ML Infrastructure`, `#Qualcomm`, `#Mojo Language`, `#Edge AI`

---

<a id="item-3"></a>
## [Superhuman Generals.io Agent Achieved via Self-Play RL and Vision Transformers](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A researcher trained a self-play reinforcement learning agent for Generals.io that achieved superhuman performance and ranked #1 on the human 1v1 leaderboard. The breakthrough involved reimplementing the entire pipeline in JAX and replacing CNNs with Vision Transformers, moving away from hand-crafted heuristics toward pure scaling. This work demonstrates that scaling and architectural choices (JAX for efficiency, Vision Transformers for better feature learning) can overcome domain-specific bottlenecks in game AI, providing a reproducible blueprint for building superhuman agents in imperfect-information RTS environments. The open-source release of the JAX simulator and agent code enables the community to build upon this approach and apply similar techniques to other strategic games. The agent was initially developed as a master's thesis using behavior cloning and RL fine-tuning with reward shaping, but required a second iteration to overcome performance plateaus. The researcher identified and addressed two critical bottlenecks: computational efficiency (switching from NumPy/PyTorch to JAX) and feature representation (replacing CNNs with Vision Transformers), both reflecting a philosophy of investing in scaling rather than ad-hoc domain-specific patches.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Self-play reinforcement learning is a technique where an agent learns by playing against itself, creating a powerful feedback loop that drives continuous improvement without requiring external opponents. Vision Transformers are neural network architectures that apply the transformer attention mechanism to image data, offering improved feature learning compared to traditional convolutional neural networks. JAX is a machine learning framework that combines automatic differentiation with XLA compilation, enabling efficient numerical computation and is often preferred for research tasks requiring low-level function definitions. Generals.io is a competitive real-time strategy game with imperfect information, where players must manage armies and territory against human opponents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_JAX">Google JAX - Wikipedia</a></li>
<li><a href="https://blog.roboflow.com/jax-framework/">What Is JAX ? Beginner's Guide to the Deep Learning Framework</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#self-play`, `#game-AI`, `#vision-transformers`, `#open-source`

---

<a id="item-4"></a>
## [Anthropic alleges Alibaba illicitly extracted Claude AI capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 7.0/10

Anthropic has accused Alibaba of illicitly extracting Claude AI model capabilities through unauthorized model distillation and reselling schemes in China, where Chinese resellers have been offering Claude API tokens at 70-90% below official prices by pooling accounts and reselling model outputs to various Chinese labs. This case highlights critical vulnerabilities in AI model security and intellectual property protection, raising important questions about how frontier AI labs can defend proprietary capabilities against unauthorized distillation and the broader implications for AI governance and IP ethics in the global market. Model distillation involves training a smaller or alternative model using outputs from a larger teacher model, a technique that is legitimate and widely used by AI labs for their own model optimization but becomes problematic when applied to competitors' models without authorization. The reselling scheme reportedly subsidizes model access in exchange for user logs and reasoning traces, which are then sold as training data to operate below cost.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Model distillation is a machine learning technique where knowledge from a large, powerful model (teacher) is transferred to a smaller model (student) to create more efficient, deployable versions while maintaining performance. While distillation is a standard, legitimate practice used by AI companies to optimize their own models for production, unauthorized distillation applies this same technique to extract capabilities from competitors' proprietary models without permission. In China, where direct access to Claude and ChatGPT is restricted, third-party resellers have created a market for discounted API access by pooling accounts and reselling model outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://beckreedriden.com/understanding-ai-distillation-in-the-trade-secret-context/">Understanding AI Distillation In The Trade Secret Context | Beck Reed Riden LLP</a></li>
<li><a href="https://www.fenwick.com/insights/publications/deepseek-model-distillation-and-the-future-of-ai-ip-protection">DeepSeek, Model Distillation, and the Future of AI IP Protection | Fenwick</a></li>

</ul>
</details>

**Discussion**: Community discussion reveals significant disagreement about the legitimacy of Anthropic's complaint, with some commenters noting that distillation is a standard technique used by thousands of businesses daily and questioning whether Anthropic's own training methods (which involved crawling the internet for training data) give them moral standing to complain about others copying their work. Others point out the specific reselling mechanisms involving payment fraud and data harvesting that distinguish unauthorized distillation from legitimate fine-tuning practices, while some raise broader questions about AI IP ethics and whether frontier labs trained on copyrighted content without permission have grounds to claim IP violations.

**Tags**: `#AI-security`, `#model-distillation`, `#intellectual-property`, `#LLM-governance`, `#China-tech`

---

<a id="item-5"></a>
## [Cloudflare launches self-managed OAuth for all users](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 7.0/10

Cloudflare has launched self-managed OAuth capabilities, enabling organizations to build and operate their own OAuth providers using Cloudflare's infrastructure. This allows developers to implement OAuth 2.1 protocol with PKCE support for third-party application integrations without relying on external identity providers. This capability addresses a significant gap in identity management infrastructure by allowing organizations to maintain control over their authentication systems while avoiding per-user pricing models common with managed services like Auth0. It enables companies to reduce costs and improve security posture by self-hosting OAuth infrastructure at scale. Cloudflare provides an OAuth Provider Library implemented as a TypeScript framework for Cloudflare Workers that handles the provider-side OAuth 2.1 protocol implementation. The solution demonstrates efficient resource utilization with remarkably low CPU usage at scale, as noted by the Ory Hydra author in community discussion.

hackernews · terryds · Jun 25, 02:18 · [Discussion](https://news.ycombinator.com/item?id=48668033)

**Background**: OAuth is an industry-standard authorization protocol that allows users to grant third-party applications access to their resources without sharing passwords. Traditionally, organizations either use managed OAuth providers (like Auth0) or implement complex identity management systems themselves. PKCE (Proof Key for Code Exchange) is a security extension to OAuth 2.0 designed to protect against authorization code interception attacks, particularly important for mobile and single-page applications.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/">Introducing self-managed OAuth clients · Changelog</a></li>
<li><a href="https://github.com/cloudflare/workers-oauth-provider">GitHub - cloudflare /workers- oauth -provider: OAuth provider library for...</a></li>
<li><a href="https://github.com/ory/hydra">GitHub - ory/hydra: Internet-scale OpenID Certified™ OpenID Connect and OAuth2.1 provider that integrates with your user management through headless APIs. Solve OIDC/OAuth2 user cases over night. Consume as a service on Ory Network or self-host. Trusted by OpenAI and many others for scale and security. Written in Go.</a></li>

</ul>
</details>

**Discussion**: Community response reveals significant debate about OAuth's complexity and appropriateness for different use cases. While the Ory Hydra author praised the implementation's performance, critics like zaptheimpaler highlighted OAuth's steep learning curve and frustration in enterprise environments, and Avery29 argued that simpler scoped API keys with rotation are often preferable for server-to-server access. Concerns were also raised about security implications of delegating infrastructure permissions to third parties, with sandeepkd questioning why major cloud providers like AWS avoid this model.

**Tags**: `#OAuth`, `#Authentication`, `#Infrastructure`, `#Identity Management`, `#Cloudflare`

---

<a id="item-6"></a>
## [NVIDIA's 45°C liquid cooling cuts data center water consumption to near zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 7.0/10

NVIDIA has unveiled a new liquid-cooling architecture for AI data centers that operates at 45°C (113°F) inlet coolant temperature, dramatically reducing water consumption compared to conventional air-cooled systems. This design enables direct-to-chip liquid cooling in the company's Rubin-generation reference architecture, eliminating the need for energy-intensive mechanical refrigeration. This development addresses critical sustainability challenges in data center operations, as cooling accounts for significant water and energy consumption in AI infrastructure. The higher coolant temperature also enables potential waste heat recovery through district heating systems, creating economic value for surrounding communities while reducing overall carbon emissions. The 45°C operating temperature is counterintuitively higher than industry norms but reduces cooling energy requirements by eliminating the need to cool water below ambient temperatures. However, the technology's effectiveness is climate-dependent, with performance varying significantly based on local ambient temperatures, and practical deployment requires geographic proximity between data centers and district heating infrastructure.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Data center cooling is a major operational challenge in AI infrastructure, traditionally relying on air conditioning or conventional liquid cooling systems that require significant water and energy inputs. District heating systems are community-scale networks that distribute thermal energy from centralized sources to multiple buildings for space heating and hot water, and waste heat from data centers—typically discarded—can be integrated into these systems to provide sustainable heating to surrounding areas.

<details><summary>References</summary>
<ul>
<li><a href="https://techstory.in/the-45c-breakthrough-nvidias-liquid-cooling-architecture-solves-data-center-water-crisis/">NVIDIA Liquid Cooling Design Cuts Water to Near Zero</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers">NVIDIA Unveils 45°C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.siemensenergy.com/global/en/home/products-services/solutions-usecase/low-carbon-heat.html">Decarbonizing Industrial Heat I Solutions and Technologies</a></li>

</ul>
</details>

**Discussion**: Community discussion reveals both enthusiasm and skepticism about the innovation. Commenters highlight the promising synergy with district heating systems (exemplified by Microsoft's existing deployment in Finland), but others question the technical novelty, noting that previous data center designs should have already optimized for higher coolant temperatures. Key concerns include climate dependency—the technology works best in cooler regions—and the practical challenge that data centers and district heating grids rarely locate adjacent to each other by accident, requiring intentional infrastructure planning.

**Tags**: `#data-center-infrastructure`, `#liquid-cooling`, `#sustainability`, `#thermal-management`, `#AI-infrastructure`

---

<a id="item-7"></a>
## [RubyLLM: Unified Ruby framework for multiple AI providers](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM is a Ruby gem that provides a unified, elegant API for integrating with multiple AI providers (such as OpenAI, Anthropic, xAI, and others), eliminating the need to use each provider's separate client library. The framework is gaining production adoption with version 2.0 in active development, as evidenced by real-world usage in projects like SerpTrail and derivative frameworks like Raix. RubyLLM addresses a critical pain point for Ruby developers by providing a single abstraction layer across multiple LLM providers, reducing vendor lock-in and allowing applications to switch providers with minimal code changes. This is significant for the Ruby/Rails ecosystem, which has historically lacked first-class AI integration tools comparable to frameworks available in other languages. The framework emphasizes clean Rails-native abstractions and handles tool-call loops automatically for building AI agents, though community feedback reveals some limitations including inconsistent caching behavior across providers (notably with xAI's completions API) and capability negotiation questions for version 2.0. Users praise the API design and out-of-the-box usability, comparing it favorably to Vercel's AI framework, though some have noted challenges with maintainer responsiveness on pull requests.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: Large Language Model (LLM) providers like OpenAI, Anthropic, and others each offer their own client libraries and APIs with different interfaces and capabilities. A unified abstraction layer allows developers to write application code once and switch between providers without rewriting business logic, following the principle of provider-agnostic design. This pattern has become increasingly important as organizations seek to avoid vendor lock-in and maintain flexibility in their AI infrastructure choices.

<details><summary>References</summary>
<ul>
<li><a href="https://rubyllm.com/overview/">Understand how RubyLLM works and how its components fit together</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ ruby _ llm : One delightful Ruby framework for every...</a></li>
<li><a href="https://medium.com/@ritukampani/future-proof-your-ai-building-a-gateway-for-multiple-llm-providers-b746f80cc169">Future-Proof Your AI: Building a Gateway for Multiple LLM Providers | by RK | Medium</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely positive about RubyLLM's API design and usability, with production users reporting 6+ months of successful deployment and derivative projects like Raix building on its abstractions. However, concerns were raised about maintainer responsiveness to pull requests, caching inconsistencies across providers (particularly with xAI), and questions about explicit capability negotiation in version 2.0, suggesting the framework is mature but faces some operational and technical challenges.

**Tags**: `#Ruby`, `#AI/LLM`, `#Framework`, `#Developer Tools`, `#Open Source`

---

<a id="item-8"></a>
## [PR spam in open-source projects mirrors early 2000s email spam crisis](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 7.0/10

Open-source projects are increasingly overwhelmed by low-quality and spam pull requests, creating significant maintainer burden similar to the email spam epidemic of the early 2000s. GitHub has recently introduced configurable pull request limits and archiving features to help maintainers filter and manage spam submissions more effectively. This problem directly impacts the sustainability of open-source projects by overwhelming maintainers with low-value work, potentially discouraging legitimate contributions and reducing project maintenance quality. The lack of organizational accountability mechanisms for individual contributors, unlike email servers' reputation systems, makes the problem particularly difficult to solve at scale. GitHub's new features include pull request archiving (hiding low-quality submissions from the default view while keeping them accessible to admins) and configurable PR limits for repository admins. Some projects have experimented with alternative approaches, such as requiring new contributors to meet maintainers in non-textual formats before their first PR is merged.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: Pull requests (PRs) are the primary mechanism for contributing code changes to open-source projects on GitHub. During Hacktoberfest and other events, spam contributors submit numerous low-quality or trivial PRs to gain rewards or inflate contribution metrics, similar to how email spammers flooded inboxes in the early 2000s. Unlike email systems where server administrators can enforce reputation and blacklist policies across thousands of users, GitHub's decentralized contributor model lacks equivalent organizational controls to prevent individual bad actors.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/">How pull request limits are cutting down the noise - The GitHub Blog</a></li>
<li><a href="https://github.com/marketplace/actions/spamtoberfest-pull-request-spam-checker">Spamtoberfest | Pull request spam checker - GitHub Marketplace</a></li>

</ul>
</details>

**Discussion**: Community members highlight a critical structural difference from email spam: email systems have organizational accountability through server reputation and blacklisting that affects hundreds of users, whereas GitHub lacks equivalent mechanisms to hold individual contributors accountable. Legitimate contributors express frustration that their genuine PRs are increasingly ignored or auto-closed by bots, while some projects have found success with alternative vetting methods like requiring non-textual interaction with maintainers before accepting first-time contributions.

**Tags**: `#open-source`, `#community-management`, `#github`, `#maintainer-burden`, `#spam-prevention`

---

<a id="item-9"></a>
## [Google Introduces Computer Use for Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google has announced computer use capabilities for Gemini 3.5 Flash, enabling the model to interact directly with computer interfaces, navigate applications, and perform tasks like filling forms and extracting data from visual content. This capability allows the AI agent to understand and manipulate desktop environments similarly to how a human user would interact with a computer. Computer use capabilities represent a significant step toward autonomous AI agents that can handle real-world tasks without human intervention, potentially transforming how users interact with software and automate workflows. This advancement is particularly important as it extends Gemini's applicability from text-based interactions to full desktop automation, competing with similar capabilities from other AI providers like Anthropic. Gemini 3.5 Flash operates with a 1M token context window and 66K token maximum output, positioning it as a fast, efficient model for agentic workflows. However, community feedback reveals significant reliability limitations: the model struggles with iterative corrections, sometimes invents data instead of accurately copying information, and can execute unintended destructive commands (such as running `git reset --hard` when not instructed), indicating that error-handling and instruction-following remain problematic in real-world usage.

hackernews · swolpers · Jun 24, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48662999)

**Background**: Computer use in AI refers to the ability of large language models to perceive and interact with computer interfaces through visual understanding and action execution, similar to how a human would use a mouse and keyboard. This capability builds on advances in multimodal AI (models that understand both text and images) and represents a natural evolution from tool-use and API-calling capabilities that earlier AI models possessed. The field has matured to the point where AI agents can now be deployed on real-world tasks across actual software environments, as measured by benchmarks like OSWorld.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3 . 5 Flash — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3 . 5 : frontier intelligence with action</a></li>

</ul>
</details>

**Discussion**: Community feedback reveals widespread concerns about the reliability and practical usability of Gemini 3.5 Flash's computer use feature. Users report critical failures including the model giving up after repeated errors, inventing data instead of accurately copying information, executing unintended destructive commands (like `git reset --hard`), and struggling with basic instruction comprehension. Additionally, commenters note that Gemini 3.5 Flash underperforms compared to competitors like Claude Opus and GPT-5.5 on performance benchmarks, and that missing features like MCP (Model Context Protocol) support limit its utility compared to alternatives.

**Tags**: `#AI/ML`, `#Gemini`, `#computer-vision-agents`, `#LLM-limitations`, `#tool-use`

---

<a id="item-10"></a>
## [Show HN: Nub – A Bun-like all-in-one toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 7.0/10

Nub is a Node.js all-in-one toolkit that augments the stock Node runtime with transpilation, module resolution, and polyfills via preload hooks, offering Bun-like developer experience without forking the runtime.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Tags**: `#nodejs`, `#tooling`, `#typescript`, `#developer-experience`, `#runtime`

---

<a id="item-11"></a>
## [Quoting Tom MacWright](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright observes that fully LLM-generated job applications, portfolios, and projects create a paradox where perfection masks authenticity, leaving hiring managers unable to assess the actual person behind the application.

rss · Simon Willison · Jun 24, 18:13

**Tags**: `#AI`, `#careers`, `#hiring`, `#LLM-generated-content`, `#professional-development`

---

<a id="item-12"></a>
## [Papers with Code launches curated open-source OCR models benchmark](https://www.reddit.com/r/MachineLearning/comments/1ueiam6/find_the_best_opensource_ocr_models_in_one_place/) ⭐️ 7.0/10

Papers with Code has published a comprehensive overview of open-source OCR (Optical Character Recognition) models and benchmarks at paperswithcode.co/tasks/ocr, featuring newly released models including Baidu's Unlimited OCR (a 3B-parameter model with Reference Sliding Window Attention) and Mistral's OCR 4 API. The curated resource aggregates top-performing models and major benchmarks like OlmOCRBench and OmniDocBench to help practitioners select the best OCR solution for their needs. OCR is critical for digitizing documents and enabling agentic AI systems to process unstructured data at scale, particularly for use cases like agentic RAG (retrieval-augmented generation) that powers chatbots and customer support systems. A centralized benchmark resource reduces friction for practitioners choosing among the growing number of OCR releases and ensures they adopt models with proven performance on standardized benchmarks. Baidu's Unlimited OCR introduces Reference Sliding Window Attention (R-SWA), an optimization technique that constrains attention computation to a fixed-size window of nearby tokens while maintaining reference context, enabling efficient inference. The top recommended models are Chandra OCR 2 (openly available for self-hosting or serverless API) and Mistral OCR v4 (API-only), with benchmarks from Ai2 and Shanghai AI Laboratory being the most authoritative.

reddit · r/MachineLearning · /u/NielsRogge · Jun 24, 16:26

**Background**: OCR (Optical Character Recognition) is the technology that converts scanned documents or PDFs into machine-readable text. Retrieval-augmented generation (RAG) is a technique that enhances large language models by retrieving relevant information from external data sources, and agentic RAG extends this by enabling AI agents to autonomously retrieve and process documents. The recent proliferation of OCR models on platforms like Hugging Face has made it difficult for practitioners to identify which models perform best, creating a need for centralized benchmarking and comparison resources.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/reference-sliding-window-attention-r-swa">Reference Sliding Window Attention ( R - SWA )</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-OCR">deepseek -ai/ DeepSeek - OCR · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#open-source-models`, `#document-processing`, `#benchmark-aggregation`, `#multimodal-AI`

---

<a id="item-13"></a>
## [MuJoFil: GPU-Native Physics Simulator for Vision-Based RL Training](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 7.0/10

A researcher has developed MuJoFil, an open-source simulator that combines NVIDIA's GPU-native Newton physics engine with Google's Filament renderer to enable high-fidelity, GPU-parallelizable vision-based reinforcement learning training. The project is available on PyPI with two variants: a CPU-based version (pip install mujofil) and a GPU-native CUDA variant (pip install mujofil-warp), with plans to make the code publicly available on GitHub. This addresses critical limitations in current RL simulation infrastructure: MuJoCo's CPU dependency creates parallelization bottlenecks, MJX lacks vision-based RL optimization, and NVIDIA Isaac requires expensive hardware and licensing. MuJoFil provides an accessible, free, open-source alternative that enables researchers with modest GPU resources to train vision-based policies efficiently. The simulator supports physically-based rendering (PBR) textures and plug-and-play functionality with multiple environment formats including GLB and OpenUSD, allowing users to import environments from online sources like Sketchfab and Polyhaven rather than being limited to MuJoCo-native environments. The project is still in early development with acknowledged bugs, and the developer is seeking community feedback on features and improvements.

reddit · r/MachineLearning · /u/MT1699 · Jun 24, 19:07

**Background**: MuJoCo is a widely-used physics engine for robotics simulation, but it runs primarily on CPUs, limiting parallel training of multiple environments. MJX is Google DeepMind's GPU-accelerated version of MuJoCo, but it was not designed specifically for vision-based reinforcement learning tasks. NVIDIA's Newton physics engine is a GPU-native reimplementation of MuJoCo's solver that can simulate 50,000+ environments simultaneously on high-end GPUs. Google's Filament is an open-source physically-based rendering engine that provides high-quality real-time 3D graphics across multiple platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>
<li><a href="https://github.com/google/filament">google / filament : Filament is a real-time physically based rendering ...</a></li>
<li><a href="https://pub.towardsai.net/isaac-sim-vs-mujoco-the-4-000-question-that-will-define-robotics-in-2025-4c41a2984c2c">Isaac Sim vs MuJoCo 2025: GPU Robotics Simulation... | Towards AI</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#physics-simulation`, `#GPU-acceleration`, `#computer-vision`, `#open-source`

---

<a id="item-14"></a>
## [HDD-RoPE: High-Dimensional Dynamic Rotary Positional Embeddings](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 7.0/10

A researcher has introduced HDD-RoPE, a novel positional embedding method that extends standard RoPE by using cumulative matrix products and treating position as multidimensional rather than linear. When trained on the TinyStories dataset with a GPT-2-like model (768-dimensional, 4 blocks), HDD-RoPE achieves faster validation loss convergence compared to baseline xPos, with full mathematical formalization and reproducible code available on GitHub. Positional embeddings are fundamental to how transformers understand sequence order and generalize to different context lengths, making improvements in this area directly impact model efficiency and performance. HDD-RoPE's approach of treating position as multidimensional and making rotation data-dependent could enable models to learn more nuanced positional relationships (e.g., paragraph or sentence structure) beyond simple linear position. HDD-RoPE breaks embedding chunks into larger groups (e.g., size 4) rather than pairs, creating multiple rotation axes (4 choose 2 = 6 axes for 4-dimensional chunks) to represent multidimensional position. The rotation amounts along each axis are made data-dependent, allowing the model to learn how to advance positions based on current layer activations, which differs from standard RoPE's fixed rotation rates.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 24, 18:16

**Background**: Rotary Positional Embeddings (RoPE) are a modern technique for encoding position information in transformers by rotating token embeddings in a multi-dimensional space, allowing models to naturally capture relative position dependencies. Standard RoPE processes embeddings in pairs, rotating each pair at predefined frequencies to represent linear sequence position. xPos is an extension of RoPE designed to improve extrapolation beyond training context length. Transformers rely on positional information to understand token order and generalize across different sequence lengths, making positional embedding design a critical component of model architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://nn.labml.ai/transformers/rope/index.html">Rotary Positional Embeddings ( RoPE )</a></li>
<li><a href="https://medium.com/@DataDry/decoding-rotary-positional-embeddings-rope-the-secret-sauce-for-smarter-transformers-193cbc01e4ed">Decoding Rotary Positional Embeddings ( RoPE ): The... | Medium</a></li>
<li><a href="https://github.com/jploski/RotaryEmbedding">jploski/RotaryEmbedding: Comparison of RoPE and xPos positional ...</a></li>

</ul>
</details>

**Tags**: `#positional-embeddings`, `#transformers`, `#attention-mechanisms`, `#deep-learning`, `#novel-architecture`

---

<a id="item-15"></a>
## [Comprehensive LLM inference pricing comparison reveals surprising caching cost variations](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 7.0/10

A developer compiled public pricing data from seven major LLM providers (OpenRouter, DeepSeek, Together AI, Fireworks, Groq, and others) into a single spreadsheet, comparing input/output token pricing, context windows, cached input pricing, and supported models. The analysis revealed that cached input costs vary dramatically across providers—sometimes by tens of times—making prompt caching policies potentially more important than headline token prices for certain workloads. This resource directly addresses a critical pain point for engineers evaluating LLM providers: the lack of centralized, comparable pricing information. For production systems running agents with large system prompts, RAG pipelines, multi-turn conversations, or repeated prompt templates, understanding caching policies can dramatically reduce operational costs—making this analysis invaluable for cost optimization decisions. The spreadsheet does not include benchmark data such as latency tests or throughput measurements; instead, it relies entirely on public pricing pages and provider APIs. Notable gaps the author identified for future versions include real throughput (tokens/sec), cold-start/queue times, model precision variants (FP16, FP8, quantized), egress costs, and reliability metrics.

reddit · r/MachineLearning · /u/Technomadlyf · Jun 24, 11:28

**Background**: Prompt caching is an optimization technique where large language models reuse attention states (internal representations of how words connect) across different prompts, avoiding redundant computation when the same context appears multiple times. This is particularly valuable in RAG (Retrieval-Augmented Generation) pipelines, which enhance LLM accuracy by retrieving and incorporating information from external data sources. Token pricing is the standard billing model for LLM inference, where costs are calculated based on the number of tokens (small units of text) processed as input and generated as output.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vellum.ai/llm-parameters/prompt-caching">Prompt Caching - LLM Parameter Guide - Vellum</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#LLM pricing`, `#cost optimization`, `#prompt caching`, `#provider comparison`, `#inference economics`

---