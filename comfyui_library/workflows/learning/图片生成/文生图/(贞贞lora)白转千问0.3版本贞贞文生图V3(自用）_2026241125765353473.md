---
key: 图片生成/文生图/(贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473.json
name: (贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/(贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473.json
hash: 0c6ac2e303e5ec9e
coverage: 0.92
learned_at: 2026-10-19 22:29:28
nodes: [ModelSamplingAuraFlow, CLIPTextEncode, CLIPLoader, CLIPTextEncode, SeedVR2ExtraArgs, SeedVR2, SeedVR2BlockSwap, String, LoraLoader, LoraLoader, LoraLoader, MarkdownNote, EmptyLatentImage, CR Prompt Text, TextConcat, UNETLoader, VAELoader, PrimitiveStringMultiline, KSampler, SaveImage, VAEDecode, SaveImage, PerturbedAttentionGuidance, LoraLoader, LoraLoader]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 928, "lora_name": "zhenzhen-baizhuan-0.3B.safetensors", "sampler_name": "res_3s_ode", "scheduler": "beta57", "seed": 732518577077965, "steps": 20, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002, "width": 1664}
---

# 图片生成/文生图/(贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/(贞贞lora)白转千问0.3版本贞贞文生图V3(自用）_2026241125765353473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `String`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `TextConcat`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PerturbedAttentionGuidance`
- `LoraLoader` ★核心
- `LoraLoader` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `zhenzhen-baizhuan-0.3B.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `width` = `1664`
- `height` = `928`
- `batch_size` = `1`
- `seed` = `732518577077965`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_3s_ode`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`CLIPLoader`、`SeedVR2ExtraArgs`、`SeedVR2`、`SeedVR2BlockSwap`、`String`、`LoraLoader`、`EmptyLatentImage`、`CR Prompt Text`、`TextConcat`、`UNETLoader`、`VAELoader`、`KSampler`、`SaveImage`、`VAEDecode`、`PerturbedAttentionGuidance`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SeedVR2
