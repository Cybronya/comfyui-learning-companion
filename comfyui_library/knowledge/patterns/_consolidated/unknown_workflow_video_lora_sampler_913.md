---
name: unknown_workflow_video_lora_sampler_913
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.643
common_nodes: [GetImageRangeFromBatch, GetNode, GrowMask, ImageConcanate, ImageResizeKJv2, LoadImage, MaskPreview, MochaEmbeds, PointsEditor, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🦖Mocha角色替换_1980895212593659906.json, 视频生成/文生视频/MoCha_像viggle一样进行角色替换_1981408974144708609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_913

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🦖Mocha角色替换_1980895212593659906.json、视频生成/文生视频/MoCha_像viggle一样进行角色替换_1981408974144708609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMask`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LoadImage`
- `MaskPreview`
- `MochaEmbeds`
- `PointsEditor`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_ImageFaceCrop` —— 1/2 个有
- `DownloadAndLoadSAM2Model` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LynxInsightFaceCrop` —— 1/2 个有
- `Sam2Segmentation` —— 1/2 个有
- `SeCModelLoader` —— 1/2 个有
- `SeCVideoSegmentation` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
