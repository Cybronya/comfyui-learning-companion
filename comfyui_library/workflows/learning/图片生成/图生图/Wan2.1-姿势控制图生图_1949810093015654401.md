---
key: 图片生成/图生图/Wan2.1-姿势控制图生图_1949810093015654401.json
name: Wan2.1-姿势控制图生图_1949810093015654401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1-姿势控制图生图_1949810093015654401.json
hash: 086364e810fbd49a
coverage: 0.964286
learned_at: 2026-10-23 11:27:48
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, TrimVideoLatent, WanVaceToVideo, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, LoraLoaderModelOnly, RepeatImageBatch, PreviewImage, GetImageRangeFromBatch, CLIPTextEncode, ImageConcanate, ImageConcanate, PDIMAGE_LongerSize, VHS_VideoCombine, VAEDecode, UNETLoader, DWPreprocessor, KSampler, LoadImage, LoadImage, JWInteger, SaveImage, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 20262209732131, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1-姿势控制图生图_1949810093015654401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1-姿势控制图生图_1949810093015654401.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `RepeatImageBatch`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `DWPreprocessor`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `SaveImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `20262209732131`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TrimVideoLatent`、`WanVaceToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`LoraLoaderModelOnly`、`RepeatImageBatch`、`GetImageRangeFromBatch`、`ImageConcanate`、`PDIMAGE_LongerSize`、`VHS_VideoCombine`、`VAEDecode`、`UNETLoader`、`DWPreprocessor`、`KSampler`、`LoadImage`、`JWInteger`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
