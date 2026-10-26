---
key: 数字人/数字人/wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786.json
name: wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786.json
hash: 080526fb89b563d3
coverage: 0.560976
learned_at: 2026-10-26 01:59:32
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, SetNode, WanVideoClipVisionEncode, INTConstant, INTConstant, ImageResizeKJv2, LoadImage, DownloadAndLoadWav2VecModel, AudioSeparation, WanVideoModelLoader, MultiTalkWav2VecEmbeds, SetNode, SetNode, GetNode, WanVideoImageToVideoMultiTalk, WanVideoSampler, VHS_LoadVideo, VHS_VideoCombine, LoadAudio, WanVideoTextEncode, AudioCrop]
patterns: []
missing: []
---

# 数字人/数字人/wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `WanVideoModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadAudio`
- `WanVideoTextEncode`
- `AudioCrop`

## 知识

覆盖率 **56%**（23/41）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`INTConstant`、`ImageResizeKJv2`、`LoadImage`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadAudio`、`WanVideoTextEncode`、`AudioCrop`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
