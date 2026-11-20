---
key: 平台全量/皮神-Qwen-Edit-High-definition_2019193753247944705.json
name: 皮神-Qwen-Edit-High-definition_2019193753247944705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/皮神-Qwen-Edit-High-definition_2019193753247944705.json
hash: dd0e9130653fdc5c
coverage: 0.954545
learned_at: 2026-11-14 02:25:49
nodes: [TextEncodeQwenImageEditPlus, CFGNorm, VAEEncode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageResize+, KSampler, CLIPLoader, VAELoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, LoadImage, SeedVR2ExtraArgs, SeedVR2BlockSwap, SaveImage, UNETLoader, SeedVR2, ImagePass, easy cleanGpuUsed, VAEDecode, Label (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 759612759500712, "steps": 15}
---

# 平台全量/皮神-Qwen-Edit-High-definition_2019193753247944705.json

> 来源文件 `comfyui_library/workflows/平台全量/皮神-Qwen-Edit-High-definition_2019193753247944705.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `TextEncodeQwenImageEditPlus`
- `CFGNorm`
- `VAEEncode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SaveImage`
- `UNETLoader` ★核心
- `SeedVR2`
- `ImagePass`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Label (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `759612759500712`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`TextEncodeQwenImageEditPlus`、`CFGNorm`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`ImageResize+`、`KSampler`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`LoadImage`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SaveImage`、`UNETLoader`、`SeedVR2`、`ImagePass`、`easy cleanGpuUsed`、`VAEDecode`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、CFGNorm、SeedVR2
