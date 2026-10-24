---
key: 图片生成/图生图/Qwen-Edit Anime2RealV1.0_1987069606663753730.json
name: Qwen-Edit Anime2RealV1.0_1987069606663753730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Edit Anime2RealV1.0_1987069606663753730.json
hash: df2b94638839ce19
coverage: 0.823529
learned_at: 2026-10-23 11:15:15
nodes: [VAELoader, ImageConcatMulti, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, ConditioningZeroOut, AddLabel, Image Comparer (rgthree), AddLabel, PreviewImage, VAEDecode, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 625125639755476, "steps": 40}
---

# 图片生成/图生图/Qwen-Edit Anime2RealV1.0_1987069606663753730.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Edit Anime2RealV1.0_1987069606663753730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `ImageConcatMulti`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `AddLabel`
- `Image Comparer (rgthree)`
- `AddLabel`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `625125639755476`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`VAELoader`、`ImageConcatMulti`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`ConditioningZeroOut`、`AddLabel`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
