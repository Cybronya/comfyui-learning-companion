---
key: 图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json
name: flux.2-去除水印-标准版-（必收藏）_2056999199815847938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json
hash: 17b79e32fa554eef
coverage: 1
learned_at: 2026-10-23 11:35:54
nodes: [VAELoader, UNETLoader, CLIPLoader, CLIPTextEncode, ModelSamplingAuraFlow, CFGNorm, CLIPTextEncode, VAEEncode, ReferenceLatent, LoadImage, VAEDecode, SaveImage, GoogleTranslator, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 354928615661789, "steps": 20}
---

# 图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.2-去除水印-标准版-（必收藏）_2056999199815847938.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `GoogleTranslator`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `354928615661789`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`VAEDecode`、`SaveImage`、`GoogleTranslator`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGNorm
