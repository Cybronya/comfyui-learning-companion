---
key: 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json
name: 平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json
hash: 43f0d0a7add6034b
coverage: 0.907407
learned_at: 2026-10-10 20:59:43
nodes: [VAELoader, VAEDecode, EmptyLatentImage, ResolutionSelector, UNETLoader, CLIPLoader, SaveImage, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, EmptyLatentImage, VAELoader, CLIPLoader, VAEDecode, QwenImage21Cache, ResolutionSelector, SaveImage, KSampler, SaveImageAdvanced, UNETLoader, TextEncodeQwenImage21, ComfySwitchNode, LoraLoaderModelOnly, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json`

## 结构

**节点**（54 个）：
- `VAELoader`
- `VAEDecode`
- `EmptyLatentImage`
- `ResolutionSelector`
- `UNETLoader`
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler`
- `EmptyLatentImage`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `KSampler`
- `SaveImageAdvanced`
- `UNETLoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoraLoaderModelOnly`
- `LoadImage`
- `LoadImage`
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

覆盖率 **91%**（49/54）

**有卡**：`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`QwenImage21Cache`、`ComfySwitchNode`、`LoraLoaderModelOnly`、`LoadImage`、`孤海注释`、`JjkText`、`CLIPTextEncode`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
