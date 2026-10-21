---
key: 图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json
name: FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json
hash: 740be9a29cec8b83
coverage: 0.826087
learned_at: 2026-10-20 00:01:11
nodes: [ModelSamplingAuraFlow, CFGNorm, PrimitiveInt, PrimitiveInt, Switch any [Crystools], Switch any [Crystools], PrimitiveFloat, PrimitiveFloat, SaveImage, CLIPLoader, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, VAELoader, FluxKontextImageScale, VAEDecode, KSampler, PrimitiveBoolean, UNETLoader, Switch any [Crystools], LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 415087228304380, "steps": 40}
---

# 图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FireRed Image Edit 1.1 阿凡达 Lora 测试流_2073314483048640514.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Output → Other

**节点**（23 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PrimitiveInt`
- `PrimitiveInt`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `SaveImage`
- `CLIPLoader`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `VAELoader`
- `FluxKontextImageScale`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `415087228304380`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`Switch any [Crystools]`、`SaveImage`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`VAELoader`、`FluxKontextImageScale`、`VAEDecode`、`KSampler`、`PrimitiveBoolean`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
