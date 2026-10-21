---
key: 图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170.json
name: Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170.json
hash: 018764c13c308a26
coverage: 0.928571
learned_at: 2026-10-19 22:45:51
nodes: [ConditioningZeroOut, UNETLoader, CLIPTextEncode, VAEDecode, CLIPLoaderGGUF, KSampler, LoraLoaderModelOnly, VAELoader, RH_LLMAPI_NODE, easy showAnything, easy seed, SaveImage, CR Prompt Text, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 262642378267574, "steps": 10, "width": 1024}
---

# 图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028109823568519170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoaderGGUF`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `easy seed`
- `SaveImage`
- `CR Prompt Text`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `262642378267574`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoaderGGUF`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`RH_LLMAPI_NODE`、`easy seed`、`SaveImage`、`CR Prompt Text`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader
