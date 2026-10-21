---
key: 图片生成/图生图/Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849.json
name: Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849.json
hash: d23971f89b52e3f5
coverage: 0.833333
learned_at: 2026-10-21 00:42:15
nodes: [CLIPLoader, VAELoader, VAEDecode, VAELoader, easy imageSizeByLongerSide, LoadImage, SaveImage, PreviewImage, easy int, 孤海外补画板按方向, 孤海注释, UNETLoader, TextEncodeQwenImage21, LayerUtility: ImageScaleByAspectRatio V2, KSampler, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 455773479815425, "steps": 25}
---

# 图片生成/图生图/Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 精准扩图｜扩展25%｜扩展300像素｜扩展为16_9_2104146400111054849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `VAELoader`
- `easy imageSizeByLongerSide`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `easy int`
- `孤海外补画板按方向`
- `孤海注释`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `DrawMaskOnImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactSwitch`

## 关键参数

- `seed` = `455773479815425`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`easy imageSizeByLongerSide`、`LoadImage`、`SaveImage`、`easy int`、`孤海外补画板按方向`、`UNETLoader`、`TextEncodeQwenImage21`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`DrawMaskOnImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、easy imageSizeByLongerSide
