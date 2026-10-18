---
key: 视频生成/文生视频/【AIO-V10大一统】文生视频-Wan2.2_1962869476662415362.json
name: 【AIO-V10大一统】文生视频-Wan2.2_1962869476662415362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【AIO-V10大一统】文生视频-Wan2.2_1962869476662415362.json
hash: 8588e988863395ef
coverage: 0.823529
learned_at: 2026-10-15 22:43:43
nodes: [ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, Int, Note, easy textSwitch, CheckpointLoaderSimple, VAEDecode, VHS_VideoCombine, Primitive integer [Crystools], MathExpression|pysssss, KSampler, EmptyHunyuanLatentVideo, LoadImage, ShowText|pysssss, RH_LLMAPI_NODE, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 59201535461047, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/【AIO-V10大一统】文生视频-Wan2.2_1962869476662415362.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1962869476662415362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `Note`
- `easy textSwitch`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `EmptyHunyuanLatentVideo`
- `LoadImage`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `PrimitiveStringMultiline`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v10-nsfw.safetensors`
- `seed` = `59201535461047`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`Int`、`easy textSwitch`、`CheckpointLoaderSimple`、`VAEDecode`、`VHS_VideoCombine`、`Primitive integer [Crystools]`、`MathExpression|pysssss`、`KSampler`、`EmptyHunyuanLatentVideo`、`LoadImage`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、EmptyHunyuanLatentVideo、Int、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
