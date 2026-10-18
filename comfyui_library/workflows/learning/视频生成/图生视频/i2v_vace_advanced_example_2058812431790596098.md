---
key: 视频生成/图生视频/i2v_vace_advanced_example_2058812431790596098.json
name: i2v_vace_advanced_example_2058812431790596098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/i2v_vace_advanced_example_2058812431790596098.json
hash: f184d9b48303dc25
coverage: 0.875
learned_at: 2026-10-15 22:38:30
nodes: [TrimVideoLatent, VAELoader, PathchSageAttentionKJ, easy int, ModelSamplingSD3, WanVaceToVideo, ModelPatchTorchSettings, ImageResize+, ImageResize+, Note, Note, CLIPTextEncode, WanVideoVACEStartToEndFrame, Note, easy int, VAEDecode, easy int, KSampler, ClipLoaderGGUF, UNETLoader, CLIPTextEncode, LoadImage, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 41, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/i2v_vace_advanced_example_2058812431790596098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058812431790596098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `TrimVideoLatent`
- `VAELoader`
- `PathchSageAttentionKJ`
- `easy int`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `ModelPatchTorchSettings`
- `ImageResize+`
- `ImageResize+`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `Note`
- `easy int`
- `VAEDecode` ★核心
- `easy int`
- `KSampler` ★核心
- `ClipLoaderGGUF`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `41`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`TrimVideoLatent`、`VAELoader`、`PathchSageAttentionKJ`、`easy int`、`ModelSamplingSD3`、`WanVaceToVideo`、`ModelPatchTorchSettings`、`ImageResize+`、`CLIPTextEncode`、`WanVideoVACEStartToEndFrame`、`VAEDecode`、`KSampler`、`ClipLoaderGGUF`、`UNETLoader`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、TrimVideoLatent、CLIPLoaderGGUF

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
