---
key: 视频生成/图生视频/Ltxvideo0.9.8 13B-图生视频+视频放大_1948228738078126081.json
name: Ltxvideo0.9.8 13B-图生视频+视频放大_1948228738078126081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948228738078126081.json
hash: 94ba6e8b668b6ff0
coverage: 1
learned_at: 2026-10-15 22:30:47
nodes: [CLIPLoader, ImageResizeKJ, CLIPTextEncode, Int, LTXVPreprocess, LTXVImgToVideo, SamplerCustom, LTXVScheduler, KSamplerSelect, LTXVConditioning, VAEDecode, RIFE VFI, Primitive integer [Crystools], ImageUpscaleWithModel, UpscaleModelLoader, VHS_VideoCombine, CheckpointLoaderSimple, LoadImage, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-13b-0.9.8-distilled-fp8.safetensors"}
---

# 视频生成/图生视频/Ltxvideo0.9.8 13B-图生视频+视频放大_1948228738078126081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948228738078126081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `CLIPLoader`
- `ImageResizeKJ`
- `CLIPTextEncode` ★核心
- `Int`
- `LTXVPreprocess`
- `LTXVImgToVideo`
- `SamplerCustom` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `VAEDecode` ★核心
- `RIFE VFI`
- `Primitive integer [Crystools]`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.8-distilled-fp8.safetensors`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPLoader`、`ImageResizeKJ`、`CLIPTextEncode`、`Int`、`LTXVPreprocess`、`LTXVImgToVideo`、`SamplerCustom`、`LTXVScheduler`、`KSamplerSelect`、`LTXVConditioning`、`VAEDecode`、`RIFE VFI`、`Primitive integer [Crystools]`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、ImageUpscaleWithModel
