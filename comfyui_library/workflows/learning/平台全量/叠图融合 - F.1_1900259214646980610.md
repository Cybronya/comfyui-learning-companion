---
key: 平台全量/叠图融合 - F.1_1900259214646980610.json
name: 叠图融合 - F.1_1900259214646980610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/叠图融合 - F.1_1900259214646980610.json
hash: f20734811ec3949b
coverage: 0.875
learned_at: 2026-11-14 01:51:20
nodes: [easy humanSegmentation, PreviewImage, LayerMask: MaskGrow, easy makeImageForICLora, MaskPreview+, PreviewImage, StyleModelApply, InpaintModelConditioning, CLIPTextEncode, VAELoader, CLIPVisionEncode, CLIPVisionLoader, FluxGuidance, CLIPTextEncode, DualCLIPLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, DownloadAndLoadFlorence2Model, ImageScale, GetImageSize+, Reroute, Florence2Run, easy cleanGpuUsed, ReActorRestoreFace, Reroute, LoadImage, LayerMask: PersonMaskUltra V2, PreviewImage, SaveImage, KSampler, CompositorTools3, VAEDecode, LoadImage, StyleModelLoader, Compositor3, easy imageInsetCrop, ImitationHueNode, CompositorConfig3, ImageScale]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 906336699386545, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/叠图融合 - F.1_1900259214646980610.json

> 来源文件 `comfyui_library/workflows/平台全量/叠图融合 - F.1_1900259214646980610.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `easy humanSegmentation`
- `PreviewImage`
- `LayerMask: MaskGrow`
- `easy makeImageForICLora`
- `MaskPreview+`
- `PreviewImage`
- `StyleModelApply`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DownloadAndLoadFlorence2Model`
- `ImageScale`
- `GetImageSize+`
- `Reroute`
- `Florence2Run`
- `easy cleanGpuUsed`
- `ReActorRestoreFace`
- `Reroute`
- `LoadImage`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `CompositorTools3`
- `VAEDecode` ★核心
- `LoadImage`
- `StyleModelLoader`
- `Compositor3`
- `easy imageInsetCrop`
- `ImitationHueNode`
- `CompositorConfig3`
- `ImageScale`

## 关键参数

- `seed` = `906336699386545`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`easy humanSegmentation`、`LayerMask: MaskGrow`、`easy makeImageForICLora`、`MaskPreview+`、`StyleModelApply`、`InpaintModelConditioning`、`CLIPTextEncode`、`VAELoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`FluxGuidance`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`DownloadAndLoadFlorence2Model`、`ImageScale`、`GetImageSize+`、`Florence2Run`、`easy cleanGpuUsed`、`ReActorRestoreFace`、`LoadImage`、`LayerMask: PersonMaskUltra V2`、`SaveImage`、`KSampler`、`CompositorTools3`、`VAEDecode`、`StyleModelLoader`、`Compositor3`、`easy imageInsetCrop`、`ImitationHueNode`、`CompositorConfig3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
