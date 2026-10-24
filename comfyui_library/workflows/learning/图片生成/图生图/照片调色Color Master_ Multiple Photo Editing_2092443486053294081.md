---
key: 图片生成/图生图/照片调色Color Master_ Multiple Photo Editing_2092443486053294081.json
name: 照片调色Color Master_ Multiple Photo Editing_2092443486053294081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/照片调色Color Master_ Multiple Photo Editing_2092443486053294081.json
hash: e217c3f5da3bbcf9
coverage: 0.854167
learned_at: 2026-10-23 13:14:08
nodes: [CR Text, CR Text, CR Text, UNETLoader, CLIPLoader, ReferenceLatent, CLIPTextEncode, VAEEncode, KSamplerAdvanced, VAEDecode, ReferenceLatent, PreviewImage, KSamplerAdvanced, ConditioningZeroOut, VAELoader, Anything Everywhere3, LoraLoaderModelOnly, Image Comparer (rgthree), VAEDecode, SaveImage, easy imageConcat, SaveImage, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, ImageResizeKJv2, LatentBlend, Float, Note, ImpactSwitch, CR Text, LoadImage, Int, Note, Note]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/照片调色Color Master_ Multiple Photo Editing_2092443486053294081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/照片调色Color Master_ Multiple Photo Editing_2092443486053294081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `CR Text`
- `CR Text`
- `CR Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `easy imageConcat`
- `SaveImage`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImageResizeKJv2`
- `LatentBlend`
- `Float`
- `Note`
- `ImpactSwitch`
- `CR Text`
- `LoadImage`
- `Int`
- `Note`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（41/48）

**有卡**：`CR Text`、`UNETLoader`、`CLIPLoader`、`ReferenceLatent`、`CLIPTextEncode`、`VAEEncode`、`KSamplerAdvanced`、`VAEDecode`、`ConditioningZeroOut`、`VAELoader`、`LoraLoaderModelOnly`、`SaveImage`、`easy imageConcat`、`ImageResizeKJv2`、`LatentBlend`、`Float`、`LoadImage`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
