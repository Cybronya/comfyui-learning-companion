---
key: 图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321.json
name: Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321.json
hash: 3a38b1cdbb673f49
coverage: 0.777778
learned_at: 2026-10-23 11:21:28
nodes: [Mask Fill Holes, CLIPLoader, DrawMaskOnImage, VAELoader, SaveImage, VAEDecode, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, KSampler, 孤海注释, Int, UNETLoader, TextEncodeQwenImage21, 孤海注释, CR Prompt Text, CR Prompt Text, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 399167912499117, "steps": 25}
---

# 图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_二合一工作流｜万物移除+局部重绘_2110191490327736321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `Mask Fill Holes`
- `CLIPLoader`
- `DrawMaskOnImage`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `孤海注释`
- `Int`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `孤海注释`
- `CR Prompt Text`
- `CR Prompt Text`
- `ImpactSwitch`

## 关键参数

- `seed` = `399167912499117`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`Mask Fill Holes`、`CLIPLoader`、`DrawMaskOnImage`、`VAELoader`、`SaveImage`、`VAEDecode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`Int`、`UNETLoader`、`TextEncodeQwenImage21`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、CR Prompt Text
