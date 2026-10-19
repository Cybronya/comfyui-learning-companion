---
key: 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json
name: Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json
hash: c3ef705f13f6db5c
coverage: 0.826087
learned_at: 2026-10-19 21:46:55
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, JDCN_StringToList, Seed (rgthree), EmptyLatentImage, Note, easy showAnything, ProcessString, ConditioningZeroOut, KSampler, Text Concatenate, LayerUtility: PurgeVRAM, VAEDecode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, Float, JWFloat, Note, Note, SaveImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO-purn.safetensors", "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 819964157499595, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `JDCN_StringToList`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `Note`
- `easy showAnything`
- `ProcessString`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `Text Concatenate`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Float`
- `JWFloat`
- `Note`
- `Note`
- `SaveImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `819964157499595`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO-purn.safetensors`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`JDCN_StringToList`、`Seed (rgthree)`、`EmptyLatentImage`、`ProcessString`、`ConditioningZeroOut`、`KSampler`、`Text Concatenate`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`Float`、`JWFloat`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
