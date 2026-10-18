---
key: 视频生成/图生视频/视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json
name: 视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json
hash: 0c088a0805bfde05
coverage: 0.957447
learned_at: 2026-10-15 22:32:23
nodes: [ModelSamplingSD3, CLIPLoader, VAELoader, CLIPVisionLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPVisionLoader, UNETLoader, UNETLoader, CLIPLoader, VAELoader, ImpactInt, ImpactInt, ImpactInt, Seed (rgthree), UNETLoader, easy cleanGpuUsed, ImageScaleBy, RIFE VFI, UNETLoader, ModelPatchTorchSettings, CLIPVisionEncode, SimpleMath+, ImpactInt, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, VAEDecode, WanFirstLastFrameToVideo, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, easy cleanGpuUsed, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, VAEDecode, WanImageToVideo, ImageResizeKJv2, easy cleanGpuUsed, RIFE VFI, SimpleMath+, ImageScaleBy, easy cleanGpuUsed, CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAEDecode, WanImageToVideo, easy cleanGpuUsed, SimpleMath+, ImageScaleBy, VHS_VideoCombine, VHS_VideoCombine, PathchSageAttentionKJ, easy cleanGpuUsed, KSamplerAdvanced, KSamplerAdvanced, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, RIFE VFI, PrimitiveStringMultiline, LoadImage, LoadImage, ImpactInt, ImpactInt, Fast Groups Bypasser (rgthree), VHS_VideoCombine, VHS_VideoCombine, ImpactInt, ImpactInt, ImpactInt, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979453083128336385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（94 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `RIFE VFI`
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `CLIPVisionEncode`
- `SimpleMath+`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanImageToVideo`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `SimpleMath+`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `RIFE VFI`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `ImpactInt`
- `ImpactInt`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（90/94）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`UNETLoader`、`ImpactInt`、`Seed (rgthree)`、`easy cleanGpuUsed`、`ImageScaleBy`、`RIFE VFI`、`ModelPatchTorchSettings`、`CLIPVisionEncode`、`SimpleMath+`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEDecode`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`KSamplerAdvanced`、`WanImageToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、Seed (rgthree)
