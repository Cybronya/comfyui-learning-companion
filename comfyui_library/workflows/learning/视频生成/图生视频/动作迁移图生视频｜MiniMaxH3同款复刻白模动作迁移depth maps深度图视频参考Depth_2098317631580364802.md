---
key: 视频生成/图生视频/动作迁移图生视频｜MiniMaxH3同款复刻白模动作迁移depth maps深度图视频参考Depth_2098317631580364802.json
name: 动作迁移图生视频｜MiniMaxH3同款复刻白模动作迁移depth maps深度图视频参考Depth_2098317631580364802
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移图生视频｜MiniMaxH3同款复刻白模动作迁移depth maps深度图视频参考Depth_2098317631580364802.json
hash: 04c09b57d5552aef
coverage: 0.83871
learned_at: 2026-10-17 01:45:05
nodes: [VAELoader, VAELoader, KSamplerSelect, UNETLoader, CLIPLoader, RandomNoise, PrimitiveStringMultiline, PrimitiveStringMultiline, BasicScheduler, ComfyMathExpression, LoraLoaderModelOnly, ImageResizeKJv2, AILab_QwenVL, DF_Int_to_Float, JoinStrings, PathchSageAttentionKJ, JoinStrings, MiniMaxH3MemoryEfficientSageAttentionPatch, ImageResizeKJv2, ImageConcanate, MiniMaxH3ReferenceToVideo, BasicGuider, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, easy imageRemBg, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoadImage, 孤海注释, 孤海注释, VHS_LoadVideo, PrimitiveFloat]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/动作迁移图生视频｜MiniMaxH3同款复刻白模动作迁移depth maps深度图视频参考Depth_2098317631580364802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/动作迁移图生视频｜MiniMaxH3同款复刻白模动作迁移depth maps深度图视频参考Depth_2098317631580364802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `VAELoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `BasicScheduler`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `AILab_QwenVL`
- `DF_Int_to_Float`
- `JoinStrings`
- `PathchSageAttentionKJ`
- `JoinStrings`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ImageResizeKJv2`
- `ImageConcanate`
- `MiniMaxH3ReferenceToVideo`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `easy imageRemBg`
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
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `VHS_LoadVideo`
- `PrimitiveFloat`

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

覆盖率 **84%**（52/62）

**有卡**：`VAELoader`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`BasicScheduler`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`AILab_QwenVL`、`DF_Int_to_Float`、`JoinStrings`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ImageConcanate`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`VHS_VideoCombine`、`easy imageRemBg`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
