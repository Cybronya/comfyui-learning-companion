---
key: 平台全量/ModelChange(ACELora_Loop)_1893860090313879554.json
name: ModelChange(ACELora_Loop)_1893860090313879554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ModelChange(ACELora_Loop)_1893860090313879554.json
hash: d2d19731ae68dc7f
coverage: 1
learned_at: 2026-11-14 00:46:28
nodes: [LayerUtility: ICMask, INPAINT_ExpandMask, CLIPVisionEncode, CLIPVisionLoader, StyleModelLoader, DifferentialDiffusion, LayerUtility: ICMaskCropBack, VAEDecode, ToBinaryMask, KSampler, ConditioningZeroOut, InpaintModelConditioning, CLIPTextEncode, CR Data Bus In, CR Data Bus In, easy forLoopEnd, easy anythingIndexSwitch, CR Data Bus Out, StyleModelApplySimple, CLIPTextEncode, VAELoader, DualCLIPLoaderGGUF, LoraLoaderModelOnly, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly, FluxGuidance, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, easy forLoopStart, LoadImage, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 50292265073341, "steps": 12}
---

# 平台全量/ModelChange(ACELora_Loop)_1893860090313879554.json

> 来源文件 `comfyui_library/workflows/平台全量/ModelChange(ACELora_Loop)_1893860090313879554.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
- `LayerUtility: ICMask`
- `INPAINT_ExpandMask`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `DifferentialDiffusion`
- `LayerUtility: ICMaskCropBack`
- `VAEDecode` ★核心
- `ToBinaryMask`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `CR Data Bus In`
- `CR Data Bus In`
- `easy forLoopEnd`
- `easy anythingIndexSwitch`
- `CR Data Bus Out`
- `StyleModelApplySimple`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `DualCLIPLoaderGGUF`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `easy forLoopStart`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `50292265073341`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（34/34）

**有卡**：`LayerUtility: ICMask`、`INPAINT_ExpandMask`、`CLIPVisionEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`DifferentialDiffusion`、`LayerUtility: ICMaskCropBack`、`VAEDecode`、`ToBinaryMask`、`KSampler`、`ConditioningZeroOut`、`InpaintModelConditioning`、`CLIPTextEncode`、`CR Data Bus In`、`easy forLoopEnd`、`easy anythingIndexSwitch`、`CR Data Bus Out`、`StyleModelApplySimple`、`VAELoader`、`DualCLIPLoaderGGUF`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`FluxGuidance`、`LayerMask: PersonMaskUltra V2`、`easy forLoopStart`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
