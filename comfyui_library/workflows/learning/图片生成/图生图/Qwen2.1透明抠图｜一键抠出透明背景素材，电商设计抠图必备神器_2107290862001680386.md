---
key: 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json
name: Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json
hash: 87e0cb0795038cf0
coverage: 0.818182
learned_at: 2026-10-06 21:42:27
nodes: [SaveImage, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [BasicGuider, QwenImage21FunPDDLoader, RandomNoise, SamplerCustomAdvanced, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识, 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识, 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（55 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `BasicGuider`
- `QwenImage21FunPDDLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PrimitiveInt`
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

覆盖率 **82%**（45/55）

**有卡**：`SaveImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`

**缺卡**（5）：`BasicGuider`、`QwenImage21FunPDDLoader`、`RandomNoise`、`SamplerCustomAdvanced`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21FunPDDLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识
- 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
