---
key: 视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json
name: Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json
hash: 3fe8a990360bdaa5
coverage: 0.434783
learned_at: 2026-10-15 22:33:45
nodes: [PathchSageAttentionKJ, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Note, Reroute, Reroute, Reroute, Reroute, Reroute, INTConstant, INTConstant, Reroute, Reroute, Reroute, easy cleanGpuUsed, VAELoader, Note, Note, Reroute, Reroute, ModelPatchTorchSettings, Reroute, VAEDecode, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PathchSageAttentionKJ, Reroute, Int, KSamplerAdvanced, KSamplerAdvanced, ModelPatchTorchSettings, WanImageToVideo, Reroute, CLIPTextEncode, easy seed, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), VHS_VideoCombine, RIFE VFI, UNETLoader, Reroute, Int, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001486989629288450.json`

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
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PathchSageAttentionKJ`
- `Reroute`
- `Int`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `WanImageToVideo`
- `Reroute`
- `CLIPTextEncode` ★核心
- `easy seed`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `RIFE VFI`
- `UNETLoader` ★核心
- `Reroute`
- `Int`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **43%**（30/69）

**有卡**：`PathchSageAttentionKJ`、`INTConstant`、`easy cleanGpuUsed`、`VAELoader`、`ModelPatchTorchSettings`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`KSamplerAdvanced`、`WanImageToVideo`、`CLIPTextEncode`、`easy seed`、`ModelSamplingSD3`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`RIFE VFI`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
