---
key: 图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json
name: Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json
hash: 94e2a36919199067
coverage: 0.904762
learned_at: 2026-10-10 20:59:14
nodes: [UNETLoader, UNETLoader, LoraLoader, LoraLoader, LoraLoader, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, CLIPTextEncode, CLIPTextEncode, PreviewImage, VAEDecode, EmptyHunyuanLatentVideo, JWInteger, JWInteger, SaveImage, CR Text]
patterns: [lora]
missing: [CR Text]
parameters: {"cfg": 14, "denoise": "bong_tangent", "lora_name": "WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "randomize", "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2双采样超写实逼真文生图，难分真假_1958551825752420353.json`

## 结构

**节点**（21 个）：
- `UNETLoader`
- `UNETLoader`
- `LoraLoader`
- `LoraLoader`
- `LoraLoader`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `PreviewImage`
- `VAEDecode`
- `EmptyHunyuanLatentVideo`
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `CR Text`

**识别到的模式**：lora

## 关键参数

- `cfg` = `14`
- `denoise` = `bong_tangent`
- `lora_name` = `WAN2.1_SmartphoneSnapshotPhotoReality_v1_by-AI_Characters.safetensors`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `seed` = `enable`
- `steps` = `randomize`
- `strength_clip` = `1.0000000000000002`
- `strength_model` = `1.0000000000000002`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`UNETLoader`、`LoraLoader`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`PreviewImage`、`EmptyHunyuanLatentVideo`、`JWInteger`

**缺卡**（1）：`CR Text`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
