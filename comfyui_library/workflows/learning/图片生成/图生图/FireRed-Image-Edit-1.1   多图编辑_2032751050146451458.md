---
key: 图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json
name: FireRed-Image-Edit-1.1   多图编辑_2032751050146451458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json
hash: ac9dbb20b34a75a8
coverage: 0.938462
learned_at: 2026-10-23 10:55:42
nodes: [VAELoader, easy setNode, CLIPLoader, easy setNode, easy setNode, CFGNorm, ModelSamplingAuraFlow, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy getNode, ReferenceLatent, ReferenceLatent, EmptySD3LatentImage, CR Latent Input Switch, ConditioningZeroOut, easy getNode, KOOK_ImageCompression, easy getNode, easy getNode, easy getNode, TextEncodeQwenImageEditPlus, VAEEncode, easy setNode, easy getNode, easy getNode, easy getNode, ImageScaleToTotalPixels, easy getNode, ImageScaleToTotalPixels, easy setNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy getNode, easy setNode, easy setNode, easy imageScaleDownToSize, easy imageScaleDownToSize, easy getNode, easy getNode, ImageConcanate, easy getNode, LoraLoaderModelOnly, easy getNode, LoadImage, easy getNode, easy getNode, ImageConcatMulti, KOOK_SaveJPGImage, KSampler (Efficient), easy getNode, ImageScaleToTotalPixels, PreviewImage, PreviewImage, ShowText|pysssss, Note, PromptExpand, CR Text Input Switch, LoadImage, LoadImage, LoraLoaderModelOnly, CR Text, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 119594075346089, "steps": 8}
---

# 图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit-1.1   多图编辑_2032751050146451458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Process → Output → Other

**节点**（65 个）：
- `VAELoader`
- `easy setNode`
- `CLIPLoader`
- `easy setNode`
- `easy setNode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptySD3LatentImage`
- `CR Latent Input Switch`
- `ConditioningZeroOut`
- `easy getNode`
- `KOOK_ImageCompression`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `ImageScaleToTotalPixels`
- `easy getNode`
- `ImageScaleToTotalPixels`
- `easy setNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy imageScaleDownToSize`
- `easy imageScaleDownToSize`
- `easy getNode`
- `easy getNode`
- `ImageConcanate`
- `easy getNode`
- `LoraLoaderModelOnly` ★核心
- `easy getNode`
- `LoadImage`
- `easy getNode`
- `easy getNode`
- `ImageConcatMulti`
- `KOOK_SaveJPGImage`
- `KSampler (Efficient)` ★核心
- `easy getNode`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `PreviewImage`
- `ShowText|pysssss`
- `Note`
- `PromptExpand`
- `CR Text Input Switch`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `119594075346089`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **94%**（61/65）

**有卡**：`VAELoader`、`easy setNode`、`CLIPLoader`、`CFGNorm`、`ModelSamplingAuraFlow`、`easy getNode`、`ReferenceLatent`、`EmptySD3LatentImage`、`CR Latent Input Switch`、`ConditioningZeroOut`、`KOOK_ImageCompression`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ImageScaleToTotalPixels`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy imageScaleDownToSize`、`ImageConcanate`、`LoraLoaderModelOnly`、`LoadImage`、`ImageConcatMulti`、`KOOK_SaveJPGImage`、`KSampler (Efficient)`、`PromptExpand`、`CR Text Input Switch`、`CR Text`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGNorm、KSampler (Efficient)
