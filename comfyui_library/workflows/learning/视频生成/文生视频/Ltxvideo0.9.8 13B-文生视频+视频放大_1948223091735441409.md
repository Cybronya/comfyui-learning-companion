---
key: 视频生成/文生视频/Ltxvideo0.9.8 13B-文生视频+视频放大_1948223091735441409.json
name: Ltxvideo0.9.8 13B-文生视频+视频放大_1948223091735441409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1948223091735441409.json
hash: 0b2696b814f3b06d
coverage: 1
learned_at: 2026-10-15 22:43:32
nodes: [CLIPLoader, SamplerCustom, EmptyLTXVLatentVideo, LTXVScheduler, KSamplerSelect, CLIPTextEncode, LTXVConditioning, VHS_VideoCombine, Primitive integer [Crystools], ImageUpscaleWithModel, UpscaleModelLoader, RIFE VFI, VAEDecode, CheckpointLoaderSimple, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 视频生成/文生视频/Ltxvideo0.9.8 13B-文生视频+视频放大_1948223091735441409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1948223091735441409.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `CLIPLoader`
- `SamplerCustom` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RIFE VFI`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPLoader`、`SamplerCustom`、`EmptyLTXVLatentVideo`、`LTXVScheduler`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVConditioning`、`VHS_VideoCombine`、`Primitive integer [Crystools]`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RIFE VFI`、`VAEDecode`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo、ImageUpscaleWithModel
