---
key: 视频生成/图生视频/LTX2.3 1080P 50帧率图生视频_2D动漫循环动态壁纸_2049604629536710658.json
name: LTX2.3 1080P 50帧率图生视频_2D动漫循环动态壁纸_2049604629536710658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2049604629536710658.json
hash: 44174c404839dd34
coverage: 0.9375
learned_at: 2026-10-15 22:37:15
nodes: [VAELoader, SimpleMath+, CFGGuider, PrimitiveInt, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, DualCLIPLoader, SimpleMath+, RandomNoise, RandomNoise, EmptyLTXVLatentVideo, CLIPTextEncode, llama_cpp_parameters, llama_cpp_model_loader, easy seed, PrimitiveBoolean, CFGGuider, LTXVAudioVAEDecode, easy getNode, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVEmptyLatentAudio, MarkdownNote, LoraLoaderModelOnly, AnyBooleanSwitch, LoraLoaderModelOnly, VAELoaderKJ, ImageResizeKJv2, UNETLoader, easy int, llama_cpp_instruct_adv, ImpactConditionalBranch, LTX2SamplingPreviewOverride, LTX2_NAG, LatentUpscaleModelLoader, easy anythingIndexSwitch, easy boolean, LTXVImgToVideoInplaceKJ, LTXVScheduler, GetImageSize, VAELoader, VAEDecode, KSamplerSelect, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVCropGuides, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveBoolean, PrimitiveInt, CR Text, LTXVImgToVideoInplaceKJ, easy setNode, LoraLoaderModelOnly, GetImageSize, ImageScaleToTotalPixels, ImageScaleBy, EmptyImage, LTXVLatentUpsampler, LTXVCropGuides, PrimitiveInt, LoadImage, CR Text, LoraLoaderModelOnly, CM_BoolToInt, CM_IntToFloat, SimpleMath+, easy boolean, ShowText|pysssss, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 1080P 50帧率图生视频_2D动漫循环动态壁纸_2049604629536710658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049604629536710658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（80 个）：
- `VAELoader`
- `SimpleMath+`
- `CFGGuider`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `DualCLIPLoader`
- `SimpleMath+`
- `RandomNoise`
- `RandomNoise`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `easy seed`
- `PrimitiveBoolean`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `easy getNode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `AnyBooleanSwitch`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `easy int`
- `llama_cpp_instruct_adv`
- `ImpactConditionalBranch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LatentUpscaleModelLoader`
- `easy anythingIndexSwitch`
- `easy boolean`
- `LTXVImgToVideoInplaceKJ`
- `LTXVScheduler`
- `GetImageSize`
- `VAELoader`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `CR Text`
- `LTXVImgToVideoInplaceKJ`
- `easy setNode`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageScaleBy`
- `EmptyImage`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `PrimitiveInt`
- `LoadImage`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `CM_BoolToInt`
- `CM_IntToFloat`
- `SimpleMath+`
- `easy boolean`
- `ShowText|pysssss`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（75/80）

**有卡**：`VAELoader`、`SimpleMath+`、`CFGGuider`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`RandomNoise`、`EmptyLTXVLatentVideo`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`easy seed`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`easy getNode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`AnyBooleanSwitch`、`VAELoaderKJ`、`ImageResizeKJv2`、`UNETLoader`、`easy int`、`llama_cpp_instruct_adv`、`ImpactConditionalBranch`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LatentUpscaleModelLoader`、`easy anythingIndexSwitch`、`easy boolean`、`LTXVImgToVideoInplaceKJ`、`LTXVScheduler`、`GetImageSize`、`VAEDecode`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`CR Text`、`easy setNode`、`ImageScaleToTotalPixels`、`ImageScaleBy`、`EmptyImage`、`LTXVLatentUpsampler`、`LoadImage`、`CM_BoolToInt`、`CM_IntToFloat`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
