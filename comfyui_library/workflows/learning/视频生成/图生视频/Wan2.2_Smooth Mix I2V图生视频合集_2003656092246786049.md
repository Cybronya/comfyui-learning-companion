---
key: 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频合集_2003656092246786049.json
name: Wan2.2_Smooth Mix I2V图生视频合集_2003656092246786049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2003656092246786049.json
hash: 1ae42b58050b0fe3
coverage: 0.819444
learned_at: 2026-10-15 22:33:51
nodes: [VAEDecode, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Note, UNETLoader, UNETLoader, CLIPLoader, UNETLoader, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, SimpleMath+, INTConstant, Note, Note, Note, Note, Note, Note, Note, Note, easy cleanGpuUsed, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, RIFE VFI, VHS_VideoCombine, VAEDecode, easy cleanGpuUsed, WanMoeKSampler, WanImageToVideo, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPVisionLoader, CLIPLoader, WanMoeKSampler, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, wanBlockSwap, wanBlockSwap, LoadImage, VAELoader, Int, VAELoader, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Int, CLIPTextEncode, Int, INTConstant, DF_Integer, Int, DF_Integer, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频合集_2003656092246786049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2003656092246786049.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（72 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `SimpleMath+`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Note`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `WanMoeKSampler` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CLIPVisionLoader`
- `CLIPLoader`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoadImage`
- `VAELoader`
- `Int`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `CLIPTextEncode` ★核心
- `Int`
- `INTConstant`
- `DF_Integer`
- `Int`
- `DF_Integer`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **82%**（59/72）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SimpleMath+`、`INTConstant`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanFirstLastFrameToVideo`、`RIFE VFI`、`VHS_VideoCombine`、`WanMoeKSampler`、`WanImageToVideo`、`wanBlockSwap`、`LoadImage`、`VAELoader`、`Int`、`DF_Integer`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode
