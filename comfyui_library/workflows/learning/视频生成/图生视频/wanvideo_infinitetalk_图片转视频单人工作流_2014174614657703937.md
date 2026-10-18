---
key: 视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json
name: wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json
hash: 501a5eedf010db5c
coverage: 0.560976
learned_at: 2026-10-15 22:34:33
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, SetNode, SetNode, MultiTalkWav2VecEmbeds, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, SetNode, WanVideoClipVisionEncode, VHS_VideoCombine, AudioCrop, AudioSeparation, LoadImage, LoadAudio, VHS_LoadVideo, ImageResizeKJv2, INTConstant, INTConstant, WanVideoImageToVideoMultiTalk]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_infinitetalk_图片转视频单人工作流_2014174614657703937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2014174614657703937.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
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
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `AudioCrop`
- `AudioSeparation`
- `LoadImage`
- `LoadAudio`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `WanVideoImageToVideoMultiTalk`

## 知识

覆盖率 **56%**（23/41）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`AudioCrop`、`AudioSeparation`、`LoadImage`、`LoadAudio`、`VHS_LoadVideo`、`ImageResizeKJv2`、`INTConstant`、`WanVideoImageToVideoMultiTalk`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
