---
key: 视频生成/图生视频/Wan2.1视频换主体工作流_1960183828935553025.json
name: Wan2.1视频换主体工作流_1960183828935553025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1960183828935553025.json
hash: c600e7b35d3acf6e
coverage: 0.833333
learned_at: 2026-10-15 22:31:25
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoVAELoader, WanVideoVACEModelSelect, LayerUtility: ImageRemoveAlpha, FaceProcessorLoader, ImageResizeKJv2, WanVideoAddStandInLatent, AIO_Preprocessor, GetNode, GetNode, LayerUtility: PurgeVRAM V2, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, PreviewImage, ImageConcatMulti, ApplyFaceProcessor, SetNode, AudioSeparation, MultiTalkModelLoader, DownloadAndLoadWav2VecModel, easy cleanGpuUsed, MultiTalkWav2VecEmbeds, WanVideoEncode, JWInteger, WanVideoSampler, VHS_VideoInfo, ColorMatch, WanVideoDecode, SimpleMath+, ImageConcatMulti, GetImageSizeAndCount, easy showAnything, SimpleMath+, JWInteger, GetImageSizeAndCount, ImageResizeKJ, InspyrenetRembg, GetImageSizeAndCount, JWInteger, WanVideoVACEEncode, LayerUtility: ImageBlend, PrimitiveString, ImageFromBatch+, WanVideoTextEncode, WanVideoSLG, WanVideoEasyCache, JWIntegerToString, AudioCrop, PreviewAudio, Sam2Segmentation, LayerUtility: PurgeVRAM V2, DownloadAndLoadSAM2Model, Florence2toCoordinates, ShowText|pysssss, RH_Translator, DownloadAndLoadFlorence2Model, Florence2Run, GrowMaskWithBlur, ImageFromBatch, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, InpaintPreprocessor, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, GetImageSizeAndCount, easy showAnything, VHS_VideoCombine, RH_Captioner, RH_Captioner, Text Multiline, Text Concatenate, easy cleanGpuUsed, ImpactSwitch, ShowText|pysssss, ImpactSwitch, PrimitiveString, Fast Groups Bypasser (rgthree), Text Multiline, VHS_LoadVideo, Text Multiline, LoadImage, JWInteger, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1视频换主体工作流_1960183828935553025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1960183828935553025.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（90 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `LayerUtility: ImageRemoveAlpha`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `WanVideoAddStandInLatent`
- `AIO_Preprocessor`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `PreviewImage`
- `ImageConcatMulti`
- `ApplyFaceProcessor`
- `SetNode`
- `AudioSeparation`
- `MultiTalkModelLoader`
- `DownloadAndLoadWav2VecModel`
- `easy cleanGpuUsed`
- `MultiTalkWav2VecEmbeds`
- `WanVideoEncode`
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoInfo`
- `ColorMatch`
- `WanVideoDecode`
- `SimpleMath+`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `easy showAnything`
- `SimpleMath+`
- `JWInteger`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `InspyrenetRembg`
- `GetImageSizeAndCount`
- `JWInteger`
- `WanVideoVACEEncode`
- `LayerUtility: ImageBlend`
- `PrimitiveString`
- `ImageFromBatch+`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoEasyCache`
- `JWIntegerToString`
- `AudioCrop`
- `PreviewAudio`
- `Sam2Segmentation`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadSAM2Model`
- `Florence2toCoordinates`
- `ShowText|pysssss`
- `RH_Translator`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `GrowMaskWithBlur`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `InpaintPreprocessor`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `GetImageSizeAndCount`
- `easy showAnything`
- `VHS_VideoCombine`
- `RH_Captioner`
- `RH_Captioner`
- `Text Multiline`
- `Text Concatenate`
- `easy cleanGpuUsed`
- `ImpactSwitch`
- `ShowText|pysssss`
- `ImpactSwitch`
- `PrimitiveString`
- `Fast Groups Bypasser (rgthree)`
- `Text Multiline`
- `VHS_LoadVideo`
- `Text Multiline`
- `LoadImage`
- `JWInteger`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 知识

覆盖率 **83%**（75/90）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`LayerUtility: ImageRemoveAlpha`、`FaceProcessorLoader`、`ImageResizeKJv2`、`WanVideoAddStandInLatent`、`AIO_Preprocessor`、`LayerUtility: PurgeVRAM V2`、`InspyrenetRembg`、`ImageConcatMulti`、`ApplyFaceProcessor`、`AudioSeparation`、`MultiTalkModelLoader`、`DownloadAndLoadWav2VecModel`、`easy cleanGpuUsed`、`MultiTalkWav2VecEmbeds`、`WanVideoEncode`、`JWInteger`、`WanVideoSampler`、`VHS_VideoInfo`、`ColorMatch`、`WanVideoDecode`、`SimpleMath+`、`GetImageSizeAndCount`、`ImageResizeKJ`、`WanVideoVACEEncode`、`LayerUtility: ImageBlend`、`ImageFromBatch+`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoEasyCache`、`JWIntegerToString`、`AudioCrop`、`PreviewAudio`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`Florence2toCoordinates`、`RH_Translator`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`GrowMaskWithBlur`、`ImageFromBatch`、`VHS_VideoCombine`、`InpaintPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Captioner`、`Text Multiline`、`Text Concatenate`、`VHS_LoadVideo`、`LoadImage`、`RHHiddenNodes`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoAddStandInLatent
