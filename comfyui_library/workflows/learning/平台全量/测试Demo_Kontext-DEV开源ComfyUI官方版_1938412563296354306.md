---
key: 平台全量/测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306.json
name: 测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306.json
hash: 750bb0553b420e46
coverage: 0.9
learned_at: 2026-11-14 02:19:45
nodes: [VAEDecode, KSampler, VAELoader, DualCLIPLoader, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ReferenceLatent, VAEEncode, SaveImage, SaveImage, ImageStitch, FluxKontextImageScale, UNETLoader, LoadImage, LoadImage, PreviewImage, Text Multiline, ShowText|pysssss, ImageConcatMulti]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 461077299326971, "steps": 20}
---

# 平台全量/测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306.json

> 来源文件 `comfyui_library/workflows/平台全量/测试Demo_Kontext-DEV开源ComfyUI官方版_1938412563296354306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `FluxKontextImageScale`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `Text Multiline`
- `ShowText|pysssss`
- `ImageConcatMulti`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `461077299326971`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAEDecode`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`SaveImage`、`ImageStitch`、`FluxKontextImageScale`、`UNETLoader`、`LoadImage`、`Text Multiline`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
