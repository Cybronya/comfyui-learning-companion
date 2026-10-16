---
key: 视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-视频-声音_1987069561856004097.json
name: Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-视频-声音_1987069561856004097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1987069561856004097.json
hash: 0e4fb2d1546078b5
coverage: 0.418605
learned_at: 2026-10-15 22:32:57
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, INTConstant, INTConstant, Int, Reroute, Reroute, Reroute, Reroute, Reroute, Note, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, UNETLoader, UNETLoader, CLIPLoader, wanBlockSwap, VAELoader, KSamplerAdvanced, VAEDecode, Note, Note, easy showAnything, Any To Any, MultiplePathsInput, VHS_SelectFilename, CLIPTextEncode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, Reroute, RIFE VFI, Reroute, LayerUtility: PurgeVRAM V2, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, KSamplerAdvanced, Reroute, Reroute, ModelSamplingSD3, Note, Fast Groups Bypasser (rgthree), easy float, Reroute, Reroute, Reroute, VHS_VideoCombine, LoadImage, wanBlockSwap, Int, CLIPTextEncode, HunyuanVideoFoley, Qwen3_VQA]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-图-视频-声音_1987069561856004097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987069561856004097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `Int`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `wanBlockSwap`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Note`
- `Note`
- `easy showAnything`
- `Any To Any`
- `MultiplePathsInput`
- `VHS_SelectFilename`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `Reroute`
- `RIFE VFI`
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `easy float`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `LoadImage`
- `wanBlockSwap`
- `Int`
- `CLIPTextEncode` ★核心
- `HunyuanVideoFoley`
- `Qwen3_VQA`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **42%**（36/86）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanImageToVideo`、`INTConstant`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`UNETLoader`、`CLIPLoader`、`wanBlockSwap`、`VAELoader`、`KSamplerAdvanced`、`VAEDecode`、`Any To Any`、`MultiplePathsInput`、`VHS_SelectFilename`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`RIFE VFI`、`ModelSamplingSD3`、`easy float`、`LoadImage`、`HunyuanVideoFoley`、`Qwen3_VQA`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
