---
key: 图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json
name: 【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json
hash: 0dbf212eb803e572
coverage: 0.9
learned_at: 2026-10-23 11:53:10
nodes: [ModelSamplingSD3, CLIPTextEncode, InpaintModelConditioning, CLIPTextEncode, UNETLoader, VAELoader, LoraLoaderModelOnly, MarkdownNote, LoadImage, CLIPLoader, UltralyticsDetectorProvider, BboxDetectorCombined_v2, LayerMask: MaskPreview, KSampler, GrowMaskWithBlur, LayerMask: MaskPreview, SaveImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.05000000000000001, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 710132226529570, "steps": 10}
---

# 图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadImage`
- `CLIPLoader`
- `UltralyticsDetectorProvider`
- `BboxDetectorCombined_v2`
- `LayerMask: MaskPreview`
- `KSampler` ★核心
- `GrowMaskWithBlur`
- `LayerMask: MaskPreview`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `710132226529570`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.05000000000000001`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`InpaintModelConditioning`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPLoader`、`UltralyticsDetectorProvider`、`BboxDetectorCombined_v2`、`LayerMask: MaskPreview`、`KSampler`、`GrowMaskWithBlur`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
