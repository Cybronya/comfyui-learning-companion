---
key: 视频生成/图生视频/WAN2.1官方版掀起衣服展示大雷高清加速版特效工作流-StarAI_1901514526544797697.json
name: WAN2.1官方版掀起衣服展示大雷高清加速版特效工作流-StarAI_1901514526544797697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1901514526544797697.json
hash: a79a8e52dc8cccdc
coverage: 1
learned_at: 2026-10-15 22:29:24
nodes: [ImageUpscaleWithModel, VRAM_Debug, RIFE VFI, ImageScale, WanImageToVideo, ApplyRifleXRoPE_WanVideo, CLIPVisionEncode, VHS_VideoCombine, VAEDecodeTiled, WanVideoTeaCacheKJ, TorchCompileModelWanVideo, Note Plus (mtb), UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, Lora Loader Stack (rgthree), LoadImage, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, Tiled KSampler, LayerUtility: PurgeVRAM, Int, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "normal", "sampler_name": 6, "scheduler": "uni_pc_bh2", "seed": 3, "steps": 1}
---

# 视频生成/图生视频/WAN2.1官方版掀起衣服展示大雷高清加速版特效工作流-StarAI_1901514526544797697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901514526544797697.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ImageUpscaleWithModel`
- `VRAM_Debug`
- `RIFE VFI`
- `ImageScale`
- `WanImageToVideo`
- `ApplyRifleXRoPE_WanVideo`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `WanVideoTeaCacheKJ`
- `TorchCompileModelWanVideo`
- `Note Plus (mtb)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `Lora Loader Stack (rgthree)`
- `LoadImage`
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Tiled KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `Int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `3`
- `steps` = `1`
- `cfg` = `20`
- `sampler_name` = `6`
- `scheduler` = `uni_pc_bh2`
- `denoise` = `normal`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ImageUpscaleWithModel`、`VRAM_Debug`、`RIFE VFI`、`ImageScale`、`WanImageToVideo`、`ApplyRifleXRoPE_WanVideo`、`CLIPVisionEncode`、`VHS_VideoCombine`、`VAEDecodeTiled`、`WanVideoTeaCacheKJ`、`TorchCompileModelWanVideo`、`Note Plus (mtb)`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`Lora Loader Stack (rgthree)`、`LoadImage`、`UpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Tiled KSampler`、`LayerUtility: PurgeVRAM`、`Int`、`CLIPTextEncode`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Tiled KSampler、VAEDecodeTiled、CLIPVisionEncode
