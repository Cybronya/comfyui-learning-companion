---
key: 视频生成/图生视频/Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json
name: Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json
hash: 5e01f51db0daa8cf
coverage: 0.481013
learned_at: 2026-10-15 22:41:30
nodes: [PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, wanBlockSwap, KSamplerAdvanced, CLIPTextEncode, Reroute, Reroute, ModelSamplingSD3, KSamplerAdvanced, Reroute, Reroute, ModelSamplingSD3, wanBlockSwap, Note, Int, INTConstant, Int, INTConstant, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Any To Any, easy showAnything, Reroute, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, Reroute, Qwen3_VQA, Label (rgthree), Fast Groups Bypasser (rgthree), ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, Reroute, VAEDecode, LoadImage, RH_LLMAPI_Pro_Node, Note, easy float, RIFE VFI, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, VHS_SelectFilename, MultiplePathsInput, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, HunyuanVideoFoley, Note]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2+Qwen3VL+Foley多模态全自动图生视频_2076490092809637889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076490092809637889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
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
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `wanBlockSwap`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `Note`
- `Int`
- `INTConstant`
- `Int`
- `INTConstant`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any To Any`
- `easy showAnything`
- `Reroute`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Qwen3_VQA`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Reroute`
- `VAEDecode` ★核心
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `Note`
- `easy float`
- `RIFE VFI`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `VHS_SelectFilename`
- `MultiplePathsInput`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `HunyuanVideoFoley`
- `Note`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **48%**（38/79）

**有卡**：`PathchSageAttentionKJ`、`WanImageToVideo`、`ImageResizeKJv2`、`wanBlockSwap`、`KSamplerAdvanced`、`CLIPTextEncode`、`ModelSamplingSD3`、`Int`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`Any To Any`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Qwen3_VQA`、`Label (rgthree)`、`ModelPatchTorchSettings`、`VAEDecode`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`easy float`、`RIFE VFI`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`VHS_SelectFilename`、`MultiplePathsInput`、`HunyuanVideoFoley`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
