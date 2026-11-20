---
key: 平台全量/多功能出图：移除+扩图+重绘+高清（Fuxl.1 OneReward）_2000209240587370498.json
name: 多功能出图：移除+扩图+重绘+高清（Fuxl.1 OneReward）_2000209240587370498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/多功能出图：移除+扩图+重绘+高清（Fuxl.1 OneReward）_2000209240587370498.json
hash: f58ad183555eb0f4
coverage: 0.586207
learned_at: 2026-11-14 01:57:30
nodes: [DualCLIPLoader, easy ifElse, easy ifElse, easy ifElse, easy ifElse, Simple String, Simple String, CLIPTextEncode, easy ifElse, VAEDecode, VAELoader, easy ifElse, ImageComposite+, InpaintModelConditioning, StringLength, SetNode, easy ifElse, GetNode, ImpactInt, easy boolean, easy ifElse, GetNode, GetNode, GetNode, ConditioningZeroOut, LoraLoaderModelOnly, Simple String, easy ifElse, UNETLoader, SetNode, PlaySound|pysssss, SetNode, INTConstant, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, GetNode, easy ifElse, GrowMaskWithBlur, ColorCorrect, LayerUtility: ColorImage, Simple String, LayerUtility: BooleanOperatorV2, DifferentialDiffusion, LayerMask: MaskGrow, FluxGuidance, LayerMask: MaskGrow, GetNode, PreviewImage, Image Comparer (rgthree), PreviewImage, Mute / Bypass Repeater (rgthree), SeedVR2VideoUpscaler, GetNode, GetNode, 孤海图像缩放按像素, PreviewImage, ImageScaleToTotalPixels, Mute / Bypass Relay (rgthree), LayerUtility: RestoreCropBox, KSampler, PreviewImage, Fast Groups Bypasser (rgthree), LoadImage, MarkdownNote, 孤海外补画板按方向, Mask Fill Holes, ToBinaryMask, easy ifElse, SetNode, PreviewImage, easy ifElse, Image Comparer (rgthree), 孤海-图像添加水印, 孤海-图像添加水印, SetNode, CR Text Replace, PreviewImage, LayerUtility: CropByMask V2, GrowMaskWithBlur, SaveImage, SetNode, SaveImage, RH_Translator, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 985351106286625, "steps": 30}
---

# 平台全量/多功能出图：移除+扩图+重绘+高清（Fuxl.1 OneReward）_2000209240587370498.json

> 来源文件 `comfyui_library/workflows/平台全量/多功能出图：移除+扩图+重绘+高清（Fuxl.1 OneReward）_2000209240587370498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `DualCLIPLoader`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `Simple String`
- `Simple String`
- `CLIPTextEncode` ★核心
- `easy ifElse`
- `VAEDecode` ★核心
- `VAELoader`
- `easy ifElse`
- `ImageComposite+`
- `InpaintModelConditioning`
- `StringLength`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `ImpactInt`
- `easy boolean`
- `easy ifElse`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `Simple String`
- `easy ifElse`
- `UNETLoader` ★核心
- `SetNode`
- `PlaySound|pysssss`
- `SetNode`
- `INTConstant`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `GetNode`
- `easy ifElse`
- `GrowMaskWithBlur`
- `ColorCorrect`
- `LayerUtility: ColorImage`
- `Simple String`
- `LayerUtility: BooleanOperatorV2`
- `DifferentialDiffusion`
- `LayerMask: MaskGrow`
- `FluxGuidance`
- `LayerMask: MaskGrow`
- `GetNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Mute / Bypass Repeater (rgthree)`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `GetNode`
- `孤海图像缩放按像素`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `Mute / Bypass Relay (rgthree)`
- `LayerUtility: RestoreCropBox`
- `KSampler` ★核心
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `MarkdownNote`
- `孤海外补画板按方向`
- `Mask Fill Holes`
- `ToBinaryMask`
- `easy ifElse`
- `SetNode`
- `PreviewImage`
- `easy ifElse`
- `Image Comparer (rgthree)`
- `孤海-图像添加水印`
- `孤海-图像添加水印`
- `SetNode`
- `CR Text Replace`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `GrowMaskWithBlur`
- `SaveImage`
- `SetNode`
- `SaveImage`
- `RH_Translator`
- `LoadImage`

## 关键参数

- `seed` = `985351106286625`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（51/87）

**有卡**：`DualCLIPLoader`、`Simple String`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`ImageComposite+`、`InpaintModelConditioning`、`StringLength`、`ImpactInt`、`easy boolean`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`UNETLoader`、`PlaySound|pysssss`、`INTConstant`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`GrowMaskWithBlur`、`ColorCorrect`、`LayerUtility: ColorImage`、`LayerUtility: BooleanOperatorV2`、`DifferentialDiffusion`、`LayerMask: MaskGrow`、`FluxGuidance`、`Mute / Bypass Repeater (rgthree)`、`SeedVR2VideoUpscaler`、`孤海图像缩放按像素`、`ImageScaleToTotalPixels`、`Mute / Bypass Relay (rgthree)`、`LayerUtility: RestoreCropBox`、`KSampler`、`LoadImage`、`孤海外补画板按方向`、`Mask Fill Holes`、`ToBinaryMask`、`孤海-图像添加水印`、`CR Text Replace`、`LayerUtility: CropByMask V2`、`SaveImage`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
