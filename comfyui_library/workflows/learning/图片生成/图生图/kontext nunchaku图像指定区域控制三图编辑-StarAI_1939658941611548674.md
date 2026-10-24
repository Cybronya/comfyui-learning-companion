---
key: 图片生成/图生图/kontext nunchaku图像指定区域控制三图编辑-StarAI_1939658941611548674.json
name: kontext nunchaku图像指定区域控制三图编辑-StarAI_1939658941611548674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext nunchaku图像指定区域控制三图编辑-StarAI_1939658941611548674.json
hash: 1294ba6e2062c502
coverage: 0.90625
learned_at: 2026-10-23 11:38:47
nodes: [easy imageRemBg, LoadImage, ImageScaleToMegapixels, LoadImage, ImageScaleToMegapixels, easy imageRemBg, LoadImage, CompositorConfig3, ImageScaleToMegapixels, ShowText|pysssss, DualCLIPLoader, VAELoader, RH_LLMAPI_NODE, CLIPTextEncode, ImageScaleToMegapixels, FluxKontextImageScale, ReferenceLatent, VAEEncode, FluxGuidance, SaveImage, ImageConcanate, VAEDecode, KSampler, ImageConcatMulti, PreviewImage, ConditioningZeroOut, NunchakuFluxDiTLoader, SaveImage, Note Plus (mtb), MarkdownNote, Compositor3, CR Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 903374086400692, "steps": 20}
---

# 图片生成/图生图/kontext nunchaku图像指定区域控制三图编辑-StarAI_1939658941611548674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext nunchaku图像指定区域控制三图编辑-StarAI_1939658941611548674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `easy imageRemBg`
- `LoadImage`
- `ImageScaleToMegapixels`
- `LoadImage`
- `ImageScaleToMegapixels`
- `easy imageRemBg`
- `LoadImage`
- `CompositorConfig3`
- `ImageScaleToMegapixels`
- `ShowText|pysssss`
- `DualCLIPLoader`
- `VAELoader`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `ImageScaleToMegapixels`
- `FluxKontextImageScale`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ImageConcatMulti`
- `PreviewImage`
- `ConditioningZeroOut`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `Note Plus (mtb)`
- `MarkdownNote`
- `Compositor3`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `903374086400692`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`easy imageRemBg`、`LoadImage`、`ImageScaleToMegapixels`、`CompositorConfig3`、`DualCLIPLoader`、`VAELoader`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`FluxKontextImageScale`、`ReferenceLatent`、`VAEEncode`、`FluxGuidance`、`SaveImage`、`ImageConcanate`、`VAEDecode`、`KSampler`、`ImageConcatMulti`、`ConditioningZeroOut`、`NunchakuFluxDiTLoader`、`Note Plus (mtb)`、`Compositor3`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
