---
key: 视频生成/图生视频/Wan2.2 smooth mix图生视频_1997495774311288833.json
name: Wan2.2 smooth mix图生视频_1997495774311288833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 smooth mix图生视频_1997495774311288833.json
hash: 03dff87b13259f5f
coverage: 1
learned_at: 2026-10-15 22:33:29
nodes: [UNETLoader, UNETLoader, CLIPLoader, CLIPVisionLoader, CLIPVisionEncode, VAELoader, WanImageToVideo, Int, Int, VAEDecode, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, wanBlock_Swap, wanBlock_Swap, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, LoadImage, Int, WanMoeKSampler, ImageResize+, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 smooth mix图生视频_1997495774311288833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997495774311288833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `VAELoader`
- `WanImageToVideo`
- `Int`
- `Int`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `wanBlock_Swap`
- `wanBlock_Swap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoadImage`
- `Int`
- `WanMoeKSampler` ★核心
- `ImageResize+`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAELoader`、`WanImageToVideo`、`Int`、`VAEDecode`、`VHS_VideoCombine`、`RIFE VFI`、`wanBlock_Swap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoadImage`、`WanMoeKSampler`、`ImageResize+`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode
