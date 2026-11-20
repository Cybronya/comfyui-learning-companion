---
key: 图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410.json
name: Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410.json
hash: 9bb861d6a528cb81
coverage: 0.772727
learned_at: 2026-10-30 17:51:18
nodes: [Text Multiline, UNETLoader, CLIPLoader, Text Concatenate, VAELoader, LoraLoaderModelOnly, Seed (rgthree), TextEncodeQwenImage21, QwenImage21Cache, KSampler, GetNode, easy cleanGpuUsed, 孤海注释, SetNode, XinbaoImageStandardizer, XinbaoLightingCompanion, Image Comparer (rgthree), VAEDecode, SaveImage, LoadImage, MuyeTextEditOutput, 孤海注释]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1109940380127346, "steps": 25}
---

# 图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1心宝全能溶图打光｜18种光效组合｜11种光照方向_2115665535491985410.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
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
- `MuyeTextEditOutput`
- `孤海注释`

## 关键参数

- `seed` = `1109940380127346`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`Text Multiline`、`UNETLoader`、`CLIPLoader`、`Text Concatenate`、`VAELoader`、`LoraLoaderModelOnly`、`Seed (rgthree)`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`easy cleanGpuUsed`、`XinbaoImageStandardizer`、`XinbaoLightingCompanion`、`VAEDecode`、`SaveImage`、`LoadImage`、`MuyeTextEditOutput`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、SaveImage、LoadImage
