---
name: text_to_image_upscale_sampler_clip_31
type: Text To Image
frequency: 2
level: weak
coverage: 0.7285
common_nodes: [AILab_QwenVL, Anything Everywhere, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageLoader, ImageScaleToTotalPixels, Int, KSampler, LayerUtility: PurgeVRAM V2, MaraScottIsEmptyOrNone_v1, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json, 图片生成/文生图/文生图，自动洗图，qwen3VL+Z-Image+SeedVR_2012875973548580865.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/qwen3VL反推+Z-Image生图+SeedVR2.5高清修复，电影场景_写实肖像_动漫角色_1995712593509617666.json、图片生成/文生图/文生图，自动洗图，qwen3VL+Z-Image+SeedVR_2012875973548580865.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `QwenImageLatentAspectRatio` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 544 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 544，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
