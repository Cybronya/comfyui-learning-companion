---
key: 视频生成/文生视频/LTX2.3+MSR V2高动效，高人物一致，高质量视频制作_2081628938446655489.json
name: LTX2.3+MSR V2高动效，高人物一致，高质量视频制作_2081628938446655489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3+MSR V2高动效，高人物一致，高质量视频制作_2081628938446655489.json
hash: 96340b8122846605
coverage: 0.427632
learned_at: 2026-10-11 20:38:34
nodes: [SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PathchSageAttentionKJ, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTX2MemoryEfficientSageAttentionPatch, GetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, CFGGuider, ComfySwitchNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, ManualSigmas, KSamplerSelect, ManualSigmas, ModelSamplingSD3, LTX2SamplingPreviewOverride, CFGGuider, KSamplerSelect, MarkdownNote, MarkdownNote, BasicScheduler, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, GetNode, GetNode, ImageResizeKJv2, ComfyMathExpression, ComfyMathExpression, GetNode, ComfySwitchNode, ComfySwitchNode, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, MarkdownNote, LTXVConditioning, ComfySwitchNode, GetNode, GetNode, GetNode, LTXVCropGuides, RandomNoise, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly, PrimitiveBoolean, GetNode, LoadImage, LoadImage, LiconMSR, ImageResizeKJv2, ImageResizeKJv2, LTXAddVideoICLoRAGuide, LTX2_NAG, CLIPTextEncode, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecode, LTX2AttentionTunerPatch, LTXVChunkFeedForward, RandomNoise, INTConstant, INTConstant, INTConstant, PrimitiveFloat, PromptRelayEncode, LoadImage, LoadImage, LoadImage, UNETLoader, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, LTXICLoRALoaderModelOnly, GetImageSizeAndCount, SetNode, GetNode, GetNode, ComfySwitchNode, GetNode, VHS_VideoCombine, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 241}
---

# 视频生成/文生视频/LTX2.3+MSR V2高动效，高人物一致，高质量视频制作_2081628938446655489.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3+MSR V2高动效，高人物一致，高质量视频制作_2081628938446655489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（152 个）：
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2MemoryEfficientSageAttentionPatch`
- `GetNode`
- `GetNode`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `ComfySwitchNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ModelSamplingSD3`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `BasicScheduler`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `LTXVConditioning`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `RandomNoise`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LiconMSR`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LTX2AttentionTunerPatch`
- `LTXVChunkFeedForward`
- `RandomNoise`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `PromptRelayEncode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `VHS_VideoCombine`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **43%**（65/152）

**有卡**：`SimpleCalculatorKJ`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`ComfyNumberConvert`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`KSamplerSelect`、`ModelSamplingSD3`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`ImageResizeKJv2`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`RandomNoise`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`LoadImage`、`LiconMSR`、`LTX2_NAG`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`LTX2AttentionTunerPatch`、`LTXVChunkFeedForward`、`INTConstant`、`PromptRelayEncode`、`UNETLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`GetImageSizeAndCount`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
