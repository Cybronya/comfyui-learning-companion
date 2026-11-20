---
key: 平台全量/Redfire image edit1.1_2041891894988382209.json
name: Redfire image edit1.1_2041891894988382209
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Redfire image edit1.1_2041891894988382209.json
hash: 8c61bf9c68a75c0f
coverage: 0.807692
learned_at: 2026-11-14 00:54:39
nodes: [ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, CFGNorm, VAEEncode, PrimitiveInt, PrimitiveInt, Switch any [Crystools], Switch any [Crystools], PrimitiveFloat, PrimitiveFloat, VAEDecode, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, CLIPLoader, VAELoader, KSampler, FluxKontextImageScale, PrimitiveBoolean, LoraLoaderModelOnly, UNETLoader, LoadImage, Fast Groups Bypasser (rgthree), Switch any [Crystools], LoadImage, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 806902971968905, "steps": 40}
---

# 平台全量/Redfire image edit1.1_2041891894988382209.json

> 来源文件 `comfyui_library/workflows/平台全量/Redfire image edit1.1_2041891894988382209.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（26 个）：
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `VAEEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Switch any [Crystools]`
- `LoadImage`
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `806902971968905`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CFGNorm`、`VAEEncode`、`Switch any [Crystools]`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`FluxKontextImageScale`、`PrimitiveBoolean`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
