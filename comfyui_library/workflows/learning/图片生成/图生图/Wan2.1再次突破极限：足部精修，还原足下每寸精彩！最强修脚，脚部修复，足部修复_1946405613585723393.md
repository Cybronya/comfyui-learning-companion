---
key: 图片生成/图生图/Wan2.1再次突破极限：足部精修，还原足下每寸精彩！最强修脚，脚部修复，足部修复_1946405613585723393.json
name: Wan2.1再次突破极限：足部精修，还原足下每寸精彩！最强修脚，脚部修复，足部修复_1946405613585723393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1再次突破极限：足部精修，还原足下每寸精彩！最强修脚，脚部修复，足部修复_1946405613585723393.json
hash: 992cc8ed9531d113
coverage: 0.826087
learned_at: 2026-10-23 11:27:50
nodes: [LayerUtility: PurgeVRAM, MaskPreview+, WanVideoNAG, ModelSamplingSD3, InpaintModelConditioning, GrowMaskWithBlur, UNETLoader, VAELoader, CLIPLoader, KSampler, Image Comparer (rgthree), SaveImage, VAEDecode, Note, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, ImpactSwitch, LayerMask: SegmentAnythingUltra V3, CLIPTextEncode, CLIPTextEncode, LayerMask: LoadSegmentAnythingModels]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 771590054083164, "steps": 10}
---

# 图片生成/图生图/Wan2.1再次突破极限：足部精修，还原足下每寸精彩！最强修脚，脚部修复，足部修复_1946405613585723393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1再次突破极限：足部精修，还原足下每寸精彩！最强修脚，脚部修复，足部修复_1946405613585723393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `LayerUtility: PurgeVRAM`
- `MaskPreview+`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `InpaintModelConditioning`
- `GrowMaskWithBlur`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ImpactSwitch`
- `LayerMask: SegmentAnythingUltra V3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerMask: LoadSegmentAnythingModels`

## 关键参数

- `seed` = `771590054083164`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`LayerUtility: PurgeVRAM`、`MaskPreview+`、`WanVideoNAG`、`ModelSamplingSD3`、`InpaintModelConditioning`、`GrowMaskWithBlur`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`KSampler`、`SaveImage`、`VAEDecode`、`LoraLoaderModelOnly`、`LoadImage`、`LayerMask: SegmentAnythingUltra V3`、`CLIPTextEncode`、`LayerMask: LoadSegmentAnythingModels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
