---
key: 视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json
name: Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957443614760693762.json
hash: 71aa3a98d3d1584c
coverage: 0.86747
learned_at: 2026-10-15 22:31:16
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTextEncode, LayerUtility: ImageRemoveAlpha, FaceProcessorLoader, ImageResizeKJv2, WanVideoAddStandInLatent, AIO_Preprocessor, GetNode, GetNode, GetNode, InpaintPreprocessor, LayerUtility: PurgeVRAM V2, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, PreviewImage, ImageConcatMulti, ApplyFaceProcessor, WanVideoLoraSelect, SetNode, VHS_VideoCombine, MaskPreview+, AudioSeparation, JWIntegerToString, MultiTalkModelLoader, DownloadAndLoadWav2VecModel, easy cleanGpuUsed, MultiTalkWav2VecEmbeds, WanVideoEncode, PreviewImage, JWInteger, WanVideoSampler, VHS_VideoInfo, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, GrowMaskWithBlur, ColorMatch, WanVideoModelLoader, WanVideoSLG, LayerUtility: PurgeVRAM V2, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, ImageFromBatch+, AudioCrop, ImageConcatMulti, SimpleMath+, JWInteger, UpscaleModelLoader, GetImageSizeAndCount, easy showAnything, WanVideoVACEEncode, PreviewAudio, WanVideoEasyCache, LayerUtility: ImageBlend, ImageResizeKJ, InspyrenetRembg, GetImageSizeAndCount, JWInteger, WanVideoLoraSelect, WanVideoVACEModelSelect, SetNode, SetNode, WanVideoVAELoader, LayerUtility: PurgeVRAM V2, ImageFromBatch, GetImageSizeAndCount, easy showAnything, ImageUpscaleWithModel, Text Multiline, RHHiddenNodes, RHHiddenNodes, VHS_LoadVideo, JWInteger, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, Text Multiline, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+Stand-In一致性人物主体替换工作流-v1_1957443614760693762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957443614760693762.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（83 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `LayerUtility: ImageRemoveAlpha`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `WanVideoAddStandInLatent`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `InpaintPreprocessor`
- `LayerUtility: PurgeVRAM V2`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `ImageConcatMulti`
- `ApplyFaceProcessor`
- `WanVideoLoraSelect`
- `SetNode`
- `VHS_VideoCombine`
- `MaskPreview+`
- `AudioSeparation`
- `JWIntegerToString`
- `MultiTalkModelLoader`
- `DownloadAndLoadWav2VecModel`
- `easy cleanGpuUsed`
- `MultiTalkWav2VecEmbeds`
- `WanVideoEncode`
- `PreviewImage`
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoInfo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `GrowMaskWithBlur`
- `ColorMatch`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `ImageFromBatch+`
- `AudioCrop`
- `ImageConcatMulti`
- `SimpleMath+`
- `JWInteger`
- `UpscaleModelLoader`
- `GetImageSizeAndCount`
- `easy showAnything`
- `WanVideoVACEEncode`
- `PreviewAudio`
- `WanVideoEasyCache`
- `LayerUtility: ImageBlend`
- `ImageResizeKJ`
- `InspyrenetRembg`
- `GetImageSizeAndCount`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM V2`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `easy showAnything`
- `ImageUpscaleWithModel`
- `Text Multiline`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **87%**（72/83）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`LayerUtility: ImageRemoveAlpha`、`FaceProcessorLoader`、`ImageResizeKJv2`、`WanVideoAddStandInLatent`、`AIO_Preprocessor`、`InpaintPreprocessor`、`LayerUtility: PurgeVRAM V2`、`InspyrenetRembg`、`ImageConcatMulti`、`ApplyFaceProcessor`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`MaskPreview+`、`AudioSeparation`、`JWIntegerToString`、`MultiTalkModelLoader`、`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`MultiTalkWav2VecEmbeds`、`WanVideoEncode`、`JWInteger`、`WanVideoSampler`、`VHS_VideoInfo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJ`、`GrowMaskWithBlur`、`ColorMatch`、`WanVideoModelLoader`、`WanVideoSLG`、`WanVideoDecode`、`SimpleMath+`、`ImageFromBatch+`、`AudioCrop`、`UpscaleModelLoader`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`PreviewAudio`、`WanVideoEasyCache`、`LayerUtility: ImageBlend`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`ImageFromBatch`、`ImageUpscaleWithModel`、`Text Multiline`、`RHHiddenNodes`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
