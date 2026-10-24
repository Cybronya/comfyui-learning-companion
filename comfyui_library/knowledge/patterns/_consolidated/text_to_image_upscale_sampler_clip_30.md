---
name: text_to_image_upscale_sampler_clip_30
type: Text To Image
frequency: 3
level: weak
coverage: 0.900333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, PrimitiveStringMultiline, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json, 图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json, 图片生成/文生图/人像 Krea2 + Z-Image_2080846052952993794.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json、图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json、图片生成/文生图/人像 Krea2 + Z-Image_2080846052952993794.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `easy loraStack` —— 2/3 个有
- `easy loraStackApply` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `HAIGC_SaveImagesToZip` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 3 | 65% |
| 高度 | 512 | 512 - 1536 | 3 | 43% |
| 采样步数 | 7.5 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler_ancestral | - | 3 | 33% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 33% |
| 重绘幅度 | 0.675 | - | 2 | 52% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，3 个样本
- 高度 中位数 512，观测区间 512 - 1536，3 个样本，取值分散，一致性仅 43%
- 采样步数 中位数 7.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 33%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 33%
- 重绘幅度 中位数 0.675，样本不足，未给区间，2 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
