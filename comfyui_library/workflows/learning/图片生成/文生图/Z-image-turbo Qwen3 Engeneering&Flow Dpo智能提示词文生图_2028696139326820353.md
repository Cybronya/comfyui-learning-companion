---
key: 图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353.json
name: Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353.json
hash: e00e3de1aa3fb319
coverage: 0.928571
learned_at: 2026-10-20 23:21:53
nodes: [ConditioningZeroOut, UNETLoader, CLIPTextEncode, VAEDecode, CLIPLoaderGGUF, EmptyLatentImage, KSampler, LoraLoaderModelOnly, VAELoader, easy seed, SaveImage, CR Prompt Text, easy showAnything, RH_LLMAPI_NODE]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 37017329535336, "steps": 10, "width": 1920}
---

# 图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-turbo Qwen3 Engeneering&Flow Dpo智能提示词文生图_2028696139326820353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoaderGGUF`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `easy seed`
- `SaveImage`
- `CR Prompt Text`
- `easy showAnything`
- `RH_LLMAPI_NODE`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `37017329535336`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoaderGGUF`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`easy seed`、`SaveImage`、`CR Prompt Text`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader
