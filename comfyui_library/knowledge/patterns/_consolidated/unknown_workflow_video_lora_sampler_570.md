---
name: unknown_workflow_video_lora_sampler_570
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7362
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/AI换脸工作流_2078669426429349890.json, 平台全量/GOZAO-角色替换-优化版_2078062526830567425.json, 平台全量/SAM3角色替换-优化版_2091524476671447042.json, 平台全量/Wan2_2_Animate_长视频单人姿态迁移工作流_1980840780245942274.json, 平台全量/Wan2_2_Animate_长视频替换人物工作流V3_1976312587359002625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_570

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/AI换脸工作流_2078669426429349890.json、平台全量/GOZAO-角色替换-优化版_2078062526830567425.json、平台全量/SAM3角色替换-优化版_2091524476671447042.json、平台全量/Wan2_2_Animate_长视频单人姿态迁移工作流_1980840780245942274.json、平台全量/Wan2_2_Animate_长视频替换人物工作流V3_1976312587359002625.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `ImageFromBatch` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `easy sam3ModelLoader` —— 3/5 个有
- `easy sam3VideoSegmentation` —— 3/5 个有
- `CM_FloatToInt` —— 2/5 个有
- `DownloadAndLoadSAM2Model` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `GrowMask` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `Sam2Segmentation` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `easy float` —— 2/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `WanVideoImageResizeToClosest` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
