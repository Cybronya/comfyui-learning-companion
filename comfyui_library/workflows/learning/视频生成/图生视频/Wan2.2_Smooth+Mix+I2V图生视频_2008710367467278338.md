---
key: 视频生成/图生视频/Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json
name: Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json
hash: e58ab9349f67ffb9
coverage: 0.819444
learned_at: 2026-10-15 22:34:08
nodes: [VAEDecode, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Note, UNETLoader, UNETLoader, CLIPLoader, UNETLoader, CLIPVisionLoader, CLIPVisionEncode, UNETLoader, SimpleMath+, INTConstant, Note, Note, Note, Note, Note, Note, Note, Note, easy cleanGpuUsed, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, WanFirstLastFrameToVideo, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, RIFE VFI, VHS_VideoCombine, VAEDecode, easy cleanGpuUsed, WanMoeKSampler, WanImageToVideo, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPVisionLoader, CLIPLoader, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, ModelPatchTorchSettings, wanBlockSwap, wanBlockSwap, LoadImage, VAELoader, Int, VAELoader, Int, CLIPTextEncode, Int, INTConstant, DF_Integer, Int, DF_Integer, Fast Groups Bypasser (rgthree), LoadImage, WanMoeKSampler, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_Smooth+Mix+I2V图生视频_2008710367467278338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008710367467278338.json`

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
- `Int`
- `CLIPTextEncode` ★核心
- `Int`
- `INTConstant`
- `DF_Integer`
- `Int`
- `DF_Integer`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

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
