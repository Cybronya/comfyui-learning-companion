---
key: 视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946.json
name: AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946.json
hash: 131d6158ae15200e
coverage: 0.890411
learned_at: 2026-10-10 22:51:49
nodes: [MiniMaxChunkFeedForward, CLIPLoader, VAELoader, VAELoader, VAEDecode, MiniMaxLowVRAMAttention, Reroute, SoundFlow_GetLength, ComfyMathExpression, ComfyNumberConvert, PreviewAny, LTXVSeparateAVLatent, ConditioningZeroOut, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LoadImage, KSamplerSelect, TrimAudioDuration, LoadAudio, PrimitiveFloat, PrimitiveFloat, ResolutionSelector, LoadImage, Textbox, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, BasicScheduler, LTXVSeparateAVLatent, LTXVAudioVAEEncode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI音乐MV数字人新二采Separate AV Latent加Minimax H_2105763503423442946.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（73 个）：
- `MiniMaxChunkFeedForward`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `MiniMaxLowVRAMAttention`
- `Reroute`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `PreviewAny`
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LoadImage`
- `KSamplerSelect` ★核心
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
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

**有卡**：`MiniMaxChunkFeedForward`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`MiniMaxLowVRAMAttention`、`SoundFlow_GetLength`、`ComfyMathExpression`、`ComfyNumberConvert`、`LTXVSeparateAVLatent`、`ConditioningZeroOut`、`SolidMask`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`LoadImage`、`KSamplerSelect`、`TrimAudioDuration`、`LoadAudio`、`ResolutionSelector`、`Textbox`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`ModelAttentionBackend`、`UNETLoader`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`BasicScheduler`、`LTXVAudioVAEEncode`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
