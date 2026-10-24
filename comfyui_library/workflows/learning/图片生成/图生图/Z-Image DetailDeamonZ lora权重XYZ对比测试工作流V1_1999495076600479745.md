---
key: 图片生成/图生图/Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745.json
name: Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745.json
hash: 3ba9f007bfab7e2d
coverage: 0.90625
learned_at: 2026-10-23 11:29:18
nodes: [JDCN_StringToList, Note, LayerUtility: PurgeVRAM, Seed (rgthree), EmptyLatentImage, Text Concatenate, ProcessString, VAELoader, CLIPLoader, KSampler, EmptyImage, VAEDecode, easy batchAnything, AddLabel, DF_Get_latent_size, easy forLoopEnd, easy showAnything, easy showAnything, Text Concatenate, CR Prompt Text, CLIPTextEncode, easy forLoopStart, MathExpression|pysssss, ConditioningZeroOut, CR Prompt Text, CheckpointLoaderSimple, LoraLoaderModelOnly, JWFloat, JWInteger, SaveImage, LoraLoaderModelOnly, Float]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO-purn.safetensors", "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 858870712153467, "steps": 10, "width": 1080}
---

# 图片生成/图生图/Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image DetailDeamonZ lora权重XYZ对比测试工作流V1_1999495076600479745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `JDCN_StringToList`
- `Note`
- `LayerUtility: PurgeVRAM`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `Text Concatenate`
- `ProcessString`
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyImage`
- `VAEDecode` ★核心
- `easy batchAnything`
- `AddLabel`
- `DF_Get_latent_size`
- `easy forLoopEnd`
- `easy showAnything`
- `easy showAnything`
- `Text Concatenate`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `easy forLoopStart`
- `MathExpression|pysssss`
- `ConditioningZeroOut`
- `CR Prompt Text`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `JWFloat`
- `JWInteger`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `Float`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `858870712153467`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO-purn.safetensors`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`JDCN_StringToList`、`LayerUtility: PurgeVRAM`、`Seed (rgthree)`、`EmptyLatentImage`、`Text Concatenate`、`ProcessString`、`VAELoader`、`CLIPLoader`、`KSampler`、`EmptyImage`、`VAEDecode`、`easy batchAnything`、`AddLabel`、`DF_Get_latent_size`、`easy forLoopEnd`、`CR Prompt Text`、`CLIPTextEncode`、`easy forLoopStart`、`MathExpression|pysssss`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`JWFloat`、`JWInteger`、`SaveImage`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
