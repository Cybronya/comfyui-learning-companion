---
key: 视频生成/图生视频/Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json
name: Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1977733586520526849.json
hash: f2dd5552e25e7c61
coverage: 0.821918
learned_at: 2026-10-15 22:32:16
nodes: [VAEDecode, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Note, UNETLoader, UNETLoader, CLIPLoader, UNETLoader, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, SimpleMath+, INTConstant, Note, Note, Note, Note, Note, Note, Note, Note, easy cleanGpuUsed, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, CLIPTextEncode, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, RIFE VFI, VHS_VideoCombine, VAEDecode, easy cleanGpuUsed, WanMoeKSampler, WanImageToVideo, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPTextEncode, CLIPVisionLoader, CLIPLoader, DF_Integer, WanMoeKSampler, VHS_VideoCombine, DF_Integer, INTConstant, wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, wanBlockSwap, wanBlockSwap, LoadImage, LoadImage, Int, Int, VAELoader, LoadImage, LoadImage, Int, Int, VAELoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977733586520526849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（73 个）：
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
- `CLIPTextEncode` ★核心
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
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPLoader`
- `DF_Integer`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `DF_Integer`
- `INTConstant`
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `wanBlockSwap`
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **82%**（60/73）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`SimpleMath+`、`INTConstant`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanFirstLastFrameToVideo`、`RIFE VFI`、`VHS_VideoCombine`、`WanMoeKSampler`、`WanImageToVideo`、`DF_Integer`、`wanBlockSwap`、`LoadImage`、`Int`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode
