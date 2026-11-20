---
key: 平台全量/flux nunchakus + redux + openpose自动换装工作流(极速版)_1938470998121316354.json
name: flux nunchakus + redux + openpose自动换装工作流(极速版)_1938470998121316354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux nunchakus + redux + openpose自动换装工作流(极速版)_1938470998121316354.json
hash: 0e3dea5364e77603
coverage: 0.869565
learned_at: 2026-11-14 01:10:43
nodes: [GrowMask, KSampler, easy imageSize, PreviewImage, Image Blank, ImageConcanate, ImageToMask, easy cleanGpuUsed, ImageConcanate, PreviewImage, DualCLIPLoader, StyleModelLoader, StyleModelLoader, DifferentialDiffusion, FluxGuidance, StyleModelApply, LoadImage, LoraLoader, MaskToImage, CLIPTextEncode, SaveImage, PreviewImage, NunchakuFluxDiTLoader, CLIPVisionLoader, CLIPVisionEncode, ReduxAdvanced, Anything Everywhere, VAELoader, Anything Everywhere, VAEDecode, CLIPTextEncode, LayerMask: PersonMaskUltra V2, InpaintModelConditioning, ControlNetApplyAdvanced, Image Blank, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetUnionControlNetType, DWPreprocessor, Crop (mtb), Int, PreviewImage, LoadImage, ImageConcanate]
patterns: [lora]
missing: []
parameters: {"cfg": 1.01, "controlnet_strength": 1, "denoise": 1, "lora_name": "ACE++ comfyui_local_lora16_comfyui_local.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 412202023184371, "steps": 30, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/flux nunchakus + redux + openpose自动换装工作流(极速版)_1938470998121316354.json

> 来源文件 `comfyui_library/workflows/平台全量/flux nunchakus + redux + openpose自动换装工作流(极速版)_1938470998121316354.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `GrowMask`
- `KSampler` ★核心
- `easy imageSize`
- `PreviewImage`
- `Image Blank`
- `ImageConcanate`
- `ImageToMask`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `PreviewImage`
- `DualCLIPLoader`
- `StyleModelLoader`
- `StyleModelLoader`
- `DifferentialDiffusion`
- `FluxGuidance`
- `StyleModelApply`
- `LoadImage`
- `LoraLoader` ★核心
- `MaskToImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `PreviewImage`
- `NunchakuFluxDiTLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ReduxAdvanced`
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LayerMask: PersonMaskUltra V2`
- `InpaintModelConditioning`
- `ControlNetApplyAdvanced` ★核心
- `Image Blank`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetUnionControlNetType`
- `DWPreprocessor`
- `Crop (mtb)`
- `Int`
- `PreviewImage`
- `LoadImage`
- `ImageConcanate`

**识别到的模式**：lora

## 关键参数

- `seed` = `412202023184371`
- `steps` = `30`
- `cfg` = `1.01`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `lora_name` = `ACE++ comfyui_local_lora16_comfyui_local.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`GrowMask`、`KSampler`、`easy imageSize`、`Image Blank`、`ImageConcanate`、`ImageToMask`、`easy cleanGpuUsed`、`DualCLIPLoader`、`StyleModelLoader`、`DifferentialDiffusion`、`FluxGuidance`、`StyleModelApply`、`LoadImage`、`LoraLoader`、`MaskToImage`、`CLIPTextEncode`、`SaveImage`、`NunchakuFluxDiTLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ReduxAdvanced`、`VAELoader`、`VAEDecode`、`LayerMask: PersonMaskUltra V2`、`InpaintModelConditioning`、`ControlNetApplyAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`SetUnionControlNetType`、`DWPreprocessor`、`Crop (mtb)`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType
