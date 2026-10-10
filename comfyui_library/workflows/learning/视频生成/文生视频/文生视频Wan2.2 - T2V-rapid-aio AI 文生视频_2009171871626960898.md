---
key: 视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json
name: 文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json
hash: fe58b7992343f7df
coverage: 1
learned_at: 2026-10-11 03:07:15
nodes: [ModelSamplingSD3, VAEDecode, CLIPTextEncode, KSampler, CheckpointLoaderSimple, EmptyHunyuanLatentVideo, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（8 个）：
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-t2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`CheckpointLoaderSimple`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyHunyuanLatentVideo、ModelSamplingSD3、VHS_VideoCombine、sd15-t2i-basic

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
