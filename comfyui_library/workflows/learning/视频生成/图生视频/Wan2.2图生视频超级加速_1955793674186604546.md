---
key: 视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json
name: Wan2.2图生视频超级加速_1955793674186604546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955793674186604546.json
hash: 7ede3b8b5788a261
coverage: 0.875
learned_at: 2026-10-15 22:31:10
nodes: [CLIPTextEncode, CLIPLoader, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, UnetLoaderGGUF, KSamplerAdvanced, KSamplerAdvanced, PrimitiveFloat, PrimitiveFloat, CR SDXL Aspect Ratio, LayerUtility: PurgeVRAM V2, UnetLoaderGGUF, WanImageToVideo, VAEDecode, VHS_VideoCombine, VAELoader, SimpleMath+, CLIPTextEncode, LoadImage, PrimitiveString]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955793674186604546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CR SDXL Aspect Ratio`
- `LayerUtility: PurgeVRAM V2`
- `UnetLoaderGGUF` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveString`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`KSamplerAdvanced`、`CR SDXL Aspect Ratio`、`LayerUtility: PurgeVRAM V2`、`WanImageToVideo`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`SimpleMath+`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CR SDXL Aspect Ratio
