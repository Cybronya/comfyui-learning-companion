---
name: text_to_image_upscale_sampler_clip_29
type: Text To Image
frequency: 3
level: strong
coverage: 0.711
common_nodes: [AILab_QwenVL, Anything Everywhere, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageLoader, ImageScaleToTotalPixels, Int, KSampler, LayerUtility: PurgeVRAM V2, MaraScottIsEmptyOrNone_v1, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/qwen3VL反推ZImage生图SeedVR25高清修复电影场景写实肖像动漫角色_2063539361647513602.json, 图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json, 图片生成/文生图/文生图，自动洗图，qwen3VL+Z-Image+SeedVR_2012875973548580865.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen3VL反推ZImage生图SeedVR25高清修复电影场景写实肖像动漫角色_2063539361647513602.json、图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json、图片生成/文生图/文生图，自动洗图，qwen3VL+Z-Image+SeedVR_2012875973548580865.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `MaraScottIsEmptyOrNone_v1`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenImageLatentAspectRatio` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 544 | 544 - 544 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 544，观测区间 544 - 544，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
