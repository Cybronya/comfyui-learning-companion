---
key: 视频生成/图生视频/AIO-V10大一统图生视频-Wan2.2_1986735841529819137.json
name: AIO-V10大一统图生视频-Wan2.2_1986735841529819137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1986735841529819137.json
hash: 94dfbdd2319d0e1f
coverage: 0.8125
learned_at: 2026-10-15 22:32:56
nodes: [PrimitiveInt, PrimitiveInt, VAEDecode, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, Primitive integer [Crystools], KSampler, CLIPVisionEncode, VHS_VideoCombine, CLIPVisionLoader, ModelSamplingSD3, WanImageToVideo, CheckpointLoaderSimple, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 211049127555107, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AIO-V10大一统图生视频-Wan2.2_1986735841529819137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986735841529819137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `211049127555107`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`KSampler`、`CLIPVisionEncode`、`VHS_VideoCombine`、`CLIPVisionLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
