---
key: 视频生成/文生视频/Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266.json
name: Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266.json
hash: 1070f44390311d76
coverage: 0.823529
learned_at: 2026-10-10 23:06:39
nodes: [CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, KSampler, VHS_VideoCombine, SaveLatent, EmptyHunyuanLatentVideo, CheckpointLoaderSimple, LoadImage, SaveImage, VAEDecode, JWInteger, JWInteger, JWInteger, Note, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-nsfw-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 All-in-one V7文生视频（自用）_1955969425952395266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `SaveLatent`
- `EmptyHunyuanLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-nsfw-v7.safetensors`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`VHS_VideoCombine`、`SaveLatent`、`EmptyHunyuanLatentVideo`、`CheckpointLoaderSimple`、`LoadImage`、`SaveImage`、`VAEDecode`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveLatent、EmptyHunyuanLatentVideo、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
