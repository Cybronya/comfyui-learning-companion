---
key: 视频生成/图生视频/LTX2.3多图引导生成工作流_2031935763281092609.json
name: LTX2.3多图引导生成工作流_2031935763281092609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3多图引导生成工作流_2031935763281092609.json
hash: 446d13bac7ae8670
coverage: 0.673684
learned_at: 2026-10-15 22:35:34
nodes: [ManualSigmas, Reroute, DualCLIPLoader, VAELoaderKJ, PrimitiveInt, PrimitiveInt, ComfyMathExpression, SolidMask, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImageMaskNode, GetNode, GetNode, GetNode, GetNode, LTXVPreprocess, LTXVPreprocess, SetNode, SetNode, SetNode, GetNode, LTXVPreprocess, GetNode, GetNode, INTConstant, SetNode, INTConstant, ResizeImagesByLongerEdge, ResizeImageMaskNode, GetNode, GetNode, LTXVPreprocess, SetNode, GetNode, GetNode, CFGGuider, CLIPTextEncode, CLIPTextEncode, PathchSageAttentionKJ, RandomNoise, KSamplerSelect, SetNode, easy showAnything, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, GetNode, ResizeImagesByLongerEdge, ComfyMathExpression, ComfyMathExpression, LTXVConditioning, LoraLoaderModelOnly, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, UNETLoader, PreviewAny, llama_cpp_model_loader, llama_cpp_instruct_adv, LTXVCropGuides, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, EmptyLTXVLatentVideo, VAELoaderKJ, LTXVImgToVideoInplaceKJ, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, INTConstant, ComfyMathExpression, Text Multiline, GetNode, ComfyMathExpression, ResizeImageMaskNode, ResizeImageMaskNode, VAEDecodeTiled, RIFEInterpolation, VHS_VideoCombine, Fast Groups Bypasser (rgthree), ComfyMathExpression, Note, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3多图引导生成工作流_2031935763281092609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031935763281092609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（95 个）：
- `ManualSigmas`
- `Reroute`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `SolidMask`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SetNode`
- `easy showAnything`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `UNETLoader` ★核心
- `PreviewAny`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LTXVCropGuides`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `INTConstant`
- `ComfyMathExpression`
- `Text Multiline`
- `GetNode`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `VAEDecodeTiled` ★核心
- `RIFEInterpolation`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `ComfyMathExpression`
- `Note`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（64/95）

**有卡**：`ManualSigmas`、`DualCLIPLoader`、`VAELoaderKJ`、`ComfyMathExpression`、`SolidMask`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`LTXVPreprocess`、`INTConstant`、`CFGGuider`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`LoraLoaderModelOnly`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`UNETLoader`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LTXVCropGuides`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`Text Multiline`、`VAEDecodeTiled`、`RIFEInterpolation`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
