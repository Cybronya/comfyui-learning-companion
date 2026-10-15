---
key: 图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json
name: WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json
hash: 1e1de7ebb126229a
coverage: 0.826087
learned_at: 2026-10-10 20:59:13
nodes: [ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageUpscaleWithModel, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, TeaCache, TeaCache, KSampler, VAEDecode, PreviewImage, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleBy, VAEEncode, UNETLoader, VAEDecode, ImageFromBatch, ImageConcanateOfUtils, ImageConcanateOfUtils, ImageConcanateOfUtils, KSampler, VAEEncode, ImageScaleBy, PreviewImage, PreviewImage, VAEDecodeTiled, SaveImage, KSampler, CLIPLoader, VAELoader, Note, CLIPTextEncode, RH_LLMAPI_NODE, EmptyHunyuanLatentVideo, Text Multiline, easy showAnything, UpscaleModelLoader, Image Tiled, PreviewImage]
patterns: []
missing: [Image Tiled, Text Multiline]
parameters: {"cfg": 10, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "beta", "seed": 14, "steps": 20}
discoveries: [次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json`

## 结构

**节点**（46 个）：
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageUpscaleWithModel`
- `UNETLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TeaCache`
- `TeaCache`
- `KSampler`
- `VAEDecode`
- `PreviewImage`
- `CLIPTextEncode`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `VAEEncode`
- `UNETLoader`
- `VAEDecode`
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `KSampler`
- `VAEEncode`
- `ImageScaleBy`
- `PreviewImage`
- `PreviewImage`
- `VAEDecodeTiled`
- `SaveImage`
- `KSampler`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `CLIPTextEncode`
- `RH_LLMAPI_NODE`
- `EmptyHunyuanLatentVideo`
- `Text Multiline`
- `easy showAnything`
- `UpscaleModelLoader`
- `Image Tiled`
- `PreviewImage`

## 关键参数

- `cfg` = `10`
- `denoise` = `0.25000000000000006`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `14`
- `steps` = `20`

## 知识

覆盖率 **83%**（38/46）

**有卡**：`ImageFromBatch`、`ImageUpscaleWithModel`、`UNETLoader`、`ModelSamplingSD3`、`TeaCache`、`KSampler`、`VAEDecode`、`PreviewImage`、`CLIPTextEncode`、`UpscaleModelLoader`、`ImageScaleBy`、`VAEEncode`、`ImageConcanateOfUtils`、`VAEDecodeTiled`、`SaveImage`、`CLIPLoader`、`VAELoader`、`Note`

**缺卡**（2）：`Image Tiled`、`Text Multiline`

## 学习发现

- 次要节点 `Image Tiled` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
