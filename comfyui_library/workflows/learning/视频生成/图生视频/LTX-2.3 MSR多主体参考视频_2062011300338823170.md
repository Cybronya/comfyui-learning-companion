---
key: 视频生成/图生视频/LTX-2.3 MSR多主体参考视频_2062011300338823170.json
name: LTX-2.3 MSR多主体参考视频_2062011300338823170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062011300338823170.json
hash: cc061ae7a68997aa
coverage: 0.443114
learned_at: 2026-10-15 22:38:58
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, RMBG, SetNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, SetNode, GetNode, INTConstant, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, ManualSigmas, GetNode, GetNode, SamplerCustomAdvanced, ComfySwitchNode, GetNode, LTX2_NAG, RandomNoise, PrimitiveBoolean, ManualSigmas, GetNode, RMBG, ImageResizeKJv2, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, ImageResizeKJv2, ImageResizeKJv2, EmptyLTXVLatentVideo, GetNode, LTXVConditioning, ComfyMathExpression, SetNode, SetNode, SetNode, ComfySwitchNode, ComfySwitchNode, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LoadImage, LoadImage, UNETLoader, SetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, INTConstant, INTConstant, CLIPTextEncode, LoadImage, ManualSigmas, GetNode, SetNode, KSamplerSelect, SeedGenerator, VAEDecode, GetNode, LTXAddVideoICLoRAGuide, GetNode, SetNode, SetNode, LTXVConcatAVLatent, CLIPTextEncode, Reroute, Reroute, Reroute, LoraLoaderModelOnly, CFGGuider, PrimitiveFloat, DualCLIPLoader, GetNode, GetImageSizeAndCount, ImageBatchMulti, LTXVAddGuidesFromBatch, LTXVAudioVAEDecode, BasicScheduler, Reroute, Reroute, Reroute, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, ComfySwitchNode, VAEDecode, GetNode, GetNode, GetNode, ComfySwitchNode, GetNode, LTXVCropGuides, GetNode, GetNode, SaveVideo, CreateVideo, VHS_VideoCombine, ImageBatchMulti, SetNode, LTXVAddGuideMulti, LiconMSR, VHS_VideoCombine, ModelSamplingSD3, LTXICLoRALoaderModelOnly, LTX2SamplingPreviewOverride, LTXAddVideoICLoRAGuide, GetNode, LTXVCropGuides, KSamplerSelect, RandomNoise, CFGGuider, LTXVAddGuidesFromBatch, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX-2.3 MSR多主体参考视频_2062011300338823170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062011300338823170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（167 个）：
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
- `LTX2_NAG`
- `RandomNoise`
- `PrimitiveBoolean`
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
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoadImage`
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
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `DualCLIPLoader`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageBatchMulti`
- `LTXVAddGuidesFromBatch`
- `LTXVAudioVAEDecode` ★核心
- `BasicScheduler`
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
- `LTXICLoRALoaderModelOnly` ★核心
- `LTX2SamplingPreviewOverride`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVAddGuidesFromBatch`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **44%**（74/167）

**有卡**：`SimpleCalculatorKJ`、`ComfyMathExpression`、`RMBG`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`INTConstant`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTX2_NAG`、`RandomNoise`、`PrimitiveBoolean`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LoadImage`、`UNETLoader`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`KSamplerSelect`、`SeedGenerator`、`VAEDecode`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`DualCLIPLoader`、`GetImageSizeAndCount`、`ImageBatchMulti`、`LTXVAddGuidesFromBatch`、`BasicScheduler`、`LTXVCropGuides`、`SaveVideo`、`CreateVideo`、`VHS_VideoCombine`、`LTXVAddGuideMulti`、`LiconMSR`、`ModelSamplingSD3`、`LTXICLoRALoaderModelOnly`、`LTX2SamplingPreviewOverride`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
