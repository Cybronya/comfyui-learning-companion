---
key: 视频生成/图生视频/3d_triposplat_image_to_gaussian_splat_2064180168951943169.json
name: 3d_triposplat_image_to_gaussian_splat_2064180168951943169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/3d_triposplat_image_to_gaussian_splat_2064180168951943169.json
hash: 28e960421d85a5a7
coverage: 0.793103
learned_at: 2026-10-15 22:39:21
nodes: [SaveVideo, SaveGLB, MarkdownNote, MarkdownNote, KSampler, ComfySwitchNode, TripoSplatSamplingPreview, VAEDecodeTripoSplat, TripoSplatConditioning, SplatToMesh, SplatToFile3D, SaveGLB, CreateVideo, CreateCameraInfo, RenderSplat, PreviewImage, RemoveBackground, InvertMask, InvertMask, ComfySwitchNode, LoadBackgroundRemovalModel, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, PreviewImage, TripoSplatPreprocessImage, JoinImageWithAlpha, LoadImage]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "simple", "seed": 46, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/3d_triposplat_image_to_gaussian_splat_2064180168951943169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064180168951943169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `SaveVideo`
- `SaveGLB`
- `MarkdownNote`
- `MarkdownNote`
- `KSampler` ★核心
- `ComfySwitchNode`
- `TripoSplatSamplingPreview`
- `VAEDecodeTripoSplat` ★核心
- `TripoSplatConditioning`
- `SplatToMesh`
- `SplatToFile3D`
- `SaveGLB`
- `CreateVideo`
- `CreateCameraInfo`
- `RenderSplat`
- `PreviewImage`
- `RemoveBackground`
- `InvertMask`
- `InvertMask`
- `ComfySwitchNode`
- `LoadBackgroundRemovalModel`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `PreviewImage`
- `TripoSplatPreprocessImage`
- `JoinImageWithAlpha`
- `LoadImage`

## 关键参数

- `seed` = `46`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（23/29）

**有卡**：`SaveVideo`、`SaveGLB`、`KSampler`、`TripoSplatSamplingPreview`、`VAEDecodeTripoSplat`、`TripoSplatConditioning`、`SplatToMesh`、`SplatToFile3D`、`CreateVideo`、`CreateCameraInfo`、`RenderSplat`、`RemoveBackground`、`InvertMask`、`LoadBackgroundRemovalModel`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatPreprocessImage`、`JoinImageWithAlpha`、`LoadImage`

**用到的条目**：KSampler、VAELoader、LoadImage、UNETLoader、VAEDecodeTripoSplat、CLIPVisionLoader、TripoSplatConditioning、SaveVideo

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
