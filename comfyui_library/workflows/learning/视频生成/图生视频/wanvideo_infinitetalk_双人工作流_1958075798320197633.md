---
key: 视频生成/图生视频/wanvideo_infinitetalk_双人工作流_1958075798320197633.json
name: wanvideo_infinitetalk_双人工作流_1958075798320197633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958075798320197633.json
hash: 1562d436d2c43935
coverage: 0.581395
learned_at: 2026-10-15 22:31:20
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, SetNode, WanVideoVAELoader, SetNode, GetNode, SetNode, SetNode, INTConstant, INTConstant, SetNode, DownloadAndLoadWav2VecModel, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, GetNode, GetNode, WanVideoSampler, WanVideoDecode, SetNode, WanVideoClipVisionEncode, ImageResizeKJv2, LoadImage, SetNode, SetNode, MultiTalkModelLoader, VHS_VideoCombine, AudioSeparation, LoadAudio, LoadAudio, AudioCrop, AudioSeparation, MultiTalkWav2VecEmbeds, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_infinitetalk_双人工作流_1958075798320197633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958075798320197633.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
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
- `SetNode`
- `DownloadAndLoadWav2VecModel`
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
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SetNode`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `AudioSeparation`
- `LoadAudio`
- `LoadAudio`
- `AudioCrop`
- `AudioSeparation`
- `MultiTalkWav2VecEmbeds`
- `AudioCrop`

## 知识

覆盖率 **58%**（25/43）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`INTConstant`、`DownloadAndLoadWav2VecModel`、`WanVideoTextEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`LoadImage`、`MultiTalkModelLoader`、`VHS_VideoCombine`、`AudioSeparation`、`LoadAudio`、`AudioCrop`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
