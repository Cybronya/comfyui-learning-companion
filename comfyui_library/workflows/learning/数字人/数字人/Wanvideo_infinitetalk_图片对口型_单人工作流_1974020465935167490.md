---
key: 数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json
name: Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json
hash: 97969458f4c8a4f6
coverage: 0.520833
learned_at: 2026-10-26 01:58:09
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, GetNode, WanVideoSampler, WanVideoDecode, WanVideoClipVisionEncode, VHS_VideoCombine, ImageConcatMulti, SetNode, ImageResizeKJv2, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PrimitiveString, PrimitiveString, LoadImage, SetNode, SetNode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioCrop, LoadAudio, AudioSeparation]
patterns: []
missing: []
---

# 数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json`

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
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PrimitiveString`
- `PrimitiveString`
- `LoadImage`
- `SetNode`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioCrop`
- `LoadAudio`
- `AudioSeparation`

## 知识

覆盖率 **52%**（25/48）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`INTConstant`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`ImageConcatMulti`、`ImageResizeKJv2`、`LoadImage`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioCrop`、`LoadAudio`、`AudioSeparation`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
