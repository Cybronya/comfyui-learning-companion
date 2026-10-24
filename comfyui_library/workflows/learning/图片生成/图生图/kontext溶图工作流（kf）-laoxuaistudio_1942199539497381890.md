---
key: 图片生成/图生图/kontext溶图工作流（kf）-laoxuaistudio_1942199539497381890.json
name: kontext溶图工作流（kf）-laoxuaistudio_1942199539497381890
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext溶图工作流（kf）-laoxuaistudio_1942199539497381890.json
hash: 36f21252283c7f40
coverage: 0.765957
learned_at: 2026-10-23 11:39:48
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, CR Prompt Text, ShowText|pysssss, CR Prompt Text, MarkdownNote, UNETLoader, ShowText|pysssss, Reroute, DualCLIPLoader, VAELoader, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, FluxGuidance, KSampler, VAEDecode, Anything Everywhere3, Reroute, PreviewBridge, CLIPTextEncode, VAEDecode, Mask Fill Holes, VAEEncode, CR Text Concatenate, FluxKontextImageScale, ImageAndMaskPreview, EmptySD3LatentImage, KSampler, CR Text Concatenate, VAEEncode, ConditioningZeroOut, ReferenceLatent, FluxGuidance, GetImageSize, CompositorConfig3, InspyrenetRembgAdvanced, PreviewImage, SaveImage, NunchakuFluxDiTLoader, LoadImage, LoadImage, ChinesePrompt_Mix, ChinesePrompt_Mix, PreviewImage, Compositor3]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 838148603581264, "steps": 20}
---

# 图片生成/图生图/kontext溶图工作流（kf）-laoxuaistudio_1942199539497381890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext溶图工作流（kf）-laoxuaistudio_1942199539497381890.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CR Prompt Text`
- `ShowText|pysssss`
- `CR Prompt Text`
- `MarkdownNote`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `Reroute`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere3`
- `Reroute`
- `PreviewBridge`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Mask Fill Holes`
- `VAEEncode` ★核心
- `CR Text Concatenate`
- `FluxKontextImageScale`
- `ImageAndMaskPreview`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `CR Text Concatenate`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `GetImageSize`
- `CompositorConfig3`
- `InspyrenetRembgAdvanced`
- `PreviewImage`
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `LoadImage`
- `ChinesePrompt_Mix`
- `ChinesePrompt_Mix`
- `PreviewImage`
- `Compositor3`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `838148603581264`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`CR Prompt Text`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`FluxGuidance`、`KSampler`、`VAEDecode`、`PreviewBridge`、`Mask Fill Holes`、`VAEEncode`、`CR Text Concatenate`、`FluxKontextImageScale`、`ImageAndMaskPreview`、`EmptySD3LatentImage`、`GetImageSize`、`CompositorConfig3`、`InspyrenetRembgAdvanced`、`SaveImage`、`NunchakuFluxDiTLoader`、`LoadImage`、`ChinesePrompt_Mix`、`Compositor3`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
