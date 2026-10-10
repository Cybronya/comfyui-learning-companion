---
key: 视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json
name: AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json
hash: d740f617ab3b3cd4
coverage: 0.885246
learned_at: 2026-10-10 22:58:38
nodes: [ModelAttentionBackend, MiniMaxLowVRAMAttention, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, MiniMaxH3ReferenceToVideo, BasicScheduler, SolidMask, KSamplerSelect, MiniMaxChunkFeedForward, LTXVConcatAVLatent, UNETLoader, CLIPLoader, VAELoader, VAELoader, ConditioningZeroOut, LoraLoaderModelOnly, PreviewAny, Reroute, LoadImage, SelfLiftAvatarH3Sampler, ResolutionSelector, Text Multiline, TrimAudioDuration, ComfyNumberConvert, SoundFlow_GetLength, ComfyMathExpression, VHS_VideoCombine, LTXVSeparateAVLatent, VAEDecode, LoadAudio, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: [Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（61 个）：
- `ModelAttentionBackend`
- `MiniMaxLowVRAMAttention`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `MiniMaxH3ReferenceToVideo`
- `BasicScheduler`
- `SolidMask`
- `KSamplerSelect` ★核心
- `MiniMaxChunkFeedForward`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `Reroute`
- `LoadImage`
- `SelfLiftAvatarH3Sampler` ★核心
- `ResolutionSelector`
- `Text Multiline`
- `TrimAudioDuration`
- `ComfyNumberConvert`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LoadAudio`
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

覆盖率 **89%**（54/61）

**有卡**：`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`SolidMask`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`LTXVConcatAVLatent`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`LoadImage`、`SelfLiftAvatarH3Sampler`、`ResolutionSelector`、`TrimAudioDuration`、`ComfyNumberConvert`、`SoundFlow_GetLength`、`ComfyMathExpression`、`VHS_VideoCombine`、`VAEDecode`、`LoadAudio`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**缺卡**（1）：`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
