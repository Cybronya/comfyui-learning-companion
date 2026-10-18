---
key: 视频生成/图生视频/WAN2.2+Smooth+Mix高质量图生视频_1980210462413459458.json
name: WAN2.2+Smooth+Mix高质量图生视频_1980210462413459458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2+Smooth+Mix高质量图生视频_1980210462413459458.json
hash: d32d58a19fab370a
coverage: 0.875
learned_at: 2026-10-15 22:32:29
nodes: [ModelSamplingSD3, CLIPLoader, VAELoader, CLIPVisionLoader, easy int, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, VAEDecode, ModelSamplingSD3, UNETLoader, UNETLoader, WanImageToVideo, easy seed, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, easy int, PrimitiveStringMultiline, PrimitiveFloat, LoadImage, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2+Smooth+Mix高质量图生视频_1980210462413459458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980210462413459458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `easy seed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `easy int`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAEDecode`、`UNETLoader`、`WanImageToVideo`、`easy seed`、`KSamplerAdvanced`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、easy seed
