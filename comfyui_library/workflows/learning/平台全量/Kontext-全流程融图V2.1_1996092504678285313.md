---
key: 平台全量/Kontext-全流程融图V2.1_1996092504678285313.json
name: Kontext-全流程融图V2.1_1996092504678285313
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext-全流程融图V2.1_1996092504678285313.json
hash: 82d293fad7d11793
coverage: 0.917526
learned_at: 2026-11-14 00:34:59
nodes: [easy setNode, easy setNode, InvertMask, ConditioningZeroOut, easy getNode, Mask Fill Holes, easy getNode, MaskPreview+, LayerUtility: ImageRemoveAlpha, FluxGuidance, easy getNode, ReferenceLatent, easy getNode, VAEDecode, VAEEncode, easy setNode, easy getNode, CLIPTextEncode, KSampler, easy setNode, UNETLoader, DualCLIPLoader, easy setNode, VAELoader, LoadImage, LoadImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, FluxGuidance, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, VAEEncode, CFGNorm, LoraLoaderModelOnly, KSampler, VAEDecode, easy seed, ImpactInt, Text Concatenate (JPS), ConditioningZeroOut, SaveImage, VAEEncode, easy getNode, KSampler, Image Comparer (rgthree), SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy getNode, SeedVR2LoadVAEModel, ImpactInt, SeedVR2VideoUpscaler, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, ImpactInt, Image Comparer (rgthree), SaveImage, SeedVR2LoadDiTModel, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), LoadImage, easy getNode, Fast Groups Bypasser (rgthree), easy getNode, LayerUtility: ImageMaskScaleAs, LayerUtility: AnyRerouter, MaskPreview+, Image Comparer (rgthree), VAEDecode, LayerUtility: HLFrequencyDetailRestore, ReferenceLatent, CLIPTextEncode, easy getNode, LoadImage, CR Text, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, Note, LayerMask: MaskGrow, easy imageRemBg, easy imageRemBg, SaveImage, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 298044255516912, "steps": 30}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Kontext-全流程融图V2.1_1996092504678285313.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext-全流程融图V2.1_1996092504678285313.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `easy setNode`
- `easy setNode`
- `InvertMask`
- `ConditioningZeroOut`
- `easy getNode`
- `Mask Fill Holes`
- `easy getNode`
- `MaskPreview+`
- `LayerUtility: ImageRemoveAlpha`
- `FluxGuidance`
- `easy getNode`
- `ReferenceLatent`
- `easy getNode`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `easy setNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `easy setNode`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `easy setNode`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxGuidance`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy seed`
- `ImpactInt`
- `Text Concatenate (JPS)`
- `ConditioningZeroOut`
- `SaveImage`
- `VAEEncode` ★核心
- `easy getNode`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy getNode`
- `SeedVR2LoadVAEModel`
- `ImpactInt`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `ImpactInt`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `easy getNode`
- `Fast Groups Bypasser (rgthree)`
- `easy getNode`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: AnyRerouter`
- `MaskPreview+`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LayerUtility: HLFrequencyDetailRestore`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `LoadImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `Note`
- `LayerMask: MaskGrow`
- `easy imageRemBg`
- `easy imageRemBg`
- `SaveImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `298044255516912`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（89/97）

**有卡**：`easy setNode`、`InvertMask`、`ConditioningZeroOut`、`easy getNode`、`Mask Fill Holes`、`MaskPreview+`、`LayerUtility: ImageRemoveAlpha`、`FluxGuidance`、`ReferenceLatent`、`VAEDecode`、`VAEEncode`、`CLIPTextEncode`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`LoraLoaderModelOnly`、`CFGNorm`、`easy seed`、`ImpactInt`、`Text Concatenate (JPS)`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageMaskScaleAs`、`LayerUtility: AnyRerouter`、`LayerUtility: HLFrequencyDetailRestore`、`CR Text`、`LayerMask: MaskGrow`、`easy imageRemBg`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
