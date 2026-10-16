---
key: 视频生成/图生视频/fisher版Wan2.2_lightx2V_I2V_2001317113182777346.json
name: fisher版Wan2.2_lightx2V_I2V_2001317113182777346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001317113182777346.json
hash: acda187e9c77aef2
coverage: 0.434783
learned_at: 2026-10-15 22:33:45
nodes: [PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, INTConstant, INTConstant, Reroute, Reroute, Reroute, easy cleanGpuUsed, VAELoader, Note, Note, Reroute, Reroute, ModelPatchTorchSettings, Reroute, VAEDecode, RIFE VFI, Reroute, Reroute, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VHS_VideoCombine, PathchSageAttentionKJ, Reroute, Int, KSamplerAdvanced, KSamplerAdvanced, ModelPatchTorchSettings, WanImageToVideo, Int, Reroute, CLIPTextEncode, easy seed, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, LoadImage, CLIPLoader, UNETLoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/fisher版Wan2.2_lightx2V_I2V_2001317113182777346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001317113182777346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `VAELoader`
- `Note`
- `Note`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `VAEDecode` ★核心
- `RIFE VFI`
- `Reroute`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `Reroute`
- `Int`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `WanImageToVideo`
- `Int`
- `Reroute`
- `CLIPTextEncode` ★核心
- `easy seed`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **43%**（30/69）

**有卡**：`PathchSageAttentionKJ`、`INTConstant`、`easy cleanGpuUsed`、`VAELoader`、`ModelPatchTorchSettings`、`VAEDecode`、`RIFE VFI`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`Int`、`KSamplerAdvanced`、`WanImageToVideo`、`CLIPTextEncode`、`easy seed`、`ModelSamplingSD3`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
