---
key: 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json
name: qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json
hash: da1362841a8b674e
coverage: 0.875
learned_at: 2026-10-10 20:59:25
nodes: [ResolutionSelector, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, SaveImage, VAELoader, CLIPLoader, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen2.1文生图基础工作流 新手友好稳定出图_2104664392800489473.json`

## 结构

**节点**（40 个）：
- `ResolutionSelector`
- `EmptyLatentImage`
- `VAEDecode`
- `KSampler`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader`
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

覆盖率 **88%**（35/40）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`ComfySwitchNode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`孤海注释`、`LoraLoaderModelOnly`、`JjkText`、`CLIPTextEncode`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
