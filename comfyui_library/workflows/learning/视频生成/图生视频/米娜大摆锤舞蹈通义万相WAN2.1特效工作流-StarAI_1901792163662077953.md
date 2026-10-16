---
key: 视频生成/图生视频/米娜大摆锤舞蹈通义万相WAN2.1特效工作流-StarAI_1901792163662077953.json
name: 米娜大摆锤舞蹈通义万相WAN2.1特效工作流-StarAI_1901792163662077953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1901792163662077953.json
hash: 344fdb8a4c5feff9
coverage: 1
learned_at: 2026-10-15 22:29:24
nodes: [VHS_VideoCombine, CLIPTextEncode, UNETLoader, VAELoader, CLIPVisionLoader, WanImageToVideo, CLIPVisionEncode, LayerUtility: PurgeVRAM, UpscaleModelLoader, ImageUpscaleWithModel, VAEDecodeTiled, RIFE VFI, ImageScale, CLIPLoader, LoraLoader, LoraLoader, Note Plus (mtb), CLIPTextEncode, CR Text, Int, Tiled KSampler, LoadImage, ImageResizeAdvanced, Int]
patterns: [lora]
missing: []
parameters: {"cfg": 15, "denoise": "simple", "lora_name": "dbc.safetensors", "sampler_name": 6, "scheduler": "uni_pc", "seed": 33640241915287, "steps": 1, "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/米娜大摆锤舞蹈通义万相WAN2.1特效工作流-StarAI_1901792163662077953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901792163662077953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPVisionLoader`
- `WanImageToVideo`
- `CLIPVisionEncode`
- `LayerUtility: PurgeVRAM`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEDecodeTiled` ★核心
- `RIFE VFI`
- `ImageScale`
- `CLIPLoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Note Plus (mtb)`
- `CLIPTextEncode` ★核心
- `CR Text`
- `Int`
- `Tiled KSampler` ★核心
- `LoadImage`
- `ImageResizeAdvanced`
- `Int`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `dbc.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `33640241915287`
- `steps` = `1`
- `cfg` = `15`
- `sampler_name` = `6`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`CLIPVisionLoader`、`WanImageToVideo`、`CLIPVisionEncode`、`LayerUtility: PurgeVRAM`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEDecodeTiled`、`RIFE VFI`、`ImageScale`、`CLIPLoader`、`LoraLoader`、`Note Plus (mtb)`、`CR Text`、`Int`、`Tiled KSampler`、`LoadImage`、`ImageResizeAdvanced`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Tiled KSampler、VAEDecodeTiled、CLIPVisionEncode
