---
key: 视频生成/图生视频/lightx2v_1.0正式版8步加速i2AV｜MInimaxH3图生视频工作流_2088174200824623105.json
name: lightx2v_1.0正式版8步加速i2AV｜MInimaxH3图生视频工作流_2088174200824623105
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/lightx2v_1.0正式版8步加速i2AV｜MInimaxH3图生视频工作流_2088174200824623105.json
hash: 62a8f42266ed8a9c
coverage: 0.914894
learned_at: 2026-10-16 21:27:54
nodes: [RandomNoise, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, EnhancedLoadDiffusionModel, VAELoader, LoraLoaderBypassModelOnly, Int, Text, RHHiddenNodes, LoadImage, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/lightx2v_1.0正式版8步加速i2AV｜MInimaxH3图生视频工作流_2088174200824623105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/lightx2v_1.0正式版8步加速i2AV｜MInimaxH3图生视频工作流_2088174200824623105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `EnhancedLoadDiffusionModel`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `Int`
- `Text`
- `RHHiddenNodes`
- `LoadImage`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **91%**（43/47）

**有卡**：`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ImageToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`EnhancedLoadDiffusionModel`、`LoraLoaderBypassModelOnly`、`Int`、`Text`、`RHHiddenNodes`、`LoadImage`、`VHS_VideoCombine`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
