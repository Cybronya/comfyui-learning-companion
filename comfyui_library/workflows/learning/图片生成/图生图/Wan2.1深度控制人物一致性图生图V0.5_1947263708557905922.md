---
key: 图片生成/图生图/Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922.json
name: Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922.json
hash: 4b65d6d2d982e214
coverage: 0.966667
learned_at: 2026-10-23 11:27:52
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, TrimVideoLatent, WanVaceToVideo, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, RepeatImageBatch, MathExpression|pysssss, KSampler, VHS_VideoCombine, UNETLoader, UNETLoader, JWInteger, LoraLoaderModelOnly, PDIMAGE_LongerSize, SaveImage, GetImageRangeFromBatch, CR Prompt Text, DownloadAndLoadDepthAnythingV2Model, LoadImage, PreviewImage, LoadImage, DepthAnything_V2, ImageConcanate, ImageConcanate]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 522401477629491, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1深度控制人物一致性图生图V0.5_1947263708557905922.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatImageBatch`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `JWInteger`
- `LoraLoaderModelOnly` ★核心
- `PDIMAGE_LongerSize`
- `SaveImage`
- `GetImageRangeFromBatch`
- `CR Prompt Text`
- `DownloadAndLoadDepthAnythingV2Model`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `DepthAnything_V2`
- `ImageConcanate`
- `ImageConcanate`

## 关键参数

- `seed` = `522401477629491`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TrimVideoLatent`、`WanVaceToVideo`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatImageBatch`、`MathExpression|pysssss`、`KSampler`、`VHS_VideoCombine`、`UNETLoader`、`JWInteger`、`LoraLoaderModelOnly`、`PDIMAGE_LongerSize`、`GetImageRangeFromBatch`、`CR Prompt Text`、`DownloadAndLoadDepthAnythingV2Model`、`LoadImage`、`DepthAnything_V2`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
