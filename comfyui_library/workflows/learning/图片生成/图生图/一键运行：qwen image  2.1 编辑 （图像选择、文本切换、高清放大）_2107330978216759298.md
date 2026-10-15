---
key: 图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json
name: 一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json
hash: 340dc2546bef686d
coverage: 0.446429
learned_at: 2026-10-15 22:59:46
nodes: [LayerFilter: HDREffects, GetNode, GetNode, SetNode, CR Seed, KSampler (Efficient), VAELoader, Fast Groups Bypasser (rgthree), Label (rgthree), Label (rgthree), VOSR2Upscale, VOSR2ModelLoader, SplitImageWithAlpha, Image Comparer (rgthree), QwenImage21Cache, LoadImage, CLIPLoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextEncodeQwenImage21, LoadImage, ImageScaleToTotalPixels, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, CR Text, SetNode, GetNode, SetNode, ShowText|pysssss, GetNode, KOOK_SaveJPGImage, Image Comparer (rgthree), GetNode, SetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, LoadImage, PromptExpand, CR Text Input Switch, UNETLoader, SetNode, PreviewImage, easy imageChooser, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403214011463433, "steps": 25}
---

# 图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（56 个）：
- `LayerFilter: HDREffects`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Seed`
- `KSampler (Efficient)` ★核心
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `SplitImageWithAlpha`
- `Image Comparer (rgthree)`
- `QwenImage21Cache`
- `LoadImage`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImage21`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `GetNode`
- `SetNode`
- `ShowText|pysssss`
- `GetNode`
- `KOOK_SaveJPGImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `PromptExpand`
- `CR Text Input Switch`
- `UNETLoader` ★核心
- `SetNode`
- `PreviewImage`
- `easy imageChooser`
- `Note`

## 关键参数

- `seed` = `403214011463433`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **45%**（25/56）

**有卡**：`LayerFilter: HDREffects`、`CR Seed`、`KSampler (Efficient)`、`VAELoader`、`Label (rgthree)`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SplitImageWithAlpha`、`QwenImage21Cache`、`LoadImage`、`CLIPLoader`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`CR Text`、`KOOK_SaveJPGImage`、`ConditioningZeroOut`、`PromptExpand`、`CR Text Input Switch`、`UNETLoader`、`easy imageChooser`

**用到的条目**：TextEncodeQwenImage21、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、QwenImage21Cache、UNETLoader、CR Seed
