---
key: 图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json
name: 可视化角度控制改图Qwen Multiangle Camera_2014245627441451009
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json
hash: 8f16f49225cd7279
coverage: 0.772727
learned_at: 2026-10-23 12:36:08
nodes: [GetNode, SaveImage, UNETLoader, LoadImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, KSampler, EmptyLatentImage, easy imageSize, VAEDecode, SetNode, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, Note, Note, CR Text, Note, QwenMultiangleCameraNode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 76780182762415, "steps": 20, "width": 1280}
---

# 图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `GetNode`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `easy imageSize`
- `VAEDecode` ★核心
- `SetNode`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Note`
- `Note`
- `CR Text`
- `Note`
- `QwenMultiangleCameraNode`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `76780182762415`
- `steps` = `20`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`SaveImage`、`UNETLoader`、`LoadImage`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`KSampler`、`EmptyLatentImage`、`easy imageSize`、`VAEDecode`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CR Text`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
