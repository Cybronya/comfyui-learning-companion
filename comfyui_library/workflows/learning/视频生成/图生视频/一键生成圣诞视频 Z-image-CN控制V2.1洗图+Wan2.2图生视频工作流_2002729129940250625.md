---
key: 视频生成/图生视频/一键生成圣诞视频 Z-image-CN控制V2.1洗图+Wan2.2图生视频工作流_2002729129940250625.json
name: 一键生成圣诞视频 Z-image-CN控制V2.1洗图+Wan2.2图生视频工作流_2002729129940250625.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/一键生成圣诞视频 Z-image-CN控制V2.1洗图+Wan2.2图生视频工作流_2002729129940250625.json
hash: 7089af891870b51f
coverage: 0.8
learned_at: 2026-10-15 22:33:49
nodes: [GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, QwenImageDiffsynthControlnet, ModelPatchLoader, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, Fast Groups Bypasser (rgthree), PreviewImage, ModelSamplingAuraFlow, VAEDecode, SetNode, KSampler, ConditioningZeroOut, CLIPLoader, UNETLoader, VAELoader, Fast Groups Bypasser (rgthree), GetNode, EmptySD3LatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, VAELoader, CLIPLoader, Fast Groups Bypasser (rgthree), PreviewImage, WanImageToVideo, WanMoeKSampler, VAEDecode, PlaySound|pysssss, Note, Note, LoadImage, CLIPTextEncode, UNETLoader, AIO_Preprocessor, LoadImage, CLIPTextEncode, CLIPTextEncode, MarkdownNote, ImageResizeKJv2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 7, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/一键生成圣诞视频 Z-image-CN控制V2.1洗图+Wan2.2图生视频工作流_2002729129940250625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2002729129940250625.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SetNode`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `WanImageToVideo`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `Note`
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ImageResizeKJv2`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **80%**（40/50）

**有卡**：`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingAuraFlow`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`CLIPTextEncode`、`WanImageToVideo`、`WanMoeKSampler`、`PlaySound|pysssss`、`LoadImage`、`AIO_Preprocessor`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
