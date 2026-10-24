---
key: 图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json
name: Qwen3VL-wan2.2首尾帧I2V_2002510541207814145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json
hash: a222de8aff1a7eb7
coverage: 0.461538
learned_at: 2026-10-23 11:19:56
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, CLIPLoader, Note, UNETLoader, wanBlockSwap, Reroute, wanBlockSwap, Reroute, Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VHS_VideoCombine, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Note, WanFirstLastFrameToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, MultiplePathsInput, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, VAELoader, UNETLoader, Qwen3_VQA, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, VHS_SelectFilename, VHS_VideoCombine, Any To Any, VHS_SelectFilename, VHS_VideoCombine, Any To Any, RIFE VFI, VHS_VideoCombine, Int, Int, ImageLoader, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen3VL-wan2.2首尾帧I2V_2002510541207814145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
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
- `Note`
- `CLIPLoader`
- `Note`
- `UNETLoader` ★核心
- `wanBlockSwap`
- `Reroute`
- `wanBlockSwap`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `WanFirstLastFrameToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `MultiplePathsInput`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `UNETLoader` ★核心
- `Qwen3_VQA`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `Any To Any`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `Any To Any`
- `RIFE VFI`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `ImageLoader`
- `ImageLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **46%**（42/91）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`CLIPLoader`、`UNETLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`WanFirstLastFrameToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`MultiplePathsInput`、`VAELoader`、`Qwen3_VQA`、`LoraLoaderModelOnly`、`VHS_SelectFilename`、`Any To Any`、`RIFE VFI`、`Int`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Int
