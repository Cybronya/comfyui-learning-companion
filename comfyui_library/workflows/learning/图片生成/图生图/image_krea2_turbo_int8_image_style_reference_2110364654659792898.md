---
key: 图片生成/图生图/image_krea2_turbo_int8_image_style_reference_2110364654659792898.json
name: image_krea2_turbo_int8_image_style_reference_2110364654659792898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_krea2_turbo_int8_image_style_reference_2110364654659792898.json
hash: 296d86bd385f9a18
coverage: 0.78125
learned_at: 2026-10-23 11:37:53
nodes: [ConditioningZeroOut, PrimitiveStringMultiline, ComfySwitchNode, CFGGuider, KSamplerSelect, BasicScheduler, VAEDecode, ModelSamplingFlux, MarkdownNote, GetImageSize, SaveImage, PreviewAny, TextGenerate, PrimitiveStringMultiline, PrimitiveBoolean, StringConcatenate, VAELoader, CLIPLoader, TextEncodeQwenImageEditPlus, FluxKontextMultiReferenceLatentMethod, EmptyLatentImage, LoadImage, LoraLoaderModelOnly, UNETLoader, PrimitiveBoolean, UNETLoader, ComfySwitchNode, EmptyLatentImage, ResolutionSelector, SamplerCustomAdvanced, RandomNoise, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/image_krea2_turbo_int8_image_style_reference_2110364654659792898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_krea2_turbo_int8_image_style_reference_2110364654659792898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ConditioningZeroOut`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `ModelSamplingFlux`
- `MarkdownNote`
- `GetImageSize`
- `SaveImage`
- `PreviewAny`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `StringConcatenate`
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `PrimitiveInt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`ConditioningZeroOut`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`ModelSamplingFlux`、`GetImageSize`、`SaveImage`、`TextGenerate`、`PrimitiveBoolean`、`StringConcatenate`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`FluxKontextMultiReferenceLatentMethod`、`EmptyLatentImage`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`ResolutionSelector`、`SamplerCustomAdvanced`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector
