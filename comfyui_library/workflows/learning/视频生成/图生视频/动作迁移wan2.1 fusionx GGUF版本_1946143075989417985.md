---
key: 视频生成/图生视频/动作迁移wan2.1 fusionx GGUF版本_1946143075989417985.json
name: 动作迁移wan2.1 fusionx GGUF版本_1946143075989417985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移wan2.1 fusionx GGUF版本_1946143075989417985.json
hash: ab18c8f44b6cf8aa
coverage: 0.83871
learned_at: 2026-10-15 22:30:44
nodes: [PrimitiveInt, ImpactSwitch, WanVaceToVideo, PreviewImage, KSampler, TrimVideoLatent, CLIPTextEncode, CLIPTextEncode, VAELoader, UnetLoaderGGUF, CLIPLoader, VHS_LoadVideo, VHS_VideoInfoLoaded, PrimitiveInt, CR Text, ModelSamplingSD3, DWPreprocessor, ImageFromBatch, PathchSageAttentionKJ, UNETLoader, CR Text Concatenate, WD14Tagger|pysssss, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, DepthAnythingV2Preprocessor, ImageBlend, CR Text, Note, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 878937543060606, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/动作迁移wan2.1 fusionx GGUF版本_1946143075989417985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1946143075989417985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `PrimitiveInt`
- `ImpactSwitch`
- `WanVaceToVideo`
- `PreviewImage`
- `KSampler` ★核心
- `TrimVideoLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `PrimitiveInt`
- `CR Text`
- `ModelSamplingSD3`
- `DWPreprocessor`
- `ImageFromBatch`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `CR Text Concatenate`
- `WD14Tagger|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `DepthAnythingV2Preprocessor`
- `ImageBlend`
- `CR Text`
- `Note`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `878937543060606`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`WanVaceToVideo`、`KSampler`、`TrimVideoLatent`、`CLIPTextEncode`、`VAELoader`、`UnetLoaderGGUF`、`CLIPLoader`、`VHS_LoadVideo`、`VHS_VideoInfoLoaded`、`CR Text`、`ModelSamplingSD3`、`DWPreprocessor`、`ImageFromBatch`、`PathchSageAttentionKJ`、`UNETLoader`、`CR Text Concatenate`、`WD14Tagger|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`DepthAnythingV2Preprocessor`、`ImageBlend`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
