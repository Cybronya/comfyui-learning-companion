---
key: 视频生成/图生视频/Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json
name: Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980507194548469761.json
hash: 3d085fadeaf001f5
coverage: 0.818182
learned_at: 2026-10-15 22:32:31
nodes: [UNETLoader, UNETLoader, CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VHS_VideoCombine, LoadImage, SimpleMath+, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, CR Text, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, WanImageToVideo, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 SmoothMix图生视频高动态（官方版）_1980507194548469761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980507194548469761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LoadImage`
- `SimpleMath+`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `CR Text`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`
- `MarkdownNote`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VHS_VideoCombine`、`LoadImage`、`SimpleMath+`、`CR Text`、`VAEDecode`、`KSamplerAdvanced`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelSamplingSD3
