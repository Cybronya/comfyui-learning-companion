---
key: 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json
name: Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json
hash: 704dbfd0dbfcbde5
coverage: 0.636364
learned_at: 2026-10-06 21:49:33
nodes: [SaveImage, Note, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, TextEncodeQwenImageEditPlus, EmptySD3LatentImage, KSampler, VAEDecode]
patterns: []
missing: [TextEncodeQwenImageEditPlus]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 24}
discoveries: [次要节点 `TextEncodeQwenImageEditPlus` 仅有 VAE 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `SaveImage`
- `Note`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `42`
- `steps` = `24`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（7/11）

**有卡**：`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`

**缺卡**（1）：`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage、sd15-t2i-basic

## 学习发现

- 次要节点 `TextEncodeQwenImageEditPlus` 仅有 VAE 的通用知识，没有该节点自己的说明
