---
key: 视频生成/文生视频/LTXV0.9.6-多帧控制-秒级图生视频_1897448492304912386.json
name: LTXV0.9.6-多帧控制-秒级图生视频_1897448492304912386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1897448492304912386.json
hash: f5aa08b827add2c7
coverage: 0.957447
learned_at: 2026-10-15 22:43:20
nodes: [LTXVScheduler, SamplerCustom, CLIPTextEncode, KSamplerSelect, LTXVConditioning, VAEDecode, LTXVScheduler, KSamplerSelect, LTXVPreprocess, CLIPTextEncode, LTXVScheduler, LTXVAddGuide, LTXVPreprocess, KSamplerSelect, LTXVAddGuide, LTXVPreprocess, Note, LTXVCropGuides, LTXVConditioning, VAEDecode, CLIPTextEncode, Note, EmptyLTXVLatentVideo, VHS_VideoCombine, CLIPTextEncode, LTXVConditioning, SamplerCustom, LTXVImgToVideo, VHS_VideoCombine, CLIPTextEncode, SamplerCustom, LoadImage, LoadImage, LoadImage, CLIPTextEncode, VHS_VideoCombine, VAEDecode, CLIPLoader, Primitive integer [Crystools], EmptyLTXVLatentVideo, Primitive integer [Crystools], Primitive integer [Crystools], CLIPLoader, CLIPLoader, CheckpointLoaderSimple, CheckpointLoaderSimple, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"checkpoint": "ltxv-2b-0.9.6-dev-04-25-v1.safetensors"}
---

# 视频生成/文生视频/LTXV0.9.6-多帧控制-秒级图生视频_1897448492304912386.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1897448492304912386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（47 个）：
- `LTXVScheduler`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LTXVScheduler`
- `LTXVAddGuide`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `LTXVAddGuide`
- `LTXVPreprocess`
- `Note`
- `LTXVCropGuides`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LTXVImgToVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPLoader`
- `Primitive integer [Crystools]`
- `EmptyLTXVLatentVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `CLIPLoader`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `ltxv-2b-0.9.6-dev-04-25-v1.safetensors`

## 知识

覆盖率 **96%**（45/47）

**有卡**：`LTXVScheduler`、`SamplerCustom`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVConditioning`、`VAEDecode`、`LTXVPreprocess`、`LTXVAddGuide`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LTXVImgToVideo`、`LoadImage`、`CLIPLoader`、`Primitive integer [Crystools]`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustom、EmptyLTXVLatentVideo
