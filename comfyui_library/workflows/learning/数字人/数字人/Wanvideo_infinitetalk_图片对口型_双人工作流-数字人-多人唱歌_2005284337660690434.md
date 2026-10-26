---
key: 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json
name: Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json
hash: 7b9c459d6dd80982
coverage: 0.590164
learned_at: 2026-10-26 01:58:09
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, WanVideoClipVisionEncode, ImageResizeKJv2, MultiTalkModelLoader, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, ImageResizeKJv2, GetNode, SoundFlow_GetLength, Bjornulf_ShowFloat, AudioSeparation, AudioSeparation, easy int, DownloadAndLoadWav2VecModel, SetNode, SetNode, WanVideoImageToVideoMultiTalk, Note, GetNode, ToInt, Note, GetNode, Display Int (rgthree), Note, SimpleMath+, SetNode, Display Int (rgthree), MultiTalkWav2VecEmbeds, AudioCrop, AudioCrop, INTConstant, INTConstant, LoadImage, LoadAudio, LoadAudio, WanVideoDecode, easy cleanGpuUsed, WanVideoSampler, VHS_VideoCombine, WanVideoTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（61 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `GetNode`
- `SoundFlow_GetLength`
- `Bjornulf_ShowFloat`
- `AudioSeparation`
- `AudioSeparation`
- `easy int`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `SetNode`
- `WanVideoImageToVideoMultiTalk`
- `Note`
- `GetNode`
- `ToInt`
- `Note`
- `GetNode`
- `Display Int (rgthree)`
- `Note`
- `SimpleMath+`
- `SetNode`
- `Display Int (rgthree)`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `AudioCrop`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoTextEncode`

## 知识

覆盖率 **59%**（36/61）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`MultiTalkModelLoader`、`LoadImage`、`ImageConcatMulti`、`SoundFlow_GetLength`、`Bjornulf_ShowFloat`、`AudioSeparation`、`easy int`、`DownloadAndLoadWav2VecModel`、`WanVideoImageToVideoMultiTalk`、`ToInt`、`Display Int (rgthree)`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`INTConstant`、`LoadAudio`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
