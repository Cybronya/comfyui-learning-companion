---
key: 图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538.json
name: bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538.json
hash: 80fa5222077f711a
coverage: 0.919355
learned_at: 2026-10-21 00:45:07
nodes: [CLIPTextEncode, PathchSageAttentionKJ, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, CLIPLoader, CLIPTextEncode, INTConstant, INTConstant, KSamplerSelect, SplitSigmas, VAELoader, SaveVideo, BatchImagesNode, ImageFromBatch, VHS_VideoCombine, CreateVideo, Int, SamplerCustom, VAEDecode, SamplerCustom, GetVideoComponents, SimpleMath+, LoadImage, CR Text, ImageConcanate, ImageConcanate, BerniniConditioning, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadVideo, UNETLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `VAELoader`
- `SaveVideo`
- `BatchImagesNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `CreateVideo`
- `Int`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `GetVideoComponents`
- `SimpleMath+`
- `LoadImage`
- `CR Text`
- `ImageConcanate`
- `ImageConcanate`
- `BerniniConditioning`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `UNETLoader` ★核心
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

覆盖率 **92%**（57/62）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`CLIPLoader`、`INTConstant`、`KSamplerSelect`、`SplitSigmas`、`VAELoader`、`SaveVideo`、`BatchImagesNode`、`ImageFromBatch`、`VHS_VideoCombine`、`CreateVideo`、`Int`、`SamplerCustom`、`VAEDecode`、`GetVideoComponents`、`SimpleMath+`、`LoadImage`、`CR Text`、`ImageConcanate`、`BerniniConditioning`、`LoadVideo`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
