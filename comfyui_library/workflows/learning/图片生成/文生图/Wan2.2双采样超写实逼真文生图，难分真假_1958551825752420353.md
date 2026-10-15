---
key: 图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json
name: Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json
hash: 94e2a36919199067
coverage: 0.952381
learned_at: 2026-10-15 22:27:36
nodes: [UNETLoader, UNETLoader, LoraLoader, LoraLoader, LoraLoader, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CLIPTextEncode, CLIPTextEncode, PreviewImage, VAEDecode, EmptyHunyuanLatentVideo, JWInteger, JWInteger, SaveImage, CR Text]
patterns: [lora]
missing: []
parameters: {"cfg": 14, "denoise": "bong_tangent", "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "randomize", "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `CR Text`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`UNETLoader`、`LoraLoader`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`JWInteger`、`SaveImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、LoraLoader
