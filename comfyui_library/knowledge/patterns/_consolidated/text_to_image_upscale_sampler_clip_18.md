---
name: text_to_image_upscale_sampler_clip_18
type: Text To Image
frequency: 6
level: strong
coverage: 0.774167
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image洗图+高清放大+自动反推_2086916546852638722.json, 图片生成/图生图/【4K 高清】Z-Image 文生图_1995501883357847553.json, 图片生成/图生图/反推Z-image生图放大滤镜_2062044431448104961.json, 图片生成/图生图/庭院景观建筑洗图重绘_2068756404294471681.json, 图片生成/图生图/洗图Z-image洗图+_高清放大带自动反推_2076208081142374402.json, 图片生成/图生图/洗图（Z-image洗图）+ 高清放大（带自动反推）_2026840484630503425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image洗图+高清放大+自动反推_2086916546852638722.json、图片生成/图生图/【4K 高清】Z-Image 文生图_1995501883357847553.json、图片生成/图生图/反推Z-image生图放大滤镜_2062044431448104961.json、图片生成/图生图/庭院景观建筑洗图重绘_2068756404294471681.json、图片生成/图生图/洗图Z-image洗图+_高清放大带自动反推_2076208081142374402.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 5/6 个有
- `CR Text` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Float` —— 5/6 个有
- `ImpactInt` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `FL_ImageAddNoise` —— 1/6 个有
- `KimFilter` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 6 | 100% |
| 高度 | 1920 | 1920 - 1920 | 6 | 100% |
| LoRA 模型强度 | 0.95 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
