---
key: 视频生成/图生视频/LTX2.3 多图剧情视频图生视频 批量生视频 超长时间 编导时间线提示词修改版_2062395094396919810.json
name: LTX2.3 多图剧情视频图生视频 批量生视频 超长时间 编导时间线提示词修改版_2062395094396919810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 多图剧情视频图生视频 批量生视频 超长时间 编导时间线提示词修改版_2062395094396919810.json
hash: 14fef4c119f6e188
coverage: 0.515625
learned_at: 2026-10-15 22:39:03
nodes: [ResizeImagesByLongerEdge, SetNode, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, GetNode, GetNode, GetNode, GetNode, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, GetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, ComfyMathExpression, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ComfyMathExpression, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, GetNode, LTXVConditioning, GetNode, GetNode, CFGGuider, VAEDecodeTiled, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, GetNode, GetNode, LTXVCropGuides, GetNode, GetNode, GetNode, LTXVCropGuides, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ComfyMathExpression, GetNode, GetNode, VAEDecodeTiled, CFGGuider, LTXVSeparateAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, SetNode, SetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, GetNode, LTX2SamplingPreviewOverride, SetNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, SetNode, ResizeImageMaskNode, SetNode, SetNode, SetNode, PrimitiveFloat, INTConstant, INTConstant, easy loraStackApply, RandomNoise, SetNode, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, LatentUpscaleModelLoader, CheckpointLoaderSimple, easy loraStack, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, INTConstant, INTConstant, LTXVAddGuideMulti, LTXVAddGuideMulti, CLIPTextEncode, MarkdownNote, VHS_VideoCombine, Fast Groups Muter (rgthree), PrimitiveNode, PromptRelayEncodeTimeline, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 313}
---

# 视频生成/图生视频/LTX2.3 多图剧情视频图生视频 批量生视频 超长时间 编导时间线提示词修改版_2062395094396919810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062395094396919810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（128 个）：
- `ResizeImagesByLongerEdge`
- `SetNode`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `SetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `INTConstant`
- `INTConstant`
- `easy loraStackApply`
- `RandomNoise`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `easy loraStack`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`
- `PrimitiveNode`
- `PromptRelayEncodeTimeline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `width` = `313`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **52%**（66/128）

**有卡**：`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ResizeImageMaskNode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVConditioning`、`CFGGuider`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`RandomNoise`、`SamplerCustomAdvanced`、`LTX2SamplingPreviewOverride`、`INTConstant`、`easy loraStackApply`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`easy loraStack`、`LTXVAddGuideMulti`、`CLIPTextEncode`、`VHS_VideoCombine`、`PromptRelayEncodeTimeline`、`LoadImage`

**用到的条目**：VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
