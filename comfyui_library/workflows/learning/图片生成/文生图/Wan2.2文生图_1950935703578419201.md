---
key: 图片生成/文生图/Wan2.2文生图_1950935703578419201.json
name: Wan2.2文生图_1950935703578419201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1950935703578419201.json
hash: 13d22196a250a100
coverage: 0.944444
learned_at: 2026-10-10 20:59:14
nodes: [VAEDecode, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, LoraLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoader, LoraLoader, LoraLoaderModelOnly, SaveImage, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, Note, UNETLoader, UNETLoader]
patterns: [lora]
missing: []
parameters: {"cfg": 8, "denoise": "simple", "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "strength_clip": 0.6000000000000001, "strength_model": 0.6000000000000001}
---

# 图片生成/文生图/Wan2.2文生图_1950935703578419201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1950935703578419201.json`

## 结构

**节点**（18 个）：
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoader`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `SaveImage`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `Note`
- `UNETLoader`
- `UNETLoader`

**识别到的模式**：lora

## 关键参数

- `cfg` = `8`
- `denoise` = `simple`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `fixed`
- `strength_clip` = `0.6000000000000001`
- `strength_model` = `0.6000000000000001`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAEDecode`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`LoraLoader`、`LoraLoaderModelOnly`、`SaveImage`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`Note`、`UNETLoader`
