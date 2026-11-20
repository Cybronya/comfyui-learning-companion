---
name: unknown_workflow_video_sampler_vae_66
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.832875
common_nodes: [GetImageSizeAndCount, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1_VACE视频扩展_1993569189042601985.json, 平台全量/视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274.json, 平台全量/视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530.json, 视频生成/图生视频/VACE 14B视频扩图稳定版V1_1922724321020579841.json, 视频生成/图生视频/VACE-视频扩图工作流_1923332542534250497.json, 视频生成/图生视频/VACE14B open Pose 人物迁移_1923563550629875714.json, 视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json, 视频生成/图生视频/通义万相最新VACE超级无限循环首尾帧图生视频_1908024871404904449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_66

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Wan2.1_VACE视频扩展_1993569189042601985.json、平台全量/视频扩图 _ Wan2.2 低噪版本+vace +高清放大_2008800813161910274.json、平台全量/视频扩图 _ Wan2.2 低噪版本+vace_1958391467368726530.json、视频生成/图生视频/VACE 14B视频扩图稳定版V1_1922724321020579841.json、视频生成/图生视频/VACE-视频扩图工作流_1923332542534250497.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 7/8 个有
- `EmptyImage` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `ImagePadKJ` —— 7/8 个有
- `VHS_LoadVideo` —— 7/8 个有
- `WanVideoVACEModelSelect` —— 7/8 个有
- `GetImageRangeFromBatch` —— 6/8 个有
- `ImageResizeKJ` —— 5/8 个有
- `MaskPreview+` —— 5/8 个有
- `WanVideoExperimentalArgs` —— 5/8 个有
- `WanVideoSLG` —— 5/8 个有
- `WanVideoTeaCache` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `INTConstant` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `WanVideoLoraSelect` —— 2/8 个有
- `WanVideoVRAMManagement` —— 2/8 个有
- `FlashVSRNode` —— 1/8 个有
- `ImageBatch` —— 1/8 个有
- `MimicMotionGetPoses` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `WanVideoLoraSelectMulti` —— 1/8 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/8 个有
- `WanVideoVACEStartToEndFrame` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
