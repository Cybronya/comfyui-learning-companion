---
key: 视频生成/图生视频/MiniMax_H3_FL2AV_BF16_LightX2V_1.0正式版8步加速V2，图生视频方案_2110532111202603010.json
name: MiniMax_H3_FL2AV_BF16_LightX2V_1.0正式版8步加速V2，图生视频方案_2110532111202603010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax_H3_FL2AV_BF16_LightX2V_1.0正式版8步加速V2，图生视频方案_2110532111202603010.json
hash: f63d24b22d9c48e9
coverage: 0.943396
learned_at: 2026-10-18 00:23:30
nodes: [KSamplerSelect, BasicGuider, SamplerCustomAdvanced, MiniMaxH3ImageToVideo, VAEDecode, BasicScheduler, VAELoader, VAELoader, CLIPLoader, Int, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, EnhancedLoadDiffusionModel, RandomNoise, VAEDecodeAudio, CreateVideo, LoadImage, LoadImage, Text, SaveVideo, VHS_VideoCombine, RHHiddenNodes, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax_H3_FL2AV_BF16_LightX2V_1.0正式版8步加速V2，图生视频方案_2110532111202603010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax_H3_FL2AV_BF16_LightX2V_1.0正式版8步加速V2，图生视频方案_2110532111202603010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ImageToVideo`
- `VAEDecode` ★核心
- `BasicScheduler`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `EnhancedLoadDiffusionModel`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `Text`
- `SaveVideo`
- `VHS_VideoCombine`
- `RHHiddenNodes`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **94%**（50/53）

**有卡**：`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`BasicScheduler`、`VAELoader`、`CLIPLoader`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`EnhancedLoadDiffusionModel`、`RandomNoise`、`VAEDecodeAudio`、`CreateVideo`、`LoadImage`、`Text`、`SaveVideo`、`VHS_VideoCombine`、`RHHiddenNodes`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
