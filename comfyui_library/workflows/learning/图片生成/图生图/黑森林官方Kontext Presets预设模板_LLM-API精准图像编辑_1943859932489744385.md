---
key: 图片生成/图生图/黑森林官方Kontext Presets预设模板_LLM-API精准图像编辑_1943859932489744385.json
name: 黑森林官方Kontext Presets预设模板_LLM-API精准图像编辑_1943859932489744385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/黑森林官方Kontext Presets预设模板_LLM-API精准图像编辑_1943859932489744385.json
hash: 482d66809fbcdc0c
coverage: 0.870968
learned_at: 2026-10-23 13:35:58
nodes: [VAEDecode, KSampler, VAELoader, DualCLIPLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, SaveImage, UNETLoader, ReferenceLatent, SaveImage, VAEEncode, EmptySD3LatentImage, GetImageSizeAndCount, ImageStitch, FluxKontextImageScale, PreviewImage, LoraLoaderModelOnly, ShowText|pysssss, Text Multiline, ImageScaleDownToSize, ImageConcatMulti, Text Multiline, Text Concatenate, Text Multiline, easy showAnything, LoadImage, ImageScaleDownToSize, RH_LLMAPI_NODE, LoadKontextPresets, easy showAnything]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 954073399403127, "steps": 20}
---

# 图片生成/图生图/黑森林官方Kontext Presets预设模板_LLM-API精准图像编辑_1943859932489744385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/黑森林官方Kontext Presets预设模板_LLM-API精准图像编辑_1943859932489744385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `SaveImage`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `SaveImage`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `GetImageSizeAndCount`
- `ImageStitch`
- `FluxKontextImageScale`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `Text Multiline`
- `ImageScaleDownToSize`
- `ImageConcatMulti`
- `Text Multiline`
- `Text Concatenate`
- `Text Multiline`
- `easy showAnything`
- `LoadImage`
- `ImageScaleDownToSize`
- `RH_LLMAPI_NODE`
- `LoadKontextPresets`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `954073399403127`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`VAEDecode`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`SaveImage`、`UNETLoader`、`ReferenceLatent`、`VAEEncode`、`EmptySD3LatentImage`、`GetImageSizeAndCount`、`ImageStitch`、`FluxKontextImageScale`、`LoraLoaderModelOnly`、`Text Multiline`、`ImageScaleDownToSize`、`ImageConcatMulti`、`Text Concatenate`、`LoadImage`、`RH_LLMAPI_NODE`、`LoadKontextPresets`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
