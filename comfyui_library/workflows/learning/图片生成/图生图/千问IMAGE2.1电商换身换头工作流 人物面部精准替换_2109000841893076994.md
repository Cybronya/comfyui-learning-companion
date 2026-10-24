---
key: 图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json
name: 千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json
hash: 670f42678a49107d
coverage: 0.811321
learned_at: 2026-10-23 12:29:48
nodes: [CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, SaveImage, EmptyLatentImage, PreviewImage, Anything Everywhere, Anything Everywhere, Anything Everywhere, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, TextEncodeQwenImage21, VAEDecode, LoadImage, LoadImage, PrimitiveStringMultiline, UNETLoader, Get resolution [Crystools], KSampler, KSampler, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问IMAGE2.1电商换身换头工作流 人物面部精准替换_2109000841893076994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `Get resolution [Crystools]`
- `KSampler` ★核心
- `KSampler` ★核心
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

覆盖率 **81%**（43/53）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`、`UNETLoader`、`Get resolution [Crystools]`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
