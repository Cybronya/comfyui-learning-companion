---
key: 图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json
name: 最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json
hash: 1b6412e6bceccd14
coverage: 0.875
learned_at: 2026-10-10 20:59:50
nodes: [BasicGuider, VAEEncode, VAELoader, RandomNoise, KSamplerSelect, VAEDecode, DualCLIPLoader, FluxGuidance, SamplerCustomAdvanced, BasicScheduler, ControlNetApplyAdvanced, ControlNetLoader, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, ApplyFBCacheOnModel, CLIPTextEncode, CLIPTextEncode, PreviewImage, SetUnionControlNetType, LoraLoaderModelOnly, UNETLoader, CR Text, LoadImage, SaveImage]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"controlnet_strength": 0.8000000000000002}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最强Flux控制工作流_FLUX ControlNet-Union-Pro-2.0_1921750937419857922.json`

## 结构

**节点**（24 个）：
- `BasicGuider`
- `VAEEncode`
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect`
- `VAEDecode`
- `DualCLIPLoader`
- `FluxGuidance`
- `SamplerCustomAdvanced`
- `BasicScheduler`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `PreviewImage`
- `SetUnionControlNetType`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `CR Text`
- `LoadImage`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`BasicGuider`、`VAEEncode`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`DualCLIPLoader`、`FluxGuidance`、`SamplerCustomAdvanced`、`BasicScheduler`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`AIO_Preprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`ApplyFBCacheOnModel`、`CLIPTextEncode`、`PreviewImage`、`SetUnionControlNetType`、`LoraLoaderModelOnly`、`UNETLoader`

**缺卡**（2）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
