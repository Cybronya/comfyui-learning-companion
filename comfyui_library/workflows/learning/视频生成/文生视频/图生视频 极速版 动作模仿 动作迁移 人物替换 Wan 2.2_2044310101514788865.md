---
key: 视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json
name: 图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json
hash: 978da5704f4c5c11
coverage: 0.527778
learned_at: 2026-10-11 19:49:48
nodes: [GetNode, GetNode, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, GIMMVFI_interpolate, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, SetNode, ImageConcatMulti, GetNode, WanVideoClipVisionEncode, BlockifyMask, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoDecode, GetNode, GetNode, GetNode, GrowMask, GetNode, DrawMaskOnImage, DownloadAndLoadSAM2Model, DrawViTPose, SetNode, GetNode, WanVideoVAELoader, WanVideoAnimateEmbeds, WanVideoSampler, GetNode, DownloadAndLoadGIMMVFIModel, SetNode, SetNode, SetNode, SetNode, SetNode, WanVideoTextEncodeCached, LayerUtility: PurgeVRAM V2, Int, PreviewImage, SetNode, SetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, GetImageSizeAndCount, VHS_VideoCombine, MathExpression|pysssss, INTConstant, INTConstant, Int, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, INTConstant, SetNode, VHS_LoadVideo, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, ImageBlend, GetNode, LoadImage, ImageResizeKJv2, CR Text]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoClipVisionEncode`
- `BlockifyMask`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMask`
- `GetNode`
- `DrawMaskOnImage`
- `DownloadAndLoadSAM2Model`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `INTConstant`
- `INTConstant`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `ImageBlend`
- `GetNode`
- `LoadImage`
- `ImageResizeKJv2`
- `CR Text`

## 知识

覆盖率 **53%**（38/72）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`BlockifyMask`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoDecode`、`GrowMask`、`DrawMaskOnImage`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTextEncodeCached`、`Int`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`Sam2Segmentation`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`INTConstant`、`VHS_LoadVideo`、`ImageBlend`、`LoadImage`、`ImageResizeKJv2`

**缺卡**（5）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
