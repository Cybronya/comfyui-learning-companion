---
key: 图片生成/图生图/Wan2.1一致性扩图图生图V1_1947268029098905601.json
name: Wan2.1一致性扩图图生图V1_1947268029098905601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1一致性扩图图生图V1_1947268029098905601.json
hash: 0fc6bd16f29364da
coverage: 0.861111
learned_at: 2026-10-23 11:27:50
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, TrimVideoLatent, WanVaceToVideo, SaveImage, VAEDecode, MathExpression|pysssss, KSampler, VHS_VideoCombine, UNETLoader, UNETLoader, LoraLoaderModelOnly, PDIMAGE_LongerSize, SaveImage, GetImageRangeFromBatch, CR Prompt Text, RepeatImageBatch, PreviewImage, LoadImage, ImageConcanate, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, DF_Get_image_size, JWInteger, JWInteger, ImagePadKJ, JWInteger, JWInteger, Note, Note, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 715686222289396, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.1一致性扩图图生图V1_1947268029098905601.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1一致性扩图图生图V1_1947268029098905601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
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
- `MathExpression|pysssss`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PDIMAGE_LongerSize`
- `SaveImage`
- `GetImageRangeFromBatch`
- `CR Prompt Text`
- `RepeatImageBatch`
- `PreviewImage`
- `LoadImage`
- `ImageConcanate`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DF_Get_image_size`
- `JWInteger`
- `JWInteger`
- `ImagePadKJ`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`

## 关键参数

- `seed` = `715686222289396`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TrimVideoLatent`、`WanVaceToVideo`、`SaveImage`、`VAEDecode`、`MathExpression|pysssss`、`KSampler`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`PDIMAGE_LongerSize`、`GetImageRangeFromBatch`、`CR Prompt Text`、`RepeatImageBatch`、`LoadImage`、`ImageConcanate`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Get_image_size`、`ImagePadKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
