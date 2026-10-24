---
key: 图片生成/图生图/各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577.json
name: 各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577.json
hash: 17bf1aa537806a52
coverage: 0.777778
learned_at: 2026-10-23 12:36:20
nodes: [CLIPTextEncode, ReferenceLatent, VAEDecodeTiled, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinOutputExtractor_EditUtils, KSampler, LoraLoaderModelOnly, UNETLoader, Flux2KleinConfigPreparer_EditUtils, CLIPLoader, VAELoader, Flux2KleinModelConfig_EditUtils, LoraLoaderModelOnly, PrimitiveStringMultiline, PrimitiveStringMultiline, Int, Float, Note, string_util_StrConcat, CropWithPadInfo_EditUtils, SaveImage, LoadImage, PrimitiveInt, AdaptiveLongestEdge_EditUtils, PrimitiveInt, PreviewImage]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 104092162224398, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/各种动漫风格转真实人物（Flux2 Klein 9B Anything2Real A ）_2018858828191768577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEDecodeTiled` ★核心
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Flux2KleinConfigPreparer_EditUtils`
- `CLIPLoader`
- `VAELoader`
- `Flux2KleinModelConfig_EditUtils`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Int`
- `Float`
- `Note`
- `string_util_StrConcat`
- `CropWithPadInfo_EditUtils`
- `SaveImage`
- `LoadImage`
- `PrimitiveInt`
- `AdaptiveLongestEdge_EditUtils`
- `PrimitiveInt`
- `PreviewImage`

## 关键参数

- `seed` = `104092162224398`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`CLIPTextEncode`、`ReferenceLatent`、`VAEDecodeTiled`、`CropWithPadInfo_EditUtils`、`EditTextEncode_EditUtils`、`Flux2KleinOutputExtractor_EditUtils`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`Flux2KleinConfigPreparer_EditUtils`、`CLIPLoader`、`VAELoader`、`Flux2KleinModelConfig_EditUtils`、`Int`、`Float`、`string_util_StrConcat`、`SaveImage`、`LoadImage`、`AdaptiveLongestEdge_EditUtils`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
