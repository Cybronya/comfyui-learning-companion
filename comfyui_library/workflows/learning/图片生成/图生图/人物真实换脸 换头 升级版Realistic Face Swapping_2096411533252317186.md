---
key: 图片生成/图生图/人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186.json
name: 人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186.json
hash: 670d8b06e7ceeea2
coverage: 0.868421
learned_at: 2026-10-21 00:48:05
nodes: [CLIPTextEncode, CLIPTextEncode, FluxGuidance, InpaintModelConditioning, MaskPreview+, VAEDecode, PreviewImage, Florence2Run, LayerMask: PersonMaskUltra V2, FastCanvasTool, FastCanvas, DownloadAndLoadFlorence2Model, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, StyleModelLoader, easy makeImageForICLora, Mask Fill Holes, StyleModelApply, KSampler, easy imageInsetCrop, VAELoader, CLIPVisionLoader, CLIPVisionEncode, LayerMask: MaskGrow, MaskPreview, PreviewImage, PreviewBridge, ReActorRestoreFace, RMBG, Note, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: CropByMask V2, Note, Note, LoadImage, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 906336699386511, "steps": 20}
---

# 图片生成/图生图/人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物真实换脸 换头 升级版Realistic Face Swapping_2096411533252317186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `InpaintModelConditioning`
- `MaskPreview+`
- `VAEDecode` ★核心
- `PreviewImage`
- `Florence2Run`
- `LayerMask: PersonMaskUltra V2`
- `FastCanvasTool`
- `FastCanvas`
- `DownloadAndLoadFlorence2Model`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `StyleModelLoader`
- `easy makeImageForICLora`
- `Mask Fill Holes`
- `StyleModelApply`
- `KSampler` ★核心
- `easy imageInsetCrop`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LayerMask: MaskGrow`
- `MaskPreview`
- `PreviewImage`
- `PreviewBridge`
- `ReActorRestoreFace`
- `RMBG`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: CropByMask V2`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `906336699386511`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`InpaintModelConditioning`、`MaskPreview+`、`VAEDecode`、`Florence2Run`、`LayerMask: PersonMaskUltra V2`、`FastCanvasTool`、`FastCanvas`、`DownloadAndLoadFlorence2Model`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`StyleModelLoader`、`easy makeImageForICLora`、`Mask Fill Holes`、`StyleModelApply`、`KSampler`、`easy imageInsetCrop`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LayerMask: MaskGrow`、`MaskPreview`、`PreviewBridge`、`ReActorRestoreFace`、`RMBG`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: CropByMask V2`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
