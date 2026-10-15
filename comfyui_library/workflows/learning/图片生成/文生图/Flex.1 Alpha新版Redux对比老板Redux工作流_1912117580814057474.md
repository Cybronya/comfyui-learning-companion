---
key: 图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json
name: Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json
hash: a7482cda87f661f3
coverage: 0.811321
learned_at: 2026-10-10 20:58:33
nodes: [PrimitiveNode, EmptySD3LatentImage, BasicGuider, CLIPTextEncode, PrimitiveNode, KSamplerSelect, BasicScheduler, LayerUtility: PurgeVRAM V2, StyleModelApply, PrimitiveNode, EmptySD3LatentImage, ModelSamplingFlux, FluxGuidance, CLIPVisionEncode, LayerUtility: PurgeVRAM V2, StyleModelLoader, CLIPTextEncode, KSamplerSelect, BasicScheduler, AdvancedVisionLoader, SamplerCustomAdvanced, PrimitiveNode, VAEDecode, AddLabel, AddLabel, ImageConcatMulti, JWImageResizeByLongerSide, RandomNoise, RandomNoise, PrimitiveNode, PrimitiveNode, AddLabel, SaveImage, VAEDecode, ApplyFBCacheOnModel, ApplyFBCacheOnModel, CheckpointLoaderSimple, PrimitiveNode, SamplerCustomAdvanced, ModelSamplingFlux, JWImageResizeByLongerSide, DF_Get_image_size, SaveImage, CheckpointLoaderSimple, AdvancedVisionLoader, CLIPVisionEncode, StyleModelLoader, FluxGuidance, StyleModelApply, BasicGuider, LoadImage, Note Plus (mtb), SaveImage]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Note Plus (mtb)]
parameters: {"checkpoint": "Flex.1-alpha.safetensors"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flex.1 Alpha新版Redux对比老板Redux工作流_1912117580814057474.json`

## 结构

**节点**（53 个）：
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `BasicGuider`
- `CLIPTextEncode`
- `PrimitiveNode`
- `KSamplerSelect`
- `BasicScheduler`
- `LayerUtility: PurgeVRAM V2`
- `StyleModelApply`
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `ModelSamplingFlux`
- `FluxGuidance`
- `CLIPVisionEncode`
- `LayerUtility: PurgeVRAM V2`
- `StyleModelLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `BasicScheduler`
- `AdvancedVisionLoader`
- `SamplerCustomAdvanced`
- `PrimitiveNode`
- `VAEDecode`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `JWImageResizeByLongerSide`
- `RandomNoise`
- `RandomNoise`
- `PrimitiveNode`
- `PrimitiveNode`
- `AddLabel`
- `SaveImage`
- `VAEDecode`
- `ApplyFBCacheOnModel`
- `ApplyFBCacheOnModel`
- `CheckpointLoaderSimple`
- `PrimitiveNode`
- `SamplerCustomAdvanced`
- `ModelSamplingFlux`
- `JWImageResizeByLongerSide`
- `DF_Get_image_size`
- `SaveImage`
- `CheckpointLoaderSimple`
- `AdvancedVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `FluxGuidance`
- `StyleModelApply`
- `BasicGuider`
- `LoadImage`
- `Note Plus (mtb)`
- `SaveImage`

## 关键参数

- `checkpoint` = `Flex.1-alpha.safetensors`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`PrimitiveNode`、`EmptySD3LatentImage`、`BasicGuider`、`CLIPTextEncode`、`KSamplerSelect`、`BasicScheduler`、`LayerUtility: PurgeVRAM V2`、`StyleModelApply`、`ModelSamplingFlux`、`FluxGuidance`、`CLIPVisionEncode`、`StyleModelLoader`、`AdvancedVisionLoader`、`SamplerCustomAdvanced`、`VAEDecode`、`AddLabel`、`ImageConcatMulti`、`JWImageResizeByLongerSide`、`RandomNoise`、`SaveImage`、`ApplyFBCacheOnModel`、`CheckpointLoaderSimple`、`DF_Get_image_size`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`Note Plus (mtb)`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
