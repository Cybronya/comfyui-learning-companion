---
key: 数字人/数字人/wanvideo_infinitetalk_单人工作流_1988849254452039682.json
name: wanvideo_infinitetalk_单人工作流_1988849254452039682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wanvideo_infinitetalk_单人工作流_1988849254452039682.json
hash: b3b8ee71a798c151
coverage: 0.560976
learned_at: 2026-10-26 01:59:32
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, DownloadAndLoadWav2VecModel, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, SetNode, VHS_VideoCombine, AudioSeparation, SetNode, WanVideoTextEncode, INTConstant, AudioCrop, SetNode, INTConstant, SetNode, WanVideoClipVisionEncode, VHS_LoadVideo, WanVideoVAELoader, CLIPVisionLoader, GetNode, MultiTalkWav2VecEmbeds, ImageResizeKJv2, WanVideoImageToVideoMultiTalk, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/wanvideo_infinitetalk_单人工作流_1988849254452039682.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wanvideo_infinitetalk_单人工作流_1988849254452039682.json`

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
- `SetNode`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `SetNode`
- `SetNode`
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
- `VHS_VideoCombine`
- `AudioSeparation`
- `SetNode`
- `WanVideoTextEncode`
- `INTConstant`
- `AudioCrop`
- `SetNode`
- `INTConstant`
- `SetNode`
- `WanVideoClipVisionEncode`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `ImageResizeKJv2`
- `WanVideoImageToVideoMultiTalk`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **56%**（23/41）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`AudioSeparation`、`WanVideoTextEncode`、`INTConstant`、`AudioCrop`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`WanVideoVAELoader`、`CLIPVisionLoader`、`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`WanVideoImageToVideoMultiTalk`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
