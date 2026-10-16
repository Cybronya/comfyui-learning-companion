---
key: 视频生成/图生视频/Wan2.2 Smooth 图生视频_2041522312066895874.json
name: Wan2.2 Smooth 图生视频_2041522312066895874.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041522312066895874.json
hash: 0224ba4727334e26
coverage: 0.909091
learned_at: 2026-10-15 22:36:20
nodes: [CLIPLoader, CLIPVisionLoader, CR Prompt Text, Text Concatenate, easy showAnything, Seed (rgthree), KSamplerAdvanced, MultiplePathsInput, CR Prompt Text, ModelSamplingSD3, KSamplerAdvanced, easy showAnything, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, VAELoader, PainterI2V, easy showAnything, ImageResizeKJv2, easy cleanGpuUsed, Qwen3_VQA, ImageResize+, ModelSamplingSD3, JWInteger, Text Concatenate, JWInteger, JWInteger, ImageLoader, CR Prompt Text, UNETLoader, UNETLoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Smooth 图生视频_2041522312066895874.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041522312066895874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（33 个）：
- `CLIPLoader`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `Text Concatenate`
- `easy showAnything`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `MultiplePathsInput`
- `CR Prompt Text`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAELoader`
- `PainterI2V`
- `easy showAnything`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `Qwen3_VQA`
- `ImageResize+`
- `ModelSamplingSD3`
- `JWInteger`
- `Text Concatenate`
- `JWInteger`
- `JWInteger`
- `ImageLoader`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`CLIPLoader`、`CLIPVisionLoader`、`CR Prompt Text`、`Text Concatenate`、`Seed (rgthree)`、`KSamplerAdvanced`、`MultiplePathsInput`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`PainterI2V`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`Qwen3_VQA`、`ImageResize+`、`JWInteger`、`ImageLoader`、`UNETLoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、CLIPVisionEncode
