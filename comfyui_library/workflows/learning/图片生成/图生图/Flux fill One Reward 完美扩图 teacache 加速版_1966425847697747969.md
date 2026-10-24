---
key: 图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json
name: Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json
hash: 3f3f0c086ed09a59
coverage: 0.888889
learned_at: 2026-10-23 10:58:05
nodes: [UNETLoader, DualCLIPLoader, VAELoader, ConditioningZeroOut, FluxGuidance, DifferentialDiffusion, KSampler, InpaintModelConditioning, TeaCache, SaveImage, VAEDecode, LoadImage, PreviewImage, PreviewImage, GrowMaskWithBlur, CLIPTextEncode, RH_Translator, ImagePadKJ]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc_bh2", "scheduler": "simple", "seed": 747201468645075, "steps": 22}
---

# 图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `FluxGuidance`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `InpaintModelConditioning`
- `TeaCache`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `GrowMaskWithBlur`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `ImagePadKJ`

## 关键参数

- `seed` = `747201468645075`
- `steps` = `22`
- `cfg` = `1`
- `sampler_name` = `uni_pc_bh2`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`FluxGuidance`、`DifferentialDiffusion`、`KSampler`、`InpaintModelConditioning`、`TeaCache`、`SaveImage`、`VAEDecode`、`LoadImage`、`GrowMaskWithBlur`、`CLIPTextEncode`、`RH_Translator`、`ImagePadKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
