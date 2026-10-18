---
key: 视频生成/图生视频/LTX2.3-视频参考生成超分720P加速版_2031927472920469506.json
name: LTX2.3-视频参考生成超分720P加速版_2031927472920469506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-视频参考生成超分720P加速版_2031927472920469506.json
hash: 5b6f81e5176c68fc
coverage: 0.67033
learned_at: 2026-10-15 22:35:33
nodes: [CFGGuider, KSamplerSelect, ResizeImageMaskNode, GetNode, GetNode, SetNode, LTXVPreprocess, PathchSageAttentionKJ, ResizeImagesByLongerEdge, ImageResizeKJv2, CannyEdgePreprocessor, DepthAnythingV2Preprocessor, GetNode, SetNode, INTConstant, SetNode, PrimitiveBoolean, INTConstant, VAELoaderKJ, DualCLIPLoader, SetNode, VAELoaderKJ, GetNode, LTXAddVideoICLoRAGuide, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ManualSigmas, Reroute, SetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, SolidMask, LTXVAudioVAEEncode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, SetLatentNoiseMask, Switch any [Crystools], LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, ManualSigmas, KSamplerSelect, RandomNoise, LTXVConditioning, GetNode, CLIPTextEncode, CLIPTextEncode, Text Multiline, Fast Groups Bypasser (rgthree), GetNode, GetNode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, PrimitiveFloat, ComfyMathExpression, SetNode, MathExpression|pysssss, ImageResizeAdvanced, SetNode, GetImageSize, SetNode, SetNode, SetNode, DWPreprocessor, ComfyMathExpression, GetNode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, RandomNoise, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVConcatAVLatent, GetNode, GetNode, VHS_VideoCombine, LTXICLoRALoaderModelOnly, GetNode, UNETLoader, INTConstant, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-视频参考生成超分720P加速版_2031927472920469506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031927472920469506.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（91 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `PathchSageAttentionKJ`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `CannyEdgePreprocessor`
- `DepthAnythingV2Preprocessor`
- `GetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `PrimitiveBoolean`
- `INTConstant`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ManualSigmas`
- `Reroute`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `Switch any [Crystools]`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `MathExpression|pysssss`
- `ImageResizeAdvanced`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LTXICLoRALoaderModelOnly` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `INTConstant`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（61/91）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ResizeImageMaskNode`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`CannyEdgePreprocessor`、`DepthAnythingV2Preprocessor`、`INTConstant`、`PrimitiveBoolean`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ManualSigmas`、`ComfyMathExpression`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`Switch any [Crystools]`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`RandomNoise`、`LTXVConditioning`、`CLIPTextEncode`、`Text Multiline`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`MathExpression|pysssss`、`ImageResizeAdvanced`、`GetImageSize`、`DWPreprocessor`、`LTXVImgToVideoConditionOnly`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXICLoRALoaderModelOnly`、`UNETLoader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、DepthAnythingV2Preprocessor、CannyEdgePreprocessor、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
