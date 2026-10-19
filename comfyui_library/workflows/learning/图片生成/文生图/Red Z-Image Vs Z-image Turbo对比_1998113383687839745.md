---
key: 图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json
name: Red Z-Image Vs Z-image Turbo对比_1998113383687839745
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json
hash: d3e162b9cb115ce2
coverage: 0.882353
learned_at: 2026-10-19 21:46:54
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ProcessString, JDCN_StringToList, Seed (rgthree), Note, Note, CR Text, Text Concatenate, CR Prompt Text, RH_LLMAPI_Pro_Node, UNETLoader, EmptyLatentImage, Note, CR Prompt Text, easy showAnything, LoraLoaderModelOnly, CR Text Replace, CR Prompt Text, CR Text, KSampler, LayerUtility: PurgeVRAM, KSampler, CheckpointLoaderSimple, LoraLoaderModelOnly, AddLabel, VAEDecode, VAEDecode, AddLabel, ImageConcatMulti, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1016760652374030, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `ProcessString`
- `JDCN_StringToList`
- `Seed (rgthree)`
- `Note`
- `Note`
- `CR Text`
- `Text Concatenate`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `Note`
- `CR Prompt Text`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `CR Text Replace`
- `CR Prompt Text`
- `CR Text`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `AddLabel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1016760652374030`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM`、`ProcessString`、`JDCN_StringToList`、`Seed (rgthree)`、`CR Text`、`Text Concatenate`、`CR Prompt Text`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CR Text Replace`、`KSampler`、`CheckpointLoaderSimple`、`AddLabel`、`VAEDecode`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader
