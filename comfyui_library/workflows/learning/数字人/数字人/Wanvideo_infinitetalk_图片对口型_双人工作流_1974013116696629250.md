---
key: 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json
name: Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json
hash: 3d4fb427d9ca8596
coverage: 0.583333
learned_at: 2026-10-26 01:58:10
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, INTConstant, INTConstant, GetNode, WanVideoDecode, SetNode, WanVideoClipVisionEncode, ImageResizeKJv2, MultiTalkModelLoader, WanVideoTextEncode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadAudio, GetNode, LoadAudio, SoundFlow_GetLength, Bjornulf_ShowFloat, AudioSeparation, AudioSeparation, easy int, DownloadAndLoadWav2VecModel, SetNode, SetNode, WanVideoSampler, WanVideoImageToVideoMultiTalk, Note, GetNode, ToInt, Note, GetNode, VHS_VideoCombine, Display Int (rgthree), Note, SimpleMath+, SetNode, Display Int (rgthree), LoadImage, MultiTalkWav2VecEmbeds, AudioCrop, AudioCrop]
patterns: []
missing: []
---

# 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
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
- `INTConstant`
- `INTConstant`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `MultiTalkModelLoader`
- `WanVideoTextEncode`
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
- `LoadAudio`
- `GetNode`
- `LoadAudio`
- `SoundFlow_GetLength`
- `Bjornulf_ShowFloat`
- `AudioSeparation`
- `AudioSeparation`
- `easy int`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `Note`
- `GetNode`
- `ToInt`
- `Note`
- `GetNode`
- `VHS_VideoCombine`
- `Display Int (rgthree)`
- `Note`
- `SimpleMath+`
- `SetNode`
- `Display Int (rgthree)`
- `LoadImage`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `AudioCrop`

## 知识

覆盖率 **58%**（35/60）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`INTConstant`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`MultiTalkModelLoader`、`WanVideoTextEncode`、`LoadImage`、`ImageConcatMulti`、`LoadAudio`、`SoundFlow_GetLength`、`Bjornulf_ShowFloat`、`AudioSeparation`、`easy int`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`ToInt`、`VHS_VideoCombine`、`Display Int (rgthree)`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`AudioCrop`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
