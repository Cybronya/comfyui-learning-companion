---
key: 视频生成/文生视频/『最优实现』LTX 2.3 双人对话增强版_2048727968108781570.json
name: 『最优实现』LTX 2.3 双人对话增强版_2048727968108781570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 双人对话增强版_2048727968108781570.json
hash: 7f433bc2f86cc0b0
coverage: 0.964286
learned_at: 2026-10-15 22:47:38
nodes: [CLIPTextEncode, image_scale_pixel_v2, PrimitiveFloat, LayerUtility: PurgeVRAM V2, CheckpointLoaderSimple, LoraLoaderModelOnly, Seed Everywhere, LoadImage, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, LTXVAudioVAELoader, LatentUpscaleModelLoader, PrimitiveBoolean, RandomNoise, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CM_FloatToInt, Image_Resize_longsize, LTXVEmptyLatentAudio, LTXVConditioning, LTX2_NAG, LTXVConcatAVLatent, CFGGuider, CFGGuider, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, DisTorchPurgeVRAMV2, LTXVPreprocess, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncode, VRAMReserver, PathchSageAttentionKJ, VAEDecodeTiled, SaveVideo, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/『最优实现』LTX 2.3 双人对话增强版_2048727968108781570.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 双人对话增强版_2048727968108781570.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPTextEncode` ★核心
- `image_scale_pixel_v2`
- `PrimitiveFloat`
- `LayerUtility: PurgeVRAM V2`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Seed Everywhere`
- `LoadImage`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `PrimitiveBoolean`
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `Image_Resize_longsize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
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
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `DisTorchPurgeVRAMV2`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`
- `VRAMReserver`
- `PathchSageAttentionKJ`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（54/56）

**有卡**：`CLIPTextEncode`、`image_scale_pixel_v2`、`LayerUtility: PurgeVRAM V2`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`Seed Everywhere`、`LoadImage`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`PrimitiveBoolean`、`RandomNoise`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`Image_Resize_longsize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTX2_NAG`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEDecode`、`CreateVideo`、`DisTorchPurgeVRAMV2`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`VRAMReserver`、`PathchSageAttentionKJ`、`VAEDecodeTiled`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
