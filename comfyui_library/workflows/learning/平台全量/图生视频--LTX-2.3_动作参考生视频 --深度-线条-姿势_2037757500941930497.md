---
key: 平台全量/图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497.json
name: 图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497.json
hash: f061706eebd65c92
coverage: 0.787234
learned_at: 2026-11-14 01:56:24
nodes: [VAELoaderKJ, VAELoaderKJ, LTXVAudioVAEDecode, LTXICLoRALoaderModelOnly, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, LTXVSeparateAVLatent, LTXVCropGuides, KSamplerSelect, ManualSigmas, RandomNoise, VAEDecodeTiled, UNETLoader, CLIPTextEncode, CLIPTextEncode, TextGenerateLTX2Prompt, PreviewAny, PreviewAny, PreviewAny, LTXVEmptyLatentAudio, SimpleMath+, GetImageSize, PreviewAny, PreviewAny, LTXVImgToVideoConditionOnly, PreviewAny, EmptyLTXVLatentVideo, VHS_VideoInfo, DualCLIPLoader, VHS_VideoCombine, LTXVPreprocess, PreviewImage, PreviewImage, PreviewImage, easy int, ResizeImageMaskNode, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, Note, LoadImage, DepthAnythingPreprocessor, CannyEdgePreprocessor, DWPreprocessor, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497.json

> 来源文件 `comfyui_library/workflows/平台全量/图生视频--LTX-2.3_动作参考生视频 --深度-线条-姿势_2037757500941930497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVAudioVAEDecode` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `GetImageSize`
- `PreviewAny`
- `PreviewAny`
- `LTXVImgToVideoConditionOnly`
- `PreviewAny`
- `EmptyLTXVLatentVideo`
- `VHS_VideoInfo`
- `DualCLIPLoader`
- `VHS_VideoCombine`
- `LTXVPreprocess`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `easy int`
- `ResizeImageMaskNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `Note`
- `LoadImage`
- `DepthAnythingPreprocessor`
- `CannyEdgePreprocessor`
- `DWPreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（37/47）

**有卡**：`VAELoaderKJ`、`LTXVAudioVAEDecode`、`LTXICLoRALoaderModelOnly`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`VAEDecodeTiled`、`UNETLoader`、`CLIPTextEncode`、`TextGenerateLTX2Prompt`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`GetImageSize`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`VHS_VideoInfo`、`DualCLIPLoader`、`VHS_VideoCombine`、`LTXVPreprocess`、`easy int`、`ResizeImageMaskNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`LoadImage`、`DepthAnythingPreprocessor`、`CannyEdgePreprocessor`、`DWPreprocessor`

**用到的条目**：CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader、CannyEdgePreprocessor、DepthAnythingPreprocessor、CFGGuider、KSamplerSelect
