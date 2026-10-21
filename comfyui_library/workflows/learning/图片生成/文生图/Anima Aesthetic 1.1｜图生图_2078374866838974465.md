---
key: 图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json
name: Anima Aesthetic 1.1｜图生图_2078374866838974465
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json
hash: 82e36ac68627836e
coverage: 0.894737
learned_at: 2026-10-20 00:18:45
nodes: [Qwen3VLProcessor, KSampler, VAEDecode, image_scale_pixel_v2, LoadImage, SaveImage, PreviewImage, VAEDecode, SaveImage, XB_UNetNameBroadcaster, EnhancedLoadDiffusionModel, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAELoader, CLIPLoader, ClownsharKSampler_Beta, PreviewImage, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 31, "denoise": 4.000000000000001, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "beta57"}
---

# 图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `Qwen3VLProcessor`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `image_scale_pixel_v2`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `XB_UNetNameBroadcaster`
- `EnhancedLoadDiffusionModel`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `ClownsharKSampler_Beta` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `31`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `4.000000000000001`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`Qwen3VLProcessor`、`KSampler`、`VAEDecode`、`image_scale_pixel_v2`、`LoadImage`、`SaveImage`、`XB_UNetNameBroadcaster`、`EnhancedLoadDiffusionModel`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`CLIPLoader`、`ClownsharKSampler_Beta`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、ClownsharKSampler_Beta
