---
name: image_to_image_upscale_sampler_unet_4
type: Image To Image
frequency: 2
level: weak
coverage: 0.7685
common_nodes: [CLIPLoader, Fast Groups Bypasser (rgthree), GetImageSize+, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/seedVR2超分洗图_2094082560245714945.json, 图片生成/图生图/全自动Krea无反推高一致性洗图（二创专用）_2077396646765350913.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/seedVR2超分洗图_2094082560245714945.json、图片生成/图生图/全自动Krea无反推高一致性洗图（二创专用）_2077396646765350913.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
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

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `KOOK_ImageCompression` —— 1/2 个有
- `Krea2ControlApply` —— 1/2 个有
- `Krea2ControlImageEncode` —— 1/2 个有
- `Krea2ControlLoRALoader` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeKrea2OstrisEdit` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 40% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.55 | - | 2 | 18% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.55，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
