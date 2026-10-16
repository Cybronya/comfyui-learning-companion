---
key: 视频生成/图生视频/wan2.2+foley 图生视频自动音效_2004446974457901057.json
name: wan2.2+foley 图生视频自动音效_2004446974457901057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004446974457901057.json
hash: 2e85c3fd6a076c27
coverage: 0.971429
learned_at: 2026-10-15 22:33:54
nodes: [CLIPLoader, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, Int, LayerUtility: ImageScaleByAspectRatio V2, Int, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, Float, LayerUtility: PurgeVRAM V2, VAEDecode, VHS_VideoCombine, VHS_SelectFilename, Any To Any, MultiplePathsInput, easy showAnything, LayerUtility: PurgeVRAM V2, Int, Int, LoadImage, WanImageToVideo, CLIPTextEncode, VAELoader, ImageResizeKJv2, VHS_VideoCombine, Qwen3_VQA, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, HunyuanVideoFoley]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2+foley 图生视频自动音效_2004446974457901057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004446974457901057.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Float`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_SelectFilename`
- `Any To Any`
- `MultiplePathsInput`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `Int`
- `LoadImage`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `Qwen3_VQA`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `HunyuanVideoFoley`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`CLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`Float`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`VHS_VideoCombine`、`VHS_SelectFilename`、`Any To Any`、`MultiplePathsInput`、`LoadImage`、`WanImageToVideo`、`CLIPTextEncode`、`VAELoader`、`ImageResizeKJv2`、`Qwen3_VQA`、`KSamplerAdvanced`、`RIFE VFI`、`HunyuanVideoFoley`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
