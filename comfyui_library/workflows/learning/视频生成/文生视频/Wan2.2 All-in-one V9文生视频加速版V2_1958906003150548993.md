---
key: 视频生成/文生视频/Wan2.2 All-in-one V9文生视频加速版V2_1958906003150548993.json
name: Wan2.2 All-in-one V9文生视频加速版V2_1958906003150548993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 All-in-one V9文生视频加速版V2_1958906003150548993.json
hash: f9fb8f2e51dc6f92
coverage: 0.8125
learned_at: 2026-10-15 22:43:42
nodes: [EmptyHunyuanLatentVideo, Note, Note, Note, ModelSamplingSD3, CLIPTextEncode, PathchSageAttentionKJ, CLIPTextEncode, VAEDecode, VHS_VideoCombine, ImageFromBatch+, JWInteger, JWInteger, JWInteger, CheckpointLoaderSimple, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v9.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 45940815864333, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 All-in-one V9文生视频加速版V2_1958906003150548993.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958906003150548993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `EmptyHunyuanLatentVideo`
- `Note`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v9.safetensors`
- `seed` = `45940815864333`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`VAEDecode`、`VHS_VideoCombine`、`ImageFromBatch+`、`JWInteger`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyHunyuanLatentVideo、ModelSamplingSD3、PathchSageAttentionKJ、VHS_VideoCombine

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
