---
key: 视频生成/文生视频/LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674.json
name: LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674.json
hash: f2dd4f5dfafb632f
coverage: 0.783133
learned_at: 2026-10-11 19:49:36
nodes: [KSamplerSelect, KSamplerSelect, ComfyMathExpression, LTXVConcatAVLatent, Reroute, LTXVConcatAVLatent, ComfyMathExpression, ManualSigmas, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, Note, Note, Note, Note, RandomNoise, LTXVAudioVAEDecode, VAEDecodeTiled, PlaySound|pysssss, VAEDecodeTiled, PlaySound|pysssss, ComfyMathExpression, LTXVAudioVAEDecode, CFGGuider, Note, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, Note, Note, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVEmptyLatentAudio, ImpactConditionalBranch, ImpactConditionalBranch, LTXVConditioning, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, VHS_VideoCombine, EmptyLTXVLatentVideo, RandomNoise, LTXVCropGuides, LTXVSeparateAVLatent, ImpactConditionalBranch, LTXVEnhanceAVideoKJ, LTXVChunkFeedForward, UnetLoaderGGUF, LoraLoaderModelOnly, CLIPTextEncode, LTXVReferenceAudio, ImpactConditionalBranch, LatentUpscaleModelLoader, DualCLIPLoaderGGUF, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, LTXVImgToVideoInplace, LoadImage, PrimitiveBoolean, LTX2_NAG, PrimitiveInt, PrimitiveInt, PrimitiveInt, PathchSageAttentionKJ, ModelPatchTorchSettings, ImpactConditionalBranch, PrimitiveNode, SamplerCustomAdvanced, VHS_VideoCombine, PrimitiveNode, ResizeImagesByLongerEdge, LTXVPreprocess, PromptRelayEncodeTimeline, Label (rgthree), LoraLoaderModelOnly, Note, VHS_LoadAudioUpload, PreviewAudio, LoraLoaderModelOnly]
patterns: []
missing: [Label (rgthree), PlaySound|pysssss, PlaySound|pysssss]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（83 个）：
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ManualSigmas`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `Note`
- `Note`
- `Note`
- `Note`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `PlaySound|pysssss`
- `VAEDecodeTiled` ★核心
- `PlaySound|pysssss`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `Note`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `Note`
- `Note`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVEmptyLatentAudio` ★核心
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `LTXVConditioning`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `ImpactConditionalBranch`
- `LTXVEnhanceAVideoKJ`
- `LTXVChunkFeedForward`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVReferenceAudio`
- `ImpactConditionalBranch`
- `LatentUpscaleModelLoader`
- `DualCLIPLoaderGGUF`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `LoadImage`
- `PrimitiveBoolean`
- `LTX2_NAG`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ImpactConditionalBranch`
- `PrimitiveNode`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `PrimitiveNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `PromptRelayEncodeTimeline`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（65/83）

**有卡**：`KSamplerSelect`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`RandomNoise`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`ImpactConditionalBranch`、`LTXVConditioning`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVEnhanceAVideoKJ`、`LTXVChunkFeedForward`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVReferenceAudio`、`LatentUpscaleModelLoader`、`DualCLIPLoaderGGUF`、`VAELoaderKJ`、`LoadImage`、`PrimitiveBoolean`、`LTX2_NAG`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`PromptRelayEncodeTimeline`、`VHS_LoadAudioUpload`、`PreviewAudio`

**缺卡**（3）：`Label (rgthree)`、`PlaySound|pysssss`、`PlaySound|pysssss`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
