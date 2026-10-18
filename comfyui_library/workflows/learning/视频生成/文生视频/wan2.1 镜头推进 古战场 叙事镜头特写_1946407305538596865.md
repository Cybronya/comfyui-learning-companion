---
key: 视频生成/文生视频/wan2.1 镜头推进 古战场 叙事镜头特写_1946407305538596865.json
name: wan2.1 镜头推进 古战场 叙事镜头特写_1946407305538596865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.1 镜头推进 古战场 叙事镜头特写_1946407305538596865.json
hash: 60b24067cf3b79e1
coverage: 0.952381
learned_at: 2026-10-15 22:43:31
nodes: [ModelPatchTorchSettings, VAEDecode, KSampler, ModelSamplingSD3, LoraLoaderModelOnly, VAELoader, CLIPVisionLoader, ImageScale, ttN concat, ShowText|pysssss, CLIPVisionEncode, VHS_VideoCombine, LoraLoaderModelOnly, PathchSageAttentionKJ, LoadImage, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, WD14Tagger|pysssss, WanImageToVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 449481665052565, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/wan2.1 镜头推进 古战场 叙事镜头特写_1946407305538596865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1946407305538596865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `ModelPatchTorchSettings`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `ImageScale`
- `ttN concat`
- `ShowText|pysssss`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WD14Tagger|pysssss`
- `WanImageToVideo`

## 关键参数

- `seed` = `449481665052565`
- `steps` = `4`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ModelPatchTorchSettings`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPVisionLoader`、`ImageScale`、`ttN concat`、`CLIPVisionEncode`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`WD14Tagger|pysssss`、`WanImageToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
