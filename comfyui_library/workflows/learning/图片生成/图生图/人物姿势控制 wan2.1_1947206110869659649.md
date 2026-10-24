---
key: 图片生成/图生图/人物姿势控制 wan2.1_1947206110869659649.json
name: 人物姿势控制 wan2.1_1947206110869659649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物姿势控制 wan2.1_1947206110869659649.json
hash: 14fc9b14b207461d
coverage: 0.869565
learned_at: 2026-10-23 12:10:16
nodes: [CLIPLoader, CLIPTextEncode, KSampler, TrimVideoLatent, VAELoader, VAEDecode, GetImageRangeFromBatch, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, Note, WanVaceToVideo, ImageResizeKJv2, ImageResizeKJv2, AIO_Preprocessor, RepeatImageBatch, LoadImage, LoadImage, SaveImage, JjkText, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 116544489403452, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人物姿势控制 wan2.1_1947206110869659649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物姿势控制 wan2.1_1947206110869659649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `Note`
- `WanVaceToVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `RepeatImageBatch`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `JjkText`
- `Note`

## 关键参数

- `seed` = `116544489403452`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`TrimVideoLatent`、`VAELoader`、`VAEDecode`、`GetImageRangeFromBatch`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`WanVaceToVideo`、`ImageResizeKJv2`、`AIO_Preprocessor`、`RepeatImageBatch`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
