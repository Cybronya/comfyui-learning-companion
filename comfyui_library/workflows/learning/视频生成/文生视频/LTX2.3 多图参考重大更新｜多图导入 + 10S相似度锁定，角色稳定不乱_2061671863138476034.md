---
key: 视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json
name: LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json
hash: 3ff2e6c1f275f2b2
coverage: 0.912621
learned_at: 2026-10-11 20:21:26
nodes: [VRAMReserver, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, RandomNoise, RandomNoise, CM_FloatToInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTX2_NAG, LTXVConditioning, EmptyLTXVLatentVideo, LTXVLatentUpsampler, Seed Everywhere, CLIPTextEncode, LatentUpscaleModelLoader, PrimitiveFloat, PrimitiveFloat, LTXVAddGuideMulti, LTXVPreprocess, GetImageSize+, PrimitiveFloat, Int, Int, Int, PrimitiveFloat, LTXVPreprocess, PrimitiveInt, PrimitiveFloat, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVAddGuideMulti, LTXVSeparateAVLatent, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, image_scale_pixel_v2, image_scale_pixel_v2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LTXVPreprocess, LTXVPreprocess, PromptRelaySmartEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ManualSigmas, LTXFaceDetector, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, Sigmas Easing, STGGuiderAdvanced, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, LTXLikenessGuide, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LoadImage, LoadImage, Int, LTXVAddGuideMulti, LoadImage, LoadImage, Text, Text, LTXVSeparateAVLatent, VAEDecodeTiled, JWImageSequenceExtractFromBatch]
patterns: []
missing: [Sigmas Easing, GetImageSize+, Seed Everywhere]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 多图参考重大更新｜多图导入 + 10S相似度锁定，角色稳定不乱_2061671863138476034.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `VRAMReserver`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `RandomNoise`
- `CM_FloatToInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `Seed Everywhere`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAddGuideMulti`
- `LTXVPreprocess`
- `GetImageSize+`
- `PrimitiveFloat`
- `Int`
- `Int`
- `Int`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `PrimitiveInt`
- `PrimitiveFloat`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVAddGuideMulti`
- `LTXVSeparateAVLatent`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `image_scale_pixel_v2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PromptRelaySmartEncode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `LTXFaceDetector`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `Sigmas Easing`
- `STGGuiderAdvanced`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LTXLikenessGuide`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `Int`
- `LTXVAddGuideMulti`
- `LoadImage`
- `LoadImage`
- `Text`
- `Text`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `JWImageSequenceExtractFromBatch`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **91%**（94/103）

**有卡**：`VRAMReserver`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`CM_FloatToInt`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`LTXVAddGuideMulti`、`LTXVPreprocess`、`Int`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`Text`、`LoraLoaderModelOnly`、`image_scale_pixel_v2`、`ImageResizeKJv2`、`PromptRelaySmartEncode`、`LTXFaceDetector`、`LTXLikenessGuide`、`LTXLatentAnchorAware`、`LTXLikenessAnchor`、`STGGuiderAdvanced`、`LTXICLoRALoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`、`JWImageSequenceExtractFromBatch`

**缺卡**（3）：`Sigmas Easing`、`GetImageSize+`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Sigmas Easing` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
