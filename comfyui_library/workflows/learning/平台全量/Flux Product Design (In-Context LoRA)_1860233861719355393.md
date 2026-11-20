---
key: 平台全量/Flux Product Design (In-Context LoRA)_1860233861719355393.json
name: Flux Product Design (In-Context LoRA)_1860233861719355393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Product Design (In-Context LoRA)_1860233861719355393.json
hash: 6ad94ff4eeb6994a
coverage: 0.88
learned_at: 2026-11-14 00:28:00
nodes: [ConditioningZeroOut, CLIPTextEncode, CFGGuider, KSamplerSelect, SetLatentNoiseMask, VAEEncode, ControlNetInpaintingAliMamaApply, ModelSamplingFlux, easy cleanGpuUsed, RandomNoise, FluxGuidance, ImageCrop+, ImageCrop+, Note, BasicScheduler, PrimitiveNode, Note, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Florence2Run, LayerUtility: ExtendCanvasV2, LayerUtility: ExtendCanvasV2, LayerUtility: If , PreviewImage, MaskPreview+, ImageResize+, SamplerCustomAdvanced, easy imageSize, easy int, easy imageSize, ImagePadForOutpaint, PreviewImage, easy compare, VAEDecode, CR Simple Image Compare, easy imageSize, Replace Text _O, Replace Text _O, DownloadAndLoadFlorence2Model, SaveImage, SaveImage, CheckpointLoaderSimple, LoraLoader, LoraLoaderModelOnly, ControlNetLoader, LoadImage, ShowText|pysssss, CR Text]
patterns: [lora]
missing: []
parameters: {"checkpoint": "flux1-dev-fp8.safetensors", "lora_name": "FLUX.1-Turbo-Alpha.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Flux Product Design (In-Context LoRA)_1860233861719355393.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Product Design (In-Context LoRA)_1860233861719355393.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `ControlNetInpaintingAliMamaApply`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `RandomNoise`
- `FluxGuidance`
- `ImageCrop+`
- `ImageCrop+`
- `Note`
- `BasicScheduler`
- `PrimitiveNode`
- `Note`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `Florence2Run`
- `LayerUtility: ExtendCanvasV2`
- `LayerUtility: ExtendCanvasV2`
- `LayerUtility: If `
- `PreviewImage`
- `MaskPreview+`
- `ImageResize+`
- `SamplerCustomAdvanced` ★核心
- `easy imageSize`
- `easy int`
- `easy imageSize`
- `ImagePadForOutpaint`
- `PreviewImage`
- `easy compare`
- `VAEDecode` ★核心
- `CR Simple Image Compare`
- `easy imageSize`
- `Replace Text _O`
- `Replace Text _O`
- `DownloadAndLoadFlorence2Model`
- `SaveImage`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `LoadImage`
- `ShowText|pysssss`
- `CR Text`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `lora_name` = `FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`CFGGuider`、`KSamplerSelect`、`SetLatentNoiseMask`、`VAEEncode`、`ControlNetInpaintingAliMamaApply`、`ModelSamplingFlux`、`easy cleanGpuUsed`、`RandomNoise`、`FluxGuidance`、`ImageCrop+`、`BasicScheduler`、`SimpleMath+`、`Florence2Run`、`LayerUtility: ExtendCanvasV2`、`LayerUtility: If `、`MaskPreview+`、`ImageResize+`、`SamplerCustomAdvanced`、`easy imageSize`、`easy int`、`ImagePadForOutpaint`、`easy compare`、`VAEDecode`、`CR Simple Image Compare`、`Replace Text _O`、`DownloadAndLoadFlorence2Model`、`SaveImage`、`CheckpointLoaderSimple`、`LoraLoader`、`LoraLoaderModelOnly`、`ControlNetLoader`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader
