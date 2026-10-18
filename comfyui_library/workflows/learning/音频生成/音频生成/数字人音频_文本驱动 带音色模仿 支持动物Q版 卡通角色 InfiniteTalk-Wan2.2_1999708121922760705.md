---
key: 音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json
name: 数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json
hash: b32c3be65d504ddf
coverage: 0.647059
learned_at: 2026-10-18 01:47:06
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, WanVideoDecode, WanVideoTextEncode, WanVideoClipVisionEncode, GetImageSizeAndCount, WanVideoVAELoader, WanVideoImageToVideoMultiTalk, WanVideoSampler, ImageResizeKJv2, MultiTalkWav2VecEmbeds, Int, easy cleanGpuUsed, ImageConcatMulti, Text Multiline, SparkTTSClone, Any Switch (rgthree), CR String To Number, Fast Groups Muter (rgthree), easy anythingIndexSwitch, VHS_VideoCombine, CR Text, AudioSeparation, WanVideoBlockSwap, LoadAudio, LoadImage, VHS_VideoCombine, MultiTalkModelLoader, WanVideoModelLoader, SetNode, LoadWanVideoT5TextEncoder, GetNode, SaveAudio, CR Text, GetNode, DownloadAndLoadWav2VecModel, Text Multiline, WanVideoLoraSelect, CLIPVisionLoader]
patterns: []
missing: []
---

# 音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `WanVideoVAELoader`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`
- `Int`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `Text Multiline`
- `SparkTTSClone`
- `Any Switch (rgthree)`
- `CR String To Number`
- `Fast Groups Muter (rgthree)`
- `easy anythingIndexSwitch`
- `VHS_VideoCombine`
- `CR Text`
- `AudioSeparation`
- `WanVideoBlockSwap`
- `LoadAudio`
- `LoadImage`
- `VHS_VideoCombine`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SaveAudio`
- `CR Text`
- `GetNode`
- `DownloadAndLoadWav2VecModel`
- `Text Multiline`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`

## 知识

覆盖率 **65%**（33/51）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoVAELoader`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`ImageResizeKJv2`、`MultiTalkWav2VecEmbeds`、`Int`、`easy cleanGpuUsed`、`ImageConcatMulti`、`Text Multiline`、`SparkTTSClone`、`CR String To Number`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`CR Text`、`AudioSeparation`、`WanVideoBlockSwap`、`LoadAudio`、`LoadImage`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`SaveAudio`、`DownloadAndLoadWav2VecModel`、`WanVideoLoraSelect`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
