---
key: 图片生成/图生图/wanvideo_infinitetalk_单人工作流_1977379439782830082.json
name: wanvideo_infinitetalk_单人工作流_1977379439782830082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wanvideo_infinitetalk_单人工作流_1977379439782830082.json
hash: bb4fca9a8c9d7a04
coverage: 0.55
learned_at: 2026-10-23 11:46:15
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, ImageResizeKJv2, SetNode, SetNode, INTConstant, INTConstant, SetNode, DownloadAndLoadWav2VecModel, SetNode, SetNode, MultiTalkWav2VecEmbeds, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, GetNode, GetNode, WanVideoSampler, WanVideoDecode, SetNode, WanVideoClipVisionEncode, AudioSeparation, VHS_VideoCombine, VHS_LoadVideo, LoadAudio, AudioCrop]
patterns: []
missing: []
---

# 图片生成/图生图/wanvideo_infinitetalk_单人工作流_1977379439782830082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wanvideo_infinitetalk_单人工作流_1977379439782830082.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
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
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
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
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `AudioSeparation`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadAudio`
- `AudioCrop`

## 知识

覆盖率 **55%**（22/40）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageResizeKJv2`、`INTConstant`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`AudioSeparation`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadAudio`、`AudioCrop`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect、CLIPVisionLoader
