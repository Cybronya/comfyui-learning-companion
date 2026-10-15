---
key: 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json
name: LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json
hash: 7e489be1f9fefb80
coverage: 0.964912
learned_at: 2026-10-15 22:44:32
nodes: [PrimitiveInt, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, PrimitiveBoolean, RandomNoise, RandomNoise, RandomNoise, CM_FloatToInt, Image_Resize_longsize, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, CFGGuider, CFGGuider, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, DisTorchPurgeVRAMV2, LTXVImgToVideoConditionOnly, SaveVideo, EmptyLTXVLatentVideo, PromptRelayEncode, LTXVConditioning, LTX2_NAG, VRAMReserver, Seed Everywhere, LoadImage, image_scale_pixel_v2, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, CLIPTextEncode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTXVAudioVAELoader, Text, Text, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜Dev-Dare 三阶渲染增强版_2051714493138382849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `CM_FloatToInt`
- `Image_Resize_longsize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `DisTorchPurgeVRAMV2`
- `LTXVImgToVideoConditionOnly`
- `SaveVideo`
- `EmptyLTXVLatentVideo`
- `PromptRelayEncode`
- `LTXVConditioning`
- `LTX2_NAG`
- `VRAMReserver`
- `Seed Everywhere`
- `LoadImage`
- `image_scale_pixel_v2`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `Text`
- `Text`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`

## 知识

覆盖率 **96%**（55/57）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`PrimitiveBoolean`、`RandomNoise`、`CM_FloatToInt`、`Image_Resize_longsize`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`DisTorchPurgeVRAMV2`、`SaveVideo`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`LTXVConditioning`、`LTX2_NAG`、`VRAMReserver`、`Seed Everywhere`、`LoadImage`、`image_scale_pixel_v2`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
