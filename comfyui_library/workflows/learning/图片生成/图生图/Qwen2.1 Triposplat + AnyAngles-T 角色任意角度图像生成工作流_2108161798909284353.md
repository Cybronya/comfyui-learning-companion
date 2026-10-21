---
key: 图片生成/图生图/Qwen2.1 Triposplat + AnyAngles-T 角色任意角度图像生成工作流_2108161798909284353.json
name: Qwen2.1 Triposplat + AnyAngles-T 角色任意角度图像生成工作流_2108161798909284353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 Triposplat + AnyAngles-T 角色任意角度图像生成工作流_2108161798909284353.json
hash: 57426fb8c0fd43f2
coverage: 0.571429
learned_at: 2026-10-21 00:43:35
nodes: [TripoSplatConditioning, TripoSplatSamplingPreview, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, QwenImage21Cache, EmptyLatentImage, KSampler, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, Note, GetImageSize, SetNode, VAEDecodeTripoSplat, InvertMask, SetNode, RemoveBackground, JoinImageWithAlpha, InvertMask, KSampler, CLIPVisionLoader, VAELoader, VAELoader, UNETLoader, UNETLoader, VAELoader, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, SetNode, LoadBackgroundRemovalModel, TripoSplatPreprocessImage, ComfySwitchNode, GetNode, PreviewImage, ComfySwitchNode, LoadImage, VAEDecode, RenderMesh, SplatToMesh, PreviewImage, GetNode, GetNode, SplatToFile3D, CreateCameraInfo, PreviewGaussianSplat, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_2m", "scheduler": "simple", "seed": 46, "steps": 20, "width": 1024}
---

# 图片生成/图生图/Qwen2.1 Triposplat + AnyAngles-T 角色任意角度图像生成工作流_2108161798909284353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1 Triposplat + AnyAngles-T 角色任意角度图像生成工作流_2108161798909284353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `TripoSplatConditioning`
- `TripoSplatSamplingPreview`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetImageSize`
- `SetNode`
- `VAEDecodeTripoSplat` ★核心
- `InvertMask`
- `SetNode`
- `RemoveBackground`
- `JoinImageWithAlpha`
- `InvertMask`
- `KSampler` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoadBackgroundRemovalModel`
- `TripoSplatPreprocessImage`
- `ComfySwitchNode`
- `GetNode`
- `PreviewImage`
- `ComfySwitchNode`
- `LoadImage`
- `VAEDecode` ★核心
- `RenderMesh`
- `SplatToMesh`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SplatToFile3D`
- `CreateCameraInfo`
- `PreviewGaussianSplat`
- `SaveImage`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `46`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **57%**（32/56）

**有卡**：`TripoSplatConditioning`、`TripoSplatSamplingPreview`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`GetImageSize`、`VAEDecodeTripoSplat`、`InvertMask`、`RemoveBackground`、`JoinImageWithAlpha`、`CLIPVisionLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadBackgroundRemovalModel`、`TripoSplatPreprocessImage`、`LoadImage`、`VAEDecode`、`RenderMesh`、`SplatToMesh`、`SplatToFile3D`、`CreateCameraInfo`、`PreviewGaussianSplat`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
