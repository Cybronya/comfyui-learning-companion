---
key: 图片生成/图生图/Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226.json
name: Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226.json
hash: 3de8a8be33f181cf
coverage: 0.961538
learned_at: 2026-10-23 11:27:48
nodes: [LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, JWInteger, JWInteger, JWInteger, JWInteger, PDIMAGE_LongerSize, CLIPLoader, LayerUtility: PurgeVRAM, InpaintModelConditioning, UNETLoader, CLIPTextEncode, JWInteger, CLIPTextEncode, KSampler, PreviewImage, ImagePadKJ, MaskPreview+, SaveImage, VAEDecode, ImageConcanate, SaveImage, MaskPreview+, LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 845748808074044, "steps": 10}
---

# 图片生成/图生图/Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `PDIMAGE_LongerSize`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM`
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `ImagePadKJ`
- `MaskPreview+`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `MaskPreview+`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `845748808074044`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`JWInteger`、`PDIMAGE_LongerSize`、`CLIPLoader`、`LayerUtility: PurgeVRAM`、`InpaintModelConditioning`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`ImagePadKJ`、`MaskPreview+`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
