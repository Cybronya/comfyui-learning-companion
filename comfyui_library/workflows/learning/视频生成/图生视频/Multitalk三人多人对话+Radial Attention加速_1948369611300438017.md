---
key: 视频生成/图生视频/Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json
name: Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json
hash: bf1a48ee615b9140
coverage: 0.964286
learned_at: 2026-10-15 22:30:47
nodes: [WanVideoBlockSwap, WanVideoTextEncodeSingle, LoadWanVideoT5TextEncoder, LoadImage, WanVideoVAELoader, WanVideoImageToVideoMultiTalk, WanVideoApplyNAG, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, SeparateMasks, MaskPreview+, LoadAudio, DownloadAndLoadWav2VecModel, WanVideoLoraSelect, WanVideoTextEncodeSingle, LoadAudio, LoadAudio, SaveAudioMP3, CLIPVisionLoader, WanVideoModelLoader, WanVideoSampler, MultiTalkModelLoader, ImageResizeKJv2, MultiTalkWav2VecEmbeds, WanVideoDecode, VHS_VideoCombine, WanVideoSetRadialAttention, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948369611300438017.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（28 个）：
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoApplyNAG`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `SeparateMasks`
- `MaskPreview+`
- `LoadAudio`
- `DownloadAndLoadWav2VecModel`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeSingle`
- `LoadAudio`
- `LoadAudio`
- `SaveAudioMP3`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `MultiTalkModelLoader`
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSetRadialAttention`
- `Note`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoBlockSwap`、`WanVideoTextEncodeSingle`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`WanVideoVAELoader`、`WanVideoImageToVideoMultiTalk`、`WanVideoApplyNAG`、`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`SeparateMasks`、`MaskPreview+`、`LoadAudio`、`DownloadAndLoadWav2VecModel`、`WanVideoLoraSelect`、`SaveAudioMP3`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoSampler`、`MultiTalkModelLoader`、`ImageResizeKJv2`、`MultiTalkWav2VecEmbeds`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSetRadialAttention`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeSingle、WanVideoLoraSelect
