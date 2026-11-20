---
name: text_to_image_controlnet_video_upscale
type: Text To Image
frequency: 2
level: weak
coverage: 0.691
common_nodes: [AnyLineArtPreprocessor_aux, BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DWPreprocessor, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageRangeFromBatch, GetNode, Grayscale Image (WLSH), Image Comparer (rgthree), ImageConcatMulti, ImageResize+, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, JjkText, JoinStringMulti, Joy_caption, Joy_caption_load, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, LongCLIPTextEncodeFlux, LoraLoaderModelOnly, PreviewImage, PrimitiveInt, RH_Captioner, RIFE VFI, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy anythingIndexSwitch, easy imageBatchToImageList, easy imageChooser, easy imageConcat, easy int]
problems: []
missing: []
members: [图片生成/图生图/VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338.json, 视频生成/图生视频/VACE Controlnet动作迁移（抽帧重绘，动作迁移版）_1923749059608104962.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_video_upscale

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/VACE+Controlnet动作迁移Causvid快速采样（抽帧重绘，动作迁移）V2_1925769917302542338.json、视频生成/图生视频/VACE Controlnet动作迁移（抽帧重绘，动作迁移版）_1923749059608104962.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DWPreprocessor`
- `DeepTranslatorTextNode`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageRangeFromBatch`
- `GetNode`
- `Grayscale Image (WLSH)`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `JjkText`
- `JoinStringMulti`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LongCLIPTextEncodeFlux`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveInt`
- `RH_Captioner`
- `RIFE VFI`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy imageBatchToImageList`
- `easy imageChooser`
- `easy imageConcat`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 864 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 864，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
