---
name: unknown_workflow_video_lora_sampler_818
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.547667
common_nodes: [DownloadAndLoadSAM2Model, GetImageRangeFromBatch, GetNode, GrowMaskWithBlur, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PointsEditor, PreviewImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/mocha点编辑器_1991061000164188162.json, 平台全量/人物替换mocha 语义识别 工作流_1988085878033682433.json, 数字人/数字人/AI换人术再升级！MoCha模型一键替换视频主角，ComfyUI详细教程来啦！_1981244039615905794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_818

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/mocha点编辑器_1991061000164188162.json、平台全量/人物替换mocha 语义识别 工作流_1988085878033682433.json、数字人/数字人/AI换人术再升级！MoCha模型一键替换视频主角，ComfyUI详细教程来啦！_1981244039615905794.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadSAM2Model`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PointsEditor`
- `PreviewImage`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BBoxesToSAM2` —— 2/3 个有
- `BlockifyMask` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `DownloadAndLoadQwenModel` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `ImageBatchGet` —— 2/3 个有
- `Int` —— 2/3 个有
- `LayerMask: SAM2VideoUltra` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `QwenVLDetection` —— 2/3 个有
- `RMBG` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
