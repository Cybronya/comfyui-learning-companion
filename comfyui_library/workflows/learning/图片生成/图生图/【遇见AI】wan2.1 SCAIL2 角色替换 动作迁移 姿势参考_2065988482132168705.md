---
key: 图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json
name: 【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json
hash: 6a1a90f727320bae
coverage: 0.909091
learned_at: 2026-10-23 11:52:24
nodes: [BatchImagesNode, KSamplerSelect, BasicScheduler, CLIPVisionEncode, CLIPTextEncode, SamplerCustom, CLIPTextEncode, VHS_VideoCombine, SAM3_VideoTrack, SAM3_VideoTrack, PreviewImage, VAEDecode, WanSCAILToVideo, VHS_VideoCombine, SCAIL2ColoredMask, ImageResizeKJv2, ImageResizeKJv2, LoadImage, VHS_VideoCombine, MarkdownNote, CLIPTextEncode, ModelSamplingSD3, MarkdownNote, LoadImage, LoadImage, DiffusionModelLoaderKJ, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, VHS_LoadVideo, CLIPVisionLoader, CheckpointLoaderSimple, VAELoader]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `BatchImagesNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `PreviewImage`
- `VAEDecode` ★核心
- `WanSCAILToVideo`
- `VHS_VideoCombine`
- `SCAIL2ColoredMask`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`BatchImagesNode`、`KSamplerSelect`、`BasicScheduler`、`CLIPVisionEncode`、`CLIPTextEncode`、`SamplerCustom`、`VHS_VideoCombine`、`SAM3_VideoTrack`、`VAEDecode`、`WanSCAILToVideo`、`SCAIL2ColoredMask`、`ImageResizeKJv2`、`LoadImage`、`ModelSamplingSD3`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`CLIPLoader`、`VHS_LoadVideo`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect
