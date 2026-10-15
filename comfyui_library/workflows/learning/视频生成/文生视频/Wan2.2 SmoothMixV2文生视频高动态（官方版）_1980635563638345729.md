---
key: 视频生成/文生视频/Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729.json
name: Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729.json
hash: c0b77999bd66defa
coverage: 0.818182
learned_at: 2026-10-15 22:47:10
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VHS_VideoCombine, LoadImage, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, MarkdownNote, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, EmptyHunyuanLatentVideo, UNETLoader, UNETLoader, CR Text, SimpleMath+, VAEDecode, ImageFromBatch+]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 SmoothMixV2文生视频高动态（官方版）_1980635563638345729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `SimpleMath+`
- `VAEDecode` ★核心
- `ImageFromBatch+`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VHS_VideoCombine`、`LoadImage`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`CR Text`、`SimpleMath+`、`VAEDecode`、`ImageFromBatch+`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
