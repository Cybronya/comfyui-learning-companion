---
key: 平台全量/Wan2.2-Rapid-AIO洗图工作流_1990940315110547457.json
name: Wan2.2-Rapid-AIO洗图工作流_1990940315110547457
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Rapid-AIO洗图工作流_1990940315110547457.json
hash: b1cb1f6b142e7cd7
coverage: 1
learned_at: 2026-11-14 01:05:58
nodes: [CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VAEDecode, SaveImage, ModelPatchTorchSettings, VAEEncode, CheckpointLoaderSimple, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, PathchSageAttentionKJ]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 0.3, "sampler_name": "euler", "scheduler": "beta", "seed": 535045281428119, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-Rapid-AIO洗图工作流_1990940315110547457.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Rapid-AIO洗图工作流_1990940315110547457.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `ModelPatchTorchSettings`
- `VAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `PathchSageAttentionKJ`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`
- `seed` = `535045281428119`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.3`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`ModelPatchTorchSettings`、`VAEEncode`、`CheckpointLoaderSimple`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`PathchSageAttentionKJ`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、SaveImage、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
