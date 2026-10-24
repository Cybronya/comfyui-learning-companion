---
key: 图片生成/图生图/kontext nunchaku Dev 三图编辑极速版- LLM提示词智能扩写-StarAI_1939681464386818050.json
name: kontext nunchaku Dev 三图编辑极速版- LLM提示词智能扩写-StarAI_1939681464386818050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext nunchaku Dev 三图编辑极速版- LLM提示词智能扩写-StarAI_1939681464386818050.json
hash: 042198368ab7314c
coverage: 0.888889
learned_at: 2026-10-23 11:38:46
nodes: [Note Plus (mtb), VAEEncode, ReferenceLatent, EmptyLatentImage, ConditioningZeroOut, KSampler, VAEDecode, FluxGuidance, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SaveImage, FluxResolutionNode, PreviewImage, RMBG, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, RMBG, LoadImage, LoadImage, MarkdownNote, RH_LLMAPI_NODE, CLIPTextEncode, Text, NunchakuFluxDiTLoader, DualCLIPLoader, VAELoader, ModelSamplingFlux, LoadImage, ImageConcanate, ImageConcanate, PreviewImage, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 344133113001658, "steps": 20, "width": 1024}
---

# 图片生成/图生图/kontext nunchaku Dev 三图编辑极速版- LLM提示词智能扩写-StarAI_1939681464386818050.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext nunchaku Dev 三图编辑极速版- LLM提示词智能扩写-StarAI_1939681464386818050.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `Note Plus (mtb)`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SaveImage`
- `FluxResolutionNode`
- `PreviewImage`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `Text`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingFlux`
- `LoadImage`
- `ImageConcanate`
- `ImageConcanate`
- `PreviewImage`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `344133113001658`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`Note Plus (mtb)`、`VAEEncode`、`ReferenceLatent`、`EmptyLatentImage`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`FluxGuidance`、`MathExpression|pysssss`、`SaveImage`、`FluxResolutionNode`、`RMBG`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`LoadImage`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`Text`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`VAELoader`、`ModelSamplingFlux`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
