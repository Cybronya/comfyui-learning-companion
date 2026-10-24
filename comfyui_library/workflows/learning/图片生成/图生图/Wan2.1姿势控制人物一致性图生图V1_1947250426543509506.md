---
key: 图片生成/图生图/Wan2.1姿势控制人物一致性图生图V1_1947250426543509506.json
name: Wan2.1姿势控制人物一致性图生图V1_1947250426543509506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1姿势控制人物一致性图生图V1_1947250426543509506.json
hash: d97ab1b889ca8e4e
coverage: 0.965517
learned_at: 2026-10-23 11:27:52
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, TrimVideoLatent, WanVaceToVideo, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, KSampler, VHS_VideoCombine, UNETLoader, UNETLoader, LoraLoaderModelOnly, PDIMAGE_LongerSize, SaveImage, GetImageRangeFromBatch, ImageConcanate, ImageConcanate, SaveImage, DWPreprocessor, LoadImage, LoadImage, JWInteger, RepeatImageBatch, PreviewImage, CLIPTextEncode, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 570690426790647, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1姿势控制人物一致性图生图V1_1947250426543509506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1姿势控制人物一致性图生图V1_1947250426543509506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PDIMAGE_LongerSize`
- `SaveImage`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `DWPreprocessor`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `RepeatImageBatch`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `570690426790647`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TrimVideoLatent`、`WanVaceToVideo`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`KSampler`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`PDIMAGE_LongerSize`、`SaveImage`、`GetImageRangeFromBatch`、`ImageConcanate`、`DWPreprocessor`、`LoadImage`、`JWInteger`、`RepeatImageBatch`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
