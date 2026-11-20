---
key: 平台全量/🈚️Flux.1 fill OneReward+sam3自动蒙版检测遮罩_手动遮罩-局部重绘_1924759250394861569.json
name: 🈚️Flux.1 fill OneReward+sam3自动蒙版检测遮罩_手动遮罩-局部重绘_1924759250394861569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️Flux.1 fill OneReward+sam3自动蒙版检测遮罩_手动遮罩-局部重绘_1924759250394861569.json
hash: ee15bcddde43e164
coverage: 0.674419
learned_at: 2026-11-14 02:54:22
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, LoadImage, Image Comparer (rgthree), ConditioningZeroOut, DifferentialDiffusion, GetNode, SetNode, VAEDecode, InpaintStitchImproved, ImageAndMaskPreview, SaveImage, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, InpaintModelConditioning, NunchakuFluxLoraLoader, DualCLIPLoader, VAELoader, UNETLoader, FluxGuidance, KSampler, CLIPTextEncode, PreviewImage, InpaintCropImproved, GetNode, Anything Everywhere3, ImpactSwitch, LayerMask: MaskGrow, GroundingDinoSAMSegment (segment anything), GetNode, SAM3Segmentation, LayerMask: MaskPreview, SaveImage, LayerMask: MaskGrow, LoadSAM3Model, GetNode, RH_Translator, RH_Translator, SAMLoader, GroundingDinoModelLoader (segment anything)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1055094822017837, "steps": 20}
---

# 平台全量/🈚️Flux.1 fill OneReward+sam3自动蒙版检测遮罩_手动遮罩-局部重绘_1924759250394861569.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️Flux.1 fill OneReward+sam3自动蒙版检测遮罩_手动遮罩-局部重绘_1924759250394861569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（43 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `ImageAndMaskPreview`
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `InpaintModelConditioning`
- `NunchakuFluxLoraLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `InpaintCropImproved`
- `GetNode`
- `Anything Everywhere3`
- `ImpactSwitch`
- `LayerMask: MaskGrow`
- `GroundingDinoSAMSegment (segment anything)`
- `GetNode`
- `SAM3Segmentation`
- `LayerMask: MaskPreview`
- `SaveImage`
- `LayerMask: MaskGrow`
- `LoadSAM3Model`
- `GetNode`
- `RH_Translator`
- `RH_Translator`
- `SAMLoader`
- `GroundingDinoModelLoader (segment anything)`

## 关键参数

- `seed` = `1055094822017837`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **67%**（29/43）

**有卡**：`LoadImage`、`ConditioningZeroOut`、`DifferentialDiffusion`、`VAEDecode`、`InpaintStitchImproved`、`ImageAndMaskPreview`、`SaveImage`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`InpaintModelConditioning`、`NunchakuFluxLoraLoader`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`FluxGuidance`、`KSampler`、`CLIPTextEncode`、`InpaintCropImproved`、`LayerMask: MaskGrow`、`GroundingDinoSAMSegment (segment anything)`、`SAM3Segmentation`、`LayerMask: MaskPreview`、`LoadSAM3Model`、`RH_Translator`、`SAMLoader`、`GroundingDinoModelLoader (segment anything)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
