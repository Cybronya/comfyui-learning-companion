---
key: 图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json
name: WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json
hash: 1e1de7ebb126229a
coverage: 0.869565
learned_at: 2026-10-15 22:27:34
nodes: [ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageUpscaleWithModel, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, TeaCache, TeaCache, KSampler, VAEDecode, PreviewImage, CLIPTextEncode, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleBy, VAEEncode, UNETLoader, VAEDecode, ImageFromBatch, ImageConcanateOfUtils, ImageConcanateOfUtils, ImageConcanateOfUtils, KSampler, VAEEncode, ImageScaleBy, PreviewImage, PreviewImage, VAEDecodeTiled, SaveImage, KSampler, CLIPLoader, VAELoader, Note, CLIPTextEncode, RH_LLMAPI_NODE, EmptyHunyuanLatentVideo, Text Multiline, easy showAnything, UpscaleModelLoader, Image Tiled, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "beta", "seed": 14, "steps": 20}
---

# 图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2文生图-大图【LLM辅助写实】_1951170868485496833.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageUpscaleWithModel`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `TeaCache`
- `TeaCache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `ImageConcanateOfUtils`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ImageScaleBy`
- `PreviewImage`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `EmptyHunyuanLatentVideo`
- `Text Multiline`
- `easy showAnything`
- `UpscaleModelLoader`
- `Image Tiled`
- `PreviewImage`

## 关键参数

- `seed` = `14`
- `steps` = `20`
- `cfg` = `10`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`ImageFromBatch`、`ImageUpscaleWithModel`、`UNETLoader`、`ModelSamplingSD3`、`TeaCache`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`UpscaleModelLoader`、`ImageScaleBy`、`VAEEncode`、`ImageConcanateOfUtils`、`VAEDecodeTiled`、`SaveImage`、`CLIPLoader`、`VAELoader`、`RH_LLMAPI_NODE`、`EmptyHunyuanLatentVideo`、`Text Multiline`、`Image Tiled`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled、VAEEncode
