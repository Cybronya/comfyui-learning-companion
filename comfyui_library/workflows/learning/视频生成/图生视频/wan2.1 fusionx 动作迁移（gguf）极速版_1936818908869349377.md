---
key: 视频生成/图生视频/wan2.1 fusionx 动作迁移（gguf）极速版_1936818908869349377.json
name: wan2.1 fusionx 动作迁移（gguf）极速版_1936818908869349377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1 fusionx 动作迁移（gguf）极速版_1936818908869349377.json
hash: bf9dcc2e2a759309
coverage: 0.8
learned_at: 2026-10-15 22:30:27
nodes: [CLIPTextEncode, CLIPTextEncode, CR Text, LoadImage, WanVaceToVideo, CR Text, VAELoader, KSampler, ImageBlend, ModelSamplingSD3, VHS_LoadVideo, ImageResize+, CLIPLoader, PrimitiveInt, TrimVideoLatent, VHS_VideoInfoLoaded, Reroute, UNETLoader, VAEDecode, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VHS_VideoCombine, ImpactSwitch, ImageFromBatch, PreviewImage, PathchSageAttentionKJ, UnetLoaderGGUF, OpenposePreprocessor, DepthAnythingV2Preprocessor]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 878937543060606, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.1 fusionx 动作迁移（gguf）极速版_1936818908869349377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936818908869349377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`
- `LoadImage`
- `WanVaceToVideo`
- `CR Text`
- `VAELoader`
- `KSampler` ★核心
- `ImageBlend`
- `ModelSamplingSD3`
- `VHS_LoadVideo`
- `ImageResize+`
- `CLIPLoader`
- `PrimitiveInt`
- `TrimVideoLatent`
- `VHS_VideoInfoLoaded`
- `Reroute`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `ImageFromBatch`
- `PreviewImage`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `OpenposePreprocessor`
- `DepthAnythingV2Preprocessor`

## 关键参数

- `seed` = `878937543060606`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **80%**（24/30）

**有卡**：`CLIPTextEncode`、`CR Text`、`LoadImage`、`WanVaceToVideo`、`VAELoader`、`KSampler`、`ImageBlend`、`ModelSamplingSD3`、`VHS_LoadVideo`、`ImageResize+`、`CLIPLoader`、`TrimVideoLatent`、`VHS_VideoInfoLoaded`、`UNETLoader`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`ImageFromBatch`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`OpenposePreprocessor`、`DepthAnythingV2Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
