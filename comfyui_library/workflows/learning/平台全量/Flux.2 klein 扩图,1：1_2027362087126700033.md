---
key: 平台全量/Flux.2 klein 扩图,1：1_2027362087126700033.json
name: Flux.2 klein 扩图,1：1_2027362087126700033
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.2 klein 扩图,1：1_2027362087126700033.json
hash: c86030eb9d68a589
coverage: 0.426471
learned_at: 2026-11-14 00:28:54
nodes: [SetNode, SetNode, GetNode, Anything Everywhere, VAELoader, CLIPLoader, SetNode, CLIPLoader, UNETLoader, GetNode, FluxGuidance, UNETLoader, CLIPTextEncode, SetNode, GetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, SetNode, GetNode, ReferenceLatent, PreviewImage, GetNode, GetNode, SetNode, SetNode, LayerMask: MaskPreview, PreviewImage, DrawMaskOnImage, PreviewImage, GetNode, SetNode, SetNode, LayerUtility: CropByMask V2, Reroute, Reroute, LayerUtility: ImageScaleRestore V2, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskGrow, PreviewImage, LayerMask: MaskPreview, GetNode, ImpactSwitch, DifferentialDiffusion, Anything Everywhere, Int, GetNode, CR Text, KSampler, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, LayerMask: MaskGrow, SetNode, VAEDecode, GetNode, EmptyLatentImage, VAEEncode, SaveImage, Image Comparer (rgthree), ImagePadForOutpaintTargetSize, LoadImage, SetNode, ColorMatch]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 365405912279520, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Flux.2 klein 扩图,1：1_2027362087126700033.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.2 klein 扩图,1：1_2027362087126700033.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `PreviewImage`
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
- `GetNode`
- `ImpactSwitch`
- `DifferentialDiffusion`
- `Anything Everywhere`
- `Int`
- `GetNode`
- `CR Text`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactSwitch`
- `LayerMask: MaskGrow`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `EmptyLatentImage` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaintTargetSize`
- `LoadImage`
- `SetNode`
- `ColorMatch`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `365405912279520`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **43%**（29/68）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`FluxGuidance`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LayerMask: MaskPreview`、`DrawMaskOnImage`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskGrow`、`DifferentialDiffusion`、`Int`、`CR Text`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`VAEEncode`、`SaveImage`、`ImagePadForOutpaintTargetSize`、`LoadImage`、`ColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
