---
key: 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json
name: Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json
hash: f0f6eb24ca84c4da
coverage: 0.875
learned_at: 2026-10-15 22:32:46
nodes: [CLIPVisionEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, VHS_VideoCombine, PrimitiveInt, KSamplerAdvanced, KSamplerAdvanced, WanFirstLastFrameToVideo, VAEDecode, SimpleMath+, CLIPVisionEncode, CLIPVisionLoader, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, CR Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "uni_pc", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 SmoothMix首尾帧视频高动态（官方版）（双图）_1983902184238710786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983902184238710786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（24 个）：
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `SimpleMath+`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPVisionEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VHS_VideoCombine`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`VAEDecode`、`SimpleMath+`、`CLIPVisionLoader`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
