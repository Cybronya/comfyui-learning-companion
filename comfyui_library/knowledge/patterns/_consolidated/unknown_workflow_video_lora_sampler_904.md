---
name: unknown_workflow_video_lora_sampler_904
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.924
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, ImageConcatMulti, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan22_standin_optimized_workflow_2005304023580372993.json, 视频生成/图生视频/wan22_standin_testing_wip_kj_2005293429506670594.json, 视频生成/文生视频/Wan2.2-Stand-in人脸一致性保持_2004807715740413953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_904

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan22_standin_optimized_workflow_2005304023580372993.json、视频生成/图生视频/wan22_standin_testing_wip_kj_2005293429506670594.json、视频生成/文生视频/Wan2.2-Stand-in人脸一致性保持_2004807715740413953.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFaceProcessor` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `FaceProcessorLoader` —— 2/3 个有
- `ImagePadKJ` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `InvertMask` —— 2/3 个有
- `ImageRemoveBackground+` —— 1/3 个有
- `LoadLynxResampler` —— 1/3 个有
- `LynxEncodeFaceIP` —— 1/3 个有
- `LynxInsightFaceCrop` —— 1/3 个有
- `MinNode` —— 1/3 个有
- `OnnxDetectionModelLoader` —— 1/3 个有
- `PoseAndFaceDetection` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `TransparentBGSession+` —— 1/3 个有
- `WanVideoAddLynxEmbeds` —— 1/3 个有
- `WanVideoExtraModelSelect` —— 1/3 个有
- `WanVideoTextEncodeCached` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
