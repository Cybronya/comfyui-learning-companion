---
key: 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json
name: Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json
hash: 0f267d3bf597c690
coverage: 0.826087
learned_at: 2026-10-19 21:46:55
nodes: [Note, Note, CR Prompt Text, LoraLoaderModelOnly, ProcessString, VAEDecode, LayerUtility: PurgeVRAM, VAELoader, Seed (rgthree), EmptyLatentImage, JDCN_StringToList, CLIPLoader, CLIPTextEncode, SaveImage, KSampler, ConditioningZeroOut, easy showAnything, Text Concatenate, CheckpointLoaderSimple, Note, JWFloat, Float, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO-purn.safetensors", "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 418767423461379, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `Note`
- `Note`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `ProcessString`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `VAELoader`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `JDCN_StringToList`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `easy showAnything`
- `Text Concatenate`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `JWFloat`
- `Float`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `418767423461379`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO-purn.safetensors`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`CR Prompt Text`、`LoraLoaderModelOnly`、`ProcessString`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`VAELoader`、`Seed (rgthree)`、`EmptyLatentImage`、`JDCN_StringToList`、`CLIPLoader`、`CLIPTextEncode`、`SaveImage`、`KSampler`、`ConditioningZeroOut`、`Text Concatenate`、`CheckpointLoaderSimple`、`JWFloat`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
