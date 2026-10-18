---
key: 视频生成/图生视频/LTX-2.3-MSR全能参考视频_2063551335492050946.json
name: LTX-2.3-MSR全能参考视频_2063551335492050946.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3-MSR全能参考视频_2063551335492050946.json
hash: eafca4d5146d52e0
coverage: 0.446429
learned_at: 2026-10-15 22:39:15
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, RMBG, SetNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, SetNode, GetNode, INTConstant, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, ManualSigmas, GetNode, GetNode, SamplerCustomAdvanced, ComfySwitchNode, GetNode, RandomNoise, ManualSigmas, GetNode, RMBG, ImageResizeKJv2, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, ImageResizeKJv2, EmptyLTXVLatentVideo, GetNode, LTXVConditioning, ComfyMathExpression, SetNode, SetNode, SetNode, ComfySwitchNode, ComfySwitchNode, LTXVEmptyLatentAudio, SamplerCustomAdvanced, UNETLoader, SetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, INTConstant, INTConstant, CLIPTextEncode, ManualSigmas, GetNode, SetNode, KSamplerSelect, SeedGenerator, VAEDecode, GetNode, LTXAddVideoICLoRAGuide, GetNode, SetNode, SetNode, LTXVConcatAVLatent, Reroute, Reroute, Reroute, CFGGuider, PrimitiveFloat, DualCLIPLoader, GetNode, GetImageSizeAndCount, ImageBatchMulti, LTXVAddGuidesFromBatch, LTXVAudioVAEDecode, Reroute, Reroute, Reroute, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, ComfySwitchNode, VAEDecode, GetNode, GetNode, GetNode, ComfySwitchNode, GetNode, LTXVCropGuides, GetNode, GetNode, SaveVideo, CreateVideo, VHS_VideoCombine, ImageBatchMulti, SetNode, LTXVAddGuideMulti, LiconMSR, VHS_VideoCombine, ModelSamplingSD3, LTXAddVideoICLoRAGuide, GetNode, LTXVCropGuides, KSamplerSelect, RandomNoise, CFGGuider, LTXVAddGuidesFromBatch, LTXVAddGuideMulti, LoadImage, ImageResizeKJv2, LoadImage, LoadImage, CLIPTextEncode, BasicScheduler, LTX2_NAG, LoraLoaderModelOnly, LTX2SamplingPreviewOverride, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX-2.3-MSR全能参考视频_2063551335492050946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063551335492050946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（168 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `RMBG`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ComfySwitchNode`
- `GetNode`
- `RandomNoise`
- `ManualSigmas`
- `GetNode`
- `RMBG`
- `ImageResizeKJv2`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVConditioning`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `SeedGenerator`
- `VAEDecode` ★核心
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `PrimitiveFloat`
- `DualCLIPLoader`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageBatchMulti`
- `LTXVAddGuidesFromBatch`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `SaveVideo`
- `CreateVideo`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `SetNode`
- `LTXVAddGuideMulti`
- `LiconMSR`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVAddGuidesFromBatch`
- `LTXVAddGuideMulti`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveBoolean`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（75/168）

**有卡**：`SimpleCalculatorKJ`、`ComfyMathExpression`、`RMBG`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`INTConstant`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`UNETLoader`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`KSamplerSelect`、`SeedGenerator`、`VAEDecode`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`DualCLIPLoader`、`GetImageSizeAndCount`、`ImageBatchMulti`、`LTXVAddGuidesFromBatch`、`LTXVCropGuides`、`SaveVideo`、`CreateVideo`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`LiconMSR`、`ModelSamplingSD3`、`LoadImage`、`BasicScheduler`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXICLoRALoaderModelOnly`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
