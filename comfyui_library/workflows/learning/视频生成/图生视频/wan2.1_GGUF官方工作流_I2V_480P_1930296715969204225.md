---
key: 视频生成/图生视频/wan2.1_GGUF官方工作流_I2V_480P_1930296715969204225.json
name: wan2.1_GGUF官方工作流_I2V_480P_1930296715969204225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1930296715969204225.json
hash: 5f8d6932c07c3816
coverage: 1
learned_at: 2026-10-15 22:30:05
nodes: [CLIPLoader, VAELoader, CLIPVisionLoader, CLIPVisionEncode, UnetLoaderGGUF, WanImageToVideo, KSampler, VAEDecode, VHS_VideoCombine, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, LoadImage, SaveAnimatedWEBP]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 766812192656496, "steps": 20}
---

# 视频生成/图生视频/wan2.1_GGUF官方工作流_I2V_480P_1930296715969204225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930296715969204225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `UnetLoaderGGUF` ★核心
- `WanImageToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveAnimatedWEBP`

## 关键参数

- `seed` = `766812192656496`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UnetLoaderGGUF`、`WanImageToVideo`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`SaveAnimatedWEBP`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、CLIPVisionLoader
