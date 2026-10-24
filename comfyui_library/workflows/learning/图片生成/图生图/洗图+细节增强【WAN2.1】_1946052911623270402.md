---
key: 图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json
name: 洗图+细节增强【WAN2.1】_1946052911623270402
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json
hash: 108e4cd01abc1046
coverage: 0.818182
learned_at: 2026-10-23 13:11:45
nodes: [UNETLoader, CLIPLoader, VAELoader, Anything Everywhere3, RH_Captioner, Text Multiline, Text Concatenate, CLIPTextEncode, CLIPTextEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, easy showAnything, VAEDecode, KSampler, LayerUtility: ImageScaleRestore, Image Comparer (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 499283374374898, "steps": 10}
---

# 图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图+细节增强【WAN2.1】_1946052911623270402.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `RH_Captioner`
- `Text Multiline`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `easy showAnything`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleRestore`
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `499283374374898`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`RH_Captioner`、`Text Multiline`、`Text Concatenate`、`CLIPTextEncode`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LoraLoaderModelOnly`、`VAEDecode`、`KSampler`、`LayerUtility: ImageScaleRestore`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
