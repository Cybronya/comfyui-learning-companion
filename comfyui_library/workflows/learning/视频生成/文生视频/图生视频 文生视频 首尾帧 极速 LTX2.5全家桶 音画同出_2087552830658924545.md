---
key: 视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json
name: 图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json
hash: 34b68426c9a833ee
coverage: 0.822695
learned_at: 2026-10-15 22:48:23
nodes: [PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ComfySwitchNode, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, PreviewAny, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, PrimitiveBoolean, VHS_VideoCombine, VHS_VideoCombine, ComfySwitchNode, LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, CLIPTextEncode, PrimitiveInt, ResolutionSelector, TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPLoader, PrimitiveStringMultiline, VHS_VideoCombine, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, TextGenerateLTX2Prompt, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, LTXVPreprocess, GetImageSize, CLIPLoader, ComfySwitchNode, PreviewAny, LoadImage, PrimitiveBoolean, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MarkdownNote, PrimitiveInt, LoadImage, ResolutionSelector, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ResizeImageMaskNode, ComfyMathExpression]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（141 个）：
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ComfySwitchNode`
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ComfySwitchNode`
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `PreviewAny`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `GetImageSize`
- `CLIPLoader`
- `ComfySwitchNode`
- `PreviewAny`
- `LoadImage`
- `PrimitiveBoolean`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `PrimitiveInt`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `ComfyMathExpression`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（116/141）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`VHS_VideoCombine`、`ResolutionSelector`、`LTXVAddGuide`、`LTXVCropGuides`、`SamplerEulerAncestral`、`GetImageSize`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerSelect
