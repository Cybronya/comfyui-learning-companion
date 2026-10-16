---
key: 视频生成/图生视频/💨wan2.2_S_Mix_MFLF首中尾帧视频💨_1985812403126509569.json
name: 💨wan2.2_S_Mix_MFLF首中尾帧视频💨_1985812403126509569.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985812403126509569.json
hash: dffbbba398d5c1c3
coverage: 0.969697
learned_at: 2026-10-15 22:32:52
nodes: [VAEDecode, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, WanFirstMiddleLastFrameToVideo, ModelSamplingSD3, wanBlockSwap, ModelPatchTorchSettings, ModelPatchTorchSettings, wanBlockSwap, ModelSamplingSD3, VHS_VideoCombine, easy cleanGpuUsed, RIFE VFI, Mute / Bypass Repeater (rgthree), FlashVSRNode, CR Text, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, INTConstant, INTConstant, UNETLoader, UNETLoader, LoraLoaderModelOnly, MarkdownNote, LoadImage, LoraLoaderModelOnly, Fast Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/💨wan2.2_S_Mix_MFLF首中尾帧视频💨_1985812403126509569.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985812403126509569.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（33 个）：
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `WanFirstMiddleLastFrameToVideo`
- `ModelSamplingSD3`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `Mute / Bypass Repeater (rgthree)`
- `FlashVSRNode`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Fast Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`VAEDecode`、`KSamplerAdvanced`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`WanFirstMiddleLastFrameToVideo`、`ModelSamplingSD3`、`wanBlockSwap`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`RIFE VFI`、`Mute / Bypass Repeater (rgthree)`、`FlashVSRNode`、`CR Text`、`LoadImage`、`INTConstant`、`UNETLoader`、`LoraLoaderModelOnly`、`Fast Bypasser (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
