---
key: 图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514.json
name: 去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514.json
hash: a813ff7a2c1f5e3e
coverage: 0.673077
learned_at: 2026-10-21 00:50:49
nodes: [Image Comparer (rgthree), Note, Note, Note, Note, Note, Note, VAELoader, LayerColor: Color of Shadow & Highlight, LayerColor: Color of Shadow & Highlight, SaveImage, PrimitiveFloat, CLIPLoader, CLIPTextEncode, PrimitiveFloat, Int, UNETLoader_Any, KSampler, easy imageColorMatch, ImageResize+, LoadImage, SaveImage, PreviewImage, PreviewImage, PreviewImage, SaveImage, PreviewImage, SaveImage, easy boolean, Int, PrimitiveFloat, RHHiddenNodes, easy imageColorMatch, easy ifElse, RHHiddenNodes, Int, Int, PrimitiveFloat, easy cleanGpuUsed, VAEEncode, CLIPTextEncode, VAEDecode, KuwaharaBlur, VAEDecode, easy cleanGpuUsed, LayerColor: RGB, KSamplerAdvanced, ShowText|pysssss, AILab_QwenVL, CR Text, GroupExecutor, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/去AI感，真实感放大_Krea重塑自然美学_2.0_2096400513066688514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `VAELoader`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: Color of Shadow & Highlight`
- `SaveImage`
- `PrimitiveFloat`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `Int`
- `UNETLoader_Any` ★核心
- `KSampler` ★核心
- `easy imageColorMatch`
- `ImageResize+`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `easy boolean`
- `Int`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `easy imageColorMatch`
- `easy ifElse`
- `RHHiddenNodes`
- `Int`
- `Int`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KuwaharaBlur`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LayerColor: RGB`
- `KSamplerAdvanced` ★核心
- `ShowText|pysssss`
- `AILab_QwenVL`
- `CR Text`
- `GroupExecutor`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **67%**（35/52）

**有卡**：`VAELoader`、`LayerColor: Color of Shadow & Highlight`、`SaveImage`、`CLIPLoader`、`CLIPTextEncode`、`Int`、`UNETLoader_Any`、`KSampler`、`easy imageColorMatch`、`ImageResize+`、`LoadImage`、`easy boolean`、`RHHiddenNodes`、`easy cleanGpuUsed`、`VAEEncode`、`VAEDecode`、`KuwaharaBlur`、`LayerColor: RGB`、`KSamplerAdvanced`、`AILab_QwenVL`、`CR Text`、`GroupExecutor`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
