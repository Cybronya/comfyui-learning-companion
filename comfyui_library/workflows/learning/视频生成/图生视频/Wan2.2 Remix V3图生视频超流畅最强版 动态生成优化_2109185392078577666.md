---
key: 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109185392078577666.json
name: Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109185392078577666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109185392078577666.json
hash: 57560b055e7b8c08
coverage: 0.938462
learned_at: 2026-10-17 22:50:21
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, INTConstant, ImageScaleBy, easy cleanGpuUsed, RIFE VFI, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Text Concatenate, VHS_VideoCombine, VHS_VideoCombine, INTConstant, CR Text, Wan22PromptSelector, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109185392078577666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109185392078577666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `INTConstant`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `CR Text`
- `Wan22PromptSelector`
- `LoadImage`
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

覆盖率 **94%**（61/65）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`WanImageToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`INTConstant`、`ImageScaleBy`、`easy cleanGpuUsed`、`RIFE VFI`、`UNETLoader`、`Text Concatenate`、`VHS_VideoCombine`、`CR Text`、`Wan22PromptSelector`、`LoadImage`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
