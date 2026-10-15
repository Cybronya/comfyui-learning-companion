---
key: 视频生成/文生视频/MiniMax_H3全能导演台手动版V3.1｜文生视频图生视频_2100762286452461569.json
name: MiniMax_H3全能导演台手动版V3.1｜文生视频图生视频_2100762286452461569
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax_H3全能导演台手动版V3.1｜文生视频图生视频_2100762286452461569.json
hash: 025b6737f640271f
coverage: 0.936508
learned_at: 2026-10-15 22:46:31
nodes: [BasicGuider, UNETLoader, VAELoader, VAELoader, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy minimaxH3ToVideo, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, MiniMaxH3MultiRateSamplerEXPT8, CLIPLoader, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, easy matchLine, easy promptLine, easy multiTrackEditor, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax_H3全能导演台手动版V3.1｜文生视频图生视频_2100762286452461569.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax_H3全能导演台手动版V3.1｜文生视频图生视频_2100762286452461569.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（63 个）：
- `BasicGuider`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy minimaxH3ToVideo`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `easy matchLine`
- `easy promptLine`
- `easy multiTrackEditor`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **94%**（59/63）

**有卡**：`BasicGuider`、`UNETLoader`、`VAELoader`、`easy multiTrackInfoOutput`、`easy multiTrackTaskOutput`、`easy minimaxH3ToVideo`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`RandomNoise`、`MiniMaxH3MultiRateSamplerEXPT8`、`CLIPLoader`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`MiniMaxH3AVDecodeT8`、`easy matchLine`、`easy promptLine`、`easy multiTrackEditor`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
