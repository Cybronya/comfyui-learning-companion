---
name: text_to_image_controlnet_upscale_latent_upscale_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.6735
common_nodes: [AIO_Preprocessor, Anything Everywhere3, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetNode, ImageBatchToList+, ImageScaleToTotalPixels, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSampler, LatentUpscaleBy, LayerFilter: FilmV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, OpenposePreprocessor, PreviewImage, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, String, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【姿势控制】-强控制-FLUX版_1895850863892561922.json, 图片生成/文生图/union姿势控制-FLUX版【可文生图_反推生图】_1931638520623116289.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【姿势控制】-强控制-FLUX版_1895850863892561922.json、图片生成/文生图/union姿势控制-FLUX版【可文生图_反推生图】_1931638520623116289.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetNode`
- `ImageBatchToList+`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LatentUpscaleBy`
- `LayerFilter: FilmV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `String`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `Load Image Batch` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.8 | - | 2 | 75% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.9 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
