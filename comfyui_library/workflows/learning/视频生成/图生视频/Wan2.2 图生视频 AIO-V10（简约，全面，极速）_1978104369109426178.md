---
key: 视频生成/图生视频/Wan2.2 图生视频 AIO-V10（简约，全面，极速）_1978104369109426178.json
name: Wan2.2 图生视频 AIO-V10（简约，全面，极速）_1978104369109426178.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978104369109426178.json
hash: 069d8e73f2bfbe87
coverage: 0.612903
learned_at: 2026-10-15 22:32:17
nodes: [KSampler, GetNode, GetNode, GetNode, WanImageToVideo, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, SimpleMath+, ImageScaleToTotalPixels, PreviewImage, CheckpointLoaderSimple, VAEDecode, VHS_VideoCombine, Int, Primitive integer [Crystools], Int, SetNode, SetNode, Note, easy textSwitch, Int, ShowText|pysssss, RH_LLMAPI_NODE, GetNode, PrimitiveStringMultiline, SetNode, SetNode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 942234703201466, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 图生视频 AIO-V10（简约，全面，极速）_1978104369109426178.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978104369109426178.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `SimpleMath+`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Int`
- `Primitive integer [Crystools]`
- `Int`
- `SetNode`
- `SetNode`
- `Note`
- `easy textSwitch`
- `Int`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `LoadImage`

## 关键参数

- `seed` = `942234703201466`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **61%**（19/31）

**有卡**：`KSampler`、`WanImageToVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SimpleMath+`、`ImageScaleToTotalPixels`、`CheckpointLoaderSimple`、`VAEDecode`、`VHS_VideoCombine`、`Int`、`Primitive integer [Crystools]`、`easy textSwitch`、`RH_LLMAPI_NODE`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ImageScaleToTotalPixels

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
