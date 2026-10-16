---
key: 视频生成/图生视频/首尾帧-WAN2.2-RemixV2-I2V_2006524559020789762.json
name: 首尾帧-WAN2.2-RemixV2-I2V_2006524559020789762.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2006524559020789762.json
hash: 0ab225ab87239f25
coverage: 0.440476
learned_at: 2026-10-15 22:34:01
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Note, CLIPLoader, Note, wanBlockSwap, Reroute, Reroute, Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, VAEDecode, Note, INTConstant, INTConstant, Reroute, Reroute, Reroute, Note, WanFirstLastFrameToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Int, Int, Reroute, KSamplerAdvanced, KSamplerAdvanced, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageResizeKJv2, wanBlockSwap, Fast Groups Bypasser (rgthree), PreviewImage, PreviewImage, VHS_VideoCombine, easy cleanGpuUsed, RIFE VFI, DuckHideNode, SaveImage, Fast Bypasser (rgthree), VHS_VideoCombine, UNETLoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageLoader, CLIPTextEncode, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧-WAN2.2-RemixV2-I2V_2006524559020789762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006524559020789762.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
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
- `Note`
- `CLIPLoader`
- `Note`
- `wanBlockSwap`
- `Reroute`
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
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Note`
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
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Int`
- `Int`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `wanBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `DuckHideNode`
- `SaveImage`
- `Fast Bypasser (rgthree)`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageLoader`
- `CLIPTextEncode` ★核心
- `ImageLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（37/84）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`VAEDecode`、`INTConstant`、`WanFirstLastFrameToVideo`、`VAELoader`、`Int`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`RIFE VFI`、`DuckHideNode`、`SaveImage`、`Fast Bypasser (rgthree)`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
