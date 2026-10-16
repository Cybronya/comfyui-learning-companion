---
key: 视频生成/文生视频/文生视频Wan2.2-MegaAIO_1968902178624741378.json
name: 文生视频Wan2.2-MegaAIO_1968902178624741378.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968902178624741378.json
hash: bdbf40823daaaeec
coverage: 0.8125
learned_at: 2026-10-15 22:43:46
nodes: [VAEDecode, KSampler, Note, WanVaceToVideo, WanVideoVACEStartToEndFrame, LoadImage, LoadImage, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, INTConstant, CheckpointLoaderSimple, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 437030341248376, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生视频Wan2.2-MegaAIO_1968902178624741378.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968902178624741378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Note`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `INTConstant`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `437030341248376`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEDecode`、`KSampler`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`LoadImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`INTConstant`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、INTConstant、ModelSamplingSD3、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
