---
key: 图片生成/文生图/Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857.json
name: Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857.json
hash: 16c352e8554b21aa
coverage: 0.5
learned_at: 2026-10-19 21:46:48
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAELoader, ModelSamplingAuraFlow, ReferenceLatent, ReferenceLatent, VAEEncode, LatentCutToBatch, PreviewImage, PreviewImage, ImageFromBatch+, PreviewImage, PreviewImage, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, Any Switch (rgthree), Note, LoadImage, ImageResizeKJv2, UNETLoader, SetNode, LoaderGGUF, CLIPLoader, AILab_QwenVL_Advanced, GetNode, SetNode, ShowText|pysssss, EmptyHunyuanLatentVideo, Note, QwenImageLayered - Layer to Length Mapper, Note, Note, ImageFromBatch+, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1043785189935837, "steps": 20}
---

# 图片生成/文生图/Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LatentCutToBatch`
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch+`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Note`
- `LoadImage`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `SetNode`
- `LoaderGGUF`
- `CLIPLoader`
- `AILab_QwenVL_Advanced`
- `GetNode`
- `SetNode`
- `ShowText|pysssss`
- `EmptyHunyuanLatentVideo`
- `Note`
- `QwenImageLayered - Layer to Length Mapper`
- `Note`
- `Note`
- `ImageFromBatch+`
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

覆盖率 **50%**（21/42）

**有卡**：`KSampler`、`CLIPTextEncode`、`VAEDecode`、`VAELoader`、`ModelSamplingAuraFlow`、`ReferenceLatent`、`VAEEncode`、`LatentCutToBatch`、`ImageFromBatch+`、`LoadImage`、`ImageResizeKJv2`、`UNETLoader`、`LoaderGGUF`、`CLIPLoader`、`AILab_QwenVL_Advanced`、`EmptyHunyuanLatentVideo`、`QwenImageLayered - Layer to Length Mapper`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceLatent
