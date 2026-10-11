---
key: 视频生成/文生视频/LTX-2.3-MSR-多主体参考视频生成_2065248408478248962.json
name: LTX-2.3-MSR-多主体参考视频生成_2065248408478248962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-MSR-多主体参考视频生成_2065248408478248962.json
hash: 65f1fb08690a5e39
coverage: 0.447059
learned_at: 2026-10-11 20:21:25
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, RMBG, SetNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, SetNode, GetNode, INTConstant, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SamplerCustomAdvanced, ComfySwitchNode, GetNode, RandomNoise, ManualSigmas, GetNode, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, ImageResizeKJv2, EmptyLTXVLatentVideo, SetNode, SetNode, SetNode, ComfySwitchNode, ComfySwitchNode, LTXVEmptyLatentAudio, SetNode, GetNode, GetNode, INTConstant, INTConstant, GetNode, KSamplerSelect, GetNode, GetNode, LTXVConcatAVLatent, Reroute, Reroute, Reroute, CFGGuider, DualCLIPLoader, GetNode, GetImageSizeAndCount, ImageBatchMulti, BasicScheduler, GetNode, SetNode, SetNode, LiconMSR, ModelSamplingSD3, GetNode, KSamplerSelect, RandomNoise, CLIPTextEncode, ManualSigmas, LTXAddVideoICLoRAGuide, SetNode, GetNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, RMBG, VHS_VideoCombine, GetNode, UNETLoader, PrimitiveFloat, PrimitiveBoolean, CFGGuider, LTXVAddGuideMulti, CreateVideo, GetNode, LoadImage, LoadImage, Reroute, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, ComfySwitchNode, LTXVCropGuides, GetNode, GetNode, ComfySwitchNode, VAEDecode, LTXVAudioVAEDecode, GetNode, GetNode, ImageBatchMulti, LTXVAddGuidesFromBatch, LTXAddVideoICLoRAGuide, LTXVLatentUpsampler, LTXVCropGuides, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecode, SeedGenerator, SamplerCustomAdvanced, LTXVAddGuidesFromBatch, LTX2_NAG, LTX2SamplingPreviewOverride, SetNode, SetNode, LTXVAddGuideMulti, TextInput_, CLIPTextEncode, ComfyMathExpression, ComfyMathExpression, GetNode, LTXVConditioning, Label (rgthree), VHS_VideoCombine, SaveVideo, ImageResizeKJv2, ImageResizeKJv2]
patterns: []
missing: [Label (rgthree)]
parameters: {"batch_size": 1, "height": 24, "width": 145}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX-2.3-MSR-多主体参考视频生成_2065248408478248962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-MSR-多主体参考视频生成_2065248408478248962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（170 个）：
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `SamplerCustomAdvanced` ★核心
- `ComfySwitchNode`
- `GetNode`
- `RandomNoise`
- `ManualSigmas`
- `GetNode`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `DualCLIPLoader`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageBatchMulti`
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `SetNode`
- `LiconMSR`
- `ModelSamplingSD3`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `LTXAddVideoICLoRAGuide`
- `SetNode`
- `GetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RMBG`
- `VHS_VideoCombine`
- `GetNode`
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `CFGGuider`
- `LTXVAddGuideMulti`
- `CreateVideo`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `LTXVAddGuidesFromBatch`
- `LTXAddVideoICLoRAGuide`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `SeedGenerator`
- `SamplerCustomAdvanced` ★核心
- `LTXVAddGuidesFromBatch`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `SetNode`
- `LTXVAddGuideMulti`
- `TextInput_`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `LTXVConditioning`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `SaveVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **45%**（76/170）

**有卡**：`SimpleCalculatorKJ`、`ComfyMathExpression`、`RMBG`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`INTConstant`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`LTXVConcatAVLatent`、`CFGGuider`、`DualCLIPLoader`、`GetImageSizeAndCount`、`ImageBatchMulti`、`BasicScheduler`、`LiconMSR`、`ModelSamplingSD3`、`CLIPTextEncode`、`LTXAddVideoICLoRAGuide`、`LTXICLoRALoaderModelOnly`、`LoadImage`、`VHS_VideoCombine`、`UNETLoader`、`PrimitiveBoolean`、`LTXVAddGuideMulti`、`CreateVideo`、`LTXVCropGuides`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVAddGuidesFromBatch`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`SeedGenerator`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`TextInput_`、`LTXVConditioning`、`SaveVideo`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
