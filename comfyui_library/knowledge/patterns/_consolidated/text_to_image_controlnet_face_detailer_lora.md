---
name: text_to_image_controlnet_face_detailer_lora
type: Text To Image
frequency: 2
level: weak
coverage: 0.7945
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DF_Image_scale_to_side, DepthAnythingV2Preprocessor, EmptyLatentImage, FaceDetailer, Image Comparer (rgthree), ImageScale, InjectLatentNoise+, KSampler, LatentInterpolate, LayerColor: Brightness & Contrast, LoadImage, ModelSamplingDiscrete, PerturbedAttentionGuidance, Power Lora Loader (rgthree), PreviewImage, RH_Captioner, SAMLoader, SaveImage, Seed Generator, ShowText|pysssss, String Literal, TTPlanet_Tile_Preprocessor_Simple, Text Concatenate, UltralyticsDetectorProvider, VAEDecode, VAEEncode, image_resize(rh)]
problems: []
missing: []
members: [图片生成/图生图/啊癫 真实感人像 写实人像 图生图基础版v3_1971577739859980290.json, 图片生成/图生图/啊癫 真实感图生图基础版v2_1951665194818850817.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_face_detailer_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/啊癫 真实感人像 写实人像 图生图基础版v3_1971577739859980290.json、图片生成/图生图/啊癫 真实感图生图基础版v2_1951665194818850817.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DF_Image_scale_to_side`
- `DepthAnythingV2Preprocessor`
- `EmptyLatentImage`
- `FaceDetailer`
- `Image Comparer (rgthree)`
- `ImageScale`
- `InjectLatentNoise+`
- `KSampler`
- `LatentInterpolate`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `ModelSamplingDiscrete`
- `PerturbedAttentionGuidance`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `RH_Captioner`
- `SAMLoader`
- `SaveImage`
- `Seed Generator`
- `ShowText|pysssss`
- `String Literal`
- `TTPlanet_Tile_Preprocessor_Simple`
- `Text Concatenate`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `image_resize(rh)`

**可变部分**（部分 workflow 才有）：
- `LayerFilter: ChannelShake` —— 1/2 个有
- `LayerFilter: FilmV2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `TTP_Tile_image_size` —— 1/2 个有
- `easy imageBatchToImageList` —— 1/2 个有
- `easy imageListToImageBatch` —— 1/2 个有
- `easy imageSize` —— 1/2 个有
- `easy imageSizeBySide` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 60 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | ddpm | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 宽度 | 1192 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 60，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddpm，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1192，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
