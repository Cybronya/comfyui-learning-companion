---
key: 视频生成/文生视频/LTX-2.3 三模对比满编生产套件 2.0｜Distilled + Dev-Dare + VAVR_2051703959529771010.json
name: LTX-2.3 三模对比满编生产套件 2.0｜Distilled + Dev-Dare + VAVR_2051703959529771010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3 三模对比满编生产套件 2.0｜Distilled + Dev-Dare + VAVR_2051703959529771010.json
hash: 2a772bacab64c09b
coverage: 0.944099
learned_at: 2026-10-11 19:49:35
nodes: [image_scale_pixel_v2, PrimitiveFloat, easy showAnything, KepStringLiteral, RH_Translator, RH_Translator, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, PrimitiveBoolean, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, PrimitiveBoolean, LatentUpscaleModelLoader, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, PrimitiveBoolean, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVAudioVAELoader, LTXVAudioVAELoader, RandomNoise, RandomNoise, RandomNoise, RandomNoise, RandomNoise, RandomNoise, RandomNoise, RandomNoise, RandomNoise, CM_FloatToInt, CM_FloatToInt, CM_FloatToInt, LayerUtility: PurgeVRAM V2, VRAMReserver, VRAMReserver, LayerUtility: PurgeVRAM V2, VRAMReserver, LayerUtility: PurgeVRAM V2, Image_Resize_longsize, Image_Resize_longsize, Image_Resize_longsize, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVEmptyLatentAudio, LTXVEmptyLatentAudio, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLTXVLatentVideo, EmptyLTXVLatentVideo, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, PromptRelayEncode, PromptRelayEncode, PromptRelayEncode, LTXVConcatAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, LTX2_NAG, LTXVConditioning, LTX2_NAG, LTXVConditioning, LTX2_NAG, LTXVConditioning, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVLatentUpsampler, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVLatentUpsampler, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, CreateVideo, CreateVideo, DisTorchPurgeVRAMV2, DisTorchPurgeVRAMV2, DisTorchPurgeVRAMV2, SamplerCustomAdvanced, SaveVideo, KepStringLiteral, PrimitiveInt, KepStringLiteral, easy showAnything, SaveVideo, SaveVideo, RH_Translator, easy showAnything, LoadImage, Seed Everywhere]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Seed Everywhere]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX-2.3 三模对比满编生产套件 2.0｜Distilled + Dev-Dare + VAVR_2051703959529771010.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3 三模对比满编生产套件 2.0｜Distilled + Dev-Dare + VAVR_2051703959529771010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（161 个）：
- `image_scale_pixel_v2`
- `PrimitiveFloat`
- `easy showAnything`
- `KepStringLiteral`
- `RH_Translator`
- `RH_Translator`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveBoolean`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveBoolean`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveBoolean`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVAudioVAELoader`
- `LTXVAudioVAELoader`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `CM_FloatToInt`
- `CM_FloatToInt`
- `CM_FloatToInt`
- `LayerUtility: PurgeVRAM V2`
- `VRAMReserver`
- `VRAMReserver`
- `LayerUtility: PurgeVRAM V2`
- `VRAMReserver`
- `LayerUtility: PurgeVRAM V2`
- `Image_Resize_longsize`
- `Image_Resize_longsize`
- `Image_Resize_longsize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `EmptyLTXVLatentVideo`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `PromptRelayEncode`
- `PromptRelayEncode`
- `PromptRelayEncode`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVConditioning`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CreateVideo`
- `CreateVideo`
- `DisTorchPurgeVRAMV2`
- `DisTorchPurgeVRAMV2`
- `DisTorchPurgeVRAMV2`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `KepStringLiteral`
- `PrimitiveInt`
- `KepStringLiteral`
- `easy showAnything`
- `SaveVideo`
- `SaveVideo`
- `RH_Translator`
- `easy showAnything`
- `LoadImage`
- `Seed Everywhere`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（152/161）

**有卡**：`image_scale_pixel_v2`、`KepStringLiteral`、`RH_Translator`、`KSamplerSelect`、`ManualSigmas`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`RandomNoise`、`CM_FloatToInt`、`VRAMReserver`、`Image_Resize_longsize`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`PromptRelayEncode`、`LTXVConcatAVLatent`、`LTX2_NAG`、`LTXVConditioning`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`DisTorchPurgeVRAMV2`、`SaveVideo`、`LoadImage`

**缺卡**（4）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
