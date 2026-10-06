---
key: 图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json
name: 一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json
hash: 340dc2546bef686d
coverage: 0.160714
learned_at: 2026-10-06 21:42:58
nodes: [LayerFilter: HDREffects, GetNode, GetNode, SetNode, CR Seed, KSampler (Efficient), VAELoader, Fast Groups Bypasser (rgthree), Label (rgthree), Label (rgthree), VOSR2Upscale, VOSR2ModelLoader, SplitImageWithAlpha, Image Comparer (rgthree), QwenImage21Cache, LoadImage, CLIPLoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextEncodeQwenImage21, LoadImage, ImageScaleToTotalPixels, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, CR Text, SetNode, GetNode, SetNode, ShowText|pysssss, GetNode, KOOK_SaveJPGImage, Image Comparer (rgthree), GetNode, SetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, LoadImage, PromptExpand, CR Text Input Switch, UNETLoader, SetNode, PreviewImage, easy imageChooser, Note]
patterns: []
missing: [CR Text, CR Text Input Switch, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Label (rgthree), Label (rgthree), LayerFilter: HDREffects, SplitImageWithAlpha, VOSR2ModelLoader, VOSR2Upscale, easy imageChooser, KSampler (Efficient), CR Seed, KOOK_SaveJPGImage, PromptExpand]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403214011463433, "steps": 25}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识, 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `VOSR2ModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `VOSR2Upscale` 相关主题 Upscale 在知识库中无对应知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `KOOK_SaveJPGImage` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `PromptExpand` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **16%**（9/56）

**有卡**：`VAELoader`、`QwenImage21Cache`、`LoadImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`ConditioningZeroOut`、`UNETLoader`

**缺卡**（17）：`CR Text`、`CR Text Input Switch`、`Fast Groups Bypasser (rgthree)`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`ImageScaleToTotalPixels`、`Label (rgthree)`、`Label (rgthree)`、`LayerFilter: HDREffects`、`SplitImageWithAlpha`、`VOSR2ModelLoader`、`VOSR2Upscale`、`easy imageChooser`、`KSampler (Efficient)`、`CR Seed`、`KOOK_SaveJPGImage`、`PromptExpand`

**用到的条目**：TextEncodeQwenImage21、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、QwenImage21Cache、UNETLoader、KSampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerFilter: HDREffects` 知识库中没有该节点类型的任何知识
- 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `VOSR2ModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `VOSR2Upscale` 相关主题 Upscale 在知识库中无对应知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `CR Seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `KOOK_SaveJPGImage` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `PromptExpand` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
