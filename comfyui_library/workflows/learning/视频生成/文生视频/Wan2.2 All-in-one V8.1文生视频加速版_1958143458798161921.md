---
key: 视频生成/文生视频/Wan2.2 All-in-one V8.1文生视频加速版_1958143458798161921.json
name: Wan2.2 All-in-one V8.1文生视频加速版_1958143458798161921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 All-in-one V8.1文生视频加速版_1958143458798161921.json
hash: 133aef1b3bc9b834
coverage: 0.8
learned_at: 2026-10-15 22:43:42
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, JWInteger, JWInteger, Note, Note, Note, CLIPTextEncode, ModelSamplingSD3, VAEDecode, JWInteger, CheckpointLoaderSimple, KSampler, VHS_VideoCombine, ImageFromBatch+]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v8.1.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1098628294045191, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 All-in-one V8.1文生视频加速版_1958143458798161921.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958143458798161921.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（15 个）：
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `ImageFromBatch+`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v8.1.safetensors`
- `seed` = `1098628294045191`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`JWInteger`、`ModelSamplingSD3`、`VAEDecode`、`CheckpointLoaderSimple`、`KSampler`、`VHS_VideoCombine`、`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyHunyuanLatentVideo、ModelSamplingSD3、VHS_VideoCombine、JWInteger

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
