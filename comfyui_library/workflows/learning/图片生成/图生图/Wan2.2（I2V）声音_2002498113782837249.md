---
key: 图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json
name: Wan2.2（I2V）声音_2002498113782837249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json
hash: c492ce1d122b670b
coverage: 0.418605
learned_at: 2026-10-23 11:28:25
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, INTConstant, INTConstant, Int, Reroute, Reroute, Reroute, Reroute, Reroute, Note, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, UNETLoader, UNETLoader, CLIPLoader, wanBlockSwap, VAELoader, KSamplerAdvanced, VAEDecode, Note, Note, CLIPTextEncode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, KSamplerAdvanced, Reroute, Reroute, ModelSamplingSD3, Note, Fast Groups Bypasser (rgthree), easy float, Reroute, Reroute, Reroute, wanBlockSwap, CLIPTextEncode, LoadImage, Int, RIFE VFI, HunyuanVideoFoley, VHS_VideoCombine, Qwen3_VQA, easy showAnything, LayerUtility: PurgeVRAM V2, MultiplePathsInput, VHS_SelectFilename, Any To Any]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2（I2V）声音_2002498113782837249.json`

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
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
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
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Int`
- `RIFE VFI`
- `HunyuanVideoFoley`
- `VHS_VideoCombine`
- `Qwen3_VQA`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `MultiplePathsInput`
- `VHS_SelectFilename`
- `Any To Any`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **42%**（36/86）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanImageToVideo`、`INTConstant`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`UNETLoader`、`CLIPLoader`、`wanBlockSwap`、`VAELoader`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`ModelSamplingSD3`、`easy float`、`LoadImage`、`RIFE VFI`、`HunyuanVideoFoley`、`Qwen3_VQA`、`MultiplePathsInput`、`VHS_SelectFilename`、`Any To Any`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
