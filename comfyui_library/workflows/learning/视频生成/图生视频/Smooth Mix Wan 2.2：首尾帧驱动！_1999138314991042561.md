---
key: 视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json
name: Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json
hash: c54805f755ef4dbd
coverage: 0.911765
learned_at: 2026-10-15 22:33:36
nodes: [CLIPLoader, Seed (rgthree), Note, ModelSamplingSD3, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, VAELoader, VAEDecode, Note, easy cleanGpuUsed, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPTextEncode, CLIPTextEncode, LoadImage, LoadImage, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, easy int, easy int, VHS_VideoCombine, UNETLoader, UNETLoader, ModelSamplingSD3, wanBlockSwap, CLIPVisionLoader, JWInteger, KSamplerAdvanced, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Smooth Mix Wan 2.2：首尾帧驱动！_1999138314991042561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999138314991042561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `CLIPLoader`
- `Seed (rgthree)`
- `Note`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `wanBlockSwap`
- `CLIPVisionLoader`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`CLIPLoader`、`Seed (rgthree)`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelPatchTorchSettings`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`LoadImage`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`VHS_VideoCombine`、`UNETLoader`、`CLIPVisionLoader`、`JWInteger`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
