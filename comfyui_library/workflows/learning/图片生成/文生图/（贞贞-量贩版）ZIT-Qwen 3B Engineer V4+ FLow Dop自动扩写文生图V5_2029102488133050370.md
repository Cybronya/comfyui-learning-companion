---
key: 图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json
name: （贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json
hash: c414916162660e23
coverage: 0.852941
learned_at: 2026-10-20 23:22:22
nodes: [ConditioningZeroOut, VAELoader, CLIPTextEncode, JDCN_StringToList, CR Text, Note, Note, Text Concatenate, CR Prompt Text, Note, Seed (rgthree), KSampler, VAEDecode, UNETLoader, EmptyLatentImage, CR Text, LoraLoaderModelOnly, easy showAnything, SaveImage, CR Prompt Text, RH_LLMAPI_Pro_Node, LayerUtility: PurgeVRAM, CR Prompt Text, Note, ProcessString, RH_LLMAPI_Pro_Node, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text Replace, CR Prompt Text, RH_LLMAPI_NODE, CLIPLoader, CLIPLoaderGGUF]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 236161881252875, "steps": 10, "width": 1920}
---

# 图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（34 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `JDCN_StringToList`
- `CR Text`
- `Note`
- `Note`
- `Text Concatenate`
- `CR Prompt Text`
- `Note`
- `Seed (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `SaveImage`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `LayerUtility: PurgeVRAM`
- `CR Prompt Text`
- `Note`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text Replace`
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `CLIPLoaderGGUF`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `236161881252875`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`JDCN_StringToList`、`CR Text`、`Text Concatenate`、`CR Prompt Text`、`Seed (rgthree)`、`KSampler`、`VAEDecode`、`UNETLoader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`LayerUtility: PurgeVRAM`、`ProcessString`、`CR Text Replace`、`RH_LLMAPI_NODE`、`CLIPLoader`、`CLIPLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
