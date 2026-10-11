---
key: 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json
name: LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json
hash: 55b1802f36ee9a93
coverage: 0.929825
learned_at: 2026-10-11 19:49:35
nodes: [PrimitiveInt, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, LTXVAudioVAELoader, PrimitiveBoolean, RandomNoise, RandomNoise, RandomNoise, CM_FloatToInt, Image_Resize_longsize, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, CFGGuider, CFGGuider, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, DisTorchPurgeVRAMV2, LTXVImgToVideoConditionOnly, SaveVideo, EmptyLTXVLatentVideo, PromptRelayEncode, LTXVConditioning, LTX2_NAG, VRAMReserver, Seed Everywhere, LoadImage, image_scale_pixel_v2, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LayerUtility: PurgeVRAM V2, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CLIPTextEncode, KepStringLiteral, KepStringLiteral, KepStringLiteral]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, Seed Everywhere]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 单双人数字人 2.0｜三阶渲染·极致打磨『最优实现』无音频版_2050915982742433793.json`

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
- `LTXVAudioVAELoader`
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
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `KepStringLiteral`
- `KepStringLiteral`
- `KepStringLiteral`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **93%**（53/57）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAELoader`、`PrimitiveBoolean`、`RandomNoise`、`CM_FloatToInt`、`Image_Resize_longsize`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`DisTorchPurgeVRAMV2`、`SaveVideo`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`LTXVConditioning`、`LTX2_NAG`、`VRAMReserver`、`LoadImage`、`image_scale_pixel_v2`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`KepStringLiteral`

**缺卡**（2）：`LayerUtility: PurgeVRAM V2`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
