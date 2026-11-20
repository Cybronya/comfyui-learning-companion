---
name: unknown_workflow_video_lora_sampler_663
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.695
common_nodes: [GetImageRangeFromBatch, GetNode, INTConstant, ImageAndMaskPreview, ImageConcatMulti, ImagePadForOutpaint, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, RH_Captioner, SetNode, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786.json, 平台全量/wan2.2 Fun VACE 视频尺寸扩充 KJ_1967848728017121282.json, 平台全量/wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810.json, 视频生成/图生视频/wan2.2-Fun-VACE视频扩展-KJ_1967240843000209410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_663

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/KJ版-wan2.2-Fun-VACE视频生视频 视频扩展 效果很棒_1968470687239286786.json、平台全量/wan2.2 Fun VACE 视频尺寸扩充 KJ_1967848728017121282.json、平台全量/wan2.2-Fun-VACE视频扩展-KJ_1967917175858167810.json、视频生成/图生视频/wan2.2-Fun-VACE视频扩展-KJ_1967240843000209410.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageAndMaskPreview`
- `ImageConcatMulti`
- `ImagePadForOutpaint`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `RH_Captioner`
- `SetNode`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveFloat` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `WanVideoScheduler` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
