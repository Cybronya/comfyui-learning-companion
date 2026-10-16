---
key: 视频生成/图生视频/LTX2.3 1080P 50帧率图生视频_2D动漫循环动态壁纸_2073419735643021314.json
name: LTX2.3 1080P 50帧率图生视频_2D动漫循环动态壁纸_2073419735643021314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073419735643021314.json
hash: 48ab71c846a67f85
coverage: 0.9375
learned_at: 2026-10-15 22:41:06
nodes: [VAELoader, SimpleMath+, CFGGuider, PrimitiveInt, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, DualCLIPLoader, SimpleMath+, RandomNoise, RandomNoise, EmptyLTXVLatentVideo, CLIPTextEncode, llama_cpp_parameters, easy seed, CFGGuider, LTXVAudioVAEDecode, easy getNode, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVEmptyLatentAudio, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, UNETLoader, easy int, ImpactConditionalBranch, LTX2SamplingPreviewOverride, LTX2_NAG, LatentUpscaleModelLoader, easy anythingIndexSwitch, LTXVImgToVideoInplaceKJ, LTXVScheduler, GetImageSize, VAELoader, VAEDecode, KSamplerSelect, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVCropGuides, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVImgToVideoInplaceKJ, easy setNode, LoraLoaderModelOnly, GetImageSize, ImageScaleToTotalPixels, ImageScaleBy, EmptyImage, LTXVLatentUpsampler, LTXVCropGuides, LoraLoaderModelOnly, CM_BoolToInt, CM_IntToFloat, SimpleMath+, llama_cpp_model_loader, CR Text, CR Text, llama_cpp_instruct_adv, PrimitiveInt, PrimitiveInt, AnyBooleanSwitch, PrimitiveBoolean, ImageResizeKJv2, LoadImage, easy boolean, easy boolean, PrimitiveBoolean, ShowText|pysssss, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 1080P 50帧率图生视频_2D动漫循环动态壁纸_2073419735643021314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073419735643021314.json`

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
- `easy seed`
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
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `easy int`
- `ImpactConditionalBranch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LatentUpscaleModelLoader`
- `easy anythingIndexSwitch`
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
- `LTXVImgToVideoInplaceKJ`
- `easy setNode`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageScaleBy`
- `EmptyImage`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `CM_BoolToInt`
- `CM_IntToFloat`
- `SimpleMath+`
- `llama_cpp_model_loader`
- `CR Text`
- `CR Text`
- `llama_cpp_instruct_adv`
- `PrimitiveInt`
- `PrimitiveInt`
- `AnyBooleanSwitch`
- `PrimitiveBoolean`
- `ImageResizeKJv2`
- `LoadImage`
- `easy boolean`
- `easy boolean`
- `PrimitiveBoolean`
- `ShowText|pysssss`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（75/80）

**有卡**：`VAELoader`、`SimpleMath+`、`CFGGuider`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`DualCLIPLoader`、`RandomNoise`、`EmptyLTXVLatentVideo`、`llama_cpp_parameters`、`easy seed`、`LTXVAudioVAEDecode`、`easy getNode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`UNETLoader`、`easy int`、`ImpactConditionalBranch`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LatentUpscaleModelLoader`、`easy anythingIndexSwitch`、`LTXVImgToVideoInplaceKJ`、`LTXVScheduler`、`GetImageSize`、`VAEDecode`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`easy setNode`、`ImageScaleToTotalPixels`、`ImageScaleBy`、`EmptyImage`、`LTXVLatentUpsampler`、`CM_BoolToInt`、`CM_IntToFloat`、`llama_cpp_model_loader`、`CR Text`、`llama_cpp_instruct_adv`、`AnyBooleanSwitch`、`PrimitiveBoolean`、`ImageResizeKJv2`、`LoadImage`、`easy boolean`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
