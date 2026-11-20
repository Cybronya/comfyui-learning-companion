---
key: 视频生成/图生视频/动物说话_Animals_That_Talk_Generate_Videos_from_Image_2116372735105519617.json
name: 动物说话_Animals_That_Talk_Generate_Videos_from_Image_2116372735105519617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动物说话_Animals_That_Talk_Generate_Videos_from_Image_2116372735105519617.json
hash: a9aaeca8251890d0
coverage: 0.809524
learned_at: 2026-11-02 19:19:29
nodes: [SetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, GetNode, GetNode, WanVideoDecode, LayerUtility: PurgeVRAM, easy cleanGpuUsed, SetNode, WanVideoLoraSelect, MultiTalkModelLoader, LayerUtility: PurgeVRAM, CLIPVisionLoader, SetNode, GetImageSizeAndCount, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, WanVideoVAELoader, AudioSeparation, easy cleanGpuUsed, If ANY execute A else B, VHS_VideoCombine, SparkTTSClone, SaveAudio, Text Multiline, LoadImage, PrimitiveInt, LoadAudio, Int, ImageResizeKJv2, MultiTalkWav2VecEmbeds, WanVideoImageToVideoMultiTalk, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, WanVideoTextEncode, Text Multiline, WanVideoSampler, WanVideoModelLoader, DF_Int_to_Float]
patterns: []
missing: []
---

# 视频生成/图生视频/动物说话_Animals_That_Talk_Generate_Videos_from_Image_2116372735105519617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动物说话_Animals_That_Talk_Generate_Videos_from_Image_2116372735105519617.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `LayerUtility: PurgeVRAM`
- `CLIPVisionLoader`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `AudioSeparation`
- `easy cleanGpuUsed`
- `If ANY execute A else B`
- `VHS_VideoCombine`
- `SparkTTSClone`
- `SaveAudio`
- `Text Multiline`
- `LoadImage`
- `PrimitiveInt`
- `LoadAudio`
- `Int`
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `WanVideoTextEncode`
- `Text Multiline`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `DF_Int_to_Float`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`CLIPVisionLoader`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`AudioSeparation`、`If ANY execute A else B`、`VHS_VideoCombine`、`SparkTTSClone`、`SaveAudio`、`Text Multiline`、`LoadImage`、`LoadAudio`、`Int`、`ImageResizeKJv2`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoModelLoader`、`DF_Int_to_Float`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
