---
key: 数字人/数字人/InfiniteTalk数字人对口型双人图像驱动工作流 V2.0_2034087466235334657.json
name: InfiniteTalk数字人对口型双人图像驱动工作流 V2.0_2034087466235334657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/InfiniteTalk数字人对口型双人图像驱动工作流 V2.0_2034087466235334657.json
hash: 67de70a93a15211c
coverage: 0.588235
learned_at: 2026-10-26 01:55:16
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, WanVideoTorchCompileSettings, SetNode, Reroute, Reroute, Anything Everywhere, GetNode, Reroute, Reroute, Reroute, Audio Duration (mtb), MathExpression|pysssss, AudioSeparation, AudioSeparation, AudioSeparation, MathExpression|pysssss, WanVideoLoraSelect, WanVideoLoraSelect, AudioCrop, AudioCrop, GetImageRangeFromBatch, SetNode, MultiTalkModelLoader, Note, Note, Note, WanVideoLoraSelect, AudioCrop, WanVideoTextEncode, MultiTalkWav2VecEmbeds, Note, SetNode, Note, Note, PreviewAudio, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskPreview, easy int, easy showAnything, WanVideoDecode, GetNode, SeparateMasks, WanVideoImageToVideoMultiTalk, WanVideoBlockSwap, WanVideoSampler, GetNode, VHS_VideoCombine, PlaySound|pysssss, LoadAudio, LoadAudio, LoadAudio, PreviewAudio, Reroute, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/InfiniteTalk数字人对口型双人图像驱动工作流 V2.0_2034087466235334657.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/InfiniteTalk数字人对口型双人图像驱动工作流 V2.0_2034087466235334657.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（68 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoClipVisionEncode`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `Reroute`
- `Reroute`
- `Anything Everywhere`
- `GetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `AudioSeparation`
- `AudioSeparation`
- `AudioSeparation`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `AudioCrop`
- `AudioCrop`
- `GetImageRangeFromBatch`
- `SetNode`
- `MultiTalkModelLoader`
- `Note`
- `Note`
- `Note`
- `WanVideoLoraSelect`
- `AudioCrop`
- `WanVideoTextEncode`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `SetNode`
- `Note`
- `Note`
- `PreviewAudio`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskPreview`
- `easy int`
- `easy showAnything`
- `WanVideoDecode`
- `GetNode`
- `SeparateMasks`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `PlaySound|pysssss`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `PreviewAudio`
- `Reroute`
- `LoadImage`

## 知识

覆盖率 **59%**（40/68）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`AudioSeparation`、`WanVideoLoraSelect`、`AudioCrop`、`GetImageRangeFromBatch`、`MultiTalkModelLoader`、`WanVideoTextEncode`、`MultiTalkWav2VecEmbeds`、`PreviewAudio`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskPreview`、`easy int`、`WanVideoDecode`、`SeparateMasks`、`WanVideoImageToVideoMultiTalk`、`WanVideoBlockSwap`、`WanVideoSampler`、`VHS_VideoCombine`、`PlaySound|pysssss`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
