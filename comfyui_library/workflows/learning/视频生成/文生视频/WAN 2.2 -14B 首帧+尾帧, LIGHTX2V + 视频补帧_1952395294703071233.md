---
key: 视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json
name: WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json
hash: 1a16acc995f33293
coverage: 0.939394
learned_at: 2026-10-15 22:47:03
nodes: [INTConstant, INTConstant, Int, INTConstant, UnetLoaderGGUF, CLIPLoader, Int, Int, UnetLoaderGGUF, LoadImage, LoadImage, VAELoader, Power Lora Loader (rgthree), SimpleMath+, Power Lora Loader (rgthree), Note, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, WanFirstLastFrameToVideo, KSamplerAdvanced, Note, VAEDecode, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `INTConstant`
- `INTConstant`
- `Int`
- `INTConstant`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `Int`
- `Int`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `Power Lora Loader (rgthree)`
- `SimpleMath+`
- `Power Lora Loader (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `Note`
- `VAEDecode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`INTConstant`、`Int`、`UnetLoaderGGUF`、`CLIPLoader`、`LoadImage`、`VAELoader`、`Power Lora Loader (rgthree)`、`SimpleMath+`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`VAEDecode`、`RIFE VFI`、`VHS_VideoCombine`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、Power Lora Loader (rgthree)、SaveImage
