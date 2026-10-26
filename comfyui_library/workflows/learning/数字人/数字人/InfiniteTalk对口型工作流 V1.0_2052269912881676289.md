---
key: 数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json
name: InfiniteTalk对口型工作流 V1.0_2052269912881676289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json
hash: 0daf78df7d6137f9
coverage: 0.75
learned_at: 2026-10-26 01:55:12
nodes: [MultiTalkModelLoader, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, WanVideoDecode, MarkdownNote, CLIPVisionLoader, PreviewAudio, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, MarkdownNote, LoadWanVideoT5TextEncoder, AudioSeparation, DownloadAndLoadWav2VecModel, MarkdownNote, ToInt, MarkdownNote, MarkdownNote, RH_GetAudioDuration, easy showAnything, SimpleMath+, WanVideoImageToVideoMultiTalk, PrimitiveFloat, ToInt, easy showAnything, VHS_VideoCombine, MultiTalkWav2VecEmbeds, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PreviewAudio, WanVideoSampler, LoadImage, AudioCrop, WanVideoTextEncode, LoadAudio, WanVideoBlockSwap]
patterns: []
missing: []
---

# 数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/InfiniteTalk对口型工作流 V1.0_2052269912881676289.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `MultiTalkModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `MarkdownNote`
- `CLIPVisionLoader`
- `PreviewAudio`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `MarkdownNote`
- `ToInt`
- `MarkdownNote`
- `MarkdownNote`
- `RH_GetAudioDuration`
- `easy showAnything`
- `SimpleMath+`
- `WanVideoImageToVideoMultiTalk`
- `PrimitiveFloat`
- `ToInt`
- `easy showAnything`
- `VHS_VideoCombine`
- `MultiTalkWav2VecEmbeds`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PreviewAudio`
- `WanVideoSampler` ★核心
- `LoadImage`
- `AudioCrop`
- `WanVideoTextEncode`
- `LoadAudio`
- `WanVideoBlockSwap`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`MultiTalkModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`CLIPVisionLoader`、`PreviewAudio`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`ToInt`、`RH_GetAudioDuration`、`SimpleMath+`、`WanVideoImageToVideoMultiTalk`、`VHS_VideoCombine`、`MultiTalkWav2VecEmbeds`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`LoadImage`、`AudioCrop`、`WanVideoTextEncode`、`LoadAudio`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelectMulti
