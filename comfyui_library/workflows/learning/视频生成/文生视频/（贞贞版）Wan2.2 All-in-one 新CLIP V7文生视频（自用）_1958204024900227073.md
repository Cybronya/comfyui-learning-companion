---
key: 视频生成/文生视频/（贞贞版）Wan2.2 All-in-one 新CLIP V7文生视频（自用）_1958204024900227073.json
name: （贞贞版）Wan2.2 All-in-one 新CLIP V7文生视频（自用）_1958204024900227073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（贞贞版）Wan2.2 All-in-one 新CLIP V7文生视频（自用）_1958204024900227073.json
hash: 2dab68f39440579f
coverage: 0.842105
learned_at: 2026-10-10 23:14:46
nodes: [CLIPTextEncode, ModelSamplingSD3, VHS_VideoCombine, SaveLatent, EmptyHunyuanLatentVideo, LoadImage, SaveImage, VAEDecode, JWInteger, Note, Note, Note, CLIPLoader, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPTextEncode, JWInteger, JWInteger, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-nsfw-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 644905946923337, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（贞贞版）Wan2.2 All-in-one 新CLIP V7文生视频（自用）_1958204024900227073.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（贞贞版）Wan2.2 All-in-one 新CLIP V7文生视频（自用）_1958204024900227073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `SaveLatent`
- `EmptyHunyuanLatentVideo`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-nsfw-v7.safetensors`
- `seed` = `644905946923337`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`SaveLatent`、`EmptyHunyuanLatentVideo`、`LoadImage`、`SaveImage`、`VAEDecode`、`JWInteger`、`CLIPLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`KSampler`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、SaveLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
