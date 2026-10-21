---
key: 图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json
name: Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json
hash: 66989a3ef972bac6
coverage: 0.882353
learned_at: 2026-10-21 00:42:15
nodes: [UNETLoader, CLIPLoader, VAELoader, XinbaoImageStandardizer, Text Multiline, Text Find and Replace, TextEncodeQwenImage21, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ComfySwitchNode, 孤海注释, EmptyLatentImage, VAEDecode, LoadImage, Text Multiline, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1200, "sampler_name": "euler", "scheduler": "simple", "seed": 1048750720469404, "steps": 25, "width": 1200}
---

# 图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `XinbaoImageStandardizer`
- `Text Multiline`
- `Text Find and Replace`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `孤海注释`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `Text Multiline`
- `SaveImage`

## 关键参数

- `seed` = `1048750720469404`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1200`
- `height` = `1200`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`XinbaoImageStandardizer`、`Text Multiline`、`Text Find and Replace`、`TextEncodeQwenImage21`、`KSampler`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
