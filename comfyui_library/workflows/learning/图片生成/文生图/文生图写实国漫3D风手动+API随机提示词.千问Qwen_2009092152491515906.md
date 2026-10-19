---
key: 图片生成/文生图/文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906.json
name: 文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906.json
hash: 96f4d2baea5ab784
coverage: 0.685714
learned_at: 2026-10-19 22:01:34
nodes: [ConditioningZeroOut, SaveImage, CLIPTextEncode, VAELoader, VAEDecode, EmptyLatentImage, Reroute, Reroute, ConditioningZeroOut, KSampler, VAELoader, CLIPLoader, VAEDecode, SaveImage, EmptyLatentImage, CLIPTextEncode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CheckpointLoaderSimple, LoraLoaderModelOnly, CheckpointLoaderSimple, CLIPLoader, LoraLoaderModelOnly, KSampler, easy showAnything, DapaoRandomPromptLineExtractNode, CR Text, DapaoRandomPromptLineExtractNode, ShowText|pysssss, RH_LLMAPI_NODE, Fast Groups Bypasser (rgthree), MarkdownNote]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "checkpoint": "Qwen-国漫3D人物CG插画大模型_Qwen image.safetensors", "denoise": 1, "height": 1112, "sampler_name": "euler", "scheduler": "simple", "seed": 510732378607487, "steps": 30, "width": 1984}
---

# 图片生成/文生图/文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（35 个）：
- `ConditioningZeroOut`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `DapaoRandomPromptLineExtractNode`
- `CR Text`
- `DapaoRandomPromptLineExtractNode`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1984`
- `height` = `1112`
- `batch_size` = `1`
- `seed` = `510732378607487`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-国漫3D人物CG插画大模型_Qwen image.safetensors`

## 知识

覆盖率 **69%**（24/35）

**有卡**：`ConditioningZeroOut`、`SaveImage`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`CLIPLoader`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DapaoRandomPromptLineExtractNode`、`CR Text`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
