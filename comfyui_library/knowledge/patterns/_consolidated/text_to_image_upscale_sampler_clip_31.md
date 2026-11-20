---
name: text_to_image_upscale_sampler_clip_31
type: Text To Image
frequency: 4
level: weak
coverage: 0.88175
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, PrimitiveStringMultiline, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json, 图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json, 图片生成/文生图/krea2+moss极致双采（注释内有模型和节点下载链接）_2115332254028353537.json, 图片生成/文生图/人像 Krea2 + Z-Image_2080846052952993794.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json、图片生成/文生图/VividMuse 红潮 ERNIE RedMIX_2048760839439650817.json、图片生成/文生图/krea2+moss极致双采（注释内有模型和节点下载链接）_2115332254028353537.json、图片生成/文生图/人像 Krea2 + Z-Image_2080846052952993794.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
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

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `easy loraStack` —— 2/4 个有
- `easy loraStackApply` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 4 | 67% |
| 高度 | 768 | 512 - 1536 | 4 | 53% |
| 采样步数 | 10 | 5 - 25 | 3 | 36% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 8 | 4 | 8% |
| 采样算法 | euler_ancestral | - | 4 | 25% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.36 | 0.35 - 1 | 3 | 47% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，4 个样本
- 高度 中位数 768，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 10，观测区间 5 - 25，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 8，4 个样本，取值分散，一致性仅 8%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 25%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.36，观测区间 0.35 - 1，3 个样本，取值分散，一致性仅 47%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
