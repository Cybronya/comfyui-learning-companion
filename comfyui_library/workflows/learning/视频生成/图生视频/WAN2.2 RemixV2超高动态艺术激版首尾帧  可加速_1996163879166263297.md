---
key: 视频生成/图生视频/WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json
name: WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1996163879166263297.json
hash: 155de11b2882d1e8
coverage: 0.689655
learned_at: 2026-10-15 22:33:25
nodes: [RIFE VFI, GetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, easy cleanGpuUsed, easy clearCacheAll, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, SetNode, Reroute, Reroute, Reroute, GetNode, GetNode, SetNode, PathchSageAttentionKJ, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, SetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, PreviewImage, WanFirstLastFrameToVideo, INTConstant, VAELoader, Note, LoadImage, LoadImage, SetNode, wanBlockSwap, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VAEDecode, VHS_VideoCombine, CLIPTextEncode, MarkdownNote, INTConstant, INTConstant, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, CLIPVisionLoader, CLIPVisionEncode, CLIPVisionEncode, UNETLoader, UNETLoader, wanBlockSwap, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2 RemixV2超高动态艺术激版首尾帧  可加速_1996163879166263297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996163879166263297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `RIFE VFI`
- `GetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `PreviewImage`
- `WanFirstLastFrameToVideo`
- `INTConstant`
- `VAELoader`
- `Note`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `wanBlockSwap`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `INTConstant`
- `INTConstant`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（40/58）

**有卡**：`RIFE VFI`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`easy clearCacheAll`、`CLIPTextEncode`、`VHS_VideoCombine`、`ModelSamplingSD3`、`ImageResizeKJv2`、`WanFirstLastFrameToVideo`、`INTConstant`、`VAELoader`、`LoadImage`、`wanBlockSwap`、`LoraLoaderModelOnly`、`ImageConcatMulti`、`VAEDecode`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
