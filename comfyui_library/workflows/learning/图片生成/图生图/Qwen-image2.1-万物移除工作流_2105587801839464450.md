---
key: 图片生成/图生图/Qwen-image2.1-万物移除工作流_2105587801839464450.json
name: Qwen-image2.1-万物移除工作流_2105587801839464450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万物移除工作流_2105587801839464450.json
hash: 2c2bb2ee61ec3e96
coverage: 0.875
learned_at: 2026-10-21 00:43:24
nodes: [UNETLoader, VAEDecode, SaveImage, PreviewImage, Mask Fill Holes, DrawMaskOnImage, TextEncodeQwenImage21, CLIPLoader, VAELoader, PreviewImage, CR Prompt Text, KSampler, CR Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Int]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 988061766903564, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-万物移除工作流_2105587801839464450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万物移除工作流_2105587801839464450.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `Mask Fill Holes`
- `DrawMaskOnImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `CR Prompt Text`
- `KSampler` ★核心
- `CR Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`

## 关键参数

- `seed` = `988061766903564`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UNETLoader`、`VAEDecode`、`SaveImage`、`Mask Fill Holes`、`DrawMaskOnImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`KSampler`、`CR Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、CR Prompt Text
