---
key: 视频生成/图生视频/Wan2.2SmoothMix首尾帧高动态视频生成_1979871682087260162.json
name: Wan2.2SmoothMix首尾帧高动态视频生成_1979871682087260162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2SmoothMix首尾帧高动态视频生成_1979871682087260162.json
hash: 512519f915d27529
coverage: 0.904762
learned_at: 2026-10-15 22:32:27
nodes: [UNETLoader, UNETLoader, CLIPLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, KSamplerAdvanced, PrimitiveInt, PrimitiveInt, WanFirstLastFrameToVideo, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, VHS_VideoCombine, KSamplerAdvanced, CR Text, LoadImage, LoadImage, CLIPVisionEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1.5, "scheduler": "uni_pc", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2SmoothMix首尾帧高动态视频生成_1979871682087260162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979871682087260162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `WanFirstLastFrameToVideo`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `CR Text`
- `LoadImage`
- `LoadImage`
- `CLIPVisionEncode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1.5`
- `scheduler` = `uni_pc`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`WanFirstLastFrameToVideo`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`VHS_VideoCombine`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
