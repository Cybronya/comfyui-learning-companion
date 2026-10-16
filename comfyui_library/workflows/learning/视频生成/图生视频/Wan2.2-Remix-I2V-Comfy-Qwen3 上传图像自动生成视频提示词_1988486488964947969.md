---
key: 视频生成/图生视频/Wan2.2-Remix-I2V-Comfy-Qwen3 上传图像自动生成视频提示词_1988486488964947969.json
name: Wan2.2-Remix-I2V-Comfy-Qwen3 上传图像自动生成视频提示词_1988486488964947969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988486488964947969.json
hash: 8a1c9f253a4a3ef8
coverage: 0.771429
learned_at: 2026-10-15 22:33:03
nodes: [easy cleanGpuUsed, KSamplerAdvanced, wanBlockSwap, ModelSamplingSD3, INTConstant, wanBlockSwap, ModelSamplingSD3, CLIPTextEncode, WanImageToVideo, VAEDecode, KSamplerAdvanced, ImageResize+, CLIPTextEncode, INTConstant, INTConstant, Seed (rgthree), Fast Groups Bypasser (rgthree), Note, SetNode, VHS_VideoCombine, INTConstant, INTConstant, INTConstant, Note, MarkdownNote, UNETLoader, Note, UNETLoader, CLIPLoader, VAELoader, GetNode, easy showAnything, MultiplePathsInput, Qwen3_VQA, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2-Remix-I2V-Comfy-Qwen3 上传图像自动生成视频提示词_1988486488964947969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988486488964947969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `wanBlockSwap`
- `ModelSamplingSD3`
- `INTConstant`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResize+`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `SetNode`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `MarkdownNote`
- `UNETLoader` ★核心
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `easy showAnything`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `ImageLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`easy cleanGpuUsed`、`KSamplerAdvanced`、`wanBlockSwap`、`ModelSamplingSD3`、`INTConstant`、`CLIPTextEncode`、`WanImageToVideo`、`VAEDecode`、`ImageResize+`、`Seed (rgthree)`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`MultiplePathsInput`、`Qwen3_VQA`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、ImageResize+
