---
key: 视频生成/文生视频/FFGO_激发Wan2.2多图参考潜能_1992972427164663810.json
name: FFGO_激发Wan2.2多图参考潜能_1992972427164663810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/FFGO_激发Wan2.2多图参考潜能_1992972427164663810.json
hash: f1b467f9f103ba86
coverage: 0.962264
learned_at: 2026-10-15 22:44:08
nodes: [GetImageRangeFromBatch, SimpleMath+, ImageSharpen, VHS_VideoCombine, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, LoadImage, InspyrenetRembg, InspyrenetRembg, InspyrenetRembg, PreviewImage, CompositorConfig3, LoadImage, INTConstant, INTConstant, CLIPTextEncode, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, GetImageSizeAndCount, VAEDecode, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, UNETLoader, UNETLoader, CLIPLoader, VAELoader, ImageResizeKJv2, easy imageRemBg, ImageConcanate, easy imageRemBg, easy imageRemBg, ImageResizeKJv2, ImageConcanate, LoadImage, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, PreviewImage, SaveImage, Compositor3, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "deis", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/FFGO_激发Wan2.2多图参考潜能_1992972427164663810.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/FFGO_激发Wan2.2多图参考潜能_1992972427164663810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `GetImageRangeFromBatch`
- `SimpleMath+`
- `ImageSharpen`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `InspyrenetRembg`
- `InspyrenetRembg`
- `InspyrenetRembg`
- `PreviewImage`
- `CompositorConfig3`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetImageSizeAndCount`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `ImageConcanate`
- `easy imageRemBg`
- `easy imageRemBg`
- `ImageResizeKJv2`
- `ImageConcanate`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Compositor3`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `deis`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（51/53）

**有卡**：`GetImageRangeFromBatch`、`SimpleMath+`、`ImageSharpen`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LoadImage`、`InspyrenetRembg`、`CompositorConfig3`、`INTConstant`、`WanImageToVideo`、`KSamplerAdvanced`、`GetImageSizeAndCount`、`VAEDecode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageResizeKJv2`、`easy imageRemBg`、`ImageConcanate`、`SaveImage`、`Compositor3`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
