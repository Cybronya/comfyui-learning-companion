---
key: 视频生成/图生视频/wan2.2-i2v_官方版图生视频_1967246222643826690.json
name: wan2.2-i2v_官方版图生视频_1967246222643826690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967246222643826690.json
hash: 9c51e996ededb143
coverage: 0.952381
learned_at: 2026-10-15 22:31:41
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPVisionEncode, VAEDecode, PreviewImage, GetImageSize+, KSamplerAdvanced, CLIPVisionLoader, CLIPTextEncode, ImageResize+, WanImageToVideo, VHS_VideoCombine, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 5.4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-i2v_官方版图生视频_1967246222643826690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967246222643826690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetImageSize+`
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `5.4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`VAEDecode`、`GetImageSize+`、`KSamplerAdvanced`、`CLIPVisionLoader`、`CLIPTextEncode`、`ImageResize+`、`WanImageToVideo`、`VHS_VideoCombine`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
