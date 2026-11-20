---
key: 平台全量/qwen-image-2.1——开源最强洗图完美版_2105964504642314241.json
name: qwen-image-2.1——开源最强洗图完美版_2105964504642314241
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image-2.1——开源最强洗图完美版_2105964504642314241.json
hash: 8bf55364dd4bcb46
coverage: 0.833333
learned_at: 2026-11-14 01:16:16
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, SaveImage, CLIPTextEncode, VAEEncode, LayerUtility: PurgeVRAM, UNETLoader, CLIPLoader, ShowText|pysssss, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, MarkdownNote, ImpactInt, TextInput_, JoinStrings, easy showAnything, Qwen3_VQA, MarkdownNote, VAEDecode, LayerUtility: PurgeVRAM, KSampler, LoadImage, ImageScaleBy, SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, Float]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.9500000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 894804216308393, "steps": 40}
---

# 平台全量/qwen-image-2.1——开源最强洗图完美版_2105964504642314241.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image-2.1——开源最强洗图完美版_2105964504642314241.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ShowText|pysssss`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `MarkdownNote`
- `ImpactInt`
- `TextInput_`
- `JoinStrings`
- `easy showAnything`
- `Qwen3_VQA`
- `MarkdownNote`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `LoadImage`
- `ImageScaleBy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Float`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `894804216308393`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.9500000000000002`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM`、`SaveImage`、`CLIPTextEncode`、`VAEEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`ImpactInt`、`TextInput_`、`JoinStrings`、`Qwen3_VQA`、`VAEDecode`、`KSampler`、`LoadImage`、`ImageScaleBy`、`LoraLoaderModelOnly`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
