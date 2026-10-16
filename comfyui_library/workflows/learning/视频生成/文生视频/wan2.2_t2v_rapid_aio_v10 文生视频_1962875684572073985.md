---
key: 视频生成/文生视频/wan2.2_t2v_rapid_aio_v10 文生视频_1962875684572073985.json
name: wan2.2_t2v_rapid_aio_v10 文生视频_1962875684572073985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1962875684572073985.json
hash: 169c814be040ce76
coverage: 0.526316
learned_at: 2026-10-15 22:43:43
nodes: [LoadImage, VAEDecode, CLIPTextEncode, CLIPTextEncode, KSampler, ModelSamplingSD3, VHS_VideoCombine, Note, easy anythingIndexSwitch, WanImageToVideo, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 391519090391882, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.2_t2v_rapid_aio_v10 文生视频_1962875684572073985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1962875684572073985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Note`
- `easy anythingIndexSwitch`
- `WanImageToVideo`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `391519090391882`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **53%**（10/19）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`ModelSamplingSD3`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`WanImageToVideo`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ModelSamplingSD3、VHS_VideoCombine、WanImageToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
