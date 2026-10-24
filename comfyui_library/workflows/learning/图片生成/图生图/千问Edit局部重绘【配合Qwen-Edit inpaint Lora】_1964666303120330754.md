---
key: 图片生成/图生图/千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754.json
name: 千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754.json
hash: 713ad99a9a7fd88c
coverage: 0.9
learned_at: 2026-10-23 12:29:46
nodes: [CFGNorm, KSampler, SaveImage, VAEDecode, VAELoader, CLIPLoader, SaveImage, ImageStitch, MarkdownNote, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, ModelSamplingAuraFlow, ImageAndMaskPreview, ImageScaleDownToSize, VAEEncode, LoadImage, PreviewImage, LoraLoaderModelOnly, RH_Translator, UNETLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 878140263234453, "steps": 20}
---

# 图片生成/图生图/千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问Edit局部重绘【配合Qwen-Edit inpaint Lora】_1964666303120330754.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CFGNorm`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `SaveImage`
- `ImageStitch`
- `MarkdownNote`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `ModelSamplingAuraFlow`
- `ImageAndMaskPreview`
- `ImageScaleDownToSize`
- `VAEEncode` ★核心
- `LoadImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `878140263234453`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`CFGNorm`、`KSampler`、`SaveImage`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`ImageStitch`、`TextEncodeQwenImageEdit`、`ModelSamplingAuraFlow`、`ImageAndMaskPreview`、`ImageScaleDownToSize`、`VAEEncode`、`LoadImage`、`LoraLoaderModelOnly`、`RH_Translator`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm
