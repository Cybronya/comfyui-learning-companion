---
key: 视频生成/图生视频/Wan2.2-14B图生视频_1951683752307142657.json
name: Wan2.2-14B图生视频_1951683752307142657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951683752307142657.json
hash: 5639b6c35951989d
coverage: 1
learned_at: 2026-10-15 22:30:59
nodes: [KSamplerAdvanced, KSamplerAdvanced, VAEDecode, WanImageToVideo, CreateVideo, CLIPTextEncode, VAELoader, LoadImage, ModelSamplingSD3, ModelSamplingSD3, SaveVideo, CLIPTextEncode, UnetLoaderGGUF, UnetLoaderGGUF, CLIPLoaderGGUF]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-14B图生视频_1951683752307142657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951683752307142657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `WanImageToVideo`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoadImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoaderGGUF`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`KSamplerAdvanced`、`VAEDecode`、`WanImageToVideo`、`CreateVideo`、`CLIPTextEncode`、`VAELoader`、`LoadImage`、`ModelSamplingSD3`、`SaveVideo`、`UnetLoaderGGUF`、`CLIPLoaderGGUF`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、KSamplerAdvanced、CLIPLoaderGGUF、ClipLoaderGGUF、ClipLoaderGGUF
