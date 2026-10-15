---
key: 图片生成/文生图/Flux CN Union Pro 2.0通用基础生成_1924342356764446722.json
name: Flux CN Union Pro 2.0通用基础生成_1924342356764446722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux CN Union Pro 2.0通用基础生成_1924342356764446722.json
hash: 9f45e924c6b50a80
coverage: 0.863636
learned_at: 2026-10-10 20:58:34
nodes: [BasicGuider, SDXLEmptyLatentSizePicker+, ImageScale, FluxGuidance, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, ModelSamplingFlux, AIO_Preprocessor, BasicScheduler, SaveImage, VAEDecode, LayerColor: AutoAdjustV2, CLIPTextEncode, VAEDecode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, ModelSamplingFlux, FluxGuidance, SDXLEmptyLatentSizePicker+, SetUnionControlNetType, SaveImage, ImageScale, CLIPTextEncode, ACN_AdvancedControlNetApplySingle_v2, LayerColor: AutoAdjustV2, VAEDecode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, ModelSamplingFlux, FluxGuidance, SDXLEmptyLatentSizePicker+, SetUnionControlNetType, AIO_Preprocessor, ImageScale, CLIPTextEncode, ACN_AdvancedControlNetApplySingle_v2, LayerColor: AutoAdjustV2, VAEDecode, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, ModelSamplingFlux, FluxGuidance, SDXLEmptyLatentSizePicker+, SetUnionControlNetType, AIO_Preprocessor, SaveImage, ImageScale, ACN_AdvancedControlNetApplySingle_v2, LayerColor: AutoAdjustV2, VAEDecode, VAELoader, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, ModelSamplingFlux, FluxGuidance, SDXLEmptyLatentSizePicker+, SetUnionControlNetType, AIO_Preprocessor, PreviewImage, ImageScale, LayerColor: AutoAdjustV2, ACN_AdvancedControlNetApplySingle_v2, CLIPTextEncode, CLIPTextEncode, SetUnionControlNetType, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, PreviewImage, SaveImage, PreviewImage, PreviewImage, SaveImage, PreviewImage, DualCLIPLoader, UNETLoader, LoadImage, ControlNetLoader, LoadImage, DualCLIPLoader, UNETLoader, VAELoader, ControlNetLoader, LoadImage, DualCLIPLoader, UNETLoader, VAELoader, ControlNetLoader, LoadImage, LoadImage, DualCLIPLoader, VAELoader, ControlNetLoader, DualCLIPLoader, UNETLoader, VAELoader, ControlNetLoader, UNETLoader]
patterns: []
missing: [LayerColor: AutoAdjustV2, LayerColor: AutoAdjustV2, LayerColor: AutoAdjustV2, LayerColor: AutoAdjustV2, LayerColor: AutoAdjustV2, SDXLEmptyLatentSizePicker+, SDXLEmptyLatentSizePicker+, SDXLEmptyLatentSizePicker+, SDXLEmptyLatentSizePicker+, SDXLEmptyLatentSizePicker+]
parameters: {"batch_size": 0, "controlnet_strength": 0.9, "height": 1, "width": "1024x1024 (1.0)"}
discoveries: [次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux CN Union Pro 2.0通用基础生成_1924342356764446722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux CN Union Pro 2.0通用基础生成_1924342356764446722.json`

## 结构

**节点**（110 个）：
- `BasicGuider`
- `SDXLEmptyLatentSizePicker+`
- `ImageScale`
- `FluxGuidance`
- `RandomNoise`
- `KSamplerSelect`
- `SamplerCustomAdvanced`
- `ModelSamplingFlux`
- `AIO_Preprocessor`
- `BasicScheduler`
- `SaveImage`
- `VAEDecode`
- `LayerColor: AutoAdjustV2`
- `CLIPTextEncode`
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
- `SaveImage`
- `ImageScale`
- `CLIPTextEncode`
- `ACN_AdvancedControlNetApplySingle_v2`
- `LayerColor: AutoAdjustV2`
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
- `ACN_AdvancedControlNetApplySingle_v2`
- `LayerColor: AutoAdjustV2`
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
- `SaveImage`
- `ImageScale`
- `ACN_AdvancedControlNetApplySingle_v2`
- `LayerColor: AutoAdjustV2`
- `VAEDecode`
- `VAELoader`
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
- `PreviewImage`
- `ImageScale`
- `LayerColor: AutoAdjustV2`
- `ACN_AdvancedControlNetApplySingle_v2`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `SetUnionControlNetType`
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `DualCLIPLoader`
- `UNETLoader`
- `LoadImage`
- `ControlNetLoader`
- `LoadImage`
- `DualCLIPLoader`
- `UNETLoader`
- `VAELoader`
- `ControlNetLoader`
- `LoadImage`
- `DualCLIPLoader`
- `UNETLoader`
- `VAELoader`
- `ControlNetLoader`
- `LoadImage`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `DualCLIPLoader`
- `UNETLoader`
- `VAELoader`
- `ControlNetLoader`
- `UNETLoader`

## 关键参数

- `batch_size` = `0`
- `controlnet_strength` = `0.9`
- `height` = `1`
- `width` = `1024x1024 (1.0)`

## 知识

覆盖率 **86%**（95/110）

**有卡**：`BasicGuider`、`SDXLEmptyLatentSizePicker+`、`ImageScale`、`FluxGuidance`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ModelSamplingFlux`、`AIO_Preprocessor`、`BasicScheduler`、`SaveImage`、`VAEDecode`、`LayerColor: AutoAdjustV2`、`CLIPTextEncode`、`SetUnionControlNetType`、`ACN_AdvancedControlNetApplySingle_v2`、`VAELoader`、`PreviewImage`、`DualCLIPLoader`、`UNETLoader`、`LoadImage`、`ControlNetLoader`

**缺卡**（10）：`LayerColor: AutoAdjustV2`、`LayerColor: AutoAdjustV2`、`LayerColor: AutoAdjustV2`、`LayerColor: AutoAdjustV2`、`LayerColor: AutoAdjustV2`、`SDXLEmptyLatentSizePicker+`、`SDXLEmptyLatentSizePicker+`、`SDXLEmptyLatentSizePicker+`、`SDXLEmptyLatentSizePicker+`、`SDXLEmptyLatentSizePicker+`

## 学习发现

- 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: AutoAdjustV2` 知识库中没有该节点类型的任何知识
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
