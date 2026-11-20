---
key: 平台全量/Flux Background Replacer for portraits_1864226915614670850.json
name: Flux Background Replacer for portraits_1864226915614670850
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Background Replacer for portraits_1864226915614670850.json
hash: 9147e7131c2383f1
coverage: 0.561798
learned_at: 2026-11-14 00:27:32
nodes: [SetNode, GetNode, Bus Node, GetNode, GetNode, GetNode, DetailTransfer, VAEEncode, VAEDecode, ControlNetApplyAdvanced, PreviewImage, SetNode, easy showAnything, MaskPreview+, SetNode, LayerUtility: ImageBlendAdvance V2, PreviewImage, Image Blank, MaskPreview+, MaskPreview+, LamaRemover, LamaRemover, PreviewImage, PreviewImage, Image Comparer (rgthree), SetNode, Preview Chooser, PreviewImage, Bus Node, GetNode, GetNode, PreviewImage, InspyrenetRembgAdvanced, GrowMask, Masks Subtract, InspyrenetRembgAdvanced, PreviewImage, PreviewImage, ImpactSwitch, Image Comparer (rgthree), Image Comparer (rgthree), GetNode, GetNode, FloatSlider, FluxResolutionNode, FloatSlider, GetNode, GetNode, LayerMask: MaskGrow, FloatSlider, LayerColor: Exposure, KSampler, Note, SetNode, CLIPTextEncode, GetNode, SetNode, Anything Everywhere, VAEEncode, KSampler, Fast Groups Bypasser (rgthree), PreviewImage, LamaRemover, SaveImage, Image Blend, SaveImage, RestoreDetail, GetNode, SaveImage, ImageCompositeMasked, SaveImage, LoadImage, UNETLoader, DualCLIPLoader, VAELoader, ControlNetLoader, ControlNetLoader, CLIPTextEncode, GetNode, AIO_Preprocessor, PreviewImage, InspyrenetRembgAdvanced, Image Comparer (rgthree), VAEDecode, ControlNetApplyAdvanced, FluxGuidance, GetNode, RH_Captioner, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.55, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 953999074754729, "steps": 28}
---

# 平台全量/Flux Background Replacer for portraits_1864226915614670850.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Background Replacer for portraits_1864226915614670850.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `SetNode`
- `GetNode`
- `Bus Node`
- `GetNode`
- `GetNode`
- `GetNode`
- `DetailTransfer`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `SetNode`
- `easy showAnything`
- `MaskPreview+`
- `SetNode`
- `LayerUtility: ImageBlendAdvance V2`
- `PreviewImage`
- `Image Blank`
- `MaskPreview+`
- `MaskPreview+`
- `LamaRemover`
- `LamaRemover`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `Preview Chooser`
- `PreviewImage`
- `Bus Node`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `InspyrenetRembgAdvanced`
- `GrowMask`
- `Masks Subtract`
- `InspyrenetRembgAdvanced`
- `PreviewImage`
- `PreviewImage`
- `ImpactSwitch`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `FloatSlider`
- `FluxResolutionNode`
- `FloatSlider`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
- `FloatSlider`
- `LayerColor: Exposure`
- `KSampler` ★核心
- `Note`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `Anything Everywhere`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `LamaRemover`
- `SaveImage`
- `Image Blend`
- `SaveImage`
- `RestoreDetail`
- `GetNode`
- `SaveImage`
- `ImageCompositeMasked`
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `AIO_Preprocessor`
- `PreviewImage`
- `InspyrenetRembgAdvanced`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `FluxGuidance`
- `GetNode`
- `RH_Captioner`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.55`
- `seed` = `953999074754729`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **56%**（50/89）

**有卡**：`Bus Node`、`DetailTransfer`、`VAEEncode`、`VAEDecode`、`ControlNetApplyAdvanced`、`MaskPreview+`、`LayerUtility: ImageBlendAdvance V2`、`Image Blank`、`LamaRemover`、`Preview Chooser`、`InspyrenetRembgAdvanced`、`GrowMask`、`Masks Subtract`、`FloatSlider`、`FluxResolutionNode`、`LayerMask: MaskGrow`、`LayerColor: Exposure`、`KSampler`、`CLIPTextEncode`、`SaveImage`、`Image Blend`、`RestoreDetail`、`ImageCompositeMasked`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ControlNetLoader`、`AIO_Preprocessor`、`FluxGuidance`、`RH_Captioner`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
