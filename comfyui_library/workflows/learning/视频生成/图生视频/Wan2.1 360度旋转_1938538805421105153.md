---
key: 视频生成/图生视频/Wan2.1 360度旋转_1938538805421105153.json
name: Wan2.1 360度旋转_1938538805421105153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 360度旋转_1938538805421105153.json
hash: c3fdd82772d46e00
coverage: 1
learned_at: 2026-10-15 22:30:31
nodes: [VAEDecode, CLIPLoader, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, VAELoader, WanVideoTeaCacheKJ, WanVideoEnhanceAVideoKJ, CLIPTextEncode, KSampler, WanImageToVideo, LoadImage, LoraLoaderModelOnly, VHS_VideoCombine, MathExpression|pysssss, UnetLoaderGGUF, ImageResizeKJ, Int, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1060784166482917, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 360度旋转_1938538805421105153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1938538805421105153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `WanVideoTeaCacheKJ`
- `WanVideoEnhanceAVideoKJ`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `WanImageToVideo`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `UnetLoaderGGUF` ★核心
- `ImageResizeKJ`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `1060784166482917`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`VAEDecode`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`VAELoader`、`WanVideoTeaCacheKJ`、`WanVideoEnhanceAVideoKJ`、`KSampler`、`WanImageToVideo`、`LoadImage`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`MathExpression|pysssss`、`UnetLoaderGGUF`、`ImageResizeKJ`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode
