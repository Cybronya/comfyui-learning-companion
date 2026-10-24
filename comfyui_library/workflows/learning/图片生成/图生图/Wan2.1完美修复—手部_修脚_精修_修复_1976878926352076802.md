---
key: 图片生成/图生图/Wan2.1完美修复—手部_修脚_精修_修复_1976878926352076802.json
name: Wan2.1完美修复—手部_修脚_精修_修复_1976878926352076802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1完美修复—手部_修脚_精修_修复_1976878926352076802.json
hash: fbc1cdaf8d1f7a0e
coverage: 0.818182
learned_at: 2026-10-23 11:27:52
nodes: [LayerUtility: PurgeVRAM, MaskPreview+, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, InpaintModelConditioning, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, KSampler, VAEDecode, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerMask: SegmentAnythingUltra V2, ImpactSwitch, GrowMaskWithBlur, Note, LoadImage, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1018472818662087, "steps": 10}
---

# 图片生成/图生图/Wan2.1完美修复—手部_修脚_精修_修复_1976878926352076802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1完美修复—手部_修脚_精修_修复_1976878926352076802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `LayerUtility: PurgeVRAM`
- `MaskPreview+`
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `ImpactSwitch`
- `GrowMaskWithBlur`
- `Note`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `1018472818662087`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`LayerUtility: PurgeVRAM`、`MaskPreview+`、`CLIPTextEncode`、`WanVideoNAG`、`ModelSamplingSD3`、`InpaintModelConditioning`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerMask: SegmentAnythingUltra V2`、`GrowMaskWithBlur`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
