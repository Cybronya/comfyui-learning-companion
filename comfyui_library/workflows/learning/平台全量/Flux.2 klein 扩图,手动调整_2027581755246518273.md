---
key: 平台全量/Flux.2 klein 扩图,手动调整_2027581755246518273.json
name: Flux.2 klein 扩图,手动调整_2027581755246518273
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 klein 扩图,手动调整_2027581755246518273.json
hash: de95cdbcece0e057
coverage: 0.407895
learned_at: 2026-11-14 00:28:55
nodes: [SetNode, SetNode, GetNode, Anything Everywhere, VAELoader, CLIPLoader, SetNode, CLIPLoader, UNETLoader, GetNode, FluxGuidance, UNETLoader, CLIPTextEncode, SetNode, GetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, SetNode, GetNode, ReferenceLatent, GetNode, SetNode, SetNode, LayerMask: MaskPreview, DrawMaskOnImage, PreviewImage, GetNode, SetNode, SetNode, LayerUtility: CropByMask V2, Reroute, Reroute, LayerUtility: ImageScaleRestore V2, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskGrow, PreviewImage, LayerMask: MaskPreview, ImpactSwitch, DifferentialDiffusion, Anything Everywhere, Int, GetNode, CR Text, KSampler, GetNode, ImpactSwitch, LayerMask: MaskGrow, VAEDecode, GetNode, EmptyLatentImage, SetNode, ColorMatch, SetNode, PreviewImage, ImagePadForOutpaintTargetSize, VAEEncode, LoadImage, ShowText|pysssss, easy showAnything, ShowText|pysssss, easy showAnything, PreviewImage, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, PreviewImage, PreviewImage, SaveImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio, ImagePadForOutpaint]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 190117963298868, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2 klein 扩图,手动调整_2027581755246518273.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 klein 扩图,手动调整_2027581755246518273.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `Anything Everywhere`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `GetNode`
- `FluxGuidance`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ReferenceLatent`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `DrawMaskOnImage`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleRestore V2`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `ImpactSwitch`
- `DifferentialDiffusion`
- `Anything Everywhere`
- `Int`
- `GetNode`
- `CR Text`
- `KSampler` ★核心
- `GetNode`
- `ImpactSwitch`
- `LayerMask: MaskGrow`
- `VAEDecode` ★核心
- `GetNode`
- `EmptyLatentImage` ★核心
- `SetNode`
- `ColorMatch`
- `SetNode`
- `PreviewImage`
- `ImagePadForOutpaintTargetSize`
- `VAEEncode` ★核心
- `LoadImage`
- `ShowText|pysssss`
- `easy showAnything`
- `ShowText|pysssss`
- `easy showAnything`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio`
- `ImagePadForOutpaint`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `190117963298868`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（31/76）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`FluxGuidance`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LayerMask: MaskPreview`、`DrawMaskOnImage`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskGrow`、`DifferentialDiffusion`、`Int`、`CR Text`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`ColorMatch`、`ImagePadForOutpaintTargetSize`、`VAEEncode`、`LoadImage`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
