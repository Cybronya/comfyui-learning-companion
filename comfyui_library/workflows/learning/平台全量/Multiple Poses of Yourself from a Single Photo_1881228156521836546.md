---
key: 平台全量/Multiple Poses of Yourself from a Single Photo_1881228156521836546.json
name: Multiple Poses of Yourself from a Single Photo_1881228156521836546
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Multiple Poses of Yourself from a Single Photo_1881228156521836546.json
hash: 103b33df1bdb4978
coverage: 0.866667
learned_at: 2026-11-14 00:46:59
nodes: [PulidEvaClipLoader, PulidInsightFaceLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, Anything Everywhere3, CLIPTextEncode, PulidModelLoader, CheckpointLoaderSimple, VAEDecode, SaveImage, Prompts Everywhere, ApplyPulidAdvanced, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.5, "checkpoint": "realvisxlV50_v50LightningBakedvae.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 1101368315710399, "steps": 5, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Multiple Poses of Yourself from a Single Photo_1881228156521836546.json

> 来源文件 `comfyui_library/workflows/平台全量/Multiple Poses of Yourself from a Single Photo_1881228156521836546.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `PulidModelLoader`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Prompts Everywhere`
- `ApplyPulidAdvanced`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1101368315710399`
- `steps` = `5`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `realvisxlV50_v50LightningBakedvae.safetensors`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`PulidEvaClipLoader`、`PulidInsightFaceLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`PulidModelLoader`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`Prompts Everywhere`、`ApplyPulidAdvanced`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、Prompts Everywhere、PulidEvaClipLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
