---
key: 图片生成/文生图/F.1+Advanced ControlNet+遮罩_1924358166027694081.json
name: F.1+Advanced ControlNet+遮罩_1924358166027694081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1+Advanced ControlNet+遮罩_1924358166027694081.json
hash: 7a1eddb053b39fc2
coverage: 0.794118
learned_at: 2026-10-10 20:58:30
nodes: [VAEDecode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, ModelSamplingFlux, FluxGuidance, SDXLEmptyLatentSizePicker+, SetUnionControlNetType, AIO_Preprocessor, ImageScale, CLIPTextEncode, LayerColor: AutoAdjustV2, ImageScale, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, InspyrenetRembg, MaskToImage, PreviewImage, PreviewImage, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, MaskToImage, Mask Invert, PreviewImage, PreviewImage, SaveImage, LoadImage, LoadImage, DualCLIPLoader, VAELoader, ControlNetLoader, UNETLoader]
patterns: []
missing: [LayerColor: AutoAdjustV2, Mask Invert, SDXLEmptyLatentSizePicker+]
parameters: {"batch_size": 0, "controlnet_strength": 0.6, "height": 1, "width": "768x1280 (0.6)"}
discoveries: [次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识, 次要节点 `Mask Invert` 知识库中没有该节点类型的任何知识, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/F.1+Advanced ControlNet+遮罩_1924358166027694081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1+Advanced ControlNet+遮罩_1924358166027694081.json`

## 结构

**节点**（34 个）：
- `VAEDecode`
- `SamplerCustomAdvanced`
- `KSamplerSelect`
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `ModelSamplingFlux`
- `FluxGuidance`
- `SDXLEmptyLatentSizePicker+`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ImageScale`
- `CLIPTextEncode`
- `LayerColor: AutoAdjustV2`
- `ImageScale`
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `InspyrenetRembg`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2`
- `MaskToImage`
- `Mask Invert`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `UNETLoader`

## 关键参数

- `batch_size` = `0`
- `controlnet_strength` = `0.6`
- `height` = `1`
- `width` = `768x1280 (0.6)`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`VAEDecode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`ModelSamplingFlux`、`FluxGuidance`、`SDXLEmptyLatentSizePicker+`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ImageScale`、`CLIPTextEncode`、`LayerColor: AutoAdjustV2`、`ACN_AdvancedControlNetApplySingle_v2`、`InspyrenetRembg`、`MaskToImage`、`PreviewImage`、`Mask Invert`

**缺卡**（3）：`LayerColor: AutoAdjustV2`、`Mask Invert`、`SDXLEmptyLatentSizePicker+`

## 学习发现

- 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识
- 次要节点 `Mask Invert` 知识库中没有该节点类型的任何知识
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
