---
key: 图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json
name: （贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json
hash: faee2f45750e2d37
coverage: 0.827586
learned_at: 2026-10-19 22:46:55
nodes: [ConditioningZeroOut, VAELoader, CLIPTextEncode, Note, Note, CR Text, EmptyLatentImage, CR Text Replace, Seed (rgthree), UNETLoader, Text Concatenate, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, CR Prompt Text, ProcessString, Note, ClipLoaderGGUF, RH_LLMAPI_Pro_Node, CR Prompt Text, KSampler, JDCN_StringToList, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, SaveImage, easy showAnything, PreviewAny, QwenImageEngineer]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 849836547290196, "steps": 10, "width": 1080}
---

# 图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `CR Text`
- `EmptyLatentImage` ★核心
- `CR Text Replace`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `CR Prompt Text`
- `ProcessString`
- `Note`
- `ClipLoaderGGUF`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `KSampler` ★核心
- `JDCN_StringToList`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SaveImage`
- `easy showAnything`
- `PreviewAny`
- `QwenImageEngineer`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `849836547290196`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`CR Text`、`EmptyLatentImage`、`CR Text Replace`、`Seed (rgthree)`、`UNETLoader`、`Text Concatenate`、`LoraLoaderModelOnly`、`CR Prompt Text`、`ProcessString`、`ClipLoaderGGUF`、`RH_LLMAPI_Pro_Node`、`KSampler`、`JDCN_StringToList`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`QwenImageEngineer`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader
