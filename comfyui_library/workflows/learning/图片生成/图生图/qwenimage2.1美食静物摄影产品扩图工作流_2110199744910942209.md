---
key: 图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json
name: qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json
hash: 8bcb9d196c67edf9
coverage: 0.777778
learned_at: 2026-10-23 11:44:21
nodes: [VAELoader, CLIPLoader, TextEncodeQwenImage21, CR Prompt Text, KSamplerAdvanced, Image Comparer (rgthree), LoadImage, ImageScaleToTotalPixels, DrawMaskOnImage, ImageScaleToTotalPixels, PreviewImage, Note, UNETLoader, LoraLoaderModelOnly, Note, VAEDecode, SaveImage, ImagePadForOutpaint]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwenimage2.1美食静物摄影产品扩图工作流_2110199744910942209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `KSamplerAdvanced` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `DrawMaskOnImage`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `ImagePadForOutpaint`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`CR Prompt Text`、`KSamplerAdvanced`、`LoadImage`、`ImageScaleToTotalPixels`、`DrawMaskOnImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`ImagePadForOutpaint`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
