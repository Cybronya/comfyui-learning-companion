---
key: 图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json
name: Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json
hash: c55eaab19b5a5b0c
coverage: 0.877551
learned_at: 2026-10-10 20:58:54
nodes: [UNETLoader, CLIPLoader, KSampler, VAEDecode, SaveImage, CLIPLoader, UNETLoader, VAELoader, QwenImage21Cache, ComfySwitchNode, KSampler, VAEDecode, SaveImage, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, LoadImage, EmptyLatentImage, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图生图工作流，轻量模型多场景覆盖方案_2103627655844294657.json`

## 结构

**节点**（49 个）：
- `UNETLoader`
- `CLIPLoader`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader`
- `VAELoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `LoadImage`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`UNETLoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`QwenImage21Cache`、`ComfySwitchNode`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`LoadImage`、`Fast Groups Bypasser (rgthree)`、`孤海注释`、`LoraLoaderModelOnly`、`JjkText`、`CLIPTextEncode`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
