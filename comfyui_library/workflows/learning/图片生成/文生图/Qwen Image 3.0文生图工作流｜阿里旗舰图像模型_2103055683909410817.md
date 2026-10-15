---
key: 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json
name: Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json
hash: 704dbfd0dbfcbde5
coverage: 0.818182
learned_at: 2026-10-10 20:58:54
nodes: [SaveImage, Note, PrimitiveStringMultiline, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, TextEncodeQwenImageEditPlus, EmptySD3LatentImage, KSampler, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 24}
---

# 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json`

## 结构

**节点**（11 个）：
- `SaveImage`
- `Note`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `TextEncodeQwenImageEditPlus`
- `EmptySD3LatentImage`
- `KSampler`
- `VAEDecode`

## 关键参数

- `cfg` = `2.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `42`
- `steps` = `24`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`SaveImage`、`Note`、`PrimitiveStringMultiline`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`TextEncodeQwenImageEditPlus`、`EmptySD3LatentImage`
