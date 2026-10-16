---
key: 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2070382789744218114.json
name: WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2070382789744218114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070382789744218114.json
hash: 5ce3e999fff6c644
coverage: 0.405063
learned_at: 2026-10-15 22:40:38
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Note, CLIPLoader, wanBlockSwap, Reroute, Reroute, Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VHS_VideoCombine, VAEDecode, Note, INTConstant, INTConstant, RIFE VFI, Reroute, Reroute, Reroute, Note, WanFirstLastFrameToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, Fast Groups Bypasser (rgthree), Reroute, Reroute, Reroute, VAELoader, Int, VHS_VideoCombine, Reroute, KSamplerAdvanced, KSamplerAdvanced, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, PreviewImage, wanBlockSwap, UNETLoader, UNETLoader, Note, ImageLoader, ImageLoader, CLIPTextEncode, Int]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-RemixV2-I2V首尾帧丝滑变装转场_2070382789744218114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070382789744218114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
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
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `INTConstant`
- `RIFE VFI`
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
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Int`
- `VHS_VideoCombine`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `ImageLoader`
- `ImageLoader`
- `CLIPTextEncode` ★核心
- `Int`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **41%**（32/79）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`CLIPLoader`、`wanBlockSwap`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`VAEDecode`、`INTConstant`、`RIFE VFI`、`WanFirstLastFrameToVideo`、`VAELoader`、`Int`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`UNETLoader`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced、ImageResizeKJv2
