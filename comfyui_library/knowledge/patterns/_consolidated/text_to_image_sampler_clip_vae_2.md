---
name: text_to_image_sampler_clip_vae_2
type: Text To Image
frequency: 32
level: weak
coverage: 0.967219
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1650 4G 文生图_Z-image量化 低显存_2061641168311640065.json, 图片生成/文生图/2029960172382195714.json, 图片生成/文生图/2030697459789336578.json, 图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json, 图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json, 图片生成/文生图/87time # 30  通义千问 QW 中文生成_1938456564812414977.json, 图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json, 图片生成/文生图/A1、文生图千问2.5高保真 - 和风_1984067041122516994.json, 图片生成/文生图/Anima正式版-文生图工作流个人自用_2076592631471230977.json, 图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json, 图片生成/文生图/Qwen Image 文生图，千问基础文生图_2005132413141479426.json, 图片生成/文生图/Qwen image 2512 我的50年_Qwen-Image-2512_2006650484186157057.json, 图片生成/文生图/Qwen image 2512文生图_2008433887889858562.json, 图片生成/文生图/Qwen-Image+Lightning4StepsLora-文生图工作流_1956201968337342466.json, 图片生成/文生图/Qwen-Image-2512 文生图 8步加速_2014683752181538818.json, 图片生成/文生图/Qwen-Image-2512 最新文生图_2006383515574738946.json, 图片生成/文生图/Qwen-Image-2512不用LoRA实现人物一致性_2006694730360430594.json, 图片生成/文生图/Qwen-Image-2512卡通女孩LoRA_2007803177848020993.json, 图片生成/文生图/Qwen-Image-2512四步10秒出图Qwen image 2512_2006497445919854594.json, 图片生成/文生图/Qwen-Image-2512文生图_1953006122934407170.json, 图片生成/文生图/Qwen-Image-2512文生图_2006354179845005313.json, 图片生成/文生图/Qwen-Image-2512的Bill_LoRA_2007418345481576449.json, 图片生成/文生图/Qwen-Image2512中文渲染全系列工作流_2010150714567299074.json, 图片生成/文生图/Qwen2512JK制服甜妹_2018334963661283330.json, 图片生成/文生图/Qwen2512性感迷人身材美女_2017894712933359617.json, 图片生成/文生图/Qwen大雷连体衣美女_2055856373283467265.json, 图片生成/文生图/Z-image D-OPSD文生图_2056614357865418754.json, 图片生成/文生图/Z-image D-OPSD文生图_2056619453462441985.json, 图片生成/文生图/Z-image D-OPSD文生图_2057839881359020034.json, 图片生成/文生图/Z-image Qwen3 4B Vs Qwen3 4b Z-image Engineer V4_2027773457253011458.json, 图片生成/文生图/Z-image-turbo Vs flow-dpo对比_2026971124013207554.json, 图片生成/文生图/Z-image-turbo Vs flow-dpo对比工作流 林耀2.27_2027214097611231233.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（图片生成/文生图/1650 4G 文生图_Z-image量化 低显存_2061641168311640065.json、图片生成/文生图/2029960172382195714.json、图片生成/文生图/2030697459789336578.json、图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json、图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json…）

- **类型**：Text To Image
- **样本数**：32
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 32 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 31/32 个有
- `CLIPLoader` —— 30/32 个有
- `LoraLoaderModelOnly` —— 27/32 个有
- `ModelSamplingAuraFlow` —— 17/32 个有
- `easy seed` —— 8/32 个有
- `CR Prompt Text` —— 7/32 个有
- `ConditioningZeroOut` —— 6/32 个有
- `AddLabel` —— 3/32 个有
- `CLIPLoaderGGUF` —— 3/32 个有
- `ImageConcanate` —— 3/32 个有
- `PreviewImage` —— 3/32 个有
- `CompressImages` —— 2/32 个有
- `Label (rgthree)` —— 1/32 个有
- `UnetLoaderGGUF` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 304 - 1920 | 32 | 72% |
| 高度 | 1280 | 304 - 1920 | 32 | 71% |
| 采样步数 | 8 | 4 - 30 | 32 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 32 | 24% |
| 采样算法 | euler | - | 32 | 91% |
| 调度器 | simple | - | 32 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 32 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 304 - 1920，32 个样本
- 高度 中位数 1280，观测区间 304 - 1920，32 个样本
- 采样步数 中位数 8，观测区间 4 - 30，32 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，32 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，32 个样本，一致性 91%
- 调度器 最常用 simple，32 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，32 个样本，取值集中（一致性 100%）
- 高发问题（18/32 个样本）：Steps较低可能导致细节不足
