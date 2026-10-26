---
key: 数字人/数字人/wan2.2数字人_1987723803025412097.json
name: wan2.2数字人_1987723803025412097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2数字人_1987723803025412097.json
hash: 1bc9a3a4b45ed688
coverage: 0.849057
learned_at: 2026-10-26 01:59:28
nodes: [WanVideoBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, Display Int (rgthree), SoundFlow_GetLength, CreateCFGScheduleFloatList, MultiTalkWav2VecEmbeds, AudioSeparation, ImageResizeKJ, LayerUtility: PurgeVRAM V2, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, PrimitiveNode, INTConstant, MultiTalkModelLoader, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoModelLoader, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, Int, Note, Note, INTConstant, LoadImage, Note, PreviewAudio, LoadAudio, SimpleMath+, ToInt, easy int, Text Multiline, Text Multiline, easy imageRemBg, ImageFromBatch+, GetImageSizeAndCount, WanVideoDecode, WanVideoVAELoader, CR Text Concatenate, AudioCrop, PrimitiveString, PrimitiveString, ColorMatch, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2数字人_1987723803025412097.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2数字人_1987723803025412097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（53 个）：
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `Display Int (rgthree)`
- `SoundFlow_GetLength`
- `CreateCFGScheduleFloatList`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `PrimitiveNode`
- `INTConstant`
- `MultiTalkModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Note`
- `Note`
- `INTConstant`
- `LoadImage`
- `Note`
- `PreviewAudio`
- `LoadAudio`
- `SimpleMath+`
- `ToInt`
- `easy int`
- `Text Multiline`
- `Text Multiline`
- `easy imageRemBg`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `CR Text Concatenate`
- `AudioCrop`
- `PrimitiveString`
- `PrimitiveString`
- `ColorMatch`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **85%**（45/53）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`Display Int (rgthree)`、`SoundFlow_GetLength`、`CreateCFGScheduleFloatList`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`ImageResizeKJ`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`INTConstant`、`MultiTalkModelLoader`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoadImage`、`PreviewAudio`、`LoadAudio`、`SimpleMath+`、`ToInt`、`easy int`、`Text Multiline`、`easy imageRemBg`、`ImageFromBatch+`、`WanVideoDecode`、`WanVideoVAELoader`、`CR Text Concatenate`、`AudioCrop`、`ColorMatch`、`ImageConcatMulti`、`VHS_VideoCombine`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
