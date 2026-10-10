---
key: 视频生成/文生视频/WanVaceAdvanced_Phantom 高级工作流 ____1986410580435206146.json
name: WanVaceAdvanced_Phantom 高级工作流 ____1986410580435206146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WanVaceAdvanced_Phantom 高级工作流 ____1986410580435206146.json
hash: 9971a90de23b067a
coverage: 0.714286
learned_at: 2026-10-10 23:08:13
nodes: [VAEDecode, ModelSamplingSD3, CLIPTextEncode, ImageResizeKJv2, ConditioningCombine, ImageResizeKJv2, TrimVideoLatent, SplineEditor, PrimitiveInt, VHS_VideoInfoLoaded, VHS_LoadVideo, Fast Groups Bypasser (rgthree), CreateShapeImageOnPath, Any Switch (rgthree), VHS_VideoCombine, LoadImage, LoadImage, LoadImage, CLIPTextEncode, CLIPLoader, DiffusionModelSelector, Note, DiffusionModelLoaderKJ, Note, LoraLoaderModelOnly, Note, Note, LoraLoaderModelOnly, VAELoader, WanVacePhantomSimpleV2, ImageResizeKJv2, PreviewImage, ImageBatch, PrimitiveInt, PrimitiveInt, MarkdownNote, DWPreprocessor, VHS_VideoCombine, SetNode, ImageResizeKJv2, KSampler, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "beta57", "seed": 1234, "steps": 12}
---

# 视频生成/文生视频/WanVaceAdvanced_Phantom 高级工作流 ____1986410580435206146.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WanVaceAdvanced_Phantom 高级工作流 ____1986410580435206146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ConditioningCombine`
- `ImageResizeKJv2`
- `TrimVideoLatent`
- `SplineEditor`
- `PrimitiveInt`
- `VHS_VideoInfoLoaded`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `CreateShapeImageOnPath`
- `Any Switch (rgthree)`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `DiffusionModelSelector`
- `Note`
- `DiffusionModelLoaderKJ`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `WanVacePhantomSimpleV2`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageBatch`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `SetNode`
- `ImageResizeKJv2`
- `KSampler` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1234`
- `steps` = `12`
- `cfg` = `2.5`
- `sampler_name` = `res_multistep`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`VAEDecode`、`ModelSamplingSD3`、`CLIPTextEncode`、`ImageResizeKJv2`、`ConditioningCombine`、`TrimVideoLatent`、`SplineEditor`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`CreateShapeImageOnPath`、`VHS_VideoCombine`、`LoadImage`、`CLIPLoader`、`DiffusionModelSelector`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`WanVacePhantomSimpleV2`、`ImageBatch`、`DWPreprocessor`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、TrimVideoLatent
