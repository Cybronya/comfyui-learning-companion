---
key: 图片生成/图生图/Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777.json
name: Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777.json
hash: 63acc980d352991d
coverage: 0.8
learned_at: 2026-10-23 11:14:09
nodes: [Text Multiline, UNETLoader, CLIPLoader, Text Concatenate, VAELoader, LoraLoaderModelOnly, Seed (rgthree), TextEncodeQwenImage21, QwenImage21Cache, KSampler, GetNode, easy cleanGpuUsed, 孤海注释, SetNode, XinbaoImageStandardizer, XinbaoLightingCompanion, Image Comparer (rgthree), VAEDecode, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1109940380127346, "steps": 25}
---

# 图片生成/图生图/Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2111632736069963777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Text Multiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Text Concatenate`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `孤海注释`
- `SetNode`
- `XinbaoImageStandardizer`
- `XinbaoLightingCompanion`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `1109940380127346`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`Text Multiline`、`UNETLoader`、`CLIPLoader`、`Text Concatenate`、`VAELoader`、`LoraLoaderModelOnly`、`Seed (rgthree)`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`easy cleanGpuUsed`、`XinbaoImageStandardizer`、`XinbaoLightingCompanion`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
