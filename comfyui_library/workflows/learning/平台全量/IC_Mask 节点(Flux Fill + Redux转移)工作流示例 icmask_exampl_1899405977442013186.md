---
key: 平台全量/IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186.json
name: IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186.json
hash: 1491ce81395807f1
coverage: 0.954545
learned_at: 2026-11-14 00:32:21
nodes: [DualCLIPLoader, FluxGuidance, CLIPVisionLoader, CLIPVisionEncode, CLIPTextEncode, KSampler, StyleModelLoader, StyleModelApply, InpaintModelConditioning, UNETLoader, VAELoader, VAEDecode, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerMask: SegmentAnythingUltra V2, PreviewImage, LoadImage, LayerUtility: ICMask, LayerUtility: ICMaskCropBack, LoadImage, LayerUtility: RestoreCropBox, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 0, "steps": 25}
---

# 平台全量/IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186.json

> 来源文件 `comfyui_library/workflows/平台全量/IC_Mask 节点(Flux Fill + Redux转移)工作流示例 icmask_exampl_1899405977442013186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `FluxGuidance`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `StyleModelLoader`
- `StyleModelApply`
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerMask: SegmentAnythingUltra V2`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ICMask`
- `LayerUtility: ICMaskCropBack`
- `LoadImage`
- `LayerUtility: RestoreCropBox`
- `SaveImage`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`DualCLIPLoader`、`FluxGuidance`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPTextEncode`、`KSampler`、`StyleModelLoader`、`StyleModelApply`、`InpaintModelConditioning`、`UNETLoader`、`VAELoader`、`VAEDecode`、`LayerMask: MaskGrow`、`LayerUtility: CropByMask V2`、`LayerMask: SegmentAnythingUltra V2`、`LoadImage`、`LayerUtility: ICMask`、`LayerUtility: ICMaskCropBack`、`LayerUtility: RestoreCropBox`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、CLIPVisionEncode
