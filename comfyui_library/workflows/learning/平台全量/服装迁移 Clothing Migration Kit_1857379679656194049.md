---
key: 平台全量/服装迁移 Clothing Migration Kit_1857379679656194049.json
name: 服装迁移 Clothing Migration Kit_1857379679656194049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/服装迁移 Clothing Migration Kit_1857379679656194049.json
hash: 461f006792914233
coverage: 0.829787
learned_at: 2026-11-14 02:16:59
nodes: [KSamplerSelect, ModelSamplingFlux, ImageCrop+, FluxGuidance, easy cleanGpuUsed, RandomNoise, VAEDecode, easy imageSize, PreviewImage, SaveImage, CR Simple Image Compare, BasicScheduler, Seed (rgthree), SamplerCustomAdvanced, VAEEncode, SetLatentNoiseMask, CLIPTextEncode, InvertMask, LayerMask: SegmentAnythingUltra V2, Reroute, Reroute, CLIPTextEncodeFlux, CFGGuider, ControlNetInpaintingAliMamaApply, INPAINT_MaskedFill, Reroute, PreviewImage, ControlNetLoader, ImageScaleToTotalPixels, ExtraOptionsNode, LoadImage, easy cleanGpuUsed, DualCLIPLoader, VAELoader, easy imageSize, PreviewImage, JoyCaption2_simple, easy cleanGpuUsed, LoraLoaderModelOnly, TTP_text_mix, easy textSwitch, ShowText|pysssss, UNETLoader, TTP_Expand_And_Mask, easy prompt, easy prompt, ShowText|pysssss]
patterns: []
missing: []
---

# 平台全量/服装迁移 Clothing Migration Kit_1857379679656194049.json

> 来源文件 `comfyui_library/workflows/平台全量/服装迁移 Clothing Migration Kit_1857379679656194049.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `ImageCrop+`
- `FluxGuidance`
- `easy cleanGpuUsed`
- `RandomNoise`
- `VAEDecode` ★核心
- `easy imageSize`
- `PreviewImage`
- `SaveImage`
- `CR Simple Image Compare`
- `BasicScheduler`
- `Seed (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `InvertMask`
- `LayerMask: SegmentAnythingUltra V2`
- `Reroute`
- `Reroute`
- `CLIPTextEncodeFlux` ★核心
- `CFGGuider`
- `ControlNetInpaintingAliMamaApply`
- `INPAINT_MaskedFill`
- `Reroute`
- `PreviewImage`
- `ControlNetLoader`
- `ImageScaleToTotalPixels`
- `ExtraOptionsNode`
- `LoadImage`
- `easy cleanGpuUsed`
- `DualCLIPLoader`
- `VAELoader`
- `easy imageSize`
- `PreviewImage`
- `JoyCaption2_simple`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `TTP_text_mix`
- `easy textSwitch`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `TTP_Expand_And_Mask`
- `easy prompt`
- `easy prompt`
- `ShowText|pysssss`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`KSamplerSelect`、`ModelSamplingFlux`、`ImageCrop+`、`FluxGuidance`、`easy cleanGpuUsed`、`RandomNoise`、`VAEDecode`、`easy imageSize`、`SaveImage`、`CR Simple Image Compare`、`BasicScheduler`、`Seed (rgthree)`、`SamplerCustomAdvanced`、`VAEEncode`、`SetLatentNoiseMask`、`CLIPTextEncode`、`InvertMask`、`LayerMask: SegmentAnythingUltra V2`、`CLIPTextEncodeFlux`、`CFGGuider`、`ControlNetInpaintingAliMamaApply`、`INPAINT_MaskedFill`、`ControlNetLoader`、`ImageScaleToTotalPixels`、`ExtraOptionsNode`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`JoyCaption2_simple`、`LoraLoaderModelOnly`、`TTP_text_mix`、`easy textSwitch`、`UNETLoader`、`TTP_Expand_And_Mask`、`easy prompt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader
