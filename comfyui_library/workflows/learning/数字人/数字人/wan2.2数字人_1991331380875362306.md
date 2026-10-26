---
key: 数字人/数字人/wan2.2数字人_1991331380875362306.json
name: wan2.2数字人_1991331380875362306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.2数字人_1991331380875362306.json
hash: 04e20103251de27d
coverage: 0.819672
learned_at: 2026-10-26 01:59:28
nodes: [WanVideoBlockSwap, WanVideoBlockSwap, WanVideoDecode, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, ToInt, Display Int (rgthree), easy int, PrimitiveString, SoundFlow_GetLength, PreviewAudio, LoadAudio, WanVideoVAELoader, CreateCFGScheduleFloatList, SimpleMath+, MultiTalkWav2VecEmbeds, AudioSeparation, LayerUtility: PurgeVRAM V2, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, PrimitiveNode, GetImageSizeAndCount, INTConstant, Text Multiline, MarkdownNote, MultiTalkModelLoader, CR Text Concatenate, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoImageToVideoEncode, easy imageRemBg, GetImageSizeAndCount, WanVideoModelLoader, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, Int, Note, Note, ImageConcatMulti, PrimitiveString, ImageFromBatch+, LoadImage, VHS_VideoCombine, VHS_VideoCombine, Text Multiline, INTConstant, AudioCrop, TT_img_enc, SaveImage, ImageResizeKJ, ColorMatch, GetImageSizeAndCount, ImageFromBatch+, SaveImage, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Note]
patterns: []
missing: []
---

# 数字人/数字人/wan2.2数字人_1991331380875362306.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.2数字人_1991331380875362306.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（61 个）：
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `ToInt`
- `Display Int (rgthree)`
- `easy int`
- `PrimitiveString`
- `SoundFlow_GetLength`
- `PreviewAudio`
- `LoadAudio`
- `WanVideoVAELoader`
- `CreateCFGScheduleFloatList`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `PrimitiveNode`
- `GetImageSizeAndCount`
- `INTConstant`
- `Text Multiline`
- `MarkdownNote`
- `MultiTalkModelLoader`
- `CR Text Concatenate`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoImageToVideoEncode`
- `easy imageRemBg`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Note`
- `Note`
- `ImageConcatMulti`
- `PrimitiveString`
- `ImageFromBatch+`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Text Multiline`
- `INTConstant`
- `AudioCrop`
- `TT_img_enc`
- `SaveImage`
- `ImageResizeKJ`
- `ColorMatch`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `SaveImage`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Note`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`WanVideoBlockSwap`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`ToInt`、`Display Int (rgthree)`、`easy int`、`SoundFlow_GetLength`、`PreviewAudio`、`LoadAudio`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`INTConstant`、`Text Multiline`、`MultiTalkModelLoader`、`CR Text Concatenate`、`WanVideoImageToVideoEncode`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`ImageConcatMulti`、`ImageFromBatch+`、`LoadImage`、`VHS_VideoCombine`、`AudioCrop`、`TT_img_enc`、`SaveImage`、`ImageResizeKJ`、`ColorMatch`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
