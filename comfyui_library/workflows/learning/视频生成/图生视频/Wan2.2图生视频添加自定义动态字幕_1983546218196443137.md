---
key: 视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json
name: Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json
hash: 6b364eb3335910d5
coverage: 0.75
learned_at: 2026-10-15 22:32:45
nodes: [CLIPLoader, VAELoader, LoadImage, SimpleMath+, PrimitiveInt, WanImageToVideo, MarkdownNote, 孤海-取色器, VAEDecode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, UNETLoader, ModelSamplingSD3, LoadImage, PrimitiveInt, PrimitiveInt, CR Text, CR Text, PrimitiveNode, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, VHS_VideoCombine, VHS_VideoCombine, HAIGC_VideoSubtitleEnhanced, Reroute, PrimitiveNode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1.5, "scheduler": "uni_pc", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2图生视频添加自定义动态字幕_1983546218196443137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983546218196443137.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `SimpleMath+`
- `PrimitiveInt`
- `WanImageToVideo`
- `MarkdownNote`
- `孤海-取色器`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Text`
- `CR Text`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `HAIGC_VideoSubtitleEnhanced`
- `Reroute`
- `PrimitiveNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1.5`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`SimpleMath+`、`WanImageToVideo`、`孤海-取色器`、`VAEDecode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`CR Text`、`CLIPTextEncode`、`VHS_VideoCombine`、`HAIGC_VideoSubtitleEnhanced`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ModelSamplingSD3
