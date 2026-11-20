---
name: unknown_workflow_video_sampler_vae_106
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.657
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE14B open Pose 人物迁移_1923563550629875714.json, 视频生成/图生视频/VACE14B-视频多方位扩展编辑_1922732185021812737.json, 视频生成/图生视频/VACE14B-首尾帧视频生成_1922723230275223554.json, 视频生成/图生视频/VACE视频编辑（图片参考视频一致性跳舞视频转绘）工作流_1922996913308954625.json, 视频生成/图生视频/【闪电极速】Wan2.1 WanVACE动作迁移视频动画生成_1924743024252022785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_106

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/VACE14B open Pose 人物迁移_1923563550629875714.json、视频生成/图生视频/VACE14B-视频多方位扩展编辑_1922732185021812737.json、视频生成/图生视频/VACE14B-首尾帧视频生成_1922723230275223554.json、视频生成/图生视频/VACE视频编辑（图片参考视频一致性跳舞视频转绘）工作流_1922996913308954625.json、视频生成/图生视频/【闪电极速】Wan2.1 WanVACE动作迁移视频动画生成_1924743024252022785.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `ImagePadKJ` —— 4/5 个有
- `ImageResizeKJ` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `GetImageRangeFromBatch` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `Primitive integer [Crystools]` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `DepthAnything_V2` —— 2/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/5 个有
- `MimicMotionGetPoses` —— 2/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/5 个有
- `WanVideoVRAMManagement` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
