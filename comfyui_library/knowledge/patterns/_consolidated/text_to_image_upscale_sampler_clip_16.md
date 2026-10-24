---
name: text_to_image_upscale_sampler_clip_16
type: Text To Image
frequency: 7
level: strong
coverage: 0.768286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json, 图片生成/图生图/Z-image洗图+高清放大+自动反推_2086916546852638722.json, 图片生成/图生图/反推Z-image生图放大滤镜_2062044431448104961.json, 图片生成/图生图/庭院景观建筑洗图重绘_2068756404294471681.json, 图片生成/图生图/洗图Z-image洗图+_高清放大带自动反推_2076208081142374402.json, 图片生成/图生图/洗图（Z-image洗图）+ 高清放大（带自动反推）_2026840484630503425.json, 图片生成/文生图/Z-tmage高清文生图_2031773633609211906.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-image  美女模特时尚人物穿搭 日常穿搭 电影级美学 网红洗图 批量生成 SeedVR2.5_2030806592970559490.json、图片生成/图生图/Z-image洗图+高清放大+自动反推_2086916546852638722.json、图片生成/图生图/反推Z-image生图放大滤镜_2062044431448104961.json、图片生成/图生图/庭院景观建筑洗图重绘_2068756404294471681.json、图片生成/图生图/洗图Z-image洗图+_高清放大带自动反推_2076208081142374402.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `AILab_QwenVL` —— 5/7 个有
- `Float` —— 5/7 个有
- `ImageScaleBy` —— 5/7 个有
- `LoraLoader` —— 2/7 个有
- `Qwen3_VQA` —— 2/7 个有
- `FL_ImageAddNoise` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `KimFilter` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy textSwitch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 7 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 720 - 1080 | 7 | 88% |
| 高度 | 1920 | 1280 - 1920 | 7 | 88% |
| LoRA 模型强度 | 0.925 | - | 2 | 97% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，7 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1080，7 个样本，取值集中（一致性 88%）
- 高度 中位数 1920，观测区间 1280 - 1920，7 个样本，取值集中（一致性 88%）
- LoRA 模型强度 中位数 0.925，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
