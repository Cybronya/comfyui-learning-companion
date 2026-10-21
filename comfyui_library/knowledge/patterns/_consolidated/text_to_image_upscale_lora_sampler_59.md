---
name: text_to_image_upscale_lora_sampler_59
type: Text To Image
frequency: 2
level: weak
coverage: 0.931
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, PrimitiveStringMultiline, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy loraStack, easy loraStackApply, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json, 图片生成/文生图/人像 Krea2 + Z-Image_2080846052952993794.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json、图片生成/文生图/人像 Krea2 + Z-Image_2080846052952993794.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
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
- `KSamplerAdvanced`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
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
- `VAEEncode`
- `VAELoader`
- `easy loraStack`
- `easy loraStackApply`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SaveImagesToZip` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 5 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 0.35 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
