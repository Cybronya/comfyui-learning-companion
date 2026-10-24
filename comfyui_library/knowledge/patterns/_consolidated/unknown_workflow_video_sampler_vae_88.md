---
name: unknown_workflow_video_sampler_vae_88
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.687
common_nodes: [EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE14B open Pose 人物迁移_1923563550629875714.json, 视频生成/图生视频/Vace首尾帧工作流修复版_1913425967614783490.json, 视频生成/图生视频/Wan VACE视频编辑参考双图出视频-KJ版_1908555077475573761.json, 视频生成/图生视频/Wan万相VACE首尾帧_1908722738436186113.json, 视频生成/图生视频/换装变身动效 + 动作迁移｜FusionX 首尾帧生成视频_1936038942514794498.json, 视频生成/图生视频/模特产品互动、多人合照、 产品结合、图片结合 WAN 2.1 VACE 14b_1926293882655457281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_88

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/VACE14B open Pose 人物迁移_1923563550629875714.json、视频生成/图生视频/Vace首尾帧工作流修复版_1913425967614783490.json、视频生成/图生视频/Wan VACE视频编辑参考双图出视频-KJ版_1908555077475573761.json、视频生成/图生视频/Wan万相VACE首尾帧_1908722738436186113.json、视频生成/图生视频/换装变身动效 + 动作迁移｜FusionX 首尾帧生成视频_1936038942514794498.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
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
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `WanVideoVACEModelSelect` —— 3/6 个有
- `WanVideoVACEStartToEndFrame` —— 3/6 个有
- `WanVideoVRAMManagement` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `MaskPreview+` —— 2/6 个有
- `MimicMotionGetPoses` —— 2/6 个有
- `TextInput_` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `easy imageScaleDownToSize` —— 2/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `ImagePadKJ` —— 1/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `Note _O` —— 1/6 个有
- `WanVideoLoraSelect` —— 1/6 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/6 个有
- `easy batchAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
