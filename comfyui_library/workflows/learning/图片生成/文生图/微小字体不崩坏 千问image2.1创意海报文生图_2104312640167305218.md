---
key: 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json
name: 微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json
hash: 73237ed6656d2539
coverage: 0.837209
learned_at: 2026-10-07 01:58:34
nodes: [CLIPLoader, ShowText|pysssss, UNETLoader, VAELoader, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, Seed (rgthree), VAEDecode, SaveImageAdvanced, KSampler, SaveImage, QwenPERewriteT8, Text Multiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Text Multiline, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/微小字体不崩坏 千问image2.1创意海报文生图_2104312640167305218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（43 个）：
- `CLIPLoader`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `KSampler` ★核心
- `SaveImage`
- `QwenPERewriteT8`
- `Text Multiline`
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

覆盖率 **84%**（36/43）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`、`SaveImage`、`QwenPERewriteT8`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`Text Multiline`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
