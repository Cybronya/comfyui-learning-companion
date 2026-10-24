---
key: 图片生成/图生图/FLUX图片转绘v1.0_1921351798492430337.json
name: FLUX图片转绘v1.0_1921351798492430337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX图片转绘v1.0_1921351798492430337.json
hash: 3fa8e0a11182e0b8
coverage: 0.806452
learned_at: 2026-10-23 10:54:50
nodes: [BasicScheduler, CLIPTextEncode, CLIPTextEncode, FluxGuidance, VAEDecode, PrimitiveNode, PrimitiveNode, Florence2Run, DepthAnythingV2Preprocessor, PreviewImage, ttN text, ShowText|pysssss, SamplerCustom, LayerUtility: TextJoin, KSamplerSelect, DF_Image_scale_to_side, VAELoader, ControlNetApplyAdvanced, ColorCorrect, LoadImage, ControlNetLoader, Florence2ModelLoader, PrimitiveNode, VAEEncode, RepeatLatentBatch, CR Apply LoRA Stack, CR LoRA Stack, DualCLIPLoader, SaveImage, Note, UNETLoader]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.7500000000000001}
---

# 图片生成/图生图/FLUX图片转绘v1.0_1921351798492430337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX图片转绘v1.0_1921351798492430337.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `VAEDecode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `Florence2Run`
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `ttN text`
- `ShowText|pysssss`
- `SamplerCustom` ★核心
- `LayerUtility: TextJoin`
- `KSamplerSelect` ★核心
- `DF_Image_scale_to_side`
- `VAELoader`
- `ControlNetApplyAdvanced` ★核心
- `ColorCorrect`
- `LoadImage`
- `ControlNetLoader`
- `Florence2ModelLoader`
- `PrimitiveNode`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `CR Apply LoRA Stack`
- `CR LoRA Stack`
- `DualCLIPLoader`
- `SaveImage`
- `Note`
- `UNETLoader` ★核心

## 关键参数

- `controlnet_strength` = `0.7500000000000001`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`BasicScheduler`、`CLIPTextEncode`、`FluxGuidance`、`VAEDecode`、`Florence2Run`、`DepthAnythingV2Preprocessor`、`ttN text`、`SamplerCustom`、`LayerUtility: TextJoin`、`KSamplerSelect`、`DF_Image_scale_to_side`、`VAELoader`、`ControlNetApplyAdvanced`、`ColorCorrect`、`LoadImage`、`ControlNetLoader`、`Florence2ModelLoader`、`VAEEncode`、`RepeatLatentBatch`、`CR Apply LoRA Stack`、`CR LoRA Stack`、`DualCLIPLoader`、`SaveImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、DepthAnythingV2Preprocessor
