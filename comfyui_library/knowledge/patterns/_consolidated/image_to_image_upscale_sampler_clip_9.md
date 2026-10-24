---
name: image_to_image_upscale_sampler_clip_9
type: Image To Image
frequency: 11
level: strong
coverage: 0.719182
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwen3 反推提示词图生图_2057288739076009986.json, 图片生成/图生图/Qwen3 反推提示词图生图_2057383692988936194.json, 图片生成/图生图/Z-IMAGE 超精致自动反推洗图+SeedVR2放大-人像效果顶级-数毛_2003367440472023042.json, 图片生成/图生图/Z-IMAGE-阿里轻量级真实感模型-反推-洗图-放大_1992083842836262913.json, 图片生成/图生图/Z-IMAGE：【洗图神器】网红写实美女模特 小红书各大平台_1994611852594323458.json, 图片生成/图生图/Z-IMAGE：小而美图像模型：自动反推洗图_1995700193033064450.json, 图片生成/图生图/Z-IMAGE：精准反推洗图+高清放大_1999818943474921474.json, 图片生成/图生图/Z-IMAGE：自动反推洗图【去ai感图生图】_1994210335209046017.json, 图片生成/图生图/qwen3反推提示词图生图_洗稿_2064920476073414658.json, 图片生成/图生图/自用，z-image3D动漫风放大4K_2008088317811761154.json, 图片生成/文生图/qwen3反推提示词并生图_2056909255499935745.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen3 反推提示词图生图_2057288739076009986.json、图片生成/图生图/Qwen3 反推提示词图生图_2057383692988936194.json、图片生成/图生图/Z-IMAGE 超精致自动反推洗图+SeedVR2放大-人像效果顶级-数毛_2003367440472023042.json、图片生成/图生图/Z-IMAGE-阿里轻量级真实感模型-反推-洗图-放大_1992083842836262913.json、图片生成/图生图/Z-IMAGE：【洗图神器】网红写实美女模特 小红书各大平台_1994611852594323458.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 10/11 个有
- `ImpactInt` —— 10/11 个有
- `JoinStrings` —— 10/11 个有
- `ImageScaleBy` —— 7/11 个有
- `LayerUtility: ImageReel` —— 7/11 个有
- `LayerUtility: ImageReelComposit` —— 7/11 个有
- `ShowText|pysssss` —— 7/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `Float` —— 4/11 个有
- `MemoryCleaner` —— 4/11 个有
- `easy saveText` —— 4/11 个有
- `孤海注释` —— 4/11 个有
- `ImageListToImageBatch` —— 2/11 个有
- `ImageScaleDownToSize` —— 2/11 个有
- `ImageUpscaleWithModel` —— 2/11 个有
- `MuyeTextEditOutput` —— 2/11 个有
- `TTP_Image_Assy` —— 2/11 个有
- `TTP_Image_Tile_Batch` —— 2/11 个有
- `TTP_Tile_image_size` —— 2/11 个有
- `UpscaleModelLoader` —— 2/11 个有
- `easy imageBatchToImageList` —— 2/11 个有
- `Anything Everywhere` —— 1/11 个有
- `CombinationText` —— 1/11 个有
- `DuckHideNode` —— 1/11 个有
- `Int` —— 1/11 个有
- `LoraLoaderModelOnly_Any` —— 1/11 个有
- `ModelSamplingAuraFlow` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.9 - 1 | 11 | 95% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 0.6 | 0.25 - 0.6 | 11 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.9 - 1，11 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.25 - 0.6，11 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
