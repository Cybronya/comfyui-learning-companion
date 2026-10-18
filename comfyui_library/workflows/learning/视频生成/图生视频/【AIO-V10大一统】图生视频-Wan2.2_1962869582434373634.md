---
key: 视频生成/图生视频/【AIO-V10大一统】图生视频-Wan2.2_1962869582434373634.json
name: 【AIO-V10大一统】图生视频-Wan2.2_1962869582434373634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【AIO-V10大一统】图生视频-Wan2.2_1962869582434373634.json
hash: 1f29f1e29a5b35af
coverage: 0.761905
learned_at: 2026-10-15 22:31:32
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, Int, easy textSwitch, WanImageToVideo, VAEDecode, ModelSamplingSD3, VHS_VideoCombine, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, PrimitiveInt, PrimitiveInt, MathExpression|pysssss, Primitive integer [Crystools], Note, LoadImage, RH_LLMAPI_NODE, ShowText|pysssss, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 116487651407624, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【AIO-V10大一统】图生视频-Wan2.2_1962869582434373634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962869582434373634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `easy textSwitch`
- `WanImageToVideo`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Note`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `116487651407624`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`KSampler`、`CLIPTextEncode`、`Int`、`easy textSwitch`、`WanImageToVideo`、`VAEDecode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`LoadImage`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、Int

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
