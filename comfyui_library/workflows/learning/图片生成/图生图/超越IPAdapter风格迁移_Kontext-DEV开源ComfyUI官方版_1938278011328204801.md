---
key: 图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json
name: 超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json
hash: 1fe5662a93f506f8
coverage: 0.909091
learned_at: 2026-10-23 13:29:50
nodes: [LoadImage, VAEDecode, KSampler, VAELoader, DualCLIPLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ReferenceLatent, VAEEncode, LoadImage, SaveImage, SaveImage, LoaderGGUF, ImageStitch, FluxKontextImageScale, ImageConcatMulti, ShowText|pysssss, PreviewImage, UNETLoader, GoogleTranslateTextNode, Text Multiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 977984460320439, "steps": 20}
---

# 图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `LoaderGGUF`
- `ImageStitch`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `ShowText|pysssss`
- `PreviewImage`
- `UNETLoader` ★核心
- `GoogleTranslateTextNode`
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `977984460320439`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`LoadImage`、`VAEDecode`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`SaveImage`、`LoaderGGUF`、`ImageStitch`、`FluxKontextImageScale`、`ImageConcatMulti`、`UNETLoader`、`GoogleTranslateTextNode`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
