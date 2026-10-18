---
key: 视频生成/图生视频/wan2.1-图生视频-发光的身体_1905817606274879490.json
name: wan2.1-图生视频-发光的身体_1905817606274879490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1-图生视频-发光的身体_1905817606274879490.json
hash: 826eb29edc9232ed
coverage: 1
learned_at: 2026-10-15 22:29:26
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, CLIPVisionEncode, ModelSamplingSD3, VAELoader, CLIPLoader, CLIPVisionLoader, UNETLoader, SaveAnimatedWEBP, LoadImage, SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 300562533691168, "steps": 20}
---

# 视频生成/图生视频/wan2.1-图生视频-发光的身体_1905817606274879490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1905817606274879490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `SaveAnimatedWEBP`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `300562533691168`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`KSampler`、`CLIPTextEncode`、`WanImageToVideo`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`UNETLoader`、`SaveAnimatedWEBP`、`LoadImage`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
