---
key: 视频生成/图生视频/Wan2.1FUNControlnetOTT20250416A横版_1912373863278411778.json
name: Wan2.1FUNControlnetOTT20250416A横版_1912373863278411778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1FUNControlnetOTT20250416A横版_1912373863278411778.json
hash: 9c21cc0d4fedcbbf
coverage: 0.782051
learned_at: 2026-10-15 22:29:32
nodes: [GetNode, LayerUtility: PurgeVRAM, Reroute, WanVideoVAELoader, LTXVPromptEnhancerLoader, GetNode, Reroute, WanVideoTextEncode, LTXVPromptEnhancer, WanVideoTorchCompileSettings, easy clearCacheAll, LoadWanVideoClipTextEncoder, Note, ImageResizeKJ, WanVideoClipVisionEncode, WanVideoDecode, WanVideoExperimentalArgs, Note, LayerUtility: PurgeVRAM, RH_Captioner, LayerUtility: PurgeVRAM, WanVideoTeaCache, WanVideoLoraSelect, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoEncode, GetNode, MarkdownNote, DownloadAndLoadGIMMVFIModel, UpscaleModelLoader, ImageScaleBy, GIMMVFI_interpolate, ImageUpscaleWithModel, JjkShowText, WanVideoSampler, DWPreprocessor, LoadWanVideoT5TextEncoder, easy clearCacheAll, VHS_VideoCombine, LayerUtility: PurgeVRAM, WanVideoModelLoader, Note, Note, Note, GetImageSizeAndCount, Fast Groups Bypasser (rgthree), LoadImage, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJ, ImpactSwitch, Text Multiline, Note, ImageUpscaleWithModel, UpscaleModelLoader, ImageResizeKJ, RIFE VFI, VHS_VideoCombine, ImageConcatMulti, Text Concatenate, SetNode, GetImageRangeFromBatch, VHS_VideoCombine, WanVideoControlEmbeds, SetNode, WanVideoEmptyEmbeds, ImageBlend, AIO_Preprocessor, AIO_Preprocessor, WanVideoImageToVideoEncode, WanVideoBlockSwap, LoadImage, VHS_LoadVideo, AIO_Preprocessor, DWPreprocessor, MeshGraphormer-DepthMapPreprocessor, Text Multiline, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1FUNControlnetOTT20250416A横版_1912373863278411778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912373863278411778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（78 个）：
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `WanVideoVAELoader`
- `LTXVPromptEnhancerLoader`
- `GetNode`
- `Reroute`
- `WanVideoTextEncode`
- `LTXVPromptEnhancer`
- `WanVideoTorchCompileSettings`
- `easy clearCacheAll`
- `LoadWanVideoClipTextEncoder` ★核心
- `Note`
- `ImageResizeKJ`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `Note`
- `LayerUtility: PurgeVRAM`
- `RH_Captioner`
- `LayerUtility: PurgeVRAM`
- `WanVideoTeaCache`
- `WanVideoLoraSelect`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoEncode`
- `GetNode`
- `MarkdownNote`
- `DownloadAndLoadGIMMVFIModel`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `GIMMVFI_interpolate`
- `ImageUpscaleWithModel`
- `JjkShowText`
- `WanVideoSampler` ★核心
- `DWPreprocessor`
- `LoadWanVideoT5TextEncoder`
- `easy clearCacheAll`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `WanVideoModelLoader`
- `Note`
- `Note`
- `Note`
- `GetImageSizeAndCount`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `ImpactSwitch`
- `Text Multiline`
- `Note`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageResizeKJ`
- `RIFE VFI`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `Text Concatenate`
- `SetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `WanVideoControlEmbeds`
- `SetNode`
- `WanVideoEmptyEmbeds`
- `ImageBlend`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `LoadImage`
- `VHS_LoadVideo`
- `AIO_Preprocessor`
- `DWPreprocessor`
- `MeshGraphormer-DepthMapPreprocessor`
- `Text Multiline`
- `GetNode`

## 知识

覆盖率 **78%**（61/78）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`LTXVPromptEnhancerLoader`、`WanVideoTextEncode`、`LTXVPromptEnhancer`、`WanVideoTorchCompileSettings`、`easy clearCacheAll`、`LoadWanVideoClipTextEncoder`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`RH_Captioner`、`WanVideoTeaCache`、`WanVideoLoraSelect`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoEncode`、`DownloadAndLoadGIMMVFIModel`、`UpscaleModelLoader`、`ImageScaleBy`、`GIMMVFI_interpolate`、`ImageUpscaleWithModel`、`JjkShowText`、`WanVideoSampler`、`DWPreprocessor`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`LoadImage`、`Text Multiline`、`RIFE VFI`、`ImageConcatMulti`、`Text Concatenate`、`GetImageRangeFromBatch`、`WanVideoControlEmbeds`、`WanVideoEmptyEmbeds`、`ImageBlend`、`AIO_Preprocessor`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`MeshGraphormer-DepthMapPreprocessor`

**用到的条目**：LoadImage、MeshGraphormer-DepthMapPreprocessor、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
