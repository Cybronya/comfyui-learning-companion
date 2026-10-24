---
key: 图片生成/图生图/kontext nunchaku Dev 双图编辑极速版- LLM提示词智能扩写-StarAI_1939670254471843842.json
name: kontext nunchaku Dev 双图编辑极速版- LLM提示词智能扩写-StarAI_1939670254471843842
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext nunchaku Dev 双图编辑极速版- LLM提示词智能扩写-StarAI_1939670254471843842.json
hash: e16f534ab073f55a
coverage: 0.903226
learned_at: 2026-10-23 11:38:46
nodes: [RH_LLMAPI_NODE, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, EmptyLatentImage, MathExpression|pysssss, VAELoader, DualCLIPLoader, ConditioningZeroOut, ReferenceLatent, FluxGuidance, VAEEncode, Note Plus (mtb), DifferentialDiffusion, ImageConcanate, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, CLIPTextEncode, LoadImage, PreviewImage, LoadImage, NunchakuFluxDiTLoader, RMBG, CR Text, FluxResolutionNode, VAEDecode, KSampler, SaveImage, MarkdownNote, easy showAnything]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 504636229302546, "steps": 20, "width": 1024}
---

# 图片生成/图生图/kontext nunchaku Dev 双图编辑极速版- LLM提示词智能扩写-StarAI_1939670254471843842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext nunchaku Dev 双图编辑极速版- LLM提示词智能扩写-StarAI_1939670254471843842.json`

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
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `VAEEncode` ★核心
- `Note Plus (mtb)`
- `DifferentialDiffusion`
- `ImageConcanate`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `RMBG`
- `CR Text`
- `FluxResolutionNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `MarkdownNote`
- `easy showAnything`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `504636229302546`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`EmptyLatentImage`、`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`ReferenceLatent`、`FluxGuidance`、`VAEEncode`、`Note Plus (mtb)`、`DifferentialDiffusion`、`ImageConcanate`、`FluxKontextImageScale`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`CLIPTextEncode`、`LoadImage`、`NunchakuFluxDiTLoader`、`RMBG`、`CR Text`、`FluxResolutionNode`、`VAEDecode`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
