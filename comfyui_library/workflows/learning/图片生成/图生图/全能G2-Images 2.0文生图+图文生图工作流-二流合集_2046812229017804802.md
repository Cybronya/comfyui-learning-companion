---
key: 图片生成/图生图/全能G2-Images 2.0文生图+图文生图工作流-二流合集_2046812229017804802.json
name: 全能G2-Images 2.0文生图+图文生图工作流-二流合集_2046812229017804802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/全能G2-Images 2.0文生图+图文生图工作流-二流合集_2046812229017804802.json
hash: c3d0fa2e7f0bacd1
coverage: 0.619048
learned_at: 2026-10-09 22:36:20
nodes: [Fast Groups Bypasser (rgthree), RH_RhartImageG2OfficialImageToImage, SaveImage, Image Comparer (rgthree), RHHiddenNodes, SaveImage, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SeedVR2ExtraArgs, SeedVR2, ImageScaleToTotalPixels, Image Comparer (rgthree), SaveImage, SeedVR2BlockSwap, DF_Integer, PrimitiveNode, PrimitiveNode, RH_RhartImageG2TextToImage, SaveImage, CR Prompt Text]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/全能G2-Images 2.0文生图+图文生图工作流-二流合集_2046812229017804802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2046812229017804802.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（21 个）：
- `Fast Groups Bypasser (rgthree)`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RHHiddenNodes`
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2BlockSwap`
- `DF_Integer`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `CR Prompt Text`

## 知识

覆盖率 **62%**（13/21）

**有卡**：`RH_RhartImageG2OfficialImageToImage`、`SaveImage`、`RHHiddenNodes`、`LoadImage`、`SeedVR2ExtraArgs`、`SeedVR2`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`DF_Integer`、`RH_RhartImageG2TextToImage`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs、SaveImage、DF_Integer、ImageScaleToTotalPixels、RH_RhartImageG2OfficialImageToImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
