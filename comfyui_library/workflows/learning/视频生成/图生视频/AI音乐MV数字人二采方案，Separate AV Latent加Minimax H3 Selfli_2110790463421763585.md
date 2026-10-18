---
key: 视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json
name: AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json
hash: a131d42820594a0a
coverage: 0.890411
learned_at: 2026-10-18 00:22:56
nodes: [MiniMaxChunkFeedForward, CLIPLoader, VAELoader, VAELoader, Reroute, SoundFlow_GetLength, ComfyMathExpression, ComfyNumberConvert, LTXVSeparateAVLatent, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LoadImage, TrimAudioDuration, LoadAudio, PrimitiveFloat, PrimitiveFloat, ResolutionSelector, LoadImage, Textbox, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, LTXVAudioVAEEncode, UNETLoader, LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, LTXVSeparateAVLatent, ConditioningZeroOut, BasicScheduler, PreviewAny, VAEDecode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI音乐MV数字人二采方案，Separate AV Latent加Minimax H3 Selfli_2110790463421763585.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（73 个）：
- `MiniMaxChunkFeedForward`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `Reroute`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `LTXVSeparateAVLatent`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LoadImage`
- `TrimAudioDuration`
- `LoadAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `Textbox`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `LTXVAudioVAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `BasicScheduler`
- `PreviewAny`
- `VAEDecode` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（65/73）

**有卡**：`MiniMaxChunkFeedForward`、`CLIPLoader`、`VAELoader`、`SoundFlow_GetLength`、`ComfyMathExpression`、`ComfyNumberConvert`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`LoadImage`、`TrimAudioDuration`、`LoadAudio`、`ResolutionSelector`、`Textbox`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`ModelAttentionBackend`、`LTXVAudioVAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`MiniMaxLowVRAMAttention`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
