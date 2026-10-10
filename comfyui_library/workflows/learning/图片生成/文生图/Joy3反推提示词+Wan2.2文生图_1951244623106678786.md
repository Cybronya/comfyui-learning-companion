---
key: Joy3反推提示词+Wan2.2文生图_1951244623106678786.json
name: Joy3反推提示词+Wan2.2文生图_1951244623106678786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Joy3反推提示词+Wan2.2文生图_1951244623106678786.json
hash: 64a13d7a73e9ebcd
coverage: 0.558824
learned_at: 2026-10-10 20:58:41
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, KSamplerAdvanced, KSamplerAdvanced, easy cleanGpuUsed, EmptyHunyuanLatentVideo, DeepTranslatorTextNode, Reroute, Image Comparer (rgthree), ShowText|pysssss, CLIPLoader, LayerUtility: JoyCaptionBeta1, Note, LayerUtility: LoadJoyCaptionBeta1Model, Note, ShowText|pysssss, LayerUtility: JoyCaptionBeta1ExtraOptions, LoadImage, Reroute, easy imageConcat, SaveImage, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, DeepTranslatorTextNode]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, easy cleanGpuUsed, easy cleanGpuUsed, easy imageConcat]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识]
---

# Joy3反推提示词+Wan2.2文生图_1951244623106678786.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Joy3反推提示词+Wan2.2文生图_1951244623106678786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `EmptyHunyuanLatentVideo`
- `DeepTranslatorTextNode`
- `Reroute`
- `Image Comparer (rgthree)`
- `ShowText|pysssss`
- `CLIPLoader`
- `LayerUtility: JoyCaptionBeta1`
- `Note`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `Note`
- `ShowText|pysssss`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LoadImage`
- `Reroute`
- `easy imageConcat`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DeepTranslatorTextNode`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **56%**（19/34）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`DeepTranslatorTextNode`、`CLIPLoader`、`LoadImage`、`SaveImage`、`VAEDecode`

**缺卡**（8）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageConcat`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
