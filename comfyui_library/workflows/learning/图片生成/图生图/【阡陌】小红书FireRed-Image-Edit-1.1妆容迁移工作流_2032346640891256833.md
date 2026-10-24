---
key: 图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json
name: 【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json
hash: e581d77baf76be16
coverage: 0.846154
learned_at: 2026-10-23 11:52:51
nodes: [CLIPLoader, VAELoader, LoadImage, CFGNorm, VAEDecode, FluxKontextImageScale, KSampler, MuyeSizeSelector, LoadImage, ConditioningZeroOut, PrimitiveInt, PrimitiveInt, ImpactConditionalBranch, ImpactConditionalBranch, PrimitiveFloat, PrimitiveFloat, ImpactConditionalBranch, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, SaveImage, Bool, VAEEncode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 351898078762104, "steps": 40}
---

# 图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阡陌】小红书FireRed-Image-Edit-1.1妆容迁移工作流_2032346640891256833.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（26 个）：
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
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `Bool`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `351898078762104`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`CFGNorm`、`VAEDecode`、`FluxKontextImageScale`、`KSampler`、`MuyeSizeSelector`、`ConditioningZeroOut`、`ImpactConditionalBranch`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`Bool`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage
