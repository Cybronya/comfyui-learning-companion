---
key: 数字人/数字人/wanvideo_infinitetalk_小宝_2017971113397067777.json
name: wanvideo_infinitetalk_小宝_2017971113397067777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wanvideo_infinitetalk_小宝_2017971113397067777.json
hash: f3241fdeb9de2a27
coverage: 0.560976
learned_at: 2026-10-26 01:59:33
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, INTConstant, INTConstant, SetNode, DownloadAndLoadWav2VecModel, SetNode, SetNode, MultiTalkWav2VecEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, GetNode, GetNode, WanVideoSampler, WanVideoDecode, SetNode, AudioSeparation, WanVideoModelLoader, LoadAudio, ImageResizeKJv2, GetNode, WanVideoClipVisionEncode, SetNode, SetNode, MuyeLoadImage, AudioCrop, VHS_LoadVideo, VHS_VideoCombine, WanVideoTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/wanvideo_infinitetalk_小宝_2017971113397067777.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wanvideo_infinitetalk_小宝_2017971113397067777.json`

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
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `AudioSeparation`
- `WanVideoModelLoader`
- `LoadAudio`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `MuyeLoadImage`
- `AudioCrop`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoTextEncode`

## 知识

覆盖率 **56%**（23/41）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`INTConstant`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`AudioSeparation`、`WanVideoModelLoader`、`LoadAudio`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`MuyeLoadImage`、`AudioCrop`、`VHS_LoadVideo`、`VHS_VideoCombine`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect、CLIPVisionLoader
