---
key: 图片生成/图生图/Flux Kontext Dev中性色彩光线RAW Photo加速版v1_1942617822352576514.json
name: Flux Kontext Dev中性色彩光线RAW Photo加速版v1_1942617822352576514
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev中性色彩光线RAW Photo加速版v1_1942617822352576514.json
hash: 7c54e657cc091b25
coverage: 0.913043
learned_at: 2026-10-23 10:56:53
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, VAEDecode, MagCache, UnetLoaderGGUF, KSampler, ImageConcanate, SaveImage, CR Prompt Text, LoraLoaderModelOnly, FluxGuidance, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 654083301602961, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev中性色彩光线RAW Photo加速版v1_1942617822352576514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev中性色彩光线RAW Photo加速版v1_1942617822352576514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `MagCache`
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `ImageConcanate`
- `SaveImage`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `654083301602961`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`VAEDecode`、`MagCache`、`UnetLoaderGGUF`、`KSampler`、`ImageConcanate`、`SaveImage`、`CR Prompt Text`、`LoraLoaderModelOnly`、`FluxGuidance`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
