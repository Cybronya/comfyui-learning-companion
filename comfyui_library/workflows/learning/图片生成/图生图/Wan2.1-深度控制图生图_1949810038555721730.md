---
key: 图片生成/图生图/Wan2.1-深度控制图生图_1949810038555721730.json
name: Wan2.1-深度控制图生图_1949810038555721730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1-深度控制图生图_1949810038555721730.json
hash: 32a938834fc6abda
coverage: 0.964286
learned_at: 2026-10-23 11:27:49
nodes: [CLIPLoader, VAELoader, WanVaceToVideo, MathExpression|pysssss, PreviewImage, KSampler, ModelSamplingSD3, GetImageRangeFromBatch, ImageConcanate, RepeatImageBatch, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, CLIPTextEncode, CLIPTextEncode, TrimVideoLatent, VAEDecode, ImageConcanate, SaveImage, PathchSageAttentionKJ, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, VHS_VideoCombine, JWInteger, LoadImage, LoadImage, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 624086624235687, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1-深度控制图生图_1949810038555721730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1-深度控制图生图_1949810038555721730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `VAELoader`
- `WanVaceToVideo`
- `MathExpression|pysssss`
- `PreviewImage`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `RepeatImageBatch`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `624086624235687`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CLIPLoader`、`VAELoader`、`WanVaceToVideo`、`MathExpression|pysssss`、`KSampler`、`ModelSamplingSD3`、`GetImageRangeFromBatch`、`ImageConcanate`、`RepeatImageBatch`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`CLIPTextEncode`、`TrimVideoLatent`、`VAEDecode`、`SaveImage`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`VHS_VideoCombine`、`JWInteger`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
