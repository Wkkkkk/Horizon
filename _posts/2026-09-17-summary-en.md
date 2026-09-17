---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
lang: en
---

> From 21 items, 10 important content pieces were selected

---

1. [Nvidia Introduces Native Rust GPU Programming](#item-1) ⭐️ 8.0/10
2. [Recovering Signing Keys for US Driver's License Barcodes](#item-2) ⭐️ 8.0/10
3. [4B Model Achieves 81% Faster Query Plans than Postgres](#item-3) ⭐️ 8.0/10
4. [Breaking the 1.58-bit Barrier for Ternary LLMs](#item-4) ⭐️ 8.0/10
5. [LARA: Modular Adaptation for Frozen Language Models](#item-5) ⭐️ 8.0/10
6. [Xiaomi Mimo 2.6 Launches Live Post-Training Dashboard](#item-6) ⭐️ 7.0/10
7. [Complexities of Data Backups Explored](#item-7) ⭐️ 7.0/10
8. [HarnessTax: Evaluating the Impact of Coding Harnesses on AI Models](#item-8) ⭐️ 7.0/10
9. [Mustafa Suleyman on AI Model Rights and Ethics](#item-9) ⭐️ 7.0/10
10. [GoBench: Evaluating LLMs on 9x9 Go Games](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Nvidia Introduces Native Rust GPU Programming](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia has announced support for native GPU programming in Rust, allowing developers to write GPU kernels using the Rust language. This new capability was introduced on September 8, 2026. This development is significant as it opens up new possibilities for the Rust and GPU programming communities, potentially improving performance and developer experience. It aligns with industry trends towards more versatile and safer programming languages. The support for Rust in GPU programming is facilitated through Nvidia's CUDA platform, which traditionally supports languages like C++ and Python. This move potentially enhances Rust's utility in high-performance computing and artificial intelligence applications.

hackernews · nonmaskable · Sep 16, 11:15 · [Discussion](https://news.ycombinator.com/item?id=49724881)

**Background**: CUDA, developed by Nvidia, is a parallel computing platform and API model that allows for general-purpose computing on GPUs. It enables developers to leverage the power of GPU acceleration for tasks beyond traditional graphics rendering, such as scientific computations and AI workloads. Rust is a systems programming language known for its safety and concurrency features, making it increasingly popular in performance-critical applications.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/">Introducing CUDA Rust: Two Tracks for Writing GPU Kernels</a></li>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with some expressing concerns about vendor lock-in with CUDA, while others see potential in combining Rust's features with GPU programming. There is also interest in how this development might affect other GPU architectures and programming models.

**Tags**: `#Nvidia`, `#Rust`, `#GPU Programming`, `#CUDA`, `#Software Development`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fnvidia-announces-native-gpu-programming-in-rust-a641edc0&content=---%0Atitle%3A%20%22Nvidia%20announces%20native%20GPU%20programming%20in%20Rust%22%0Aurl%3A%20https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintroducing-cuda-rust-two-tracks-for-writing-gpu-kernels%2F%0Asource%3A%20%22hackernews%20%C2%B7%20nonmaskable%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22Nvidia%22%2C%20%22Rust%22%2C%20%22GPU%20Programming%22%2C%20%22CUDA%22%2C%20%22Software%20Development%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BNvidia%20announces%20native%20GPU%20programming%20in%20Rust%5D%28https%3A%2F%2Fdeveloper.nvidia.com%2Fblog%2Fintroducing-cuda-rust-two-tracks-for-writing-gpu-kernels%2F%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20nonmaskable%0A%0ANvidia%20has%20announced%20support%20for%20native%20GPU%20programming%20in%20Rust%2C%20allowing%20developers%20to%20write%20GPU%20kernels%20using%20the%20Rust%20language.%20This%20new%20capability%20was%20introduced%20on%20September%208%2C%202026.%20This%20development%20is%20significant%20as%20it%20opens%20up%20new%20possibilities%20for%20the%20Rust%20and%20GPU%20programming%20communities%2C%20potentially%20improving%20performance%20and%20developer%20experience.%20It%20aligns%20with%20industry%20trends%20towards%20more%20versatile%20and%20safer%20programming%20languages.%20The%20support%20for%20Rust%20in%20GPU%20programming%20is%20facilitated%20through%20Nvidia%27s%20CUDA%20platform%2C%20which%20traditionally%20supports%20languages%20like%20C%2B%2B%20and%20Python.%20This%20move%20potentially%20enhances%20Rust%27s%20utility%20in%20high-performance%20computing%20and%20artificial%20intelligence%20applications.%0A%0A%23%23%20Background%0ACUDA%2C%20developed%20by%20Nvidia%2C%20is%20a%20parallel%20computing%20platform%20and%20API%20model%20that%20allows%20for%20general-purpose%20computing%20on%20GPUs.%20It%20enables%20developers%20to%20leverage%20the%20power%20of%20GPU%20acceleration%20for%20tasks%20beyond%20traditional%20graphics%20rendering%2C%20such%20as%20scientific%20computations%20and%20AI%20workloads.%20Rust%20is%20a%20systems%20programming%20language%20known%20for%20its%20safety%20and%20concurrency%20features%2C%20making%20it%20increasingly%20popular%20in%20performance-critical%20applications.%0A%0A%23%23%20Discussion%0ACommunity%20reactions%20are%20mixed%2C%20with%20some%20expressing%20concerns%20about%20vendor%20lock-in%20with%20CUDA%2C%20while%20others%20see%20potential%20in%20combining%20Rust%27s%20features%20with%20GPU%20programming.%20There%20is%20also%20interest%20in%20how%20this%20development%20might%20affect%20other%20GPU%20architectures%20and%20programming%20models.%0A">💾 Save to Obsidian</a>

---

<a id="item-2"></a>
## [Recovering Signing Keys for US Driver's License Barcodes](https://ryan.science/blog/keys-not-included) ⭐️ 8.0/10

The article explores the recovery of signing keys for US driver's license barcodes, revealing potential security vulnerabilities. This investigation highlights weaknesses in the cryptographic practices used in identity verification systems. This is significant because it exposes vulnerabilities in identity verification systems that rely on driver's license barcodes. Such weaknesses could be exploited, affecting industries like banking and security that depend on reliable identity verification. The investigation found that while public keys can be determined from barcodes, the signing keys themselves were not directly recoverable. The discussion also touches on the implications of post-quantum threats to current cryptographic methods.

hackernews · Ryan5453 · Sep 17, 03:03 · [Discussion](https://news.ycombinator.com/item?id=49735930)

**Background**: Driver's licenses in the US often use barcodes that contain encoded information, including digital signatures for verification. Digital signatures are cryptographic tools that ensure the authenticity and integrity of digital messages or documents. The security of these systems relies on the confidentiality of signing keys, which, if compromised, could allow forgeries.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49735930">Keys Not Included: recovering the signing keys for US... | Hacker News</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of skepticism and concern. Some users argue that public keys are meant to be disclosed, while others emphasize the potential impact of quantum computing on cryptographic security. There are also discussions about the practical implications for industries like banking.

**Tags**: `#security`, `#cryptography`, `#identity verification`, `#reverse engineering`, `#digital signatures`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fkeys-not-included-recovering-the-signing-keys-for-us-driver%27s-license-barcodes-16cf108d&content=---%0Atitle%3A%20%22Keys%20Not%20Included%3A%20recovering%20the%20signing%20keys%20for%20US%20driver%27s%20license%20barcodes%22%0Aurl%3A%20https%3A%2F%2Fryan.science%2Fblog%2Fkeys-not-included%0Asource%3A%20%22hackernews%20%C2%B7%20Ryan5453%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22security%22%2C%20%22cryptography%22%2C%20%22identity%20verification%22%2C%20%22reverse%20engineering%22%2C%20%22digital%20signatures%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BKeys%20Not%20Included%3A%20recovering%20the%20signing%20keys%20for%20US%20driver%27s%20license%20barcodes%5D%28https%3A%2F%2Fryan.science%2Fblog%2Fkeys-not-included%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20Ryan5453%0A%0AThe%20article%20explores%20the%20recovery%20of%20signing%20keys%20for%20US%20driver%27s%20license%20barcodes%2C%20revealing%20potential%20security%20vulnerabilities.%20This%20investigation%20highlights%20weaknesses%20in%20the%20cryptographic%20practices%20used%20in%20identity%20verification%20systems.%20This%20is%20significant%20because%20it%20exposes%20vulnerabilities%20in%20identity%20verification%20systems%20that%20rely%20on%20driver%27s%20license%20barcodes.%20Such%20weaknesses%20could%20be%20exploited%2C%20affecting%20industries%20like%20banking%20and%20security%20that%20depend%20on%20reliable%20identity%20verification.%20The%20investigation%20found%20that%20while%20public%20keys%20can%20be%20determined%20from%20barcodes%2C%20the%20signing%20keys%20themselves%20were%20not%20directly%20recoverable.%20The%20discussion%20also%20touches%20on%20the%20implications%20of%20post-quantum%20threats%20to%20current%20cryptographic%20methods.%0A%0A%23%23%20Background%0ADriver%27s%20licenses%20in%20the%20US%20often%20use%20barcodes%20that%20contain%20encoded%20information%2C%20including%20digital%20signatures%20for%20verification.%20Digital%20signatures%20are%20cryptographic%20tools%20that%20ensure%20the%20authenticity%20and%20integrity%20of%20digital%20messages%20or%20documents.%20The%20security%20of%20these%20systems%20relies%20on%20the%20confidentiality%20of%20signing%20keys%2C%20which%2C%20if%20compromised%2C%20could%20allow%20forgeries.%0A%0A%23%23%20Discussion%0ACommunity%20comments%20reflect%20a%20mix%20of%20skepticism%20and%20concern.%20Some%20users%20argue%20that%20public%20keys%20are%20meant%20to%20be%20disclosed%2C%20while%20others%20emphasize%20the%20potential%20impact%20of%20quantum%20computing%20on%20cryptographic%20security.%20There%20are%20also%20discussions%20about%20the%20practical%20implications%20for%20industries%20like%20banking.%0A">💾 Save to Obsidian</a>

---

<a id="item-3"></a>
## [4B Model Achieves 81% Faster Query Plans than Postgres](https://rohanbansal.com/qorl) ⭐️ 8.0/10

A 4 billion parameter model was trained to produce query plans that are 81% faster than those generated by Postgres on a specific dataset. This development is significant as it showcases the potential of large language models in optimizing database query performance, which could revolutionize database management systems. The model's performance was tested on an 8 GB dataset that fits entirely in memory, with specific settings like enable_sort=off and random_page_cost=1.1, which may not reflect real-world scenarios.

hackernews · polyphilz · Sep 16, 18:50 · [Discussion](https://news.ycombinator.com/item?id=49731285)

**Background**: Query optimization is a critical process in database management, aiming to determine the most efficient way to execute a query. Traditional systems like Postgres use heuristics and cost-based methods to generate query plans. Large language models (LLMs), like the 4 billion parameter model discussed, are typically used for natural language processing tasks but are now being explored for database optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_large_language_models">List of large language models - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed skepticism about the model's practicality, noting that the test conditions were not representative of real-world workloads. Concerns were raised about overfitting and the model's reliability in production environments. Some suggested that more sophisticated approaches, like neural net heuristics, might be more effective.

**Tags**: `#database`, `#query optimization`, `#machine learning`, `#Postgres`, `#performance`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Ftraining-a-4b-model-to-produce-81%25-faster-query-plans-than-postgres-4b99a853&content=---%0Atitle%3A%20%22Training%20a%204B%20model%20to%20produce%2081%25%20faster%20query%20plans%20than%20Postgres%22%0Aurl%3A%20https%3A%2F%2Frohanbansal.com%2Fqorl%0Asource%3A%20%22hackernews%20%C2%B7%20polyphilz%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22database%22%2C%20%22query%20optimization%22%2C%20%22machine%20learning%22%2C%20%22Postgres%22%2C%20%22performance%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BTraining%20a%204B%20model%20to%20produce%2081%25%20faster%20query%20plans%20than%20Postgres%5D%28https%3A%2F%2Frohanbansal.com%2Fqorl%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20polyphilz%0A%0AA%204%20billion%20parameter%20model%20was%20trained%20to%20produce%20query%20plans%20that%20are%2081%25%20faster%20than%20those%20generated%20by%20Postgres%20on%20a%20specific%20dataset.%20This%20development%20is%20significant%20as%20it%20showcases%20the%20potential%20of%20large%20language%20models%20in%20optimizing%20database%20query%20performance%2C%20which%20could%20revolutionize%20database%20management%20systems.%20The%20model%27s%20performance%20was%20tested%20on%20an%208%20GB%20dataset%20that%20fits%20entirely%20in%20memory%2C%20with%20specific%20settings%20like%20enable_sort%3Doff%20and%20random_page_cost%3D1.1%2C%20which%20may%20not%20reflect%20real-world%20scenarios.%0A%0A%23%23%20Background%0AQuery%20optimization%20is%20a%20critical%20process%20in%20database%20management%2C%20aiming%20to%20determine%20the%20most%20efficient%20way%20to%20execute%20a%20query.%20Traditional%20systems%20like%20Postgres%20use%20heuristics%20and%20cost-based%20methods%20to%20generate%20query%20plans.%20Large%20language%20models%20%28LLMs%29%2C%20like%20the%204%20billion%20parameter%20model%20discussed%2C%20are%20typically%20used%20for%20natural%20language%20processing%20tasks%20but%20are%20now%20being%20explored%20for%20database%20optimization.%0A%0A%23%23%20Discussion%0ACommunity%20members%20expressed%20skepticism%20about%20the%20model%27s%20practicality%2C%20noting%20that%20the%20test%20conditions%20were%20not%20representative%20of%20real-world%20workloads.%20Concerns%20were%20raised%20about%20overfitting%20and%20the%20model%27s%20reliability%20in%20production%20environments.%20Some%20suggested%20that%20more%20sophisticated%20approaches%2C%20like%20neural%20net%20heuristics%2C%20might%20be%20more%20effective.%0A">💾 Save to Obsidian</a>

---

<a id="item-4"></a>
## [Breaking the 1.58-bit Barrier for Ternary LLMs](https://arxiv.org/abs/2609.16338) ⭐️ 8.0/10

A new method called BITCOS reduces the bit usage in ternary LLMs by exploiting weight distribution, potentially enhancing efficiency if integrated into hardware. This breakthrough could significantly improve the efficiency of large language models by reducing memory and computational requirements, making them more feasible for deployment on less specialized hardware. The BITCOS method reduces the bit usage from 1.58 to 1.48 bits per weight by taking advantage of the fact that zeros account for up to 51.5% of all weights in ternary LLMs.

hackernews · matt_d · Sep 16, 20:59 · [Discussion](https://news.ycombinator.com/item?id=49732931)

**Background**: Ternary LLMs are a type of large language model that uses weights restricted to three values: −1, 0, and +1, which reduces memory footprint and speeds up processing. These models are known as 1.58-bit LLMs because a value with three states contains approximately 1.58 bits of information. They are designed to be computationally efficient and can perform comparably to full-precision models on various tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ternary_LLM">Ternary LLM</a></li>
<li><a href="https://arxiv.org/abs/2609.16338">[2609.16338] Breaking the 1.58-bit Barrier for Ternary LLMs - arXiv</a></li>

</ul>
</details>

**Discussion**: Community members are intrigued by the efficiency gains and potential hardware integration of the BITCOS method. Some express surprise that such adaptive encoding wasn't standard practice, while others debate the merits of ternary quantization versus other methods.

**Tags**: `#LLM`, `#quantization`, `#machine learning`, `#hardware optimization`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fbreaking-the-1.58-bit-barrier-for-ternary-llms-cab4f1a0&content=---%0Atitle%3A%20%22Breaking%20the%201.58-bit%20Barrier%20for%20Ternary%20LLMs%22%0Aurl%3A%20https%3A%2F%2Farxiv.org%2Fabs%2F2609.16338%0Asource%3A%20%22hackernews%20%C2%B7%20matt_d%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22LLM%22%2C%20%22quantization%22%2C%20%22machine%20learning%22%2C%20%22hardware%20optimization%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BBreaking%20the%201.58-bit%20Barrier%20for%20Ternary%20LLMs%5D%28https%3A%2F%2Farxiv.org%2Fabs%2F2609.16338%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20matt_d%0A%0AA%20new%20method%20called%20BITCOS%20reduces%20the%20bit%20usage%20in%20ternary%20LLMs%20by%20exploiting%20weight%20distribution%2C%20potentially%20enhancing%20efficiency%20if%20integrated%20into%20hardware.%20This%20breakthrough%20could%20significantly%20improve%20the%20efficiency%20of%20large%20language%20models%20by%20reducing%20memory%20and%20computational%20requirements%2C%20making%20them%20more%20feasible%20for%20deployment%20on%20less%20specialized%20hardware.%20The%20BITCOS%20method%20reduces%20the%20bit%20usage%20from%201.58%20to%201.48%20bits%20per%20weight%20by%20taking%20advantage%20of%20the%20fact%20that%20zeros%20account%20for%20up%20to%2051.5%25%20of%20all%20weights%20in%20ternary%20LLMs.%0A%0A%23%23%20Background%0ATernary%20LLMs%20are%20a%20type%20of%20large%20language%20model%20that%20uses%20weights%20restricted%20to%20three%20values%3A%20%E2%88%921%2C%200%2C%20and%20%2B1%2C%20which%20reduces%20memory%20footprint%20and%20speeds%20up%20processing.%20These%20models%20are%20known%20as%201.58-bit%20LLMs%20because%20a%20value%20with%20three%20states%20contains%20approximately%201.58%20bits%20of%20information.%20They%20are%20designed%20to%20be%20computationally%20efficient%20and%20can%20perform%20comparably%20to%20full-precision%20models%20on%20various%20tasks.%0A%0A%23%23%20Discussion%0ACommunity%20members%20are%20intrigued%20by%20the%20efficiency%20gains%20and%20potential%20hardware%20integration%20of%20the%20BITCOS%20method.%20Some%20express%20surprise%20that%20such%20adaptive%20encoding%20wasn%27t%20standard%20practice%2C%20while%20others%20debate%20the%20merits%20of%20ternary%20quantization%20versus%20other%20methods.%0A">💾 Save to Obsidian</a>

---

<a id="item-5"></a>
## [LARA: Modular Adaptation for Frozen Language Models](https://www.reddit.com/r/MachineLearning/comments/1whx9tr/lara_small_composable_behaviours_for_frozen_llms_p/) ⭐️ 8.0/10

LARA introduces a method for adapting frozen language models using lightweight residual adapters. This allows multiple behaviors to be combined or switched at inference time. This approach could significantly impact how language models are fine-tuned and utilized across different tasks, offering a more flexible and efficient way to adapt models without retraining. LARA uses low-rank residual adapters at selected layers, allowing behaviors to be loaded, removed, blended, or routed during inference. It supports a mixture of behaviors, enabling a single model to perform multiple tasks.

reddit · r/MachineLearning · /u/kertara · Sep 16, 13:28

**Background**: Frozen language models are pre-trained models that are not further trained on downstream tasks. Residual adapters are a method to adapt these models by adding small, trainable modules. This allows the model to retain its original capabilities while being adapted to new tasks without changing the core model weights.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1705.08045">Learning multiple visual domains with residual adapters - arXiv</a></li>
<li><a href="https://arxiv.org/html/2110.07904">SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer</a></li>

</ul>
</details>

**Discussion**: The community has shown interest in the practical applications of LARA, particularly in comparison to existing methods like LoRA. There is a focus on the flexibility and efficiency of this approach.

**Tags**: `#Machine Learning`, `#Language Models`, `#Model Adaptation`, `#PyTorch`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Flara-small%2C-composable-behaviours-for-frozen-llms-p-ab794833&content=---%0Atitle%3A%20%22LARA%3A%20small%2C%20composable%20behaviours%20for%20frozen%20LLMs%20%5BP%5D%22%0Aurl%3A%20https%3A%2F%2Fwww.reddit.com%2Fr%2FMachineLearning%2Fcomments%2F1whx9tr%2Flara_small_composable_behaviours_for_frozen_llms_p%2F%0Asource%3A%20%22reddit%20%C2%B7%20r%2FMachineLearning%22%0Ascore%3A%208.0%0Atags%3A%20%5B%22Machine%20Learning%22%2C%20%22Language%20Models%22%2C%20%22Model%20Adaptation%22%2C%20%22PyTorch%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BLARA%3A%20small%2C%20composable%20behaviours%20for%20frozen%20LLMs%20%28P%29%5D%28https%3A%2F%2Fwww.reddit.com%2Fr%2FMachineLearning%2Fcomments%2F1whx9tr%2Flara_small_composable_behaviours_for_frozen_llms_p%2F%29%0A%E2%AD%90%EF%B8%8F%208.0%2F10%20%C2%B7%20reddit%20%C2%B7%20r%2FMachineLearning%0A%0ALARA%20introduces%20a%20method%20for%20adapting%20frozen%20language%20models%20using%20lightweight%20residual%20adapters.%20This%20allows%20multiple%20behaviors%20to%20be%20combined%20or%20switched%20at%20inference%20time.%20This%20approach%20could%20significantly%20impact%20how%20language%20models%20are%20fine-tuned%20and%20utilized%20across%20different%20tasks%2C%20offering%20a%20more%20flexible%20and%20efficient%20way%20to%20adapt%20models%20without%20retraining.%20LARA%20uses%20low-rank%20residual%20adapters%20at%20selected%20layers%2C%20allowing%20behaviors%20to%20be%20loaded%2C%20removed%2C%20blended%2C%20or%20routed%20during%20inference.%20It%20supports%20a%20mixture%20of%20behaviors%2C%20enabling%20a%20single%20model%20to%20perform%20multiple%20tasks.%0A%0A%23%23%20Background%0AFrozen%20language%20models%20are%20pre-trained%20models%20that%20are%20not%20further%20trained%20on%20downstream%20tasks.%20Residual%20adapters%20are%20a%20method%20to%20adapt%20these%20models%20by%20adding%20small%2C%20trainable%20modules.%20This%20allows%20the%20model%20to%20retain%20its%20original%20capabilities%20while%20being%20adapted%20to%20new%20tasks%20without%20changing%20the%20core%20model%20weights.%0A%0A%23%23%20Discussion%0AThe%20community%20has%20shown%20interest%20in%20the%20practical%20applications%20of%20LARA%2C%20particularly%20in%20comparison%20to%20existing%20methods%20like%20LoRA.%20There%20is%20a%20focus%20on%20the%20flexibility%20and%20efficiency%20of%20this%20approach.%0A">💾 Save to Obsidian</a>

---

<a id="item-6"></a>
## [Xiaomi Mimo 2.6 Launches Live Post-Training Dashboard](https://mimo.xiaomi.com/rl/) ⭐️ 7.0/10

Xiaomi has introduced a live post-training dashboard for its Mimo 2.6 AI model. This feature provides real-time tracking of reinforcement learning metrics. This update enhances transparency in AI model training, offering users insights into the model's performance. It positions Xiaomi as a competitive player in the AI space, challenging established models like those from OpenAI and Anthropic. The live dashboard streams reward curves and evaluation metrics, which are not typically offered by competitors. This transparency could influence user trust and adoption.

hackernews · krackers · Sep 16, 20:09 · [Discussion](https://news.ycombinator.com/item?id=49732270)

**Background**: Xiaomi's Mimo series is part of its efforts to enter the open-source AI market. Mimo 2.6 follows the release of Mimo 2.5-Pro, which was praised for its capabilities in software engineering tasks. The introduction of a live post-training dashboard is a move to provide greater transparency and user engagement.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/rl/">mimo-v2.6 RL</a></li>
<li><a href="https://aiweekly.co/alerts/xiaomi-publishes-live-post-training-dashboard-for-mimo-26-rl-run-streams-real">Xiaomi Publishes Live Post - Training Dashboard for Mimo... | AI Weekly</a></li>
<li><a href="https://melink.ai/mimo-2-6-training-dashboard/">MiMo 2.6 Training Dashboard Goes Live</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely positive, with users appreciating the model's power and cost-effectiveness. Some users compare it favorably to Anthropic models, while others express concerns about the implications of open-source AI.

**Tags**: `#AI`, `#Machine Learning`, `#Software Engineering`, `#Model Deployment`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fxiaomi-mimo-2.6-live-post-training-dashboard-e15e9f57&content=---%0Atitle%3A%20%22Xiaomi%20Mimo%202.6%20live%20post-training%20dashboard%22%0Aurl%3A%20https%3A%2F%2Fmimo.xiaomi.com%2Frl%2F%0Asource%3A%20%22hackernews%20%C2%B7%20krackers%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22AI%22%2C%20%22Machine%20Learning%22%2C%20%22Software%20Engineering%22%2C%20%22Model%20Deployment%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BXiaomi%20Mimo%202.6%20live%20post-training%20dashboard%5D%28https%3A%2F%2Fmimo.xiaomi.com%2Frl%2F%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20krackers%0A%0AXiaomi%20has%20introduced%20a%20live%20post-training%20dashboard%20for%20its%20Mimo%202.6%20AI%20model.%20This%20feature%20provides%20real-time%20tracking%20of%20reinforcement%20learning%20metrics.%20This%20update%20enhances%20transparency%20in%20AI%20model%20training%2C%20offering%20users%20insights%20into%20the%20model%27s%20performance.%20It%20positions%20Xiaomi%20as%20a%20competitive%20player%20in%20the%20AI%20space%2C%20challenging%20established%20models%20like%20those%20from%20OpenAI%20and%20Anthropic.%20The%20live%20dashboard%20streams%20reward%20curves%20and%20evaluation%20metrics%2C%20which%20are%20not%20typically%20offered%20by%20competitors.%20This%20transparency%20could%20influence%20user%20trust%20and%20adoption.%0A%0A%23%23%20Background%0AXiaomi%27s%20Mimo%20series%20is%20part%20of%20its%20efforts%20to%20enter%20the%20open-source%20AI%20market.%20Mimo%202.6%20follows%20the%20release%20of%20Mimo%202.5-Pro%2C%20which%20was%20praised%20for%20its%20capabilities%20in%20software%20engineering%20tasks.%20The%20introduction%20of%20a%20live%20post-training%20dashboard%20is%20a%20move%20to%20provide%20greater%20transparency%20and%20user%20engagement.%0A%0A%23%23%20Discussion%0ACommunity%20feedback%20is%20largely%20positive%2C%20with%20users%20appreciating%20the%20model%27s%20power%20and%20cost-effectiveness.%20Some%20users%20compare%20it%20favorably%20to%20Anthropic%20models%2C%20while%20others%20express%20concerns%20about%20the%20implications%20of%20open-source%20AI.%0A">💾 Save to Obsidian</a>

---

<a id="item-7"></a>
## [Complexities of Data Backups Explored](https://filipovski.net/2026/09/16/backups-arent-simple.html) ⭐️ 7.0/10

The article delves into the intricacies of data backups, using personal stories and technical solutions to highlight their importance. It has generated significant community engagement with 143 comments sharing experiences and insights. Data backups are a critical component of data management, essential for preventing data loss. Understanding their complexities can help individuals and organizations better protect their data assets. The article discusses various backup strategies, including the use of ZFS snapshots and offsite syncs, and emphasizes the importance of distinguishing between ephemeral and persistent data. It also highlights the shift from merely backing up data to focusing on data restoration.

hackernews · afilipovski · Sep 16, 20:27 · [Discussion](https://news.ycombinator.com/item?id=49732513)

**Background**: Data backup is a process of copying and archiving computer data to ensure it can be restored in case of data loss. Common backup strategies include full, incremental, and differential backups. The 3-2-1 backup rule is a widely recommended practice, suggesting three copies of data, on two different media, with one copy offsite.

<details><summary>References</summary>
<ul>
<li><a href="https://www.splunk.com/en_us/blog/learn/data-backup-strategies.html">Data Backup Strategies: The Ultimate Guide - Splunk</a></li>
<li><a href="https://portworx.com/knowledge-hub/incremental-vs-differential-backup/">Incremental vs Differential Backup: Which Is Best for You? - Portworx</a></li>

</ul>
</details>

**Discussion**: Community members shared personal anecdotes of data loss, emphasizing the importance of reliable backup solutions. Some highlighted the transition from backup to restoration as a key focus, while others discussed technical preferences like ZFS snapshots.

**Tags**: `#backups`, `#data management`, `#personal experiences`, `#technical insights`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fbackups-aren%27t-simple-ec59fc44&content=---%0Atitle%3A%20%22Backups%20Aren%27t%20Simple%22%0Aurl%3A%20https%3A%2F%2Ffilipovski.net%2F2026%2F09%2F16%2Fbackups-arent-simple.html%0Asource%3A%20%22hackernews%20%C2%B7%20afilipovski%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22backups%22%2C%20%22data%20management%22%2C%20%22personal%20experiences%22%2C%20%22technical%20insights%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BBackups%20Aren%27t%20Simple%5D%28https%3A%2F%2Ffilipovski.net%2F2026%2F09%2F16%2Fbackups-arent-simple.html%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20afilipovski%0A%0AThe%20article%20delves%20into%20the%20intricacies%20of%20data%20backups%2C%20using%20personal%20stories%20and%20technical%20solutions%20to%20highlight%20their%20importance.%20It%20has%20generated%20significant%20community%20engagement%20with%20143%20comments%20sharing%20experiences%20and%20insights.%20Data%20backups%20are%20a%20critical%20component%20of%20data%20management%2C%20essential%20for%20preventing%20data%20loss.%20Understanding%20their%20complexities%20can%20help%20individuals%20and%20organizations%20better%20protect%20their%20data%20assets.%20The%20article%20discusses%20various%20backup%20strategies%2C%20including%20the%20use%20of%20ZFS%20snapshots%20and%20offsite%20syncs%2C%20and%20emphasizes%20the%20importance%20of%20distinguishing%20between%20ephemeral%20and%20persistent%20data.%20It%20also%20highlights%20the%20shift%20from%20merely%20backing%20up%20data%20to%20focusing%20on%20data%20restoration.%0A%0A%23%23%20Background%0AData%20backup%20is%20a%20process%20of%20copying%20and%20archiving%20computer%20data%20to%20ensure%20it%20can%20be%20restored%20in%20case%20of%20data%20loss.%20Common%20backup%20strategies%20include%20full%2C%20incremental%2C%20and%20differential%20backups.%20The%203-2-1%20backup%20rule%20is%20a%20widely%20recommended%20practice%2C%20suggesting%20three%20copies%20of%20data%2C%20on%20two%20different%20media%2C%20with%20one%20copy%20offsite.%0A%0A%23%23%20Discussion%0ACommunity%20members%20shared%20personal%20anecdotes%20of%20data%20loss%2C%20emphasizing%20the%20importance%20of%20reliable%20backup%20solutions.%20Some%20highlighted%20the%20transition%20from%20backup%20to%20restoration%20as%20a%20key%20focus%2C%20while%20others%20discussed%20technical%20preferences%20like%20ZFS%20snapshots.%0A">💾 Save to Obsidian</a>

---

<a id="item-8"></a>
## [HarnessTax: Evaluating the Impact of Coding Harnesses on AI Models](https://harnesstax.github.io/) ⭐️ 7.0/10

The article 'HarnessTax' investigates the role of coding harnesses in AI models, focusing on their importance for tool compatibility and efficiency. It highlights the need for better benchmarks to evaluate these harnesses. Understanding the significance of coding harnesses is crucial for optimizing AI model performance and ensuring compatibility with various tools. This can lead to more efficient AI development and deployment processes. Coding harnesses serve as the scaffolding around AI models, enabling them to function effectively as agents by integrating tools, memory, and feedback loops. The article suggests that while harnesses are critical, differences between them may be overstated.

hackernews · matt_d · Sep 16, 22:10 · [Discussion](https://news.ycombinator.com/item?id=49733726)

**Background**: A coding harness in AI refers to the software infrastructure that surrounds a language model, allowing it to operate as an agent. This includes tools, memory, sandboxes, and feedback loops. The compatibility of these harnesses with various AI tools is essential for maximizing the efficiency and effectiveness of AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights a need for better benchmarks for coding harnesses, with users noting the importance of using tools that models were fine-tuned on. Some users argue that while harnesses are important, their differences are often exaggerated.

**Tags**: `#AI`, `#Machine Learning`, `#Coding`, `#Tools`, `#Benchmarking`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fharnesstax-how-much-does-the-harness-matter-for-coding-agents-7e847601&content=---%0Atitle%3A%20%22HarnessTax%3A%20How%20Much%20Does%20the%20Harness%20Matter%20for%20Coding%20Agents%3F%22%0Aurl%3A%20https%3A%2F%2Fharnesstax.github.io%2F%0Asource%3A%20%22hackernews%20%C2%B7%20matt_d%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22AI%22%2C%20%22Machine%20Learning%22%2C%20%22Coding%22%2C%20%22Tools%22%2C%20%22Benchmarking%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BHarnessTax%3A%20How%20Much%20Does%20the%20Harness%20Matter%20for%20Coding%20Agents%3F%5D%28https%3A%2F%2Fharnesstax.github.io%2F%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20hackernews%20%C2%B7%20matt_d%0A%0AThe%20article%20%27HarnessTax%27%20investigates%20the%20role%20of%20coding%20harnesses%20in%20AI%20models%2C%20focusing%20on%20their%20importance%20for%20tool%20compatibility%20and%20efficiency.%20It%20highlights%20the%20need%20for%20better%20benchmarks%20to%20evaluate%20these%20harnesses.%20Understanding%20the%20significance%20of%20coding%20harnesses%20is%20crucial%20for%20optimizing%20AI%20model%20performance%20and%20ensuring%20compatibility%20with%20various%20tools.%20This%20can%20lead%20to%20more%20efficient%20AI%20development%20and%20deployment%20processes.%20Coding%20harnesses%20serve%20as%20the%20scaffolding%20around%20AI%20models%2C%20enabling%20them%20to%20function%20effectively%20as%20agents%20by%20integrating%20tools%2C%20memory%2C%20and%20feedback%20loops.%20The%20article%20suggests%20that%20while%20harnesses%20are%20critical%2C%20differences%20between%20them%20may%20be%20overstated.%0A%0A%23%23%20Background%0AA%20coding%20harness%20in%20AI%20refers%20to%20the%20software%20infrastructure%20that%20surrounds%20a%20language%20model%2C%20allowing%20it%20to%20operate%20as%20an%20agent.%20This%20includes%20tools%2C%20memory%2C%20sandboxes%2C%20and%20feedback%20loops.%20The%20compatibility%20of%20these%20harnesses%20with%20various%20AI%20tools%20is%20essential%20for%20maximizing%20the%20efficiency%20and%20effectiveness%20of%20AI%20models.%0A%0A%23%23%20Discussion%0AThe%20community%20discussion%20highlights%20a%20need%20for%20better%20benchmarks%20for%20coding%20harnesses%2C%20with%20users%20noting%20the%20importance%20of%20using%20tools%20that%20models%20were%20fine-tuned%20on.%20Some%20users%20argue%20that%20while%20harnesses%20are%20important%2C%20their%20differences%20are%20often%20exaggerated.%0A">💾 Save to Obsidian</a>

---

<a id="item-9"></a>
## [Mustafa Suleyman on AI Model Rights and Ethics](https://simonwillison.net/2026/Sep/16/mustafa-suleyman/) ⭐️ 7.0/10

Mustafa Suleyman argues against attributing human-like rights or feelings to AI models. He emphasizes the challenges this poses to AI alignment and containment. This perspective is significant as it challenges the emerging discourse on 'model welfare' in AI ethics. It highlights potential complications in ensuring AI systems align with human values and remain controllable. Suleyman argues that consciousness is the basis of ethical and legal systems, and extending these rights to AI is unjustified. This could complicate efforts to align AI with human intentions and control its behavior.

rss · Simon Willison · Sep 16, 16:00

**Background**: AI alignment is a subfield of AI safety focused on ensuring AI systems pursue goals consistent with human values. AI containment involves strategies to monitor and control AI behavior. The concept of 'model welfare' explores whether AI systems might have morally relevant experiences, a topic that intersects with AI alignment and ethics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://www.osohq.com/learn/ai-agent-containment-authorization">What is AI Agent Containment? - Oso Security</a></li>
<li><a href="https://aiwiki.ai/wiki/model_welfare">Model welfare | AI Wiki</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#generative-ai`, `#ai`, `#llms`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fquoting-mustafa-suleyman-35cfdc3f&content=---%0Atitle%3A%20%22Quoting%20Mustafa%20Suleyman%22%0Aurl%3A%20https%3A%2F%2Fsimonwillison.net%2F2026%2FSep%2F16%2Fmustafa-suleyman%2F%0Asource%3A%20%22rss%20%C2%B7%20Simon%20Willison%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22ai-ethics%22%2C%20%22generative-ai%22%2C%20%22ai%22%2C%20%22llms%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BQuoting%20Mustafa%20Suleyman%5D%28https%3A%2F%2Fsimonwillison.net%2F2026%2FSep%2F16%2Fmustafa-suleyman%2F%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20rss%20%C2%B7%20Simon%20Willison%0A%0AMustafa%20Suleyman%20argues%20against%20attributing%20human-like%20rights%20or%20feelings%20to%20AI%20models.%20He%20emphasizes%20the%20challenges%20this%20poses%20to%20AI%20alignment%20and%20containment.%20This%20perspective%20is%20significant%20as%20it%20challenges%20the%20emerging%20discourse%20on%20%27model%20welfare%27%20in%20AI%20ethics.%20It%20highlights%20potential%20complications%20in%20ensuring%20AI%20systems%20align%20with%20human%20values%20and%20remain%20controllable.%20Suleyman%20argues%20that%20consciousness%20is%20the%20basis%20of%20ethical%20and%20legal%20systems%2C%20and%20extending%20these%20rights%20to%20AI%20is%20unjustified.%20This%20could%20complicate%20efforts%20to%20align%20AI%20with%20human%20intentions%20and%20control%20its%20behavior.%0A%0A%23%23%20Background%0AAI%20alignment%20is%20a%20subfield%20of%20AI%20safety%20focused%20on%20ensuring%20AI%20systems%20pursue%20goals%20consistent%20with%20human%20values.%20AI%20containment%20involves%20strategies%20to%20monitor%20and%20control%20AI%20behavior.%20The%20concept%20of%20%27model%20welfare%27%20explores%20whether%20AI%20systems%20might%20have%20morally%20relevant%20experiences%2C%20a%20topic%20that%20intersects%20with%20AI%20alignment%20and%20ethics.%0A">💾 Save to Obsidian</a>

---

<a id="item-10"></a>
## [GoBench: Evaluating LLMs on 9x9 Go Games](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 7.0/10

GoBench introduces a novel framework to evaluate large language models (LLMs) using 9x9 Go games against KataGo opponents. The evaluation shows a strong correlation with the ARC-AGI 2 benchmark, with GPT-6 Astra max achieving 2500 Elo. This evaluation method is significant as it provides a unique approach to assessing the general reasoning abilities of LLMs, which are crucial for advancements in artificial general intelligence. It offers a new perspective on how these models perform in strategic games compared to specialized AI like KataGo. The GoBench framework evaluates LLMs on a 9x9 Go board, with results showing that GPT-6 Astra max achieves a lower Elo rating compared to KataGo. Codex with Astra, using coding tools and two hours of preparation, achieves a higher Elo of 3560.

reddit · r/MachineLearning · /u/Roland31415 · Sep 16, 18:54

**Background**: KataGo is a well-known open-source Go program that uses deep learning techniques to play Go, often outperforming human players. It employs self-play reinforcement learning, similar to AlphaZero, to improve its gameplay. ARC-AGI 2 is a benchmark designed to evaluate AI systems' abstract reasoning capabilities, aiming to measure progress towards artificial general intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo</a></li>
<li><a href="https://grokipedia.com/page/ARC-AGI-2">ARC-AGI-2</a></li>

</ul>
</details>

**Discussion**: The community discussion shows moderate engagement with some users expressing interest in the novel evaluation approach. However, there is a lack of extensive debate or diverse viewpoints on the implications of the findings.

**Tags**: `#Machine Learning`, `#AI Evaluation`, `#Go Game`, `#LLMs`

<a href="obsidian://new?vault=Obsidian&file=News%2FHorizon%2Fgobench-evaluating-llms-on-the-game-of-go-r-b536fa3c&content=---%0Atitle%3A%20%22GoBench%3A%20Evaluating%20LLMs%20on%20the%20game%20of%20Go%20%5BR%5D%22%0Aurl%3A%20https%3A%2F%2Fwww.reddit.com%2Fr%2FMachineLearning%2Fcomments%2F1wi68jg%2Fgobench_evaluating_llms_on_the_game_of_go_r%2F%0Asource%3A%20%22reddit%20%C2%B7%20r%2FMachineLearning%22%0Ascore%3A%207.0%0Atags%3A%20%5B%22Machine%20Learning%22%2C%20%22AI%20Evaluation%22%2C%20%22Go%20Game%22%2C%20%22LLMs%22%5D%0Asaved%3A%202026-09-17%0A---%0A%23%20%5BGoBench%3A%20Evaluating%20LLMs%20on%20the%20game%20of%20Go%20%28R%29%5D%28https%3A%2F%2Fwww.reddit.com%2Fr%2FMachineLearning%2Fcomments%2F1wi68jg%2Fgobench_evaluating_llms_on_the_game_of_go_r%2F%29%0A%E2%AD%90%EF%B8%8F%207.0%2F10%20%C2%B7%20reddit%20%C2%B7%20r%2FMachineLearning%0A%0AGoBench%20introduces%20a%20novel%20framework%20to%20evaluate%20large%20language%20models%20%28LLMs%29%20using%209x9%20Go%20games%20against%20KataGo%20opponents.%20The%20evaluation%20shows%20a%20strong%20correlation%20with%20the%20ARC-AGI%202%20benchmark%2C%20with%20GPT-6%20Astra%20max%20achieving%202500%20Elo.%20This%20evaluation%20method%20is%20significant%20as%20it%20provides%20a%20unique%20approach%20to%20assessing%20the%20general%20reasoning%20abilities%20of%20LLMs%2C%20which%20are%20crucial%20for%20advancements%20in%20artificial%20general%20intelligence.%20It%20offers%20a%20new%20perspective%20on%20how%20these%20models%20perform%20in%20strategic%20games%20compared%20to%20specialized%20AI%20like%20KataGo.%20The%20GoBench%20framework%20evaluates%20LLMs%20on%20a%209x9%20Go%20board%2C%20with%20results%20showing%20that%20GPT-6%20Astra%20max%20achieves%20a%20lower%20Elo%20rating%20compared%20to%20KataGo.%20Codex%20with%20Astra%2C%20using%20coding%20tools%20and%20two%20hours%20of%20preparation%2C%20achieves%20a%20higher%20Elo%20of%203560.%0A%0A%23%23%20Background%0AKataGo%20is%20a%20well-known%20open-source%20Go%20program%20that%20uses%20deep%20learning%20techniques%20to%20play%20Go%2C%20often%20outperforming%20human%20players.%20It%20employs%20self-play%20reinforcement%20learning%2C%20similar%20to%20AlphaZero%2C%20to%20improve%20its%20gameplay.%20ARC-AGI%202%20is%20a%20benchmark%20designed%20to%20evaluate%20AI%20systems%27%20abstract%20reasoning%20capabilities%2C%20aiming%20to%20measure%20progress%20towards%20artificial%20general%20intelligence.%0A%0A%23%23%20Discussion%0AThe%20community%20discussion%20shows%20moderate%20engagement%20with%20some%20users%20expressing%20interest%20in%20the%20novel%20evaluation%20approach.%20However%2C%20there%20is%20a%20lack%20of%20extensive%20debate%20or%20diverse%20viewpoints%20on%20the%20implications%20of%20the%20findings.%0A">💾 Save to Obsidian</a>

---