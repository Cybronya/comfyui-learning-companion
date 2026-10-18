---
key: 视频生成/文生视频/（贞贞版）Wan2.2 All-in-one V9文生视频高动态极速版V1_1958907032336281602.json
name: （贞贞版）Wan2.2 All-in-one V9文生视频高动态极速版V1_1958907032336281602.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（贞贞版）Wan2.2 All-in-one V9文生视频高动态极速版V1_1958907032336281602.json
hash: 5142c10a0048f1a6
coverage: 0.823529
learned_at: 2026-10-15 22:43:42
nodes: [EmptyHunyuanLatentVideo, JWInteger, JWInteger, Note, Note, Note, ModelSamplingSD3, VAEDecode, JWInteger, KSampler, VHS_VideoCombine, CheckpointLoaderSimple, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, ImageFromBatch+, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-nsfw-v7.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 991781648296818, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（贞贞版）Wan2.2 All-in-one V9文生视频高动态极速版V1_1958907032336281602.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958907032336281602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `JWInteger`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ImageFromBatch+`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `991781648296818`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-nsfw-v7.safetensors`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`EmptyHunyuanLatentVideo`、`JWInteger`、`ModelSamplingSD3`、`VAEDecode`、`KSampler`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、EmptyHunyuanLatentVideo、ModelSamplingSD3、PathchSageAttentionKJ

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
