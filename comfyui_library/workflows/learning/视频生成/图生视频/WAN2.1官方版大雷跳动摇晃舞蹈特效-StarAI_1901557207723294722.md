---
key: 视频生成/图生视频/WAN2.1官方版大雷跳动摇晃舞蹈特效-StarAI_1901557207723294722.json
name: WAN2.1官方版大雷跳动摇晃舞蹈特效-StarAI_1901557207723294722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1901557207723294722.json
hash: 9323c929cf3dcccd
coverage: 1
learned_at: 2026-10-15 22:29:24
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, WanImageToVideo, CLIPVisionEncode, LayerUtility: PurgeVRAM, ImageResizeAdvanced, VHS_VideoCombine, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModel, ImageScale, Note Plus (mtb), Int, LoadImage, UNETLoader, LoraLoader, CLIPTextEncode, Tiled KSampler, CLIPTextEncode, VAEDecodeTiled, CR Text]
patterns: [lora]
missing: []
parameters: {"cfg": 20, "denoise": "simple", "lora_name": "bounce1.0.safetensors", "sampler_name": 6, "scheduler": "uni_pc", "seed": 33640241915287, "steps": 1, "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/WAN2.1官方版大雷跳动摇晃舞蹈特效-StarAI_1901557207723294722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901557207723294722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `WanImageToVideo`
- `CLIPVisionEncode`
- `LayerUtility: PurgeVRAM`
- `ImageResizeAdvanced`
- `VHS_VideoCombine`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScale`
- `Note Plus (mtb)`
- `Int`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `Tiled KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `CR Text`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `bounce1.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `33640241915287`
- `steps` = `1`
- `cfg` = `20`
- `sampler_name` = `6`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`WanImageToVideo`、`CLIPVisionEncode`、`LayerUtility: PurgeVRAM`、`ImageResizeAdvanced`、`VHS_VideoCombine`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScale`、`Note Plus (mtb)`、`Int`、`LoadImage`、`UNETLoader`、`LoraLoader`、`CLIPTextEncode`、`Tiled KSampler`、`VAEDecodeTiled`、`CR Text`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Tiled KSampler、VAEDecodeTiled、CLIPVisionEncode
