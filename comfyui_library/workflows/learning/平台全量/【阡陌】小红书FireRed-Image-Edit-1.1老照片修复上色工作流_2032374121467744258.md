---
key: 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1老照片修复上色工作流_2032374121467744258.json
name: 【阡陌】小红书FireRed-Image-Edit-1.1老照片修复上色工作流_2032374121467744258
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】小红书FireRed-Image-Edit-1.1老照片修复上色工作流_2032374121467744258.json
hash: e259dace326b50f4
coverage: 0.833333
learned_at: 2026-11-14 01:26:30
nodes: [CLIPLoader, VAELoader, LoadImage, CFGNorm, VAEDecode, FluxKontextImageScale, KSampler, MuyeSizeSelector, LoadImage, ConditioningZeroOut, PrimitiveInt, PrimitiveInt, ImpactConditionalBranch, ImpactConditionalBranch, PrimitiveFloat, PrimitiveFloat, ImpactConditionalBranch, ModelSamplingAuraFlow, Bool, VAEEncode, UNETLoader, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1059524232296285, "steps": 40}
---

# 平台全量/【阡陌】小红书FireRed-Image-Edit-1.1老照片修复上色工作流_2032374121467744258.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】小红书FireRed-Image-Edit-1.1老照片修复上色工作流_2032374121467744258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `CFGNorm`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `KSampler` ★核心
- `MuyeSizeSelector`
- `LoadImage`
- `ConditioningZeroOut`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImpactConditionalBranch`
- `ImpactConditionalBranch`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ImpactConditionalBranch`
- `ModelSamplingAuraFlow`
- `Bool`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1059524232296285`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`CFGNorm`、`VAEDecode`、`FluxKontextImageScale`、`KSampler`、`MuyeSizeSelector`、`ConditioningZeroOut`、`ImpactConditionalBranch`、`ModelSamplingAuraFlow`、`Bool`、`VAEEncode`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage
