---
key: 数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json
name: Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json
hash: 60cdfe931f3b9a5b
coverage: 0.5625
learned_at: 2026-10-26 01:58:10
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, DownloadAndLoadWav2VecModel, SetNode, SetNode, MultiTalkWav2VecEmbeds, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, GetNode, WanVideoSampler, WanVideoDecode, WanVideoClipVisionEncode, ImageResizeKJv2, AudioCrop, VHS_VideoCombine, ImageConcatMulti, SetNode, ImageResizeKJv2, GetNode, VHS_LoadVideo, LoadImage, LoadImage, VHS_LoadVideo, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncode, AudioSeparation, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
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
- `INTConstant`
- `INTConstant`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `AudioCrop`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `AudioSeparation`
- `LoadAudio`

## 知识

覆盖率 **56%**（27/48）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`INTConstant`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`AudioCrop`、`VHS_VideoCombine`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncode`、`AudioSeparation`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
