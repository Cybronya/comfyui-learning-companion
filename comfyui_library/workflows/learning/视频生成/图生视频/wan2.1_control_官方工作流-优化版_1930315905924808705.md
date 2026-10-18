---
key: 视频生成/图生视频/wan2.1_control_官方工作流-优化版_1930315905924808705.json
name: wan2.1_control_官方工作流-优化版_1930315905924808705.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1_control_官方工作流-优化版_1930315905924808705.json
hash: 4f135c276c62982f
coverage: 1
learned_at: 2026-10-15 22:30:06
nodes: [SaveAnimatedWEBP, CLIPTextEncode, CLIPVisionEncode, ModelSamplingSD3, CFGZeroStar, CLIPLoader, VAELoader, CLIPVisionLoader, KSampler, CLIPTextEncode, WanFunControlToVideo, UNETLoader, LoadImage, LoadImage, VHS_VideoCombine, VAEDecode, AnimateDiffCombine]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 533987555276871, "steps": 20}
---

# 视频生成/图生视频/wan2.1_control_官方工作流-优化版_1930315905924808705.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1930315905924808705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `SaveAnimatedWEBP`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `CFGZeroStar`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `WanFunControlToVideo`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `AnimateDiffCombine`

## 关键参数

- `seed` = `533987555276871`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`SaveAnimatedWEBP`、`CLIPTextEncode`、`CLIPVisionEncode`、`ModelSamplingSD3`、`CFGZeroStar`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`KSampler`、`WanFunControlToVideo`、`UNETLoader`、`LoadImage`、`VHS_VideoCombine`、`VAEDecode`、`AnimateDiffCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStar
