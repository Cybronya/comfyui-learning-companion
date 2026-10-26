---
key: 数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json
name: 语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json
hash: 94f13bece83cfd54
coverage: 0.644444
learned_at: 2026-10-26 02:05:33
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, WanVideoClipVisionEncode, SetNode, SetNode, MultiTalkModelLoader, VHS_VideoCombine, AudioSeparation, MultiTalkWav2VecEmbeds, AudioCrop, ImageResizeKJv2, IndexTTSNode, WanVideoImageToVideoMultiTalk, IndexTTSNode, LoadAudio, Text, PreviewAudio, AudioSeparation, AudioCrop, LoadImage, Text, PreviewAudio, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
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
- `DownloadAndLoadWav2VecModel`
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
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `AudioSeparation`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`
- `ImageResizeKJv2`
- `IndexTTSNode`
- `WanVideoImageToVideoMultiTalk`
- `IndexTTSNode`
- `LoadAudio`
- `Text`
- `PreviewAudio`
- `AudioSeparation`
- `AudioCrop`
- `LoadImage`
- `Text`
- `PreviewAudio`
- `LoadAudio`

## 知识

覆盖率 **64%**（29/45）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`MultiTalkModelLoader`、`VHS_VideoCombine`、`AudioSeparation`、`MultiTalkWav2VecEmbeds`、`AudioCrop`、`ImageResizeKJv2`、`IndexTTSNode`、`WanVideoImageToVideoMultiTalk`、`LoadAudio`、`Text`、`PreviewAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
