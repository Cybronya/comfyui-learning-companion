---
key: 图片生成/图生图/免费开源flux kontext dev 双图编辑 LLM自能扩写 一句修改图-StarAI_1938532876793372673.json
name: 免费开源flux kontext dev 双图编辑 LLM自能扩写 一句修改图-StarAI_1938532876793372673
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/免费开源flux kontext dev 双图编辑 LLM自能扩写 一句修改图-StarAI_1938532876793372673.json
hash: 063f2f880fca8d13
coverage: 0.903226
learned_at: 2026-10-23 12:13:07
nodes: [RH_LLMAPI_NODE, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, EmptyLatentImage, MathExpression|pysssss, VAELoader, DualCLIPLoader, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, FluxGuidance, VAEEncode, Note Plus (mtb), DifferentialDiffusion, UNETLoader, LoadImage, ImageConcanate, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RMBG, ImageResize+, easy showAnything, CR Text, KSampler, PreviewImage, FluxResolutionNode, VAEDecode, MarkdownNote, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 121777753648199, "steps": 20, "width": 1024}
---

# 图片生成/图生图/免费开源flux kontext dev 双图编辑 LLM自能扩写 一句修改图-StarAI_1938532876793372673.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/免费开源flux kontext dev 双图编辑 LLM自能扩写 一句修改图-StarAI_1938532876793372673.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `RH_LLMAPI_NODE`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `EmptyLatentImage` ★核心
- `MathExpression|pysssss`
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `Note Plus (mtb)`
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageConcanate`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RMBG`
- `ImageResize+`
- `easy showAnything`
- `CR Text`
- `KSampler` ★核心
- `PreviewImage`
- `FluxResolutionNode`
- `VAEDecode` ★核心
- `MarkdownNote`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `121777753648199`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`EmptyLatentImage`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`FluxGuidance`、`VAEEncode`、`Note Plus (mtb)`、`DifferentialDiffusion`、`UNETLoader`、`LoadImage`、`ImageConcanate`、`FluxKontextImageScale`、`LayerUtility: ImageScaleByAspectRatio V2`、`RMBG`、`ImageResize+`、`CR Text`、`KSampler`、`FluxResolutionNode`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
