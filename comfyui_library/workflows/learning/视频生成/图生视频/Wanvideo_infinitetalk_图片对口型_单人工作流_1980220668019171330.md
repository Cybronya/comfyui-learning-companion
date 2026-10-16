---
key: 视频生成/图生视频/Wanvideo_infinitetalk_图片对口型_单人工作流_1980220668019171330.json
name: Wanvideo_infinitetalk_图片对口型_单人工作流_1980220668019171330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980220668019171330.json
hash: 586d7d8d95b6e41f
coverage: 0.520833
learned_at: 2026-10-15 22:32:29
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, SetNode, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, GetNode, WanVideoSampler, WanVideoDecode, WanVideoClipVisionEncode, VHS_VideoCombine, ImageConcatMulti, SetNode, ImageResizeKJv2, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, PrimitiveString, SetNode, SetNode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, GetNode, ImageResizeKJv2, LoadImage, PrimitiveString, LoadAudio, AudioCrop, AudioSeparation, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wanvideo_infinitetalk_图片对口型_单人工作流_1980220668019171330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980220668019171330.json`

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
- `SetNode`
- `SetNode`
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
- `PrimitiveString`
- `SetNode`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `PrimitiveString`
- `LoadAudio`
- `AudioCrop`
- `AudioSeparation`
- `Int`
- `Int`

## 知识

覆盖率 **52%**（25/48）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`ImageConcatMulti`、`ImageResizeKJv2`、`LoadImage`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`LoadAudio`、`AudioCrop`、`AudioSeparation`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
