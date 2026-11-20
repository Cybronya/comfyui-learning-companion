---
name: unknown_workflow_lora_sampler_unet_55
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9094
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Anything2Real 2601：动漫转真人_2009908341815906305.json, 图片生成/图生图/Qwen 2511一键换装，复杂场景超高一致性_2055129671032942594.json, 图片生成/图生图/Qwen 2511零偏移换装流_2060847633358479361.json, 图片生成/图生图/Qwen Image Edit 2511 Anime：真人转动漫_2009866929703489537.json, 图片生成/图生图/Qwen Image-Eidt 2511零偏移换装流_2029356578679300098.json, 图片生成/图生图/Qwen-Image-Edit-2511-Anime：真人转动漫_2012495893307592705.json, 图片生成/图生图/Qwen2511- Anime-真人转动漫-写实转二次元_2046231083565457410.json, 图片生成/图生图/Qwen2511-Anything2Real 2601：动漫转真人-二次元转真人_2046228567264071681.json, 图片生成/图生图/Qwenedit2511（强化编辑效果一致性）_2011527482813452289.json, 图片生成/图生图/【三种对比】QwenEdit2511任意风格转写实_2010304815355666433.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_55

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Anything2Real 2601：动漫转真人_2009908341815906305.json、图片生成/图生图/Qwen 2511一键换装，复杂场景超高一致性_2055129671032942594.json、图片生成/图生图/Qwen 2511零偏移换装流_2060847633358479361.json、图片生成/图生图/Qwen Image Edit 2511 Anime：真人转动漫_2009866929703489537.json、图片生成/图生图/Qwen Image-Eidt 2511零偏移换装流_2029356578679300098.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/10 个有
- `Seed Everywhere` —— 5/10 个有
- `VAEDecode` —— 5/10 个有
- `VAEDecodeTiled` —— 5/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `CFGNorm` —— 3/10 个有
- `CustomAddLabel` —— 3/10 个有
- `Label (rgthree)` —— 3/10 个有
- `LayerUtility: ImageReel` —— 3/10 个有
- `LayerUtility: ImageReelComposit` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `ImageResize+` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `GetImageSize` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `QwenEditAdaptiveLongestEdge` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta57 | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 5/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta57，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（15/10 个样本）：Steps较低可能导致细节不足
- 高发问题（5/10 个样本）：发现KSampler但没有VAEDecode
