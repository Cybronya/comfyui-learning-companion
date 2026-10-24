---
key: 图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json
name: 【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json
hash: ba1064707f22c676
coverage: 0.894737
learned_at: 2026-10-23 11:52:09
nodes: [CFGNorm, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, VAEDecode, SaveImage, KSampler, AIO_Preprocessor, VAEEncode, PreviewImage, Note, QwenImageDiffsynthControlnet, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, LoadImage, ModelPatchLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 174139002538351, "steps": 40}
---

# 图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】Qwen-image controlnet diffsynth版_2050875911662260226.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `VAEEncode` ★核心
- `PreviewImage`
- `Note`
- `QwenImageDiffsynthControlnet`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `ModelPatchLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `174139002538351`
- `steps` = `40`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CFGNorm`、`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`KSampler`、`AIO_Preprocessor`、`VAEEncode`、`QwenImageDiffsynthControlnet`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet、CFGNorm
