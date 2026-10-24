---
key: 图片生成/图生图/Flux2+Klein+人物替换++V1.5+一致性增强+工作流（6G显存可用）_2073337131463958530.json
name: Flux2+Klein+人物替换++V1.5+一致性增强+工作流（6G显存可用）_2073337131463958530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2+Klein+人物替换++V1.5+一致性增强+工作流（6G显存可用）_2073337131463958530.json
hash: de4117f6b8e339ac
coverage: 0.805369
learned_at: 2026-10-23 10:59:52
nodes: [SaveImage, easy setNode, SimpleMath+, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, SimpleMath+, SimpleMathCondition+, SimpleMath+, easy getNode, easy setNode, easy getNode, SimpleMathCondition+, LayerUtility: ColorImage V2, easy setNode, easy setNode, MaskPreview+, easy setNode, Get resolution [Crystools], easy getNode, SimpleMath+, easy getNode, SimpleMath+, ImpactCompare, easy setNode, LayerUtility: ImageBlendAdvance, easy showAnything, easy setNode, SimpleMath+, easy setNode, Reroute, MarkdownNote, LayerMask: LoadBiRefNetModelV2, MarkdownNote, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, GrowMaskWithBlur, ImpactCompare, easy getNode, SimpleMathCondition+, easy setNode, easy getNode, SimpleMath+, MaskToImage, ImageCompositeMasked, VAEEncode, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, InpaintModelConditioning, ReferenceLatent, ReferenceLatent, ReferenceLatent, RandomNoise, easy getNode, easy getNode, easy getNode, easy setNode, LayerUtility: ImageScaleByAspectRatio V2, easy setNode, easy getNode, Get resolution [Crystools], SaveImage, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, Get resolution [Crystools], easy setNode, easy setNode, VAELoader, SamplerCustomAdvanced, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, Get resolution [Crystools], ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, VAEDecode, EmptyFlux2LatentImage, Reroute, Reroute, Reroute, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, LayerUtility: ImageReelComposit, EmptyFlux2LatentImage, Flux2Scheduler, MaskFillHoles, UNETLoader, SDPoseOODLoader, LayerUtility: ImageReel, MarkdownNote, MarkdownNote, Seed (rgthree), Reroute, PreviewImage, Reroute, Reroute, Reroute, easy setNode, ConcatTextOfUtils, JWStringConcat, CR Text, LayerMask: BiRefNetUltraV2, LoadImage, LoadImage, LayerUtility: ImageReel, SDPoseOODProcessor, LoadImage, CFGGuider, KSamplerSelect, Fast Bypasser (rgthree), Reroute, CFGGuider, RandomNoise, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, LoraLoaderModelOnly, Get resolution [Crystools], VAEEncode, VAEDecode, Reroute, CLIPLoader, ConditioningZeroOut, Reroute, PreviewImage, CLIPTextEncode, KSamplerSelect, Fast Groups Bypasser (rgthree), MarkdownNote, ShowText|pysssss, LoraLoaderModelOnly, Int, Seed (rgthree), easy getNode, easy imageSwitch, CR Text, DWPreprocessor, Reroute, MarkdownNote, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2+Klein+人物替换++V1.5+一致性增强+工作流（6G显存可用）_2073337131463958530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2+Klein+人物替换++V1.5+一致性增强+工作流（6G显存可用）_2073337131463958530.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
- `SaveImage`
- `easy setNode`
- `SimpleMath+`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `SimpleMath+`
- `SimpleMathCondition+`
- `SimpleMath+`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `SimpleMathCondition+`
- `LayerUtility: ColorImage V2`
- `easy setNode`
- `easy setNode`
- `MaskPreview+`
- `easy setNode`
- `Get resolution [Crystools]`
- `easy getNode`
- `SimpleMath+`
- `easy getNode`
- `SimpleMath+`
- `ImpactCompare`
- `easy setNode`
- `LayerUtility: ImageBlendAdvance`
- `easy showAnything`
- `easy setNode`
- `SimpleMath+`
- `easy setNode`
- `Reroute`
- `MarkdownNote`
- `LayerMask: LoadBiRefNetModelV2`
- `MarkdownNote`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMaskWithBlur`
- `ImpactCompare`
- `easy getNode`
- `SimpleMathCondition+`
- `easy setNode`
- `easy getNode`
- `SimpleMath+`
- `MaskToImage`
- `ImageCompositeMasked`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `InpaintModelConditioning`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy setNode`
- `easy getNode`
- `Get resolution [Crystools]`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `Get resolution [Crystools]`
- `easy setNode`
- `easy setNode`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `Get resolution [Crystools]`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `MaskFillHoles`
- `UNETLoader` ★核心
- `SDPoseOODLoader`
- `LayerUtility: ImageReel`
- `MarkdownNote`
- `MarkdownNote`
- `Seed (rgthree)`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy setNode`
- `ConcatTextOfUtils`
- `JWStringConcat`
- `CR Text`
- `LayerMask: BiRefNetUltraV2`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageReel`
- `SDPoseOODProcessor`
- `LoadImage`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Fast Bypasser (rgthree)`
- `Reroute`
- `CFGGuider`
- `RandomNoise`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Get resolution [Crystools]`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Reroute`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Seed (rgthree)`
- `easy getNode`
- `easy imageSwitch`
- `CR Text`
- `DWPreprocessor`
- `Reroute`
- `MarkdownNote`
- `PreviewImage`

## 知识

覆盖率 **81%**（120/149）

**有卡**：`SaveImage`、`easy setNode`、`SimpleMath+`、`easy getNode`、`SimpleMathCondition+`、`LayerUtility: ColorImage V2`、`MaskPreview+`、`Get resolution [Crystools]`、`ImpactCompare`、`LayerUtility: ImageBlendAdvance`、`LayerMask: LoadBiRefNetModelV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`MaskToImage`、`ImageCompositeMasked`、`VAEEncode`、`ReferenceLatent`、`InpaintModelConditioning`、`RandomNoise`、`ImagePadForOutpaint`、`VAELoader`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`ConditioningZeroOut`、`Flux2Scheduler`、`VAEDecode`、`EmptyFlux2LatentImage`、`LayerUtility: ImageReelComposit`、`MaskFillHoles`、`UNETLoader`、`SDPoseOODLoader`、`LayerUtility: ImageReel`、`Seed (rgthree)`、`ConcatTextOfUtils`、`JWStringConcat`、`CR Text`、`LayerMask: BiRefNetUltraV2`、`LoadImage`、`SDPoseOODProcessor`、`CFGGuider`、`KSamplerSelect`、`Fast Bypasser (rgthree)`、`LoraLoaderModelOnly`、`CLIPLoader`、`Int`、`easy imageSwitch`、`DWPreprocessor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
