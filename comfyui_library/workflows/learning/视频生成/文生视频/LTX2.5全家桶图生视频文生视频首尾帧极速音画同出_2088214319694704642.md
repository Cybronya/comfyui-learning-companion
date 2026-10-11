---
key: 视频生成/文生视频/LTX2.5全家桶图生视频文生视频首尾帧极速音画同出_2088214319694704642.json
name: LTX2.5全家桶图生视频文生视频首尾帧极速音画同出_2088214319694704642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5全家桶图生视频文生视频首尾帧极速音画同出_2088214319694704642.json
hash: 76b3a3fb7c67e575
coverage: 0.833333
learned_at: 2026-10-11 20:53:38
nodes: [PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ComfySwitchNode, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, PreviewAny, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, PrimitiveBoolean, VHS_VideoCombine, VHS_VideoCombine, ComfySwitchNode, LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, CLIPTextEncode, PrimitiveInt, ResolutionSelector, TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPLoader, PrimitiveStringMultiline, VHS_VideoCombine, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, TextGenerateLTX2Prompt, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, LTXVPreprocess, GetImageSize, CLIPLoader, ComfySwitchNode, PreviewAny, LoadImage, PrimitiveBoolean, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), PrimitiveInt, LoadImage, ResolutionSelector, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ResizeImageMaskNode, ComfyMathExpression, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.5全家桶图生视频文生视频首尾帧极速音画同出_2088214319694704642.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5全家桶图生视频文生视频首尾帧极速音画同出_2088214319694704642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（168 个）：
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
- `PrimitiveInt`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **83%**（140/168）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`TextGenerateLTX2Prompt`、`VHS_VideoCombine`、`ResolutionSelector`、`LTXVAddGuide`、`LTXVCropGuides`、`SamplerEulerAncestral`、`GetImageSize`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`VAEDecode`、`EmptyLatentImage`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
