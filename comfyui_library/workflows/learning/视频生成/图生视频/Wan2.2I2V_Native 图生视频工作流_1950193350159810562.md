---
key: 视频生成/图生视频/Wan2.2I2V_Native 图生视频工作流_1950193350159810562.json
name: Wan2.2I2V_Native 图生视频工作流_1950193350159810562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2I2V_Native 图生视频工作流_1950193350159810562.json
hash: 196d10dfc5ea4d22
coverage: 1
learned_at: 2026-10-15 22:30:54
nodes: [CLIPTextEncode, Switch any [Crystools], Switch any [Crystools], LayerUtility: BooleanOperator, GetImageSizeAndCount, KSamplerAdvanced, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, INTConstant, INTConstant, ModelSamplingSD3, ModelSamplingSD3, VAELoader, CLIPLoader, WanImageToVideo, LoadImage, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2I2V_Native 图生视频工作流_1950193350159810562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950193350159810562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `LayerUtility: BooleanOperator`
- `GetImageSizeAndCount`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `INTConstant`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `WanImageToVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`CLIPTextEncode`、`Switch any [Crystools]`、`LayerUtility: BooleanOperator`、`GetImageSizeAndCount`、`KSamplerAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`PathchSageAttentionKJ`、`INTConstant`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`WanImageToVideo`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
