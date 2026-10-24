---
key: 图片生成/图生图/小学生扮演：坦克是没有后视镜的-吴京梗waninfinit+InfiniteTalk_1963984357075599362.json
name: 小学生扮演：坦克是没有后视镜的-吴京梗waninfinit+InfiniteTalk_1963984357075599362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小学生扮演：坦克是没有后视镜的-吴京梗waninfinit+InfiniteTalk_1963984357075599362.json
hash: 56026572e248738d
coverage: 0.469697
learned_at: 2026-10-23 12:48:49
nodes: [SetNode, SetNode, GetNode, GetNode, Note, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, SetNode, WanVideoImageToVideoMultiTalk, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, WanVideoBlockSwap, MultiTalkWav2VecEmbeds, LayerUtility: PurgeVRAM V2, GetNode, VHS_VideoInfoLoaded, Any Switch (rgthree), Any Switch (rgthree), GetNode, Note, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, WanVideoClipVisionEncode, WanVideoEncode, SetNode, GetNode, MathExpression|pysssss, AudioSeparation, SetNode, SetNode, SetNode, SetNode, GetNode, Audio Duration (mtb), Any Switch (rgthree), VHS_VideoCombine, Note, WanVideoTorchCompileSettings, PreviewAudio, WanVideoSampler, GetNode, WanVideoVAELoader, WanVideoModelLoader, MultiTalkModelLoader, WanVideoLoraSelect, SetNode, SetNode, Label (rgthree), INTConstant, INTConstant, WanVideoTextEncode, LoadAudio, PreviewImage, WanVideoDecode, ImageResizeKJv2, VHS_LoadVideo]
patterns: []
missing: []
---

# 图片生成/图生图/小学生扮演：坦克是没有后视镜的-吴京梗waninfinit+InfiniteTalk_1963984357075599362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小学生扮演：坦克是没有后视镜的-吴京梗waninfinit+InfiniteTalk_1963984357075599362.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（66 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoImageToVideoMultiTalk`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `SetNode`
- `GetNode`
- `MathExpression|pysssss`
- `AudioSeparation`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Audio Duration (mtb)`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTorchCompileSettings`
- `PreviewAudio`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `LoadAudio`
- `PreviewImage`
- `WanVideoDecode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`

## 知识

覆盖率 **47%**（31/66）

**有卡**：`CLIPVisionLoader`、`WanVideoImageToVideoMultiTalk`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`MultiTalkWav2VecEmbeds`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoInfoLoaded`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`WanVideoEncode`、`MathExpression|pysssss`、`AudioSeparation`、`Audio Duration (mtb)`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`PreviewAudio`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`Label (rgthree)`、`INTConstant`、`WanVideoTextEncode`、`LoadAudio`、`WanVideoDecode`、`ImageResizeKJv2`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect
