---
key: 视频生成/图生视频/Wan2.2-Smooth Mix+FMLF首尾帧实现人物场景融合_1990339070041747458.json
name: Wan2.2-Smooth Mix+FMLF首尾帧实现人物场景融合_1990339070041747458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Smooth Mix+FMLF首尾帧实现人物场景融合_1990339070041747458.json
hash: ddd9c31e5bfe3486
coverage: 1
learned_at: 2026-10-15 22:33:10
nodes: [ModelPatchTorchSettings, CLIPLoader, DF_Integer, UNETLoader, VAELoader, VHS_VideoCombine, wanBlockSwap, wanBlockSwap, WanMoeKSampler, CLIPTextEncode, LoadImage, WanFirstMiddleLastFrameToVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, Int, Int, SimpleMath+, VAEDecode, CLIPTextEncode, RIFE VFI, VHS_VideoCombine, easy imageRemBg, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Smooth Mix+FMLF首尾帧实现人物场景融合_1990339070041747458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990339070041747458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（25 个）：
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `DF_Integer`
- `UNETLoader` ★核心
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `wanBlockSwap`
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `WanFirstMiddleLastFrameToVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `Int`
- `Int`
- `SimpleMath+`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ModelPatchTorchSettings`、`CLIPLoader`、`DF_Integer`、`UNETLoader`、`VAELoader`、`VHS_VideoCombine`、`wanBlockSwap`、`WanMoeKSampler`、`CLIPTextEncode`、`LoadImage`、`WanFirstMiddleLastFrameToVideo`、`PathchSageAttentionKJ`、`Int`、`SimpleMath+`、`VAEDecode`、`RIFE VFI`、`easy imageRemBg`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、DF_Integer
