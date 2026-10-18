---
key: 视频生成/图生视频/InfiniTetalk+美化lora数字人workflow_2101551649981554690.json
name: InfiniTetalk+美化lora数字人workflow_2101551649981554690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/InfiniTetalk+美化lora数字人workflow_2101551649981554690.json
hash: c13d9b8c0ed7f823
coverage: 0.571429
learned_at: 2026-10-17 02:14:05
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, SetNode, easy showAnything, CLIPVisionLoader, Reroute, LoadWanVideoT5TextEncoder, GetImageRangeFromBatch, Reroute, WanVideoVAELoader, Anything Everywhere, Reroute, Reroute, Note, PreviewAudio, SetNode, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoTorchCompileSettings, Note, PreviewAudio, Audio Duration (mtb), MathExpression|pysssss, AudioSeparation, SetNode, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, WanVideoModelLoader, AudioCrop, DownloadAndLoadWav2VecModel, WanVideoBlockSwap, MathExpression|pysssss, MultiTalkWav2VecEmbeds, WanVideoSampler, PlaySound|pysssss, WanVideoDecode, GetNode, VHS_VideoCombine, WanVideoImageToVideoMultiTalk, LoadAudio, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, easy int, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/InfiniTetalk+美化lora数字人workflow_2101551649981554690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/InfiniTetalk+美化lora数字人workflow_2101551649981554690.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoClipVisionEncode`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `easy showAnything`
- `CLIPVisionLoader`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `GetImageRangeFromBatch`
- `Reroute`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `Reroute`
- `Reroute`
- `Note`
- `PreviewAudio`
- `SetNode`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `Note`
- `PreviewAudio`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `AudioSeparation`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `WanVideoSampler` ★核心
- `PlaySound|pysssss`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoImageToVideoMultiTalk`
- `LoadAudio`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `WanVideoLoraSelect`

## 知识

覆盖率 **57%**（32/56）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`GetImageRangeFromBatch`、`WanVideoVAELoader`、`PreviewAudio`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`AudioSeparation`、`WanVideoTextEncode`、`WanVideoModelLoader`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`WanVideoBlockSwap`、`MultiTalkWav2VecEmbeds`、`WanVideoSampler`、`PlaySound|pysssss`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`LoadAudio`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
