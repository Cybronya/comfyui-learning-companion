---
name: unknown_workflow_video_lora_sampler_367
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8385
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan22_standin_optimized_workflow_2005304023580372993.json, 视频生成/图生视频/wan22_standin_testing_wip_kj_2005293429506670594.json, 视频生成/图生视频/wanvideo_Stand-In_人脸一致性_1959331317118873601.json, 视频生成/图生视频/wanvideo_Stand-In角色一致性工作流_1956293638198362114.json, 视频生成/图生视频/角色一致性图生视频_1973164651716415490.json, 视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_367

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/wan22_standin_optimized_workflow_2005304023580372993.json、视频生成/图生视频/wan22_standin_testing_wip_kj_2005293429506670594.json、视频生成/图生视频/wanvideo_Stand-In_人脸一致性_1959331317118873601.json、视频生成/图生视频/wanvideo_Stand-In角色一致性工作流_1956293638198362114.json、视频生成/图生视频/角色一致性图生视频_1973164651716415490.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ApplyFaceProcessor` —— 5/6 个有
- `FaceProcessorLoader` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `CreateCFGScheduleFloatList` —— 3/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `WanVideoSetLoRAs` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `Label (rgthree)` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `DrawMaskOnImage` —— 1/6 个有
- `FaceOnlyModeSwitch` —— 1/6 个有
- `GetImageSize+` —— 1/6 个有
- `ImagePadKJ` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `VideoInputPreprocessor` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
