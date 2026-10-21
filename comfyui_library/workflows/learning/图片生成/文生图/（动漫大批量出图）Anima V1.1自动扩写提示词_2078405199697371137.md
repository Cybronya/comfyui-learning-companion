---
key: 图片生成/文生图/（动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137.json
name: （动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137.json
hash: a2e9e85220022c80
coverage: 0.827586
learned_at: 2026-10-20 00:21:40
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, CLIPTextEncode, VAELoader, easy cleanGpuUsed, EmptyLatentImage, Random Line, CR Prompt Text, easy showAnything, CLIPTextEncode, CR Prompt Text, RHLLMChatNode, easy showAnything, RHLLMChatNode, SaveImage, ProcessString, easy promptLine, CR Prompt Text, ProcessString, easy promptLine, easy convertAnything, ConcatTextOfUtils, easy showAnything, easy showAnything, ProcessString, easy promptLine, 孤海注释]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1920, "sampler_name": "er_sde", "scheduler": "beta", "seed": 501620591509957, "steps": 40, "width": 1080}
---

# 图片生成/文生图/（动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（动漫大批量出图）Anima V1.1自动扩写提示词_2078405199697371137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `easy cleanGpuUsed`
- `EmptyLatentImage` ★核心
- `Random Line`
- `CR Prompt Text`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `RHLLMChatNode`
- `easy showAnything`
- `RHLLMChatNode`
- `SaveImage`
- `ProcessString`
- `easy promptLine`
- `CR Prompt Text`
- `ProcessString`
- `easy promptLine`
- `easy convertAnything`
- `ConcatTextOfUtils`
- `easy showAnything`
- `easy showAnything`
- `ProcessString`
- `easy promptLine`
- `孤海注释`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `501620591509957`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`easy cleanGpuUsed`、`EmptyLatentImage`、`Random Line`、`CR Prompt Text`、`RHLLMChatNode`、`SaveImage`、`ProcessString`、`easy promptLine`、`easy convertAnything`、`ConcatTextOfUtils`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text
