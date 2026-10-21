---
key: 图片生成/图生图/qwen image  2.1 最新扩图_2107769241435987970.json
name: qwen image  2.1 最新扩图_2107769241435987970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image  2.1 最新扩图_2107769241435987970.json
hash: 71984fdd01ab3043
coverage: 0.456522
learned_at: 2026-10-21 00:46:00
nodes: [SetNode, GetNode, GetNode, SetNode, CR Seed, KSampler (Efficient), VAELoader, UNETLoader, Fast Groups Bypasser (rgthree), Note, Label (rgthree), Label (rgthree), VOSR2Upscale, VOSR2ModelLoader, SplitImageWithAlpha, Image Comparer (rgthree), QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, GetNode, GetNode, SetNode, CR Text, SetNode, GetNode, SetNode, GetNode, KOOK_SaveJPGImage, Image Comparer (rgthree), SetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, ImagePadForOutpaint, LayerUtility: ImageScaleByAspectRatio V2, TESpeedQwenImage21, LoraLoaderModelOnly, LoadImage, PreviewImage, easy imageChooser]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403214011463433, "steps": 25}
---

# 图片生成/图生图/qwen image  2.1 最新扩图_2107769241435987970.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image  2.1 最新扩图_2107769241435987970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（46 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Seed`
- `KSampler (Efficient)` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `SplitImageWithAlpha`
- `Image Comparer (rgthree)`
- `QwenImage21Cache`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `KOOK_SaveJPGImage`
- `Image Comparer (rgthree)`
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
- `ImagePadForOutpaint`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TESpeedQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PreviewImage`
- `easy imageChooser`

## 关键参数

- `seed` = `403214011463433`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（21/46）

**有卡**：`CR Seed`、`KSampler (Efficient)`、`VAELoader`、`UNETLoader`、`Label (rgthree)`、`VOSR2Upscale`、`VOSR2ModelLoader`、`SplitImageWithAlpha`、`QwenImage21Cache`、`CLIPLoader`、`TextEncodeQwenImage21`、`CR Text`、`KOOK_SaveJPGImage`、`ConditioningZeroOut`、`ImagePadForOutpaint`、`LayerUtility: ImageScaleByAspectRatio V2`、`TESpeedQwenImage21`、`LoraLoaderModelOnly`、`LoadImage`、`easy imageChooser`

**用到的条目**：TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、QwenImage21Cache、UNETLoader
