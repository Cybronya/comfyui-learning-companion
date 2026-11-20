---
name: image_to_image_lora_sampler_clip_70
type: Image To Image
frequency: 4
level: strong
coverage: 0.80525
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/QY7-千像归一（kontext）双图版 自动抠图一键融合打光，溶图kontext_1967598647435288578.json, 图片生成/图生图/kontext万物迁移（产品替换+光影融合）_1948345697857863681.json, 图片生成/图生图/kontext产品溶图_1966031556299100161.json, 图片生成/图生图/🐲电商产品完美溶图【透视矫正 光影融合】🐲_2001553801477779457.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QY7-千像归一（kontext）双图版 自动抠图一键融合打光，溶图kontext_1967598647435288578.json、图片生成/图生图/kontext万物迁移（产品替换+光影融合）_1948345697857863681.json、图片生成/图生图/kontext产品溶图_1966031556299100161.json、图片生成/图生图/🐲电商产品完美溶图【透视矫正 光影融合】🐲_2001553801477779457.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DetailTransfer` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `LayerMask: BiRefNetUltraV2` —— 2/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `ChinesePrompt_Mix` —— 1/4 个有
- `Fast Bypasser (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `LayerUtility: FluxKontextImageScale` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | deis | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
