---
name: unknown_workflow_video_lora_sampler_276
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.873375
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1956951152292192258.json, 视频生成/图生视频/1955673336359653378.json, 视频生成/图生视频/1956191796604882946.json, 视频生成/图生视频/2005304023580372993.json, 视频生成/图生视频/2005293429506670594.json, 视频生成/图生视频/1959331317118873601.json, 视频生成/文生视频/1959187908609650689.json, 视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_276

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1956951152292192258.json、视频生成/图生视频/1955673336359653378.json、视频生成/图生视频/1956191796604882946.json、视频生成/图生视频/2005304023580372993.json、视频生成/图生视频/2005293429506670594.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ApplyFaceProcessor` —— 7/8 个有
- `FaceProcessorLoader` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `WanVideoSetLoRAs` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 5/8 个有
- `CreateCFGScheduleFloatList` —— 3/8 个有
- `GetImageSizeAndCount` —— 3/8 个有
- `INTConstant` —— 3/8 个有
- `Primitive integer [Crystools]` —— 3/8 个有
- `DrawMaskOnImage` —— 1/8 个有
- `FaceOnlyModeSwitch` —— 1/8 个有
- `GetImageSize+` —— 1/8 个有
- `ImagePadKJ` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `InvertMask` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `RMBG` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VideoInputPreprocessor` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
