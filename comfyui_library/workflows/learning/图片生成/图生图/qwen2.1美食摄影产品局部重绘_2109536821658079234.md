---
key: 图片生成/图生图/qwen2.1美食摄影产品局部重绘_2109536821658079234.json
name: qwen2.1美食摄影产品局部重绘_2109536821658079234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1美食摄影产品局部重绘_2109536821658079234.json
hash: b53df3f417545e2a
coverage: 0.833333
learned_at: 2026-10-23 11:43:02
nodes: [VAELoader, CLIPLoader, KSamplerAdvanced, TextEncodeQwenImage21, CR Prompt Text, VAEDecode, Image Comparer (rgthree), LoadImage, INTConstant, SimpleMath+, PreviewImage, InpaintCropImproved, VAEEncode, SetLatentNoiseMask, UNETLoader, InpaintStitchImproved, SaveImage, Note]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/qwen2.1美食摄影产品局部重绘_2109536821658079234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1美食摄影产品局部重绘_2109536821658079234.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `INTConstant`
- `SimpleMath+`
- `PreviewImage`
- `InpaintCropImproved`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `UNETLoader` ★核心
- `InpaintStitchImproved`
- `SaveImage`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`TextEncodeQwenImage21`、`CR Prompt Text`、`VAEDecode`、`LoadImage`、`INTConstant`、`SimpleMath+`、`InpaintCropImproved`、`VAEEncode`、`SetLatentNoiseMask`、`UNETLoader`、`InpaintStitchImproved`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SetLatentNoiseMask
