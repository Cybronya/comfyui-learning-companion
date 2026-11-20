---
key: 平台全量/AI-动漫短剧分镜-九宫格-Sparkvideo2.0_模型升级_直出素描_2022274131420520449.json
name: AI-动漫短剧分镜-九宫格-Sparkvideo2.0_模型升级_直出素描_2022274131420520449
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/AI-动漫短剧分镜-九宫格-Sparkvideo2.0_模型升级_直出素描_2022274131420520449.json
hash: c065f749d2f1b559
coverage: 0.948718
learned_at: 2026-11-14 00:15:09
nodes: [LoadImage, ImpactImageInfo, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, ImageResize+, Image Overlay, Image Overlay, Image Overlay, Image Overlay, Image Overlay, Image Overlay, Image Overlay, Image Overlay, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Image Overlay, CR Text Concatenate, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, ImageFromBatch, Int, Anything Everywhere3, CLIPLoader, VAELoader, JjkText, ProcessString, Display Any (rgthree), ImageResize+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, Display Any (rgthree), CR Text Concatenate, CR Text Concatenate, AILab_QwenVL_Advanced, LongCatImageEdit, LongCatImageModelLoader, easy cleanGpuUsed, TextEncodeQwenImageEditPlus, ImageFromBatch, ImageResize+, EmptyImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy promptLine, RH_LLMAPI_Pro_Node, easy imageListToImageBatch, Note, easy showAnything, SaveImage, CR Text, SaveImage, CR Text, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 605822232006026, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/AI-动漫短剧分镜-九宫格-Sparkvideo2.0_模型升级_直出素描_2022274131420520449.json

> 来源文件 `comfyui_library/workflows/平台全量/AI-动漫短剧分镜-九宫格-Sparkvideo2.0_模型升级_直出素描_2022274131420520449.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `LoadImage`
- `ImpactImageInfo`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `Image Overlay`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `Image Overlay`
- `CR Text Concatenate`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `Int`
- `Anything Everywhere3`
- `CLIPLoader`
- `VAELoader`
- `JjkText`
- `ProcessString`
- `Display Any (rgthree)`
- `ImageResize+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Display Any (rgthree)`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `AILab_QwenVL_Advanced`
- `LongCatImageEdit`
- `LongCatImageModelLoader`
- `easy cleanGpuUsed`
- `TextEncodeQwenImageEditPlus`
- `ImageFromBatch`
- `ImageResize+`
- `EmptyImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy promptLine`
- `RH_LLMAPI_Pro_Node`
- `easy imageListToImageBatch`
- `Note`
- `easy showAnything`
- `SaveImage`
- `CR Text`
- `SaveImage`
- `CR Text`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `605822232006026`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（74/78）

**有卡**：`LoadImage`、`ImpactImageInfo`、`ImageResize+`、`Image Overlay`、`SimpleMath+`、`CR Text Concatenate`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`ImageFromBatch`、`Int`、`CLIPLoader`、`VAELoader`、`ProcessString`、`Display Any (rgthree)`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_QwenVL_Advanced`、`LongCatImageEdit`、`LongCatImageModelLoader`、`easy cleanGpuUsed`、`EmptyImage`、`UNETLoader`、`LoraLoaderModelOnly`、`easy promptLine`、`RH_LLMAPI_Pro_Node`、`easy imageListToImageBatch`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
