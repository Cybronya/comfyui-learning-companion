---
key: 视频生成/图生视频/Hunyuan 1.5 720P 图生视频加速版_1993306482808733698.json
name: Hunyuan 1.5 720P 图生视频加速版_1993306482808733698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1993306482808733698.json
hash: 9e375efd88f04bab
coverage: 1
learned_at: 2026-10-15 22:33:18
nodes: [DualCLIPLoader, CLIPVisionEncode, CLIPTextEncode, CLIPVisionLoader, VAELoader, VAEDecode, ModelSamplingSD3, HunyuanVideo15ImageToVideo, KSampler, VAEDecodeTiled, LoadImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, ImageResizeKJv2, CreateVideo, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 376293642524360, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Hunyuan 1.5 720P 图生视频加速版_1993306482808733698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993306482808733698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `DualCLIPLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `HunyuanVideo15ImageToVideo`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `seed` = `376293642524360`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`DualCLIPLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`CLIPVisionLoader`、`VAELoader`、`VAEDecode`、`ModelSamplingSD3`、`HunyuanVideo15ImageToVideo`、`KSampler`、`VAEDecodeTiled`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
