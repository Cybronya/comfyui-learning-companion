---
key: 图片生成/文生图/工作流系列6-生成多视频封面-基于image2.0_2048257002421358594.json
name: 工作流系列6-生成多视频封面-基于image2.0_2048257002421358594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/工作流系列6-生成多视频封面-基于image2.0_2048257002421358594.json
hash: ca83885e900a1337
coverage: 0.666667
learned_at: 2026-10-21 02:59:57
nodes: [GetNode, GetNode, GetNode, SaveImage, SeedVR2LoadDiTModel, SetNode, SetNode, SetNode, GetImageSize+, MinNode, LayerUtility: NumberCalculator, LayerUtility: Integer, PreviewImage, PreviewImage, PreviewImage, SaveImage, SaveImage, LayerUtility: TextBox, RH_RhartImageG2ImageToImage, RH_RhartImageG2ImageToImage, LayerUtility: TextBox, LoadImage, RH_RhartImageG2ImageToImage, LoadImage, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, LoadImage, PreviewImage, SaveImage, LayerUtility: TextBox]
patterns: []
missing: []
---

# 图片生成/文生图/工作流系列6-生成多视频封面-基于image2.0_2048257002421358594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/工作流系列6-生成多视频封面-基于image2.0_2048257002421358594.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（30 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize+`
- `MinNode`
- `LayerUtility: NumberCalculator`
- `LayerUtility: Integer`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: TextBox`
- `RH_RhartImageG2ImageToImage`
- `RH_RhartImageG2ImageToImage`
- `LayerUtility: TextBox`
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: TextBox`

## 知识

覆盖率 **67%**（20/30）

**有卡**：`SaveImage`、`SeedVR2LoadDiTModel`、`GetImageSize+`、`MinNode`、`LayerUtility: NumberCalculator`、`LayerUtility: Integer`、`LayerUtility: TextBox`、`RH_RhartImageG2ImageToImage`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、GetImageSize+、SaveImage、RH_RhartImageG2ImageToImage、MinNode
