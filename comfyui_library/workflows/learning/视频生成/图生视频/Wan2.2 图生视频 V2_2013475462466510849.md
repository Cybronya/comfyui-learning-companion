---
key: 视频生成/图生视频/Wan2.2 图生视频 V2_2013475462466510849.json
name: Wan2.2 图生视频 V2_2013475462466510849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2013475462466510849.json
hash: 418a9a3ab3474302
coverage: 0.9
learned_at: 2026-10-15 22:34:31
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, easy imageSize, KSamplerAdvanced, VAEDecode, ImageFromBatch+, SaveImage, UNETLoader, UNETLoader, UNETLoader, UNETLoader, Any Switch (rgthree), Any Switch (rgthree), CLIPLoader, VAELoader, JWImageResizeByLongerSide, WanImageToVideo, KSamplerAdvanced, RIFE VFI, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy positive, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 图生视频 V2_2013475462466510849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013475462466510849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `easy imageSize`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `JWImageResizeByLongerSide`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy positive`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`easy imageSize`、`KSamplerAdvanced`、`VAEDecode`、`ImageFromBatch+`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`JWImageResizeByLongerSide`、`WanImageToVideo`、`RIFE VFI`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LoadImage`、`easy positive`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
