---
key: 视频生成/图生视频/本地版 SCAIL2  Wan 2.1 神级模型  单人单图 _ 多图参考图视频迁移工作流_2083431427026284546.json
name: 本地版 SCAIL2  Wan 2.1 神级模型  单人单图 _ 多图参考图视频迁移工作流_2083431427026284546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/本地版 SCAIL2  Wan 2.1 神级模型  单人单图 _ 多图参考图视频迁移工作流_2083431427026284546.json
hash: 8b034d75e82e0b89
coverage: 0.833333
learned_at: 2026-10-16 19:17:41
nodes: [ImageResizeKJv2, LoadImage, LoadImage, PixaromaLabel, MarkdownNote, LoadImage, LoadImage, PixaromaLabel, PixaromaLabel, PixaromaLabel, RIFE VFI, Fast Groups Bypasser (rgthree), INTConstant, SimpleMath+, easy showAnything, CLIPLoader, CLIPTextEncode, RMBG, RMBG, ImpactInt, BatchImagesNode, CLIPTextEncode, CLIPTextEncode, PreviewImage, WanSCAILToVideo, RMBG, ImageResizeKJv2, PreviewImage, MarkdownNote, MarkdownNote, VAEDecodeTiled, CLIPTextEncode, VHS_VideoCombine, Switch any [Crystools], BatchImagesNode, KSampler, VHS_VideoCombine, PreviewImage, VHS_VideoInfoLoaded, Any Switch (rgthree), PrimitiveBoolean, SAM3_VideoTrack, SAM3_VideoTrack, VHS_VideoCombine, CheckpointLoaderSimple, CLIPVisionEncode, Any Switch (rgthree), ImageResizeKJv2, LoadImage, ImageResizeKJv2, CR Prompt Text, PixaromaResolution, DiffusionModelLoaderKJ, VHS_LoadVideo, VAELoader, CLIPVisionLoader, WanContextWindowsManual, SCAIL2ColoredMask, RHHiddenNodes, PathchSageAttentionKJ]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 287451098834451, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/本地版 SCAIL2  Wan 2.1 神级模型  单人单图 _ 多图参考图视频迁移工作流_2083431427026284546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/本地版 SCAIL2  Wan 2.1 神级模型  单人单图 _ 多图参考图视频迁移工作流_2083431427026284546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `PixaromaLabel`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `PixaromaLabel`
- `PixaromaLabel`
- `PixaromaLabel`
- `RIFE VFI`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `SimpleMath+`
- `easy showAnything`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `RMBG`
- `RMBG`
- `ImpactInt`
- `BatchImagesNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `WanSCAILToVideo`
- `RMBG`
- `ImageResizeKJv2`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Switch any [Crystools]`
- `BatchImagesNode`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `Any Switch (rgthree)`
- `PrimitiveBoolean`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionEncode`
- `Any Switch (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `PixaromaResolution`
- `DiffusionModelLoaderKJ`
- `VHS_LoadVideo`
- `VAELoader`
- `CLIPVisionLoader`
- `WanContextWindowsManual`
- `SCAIL2ColoredMask`
- `RHHiddenNodes`
- `PathchSageAttentionKJ`

## 关键参数

- `seed` = `287451098834451`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`ImageResizeKJv2`、`LoadImage`、`PixaromaLabel`、`RIFE VFI`、`INTConstant`、`SimpleMath+`、`CLIPLoader`、`CLIPTextEncode`、`RMBG`、`ImpactInt`、`BatchImagesNode`、`WanSCAILToVideo`、`VAEDecodeTiled`、`VHS_VideoCombine`、`Switch any [Crystools]`、`KSampler`、`VHS_VideoInfoLoaded`、`PrimitiveBoolean`、`SAM3_VideoTrack`、`CheckpointLoaderSimple`、`CLIPVisionEncode`、`CR Prompt Text`、`PixaromaResolution`、`DiffusionModelLoaderKJ`、`VHS_LoadVideo`、`VAELoader`、`CLIPVisionLoader`、`WanContextWindowsManual`、`SCAIL2ColoredMask`、`RHHiddenNodes`、`PathchSageAttentionKJ`

**用到的条目**：KSampler、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、VAEDecodeTiled、CLIPVisionEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
