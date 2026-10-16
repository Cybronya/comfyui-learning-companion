---
key: 视频生成/图生视频/FireRed-Image-Edit-1.1   单图编辑_2032730903151120385.json
name: FireRed-Image-Edit-1.1   单图编辑_2032730903151120385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032730903151120385.json
hash: c3f227440beb08f1
coverage: 0.913043
learned_at: 2026-10-15 22:35:37
nodes: [easy getNode, easy setNode, easy getNode, easy getNode, KOOK_ImageCompression, KOOK_SaveJPGImage, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, VAELoader, easy setNode, CLIPLoader, easy setNode, easy setNode, ModelSamplingAuraFlow, Image Comparer (rgthree), easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy getNode, ReferenceLatent, ReferenceLatent, EmptySD3LatentImage, CR Latent Input Switch, ConditioningZeroOut, easy getNode, easy getNode, easy getNode, VAEEncode, KSampler (Efficient), LoraLoaderModelOnly, easy getNode, easy getNode, easy getNode, CFGNorm, FluxKontextMultiReferenceLatentMethod, Note, LoadImage, LoraLoaderModelOnly, UNETLoader, TextEncodeQwenImageEditPlus, ShowText|pysssss, CR Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 314163163489330, "steps": 8}
---

# 视频生成/图生视频/FireRed-Image-Edit-1.1   单图编辑_2032730903151120385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032730903151120385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Process → Output → Other

**节点**（46 个）：
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAELoader`
- `easy setNode`
- `CLIPLoader`
- `easy setNode`
- `easy setNode`
- `ModelSamplingAuraFlow`
- `Image Comparer (rgthree)`
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
- `easy getNode`
- `easy getNode`
- `VAEEncode` ★核心
- `KSampler (Efficient)` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `ShowText|pysssss`
- `CR Text`

## 关键参数

- `seed` = `314163163489330`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`easy getNode`、`easy setNode`、`KOOK_ImageCompression`、`KOOK_SaveJPGImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`EmptySD3LatentImage`、`CR Latent Input Switch`、`ConditioningZeroOut`、`VAEEncode`、`KSampler (Efficient)`、`LoraLoaderModelOnly`、`CFGNorm`、`FluxKontextMultiReferenceLatentMethod`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`CR Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGNorm、KSampler (Efficient)
