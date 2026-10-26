---
key: 数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json
name: Wan2.2+Multitalk数字人工作流_1952579748809641986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json
hash: 27fc13c5bb6e0ca9
coverage: 0.954545
learned_at: 2026-10-26 01:57:54
nodes: [ttN int, ttN int, CR Integer To String, AudioSeparation, AudioCrop, PreviewAudio, MathExpression|pysssss, DownloadAndLoadWav2VecModel, Note, MultiTalkWav2VecEmbeds, ttN int, ImageResizeKJv2, PreviewImage, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoVAELoader, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, CR Prompt Text, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, easy seed, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2+Multitalk数字人工作流_1952579748809641986.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `ttN int`
- `ttN int`
- `CR Integer To String`
- `AudioSeparation`
- `AudioCrop`
- `PreviewAudio`
- `MathExpression|pysssss`
- `DownloadAndLoadWav2VecModel`
- `Note`
- `MultiTalkWav2VecEmbeds`
- `ttN int`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `CR Prompt Text`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `easy seed`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`ttN int`、`CR Integer To String`、`AudioSeparation`、`AudioCrop`、`PreviewAudio`、`MathExpression|pysssss`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`CR Prompt Text`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`easy seed`、`LoadImage`、`LoadAudio`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
