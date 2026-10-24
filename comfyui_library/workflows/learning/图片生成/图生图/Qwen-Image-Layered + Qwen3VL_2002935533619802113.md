---
key: 图片生成/图生图/Qwen-Image-Layered + Qwen3VL_2002935533619802113.json
name: Qwen-Image-Layered + Qwen3VL_2002935533619802113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered + Qwen3VL_2002935533619802113.json
hash: 3a2b072affe12295
coverage: 0.487805
learned_at: 2026-10-23 11:17:12
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, ModelSamplingAuraFlow, ReferenceLatent, ReferenceLatent, VAEEncode, LatentCutToBatch, Note, ImageResizeKJv2, PreviewImage, ShowText|pysssss, ImageFromBatch+, PreviewImage, ImageFromBatch+, PreviewImage, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, Note, LoaderGGUF, Any Switch (rgthree), Note, Note, LoadImage, EmptyHunyuanLatentVideo, UNETLoader, AILab_QwenVL, PreviewImage, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1043785189935837, "steps": 20}
---

# 图片生成/图生图/Qwen-Image-Layered + Qwen3VL_2002935533619802113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered + Qwen3VL_2002935533619802113.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LatentCutToBatch`
- `Note`
- `ImageResizeKJv2`
- `PreviewImage`
- `ShowText|pysssss`
- `ImageFromBatch+`
- `PreviewImage`
- `ImageFromBatch+`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `LoaderGGUF`
- `Any Switch (rgthree)`
- `Note`
- `Note`
- `LoadImage`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `AILab_QwenVL`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1043785189935837`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **49%**（20/41）

**有卡**：`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`VAEEncode`、`LatentCutToBatch`、`ImageResizeKJv2`、`ImageFromBatch+`、`LoaderGGUF`、`LoadImage`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`AILab_QwenVL`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceLatent
