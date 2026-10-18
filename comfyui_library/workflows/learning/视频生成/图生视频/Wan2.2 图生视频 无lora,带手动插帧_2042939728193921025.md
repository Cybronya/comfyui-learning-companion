---
key: 视频生成/图生视频/Wan2.2 图生视频 无lora,带手动插帧_2042939728193921025.json
name: Wan2.2 图生视频 无lora,带手动插帧_2042939728193921025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 图生视频 无lora,带手动插帧_2042939728193921025.json
hash: b8a97fa2e53934d5
coverage: 0.625
learned_at: 2026-10-15 22:36:30
nodes: [KSampler, GetNode, GetNode, GetNode, WanImageToVideo, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, SimpleMath+, ImageScaleToTotalPixels, PreviewImage, CheckpointLoaderSimple, Int, Primitive integer [Crystools], Int, SetNode, SetNode, Note, easy textSwitch, Int, RH_LLMAPI_NODE, GetNode, PrimitiveStringMultiline, SetNode, SetNode, LoadImage, ShowText|pysssss, VHS_VideoCombine, VAEDecode, RIFE VFI]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 395753018662878, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 图生视频 无lora,带手动插帧_2042939728193921025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042939728193921025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
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
- `Int`
- `Primitive integer [Crystools]`
- `Int`
- `SetNode`
- `SetNode`
- `Note`
- `easy textSwitch`
- `Int`
- `RH_LLMAPI_NODE`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `RIFE VFI`

## 关键参数

- `seed` = `395753018662878`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **62%**（20/32）

**有卡**：`KSampler`、`WanImageToVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SimpleMath+`、`ImageScaleToTotalPixels`、`CheckpointLoaderSimple`、`Int`、`Primitive integer [Crystools]`、`easy textSwitch`、`RH_LLMAPI_NODE`、`LoadImage`、`VHS_VideoCombine`、`VAEDecode`、`RIFE VFI`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ImageScaleToTotalPixels

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
