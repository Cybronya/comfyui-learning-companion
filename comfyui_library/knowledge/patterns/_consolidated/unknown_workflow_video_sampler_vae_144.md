---
name: unknown_workflow_video_sampler_vae_144
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.72925
common_nodes: [EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, Int, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MimicMotionGetPoses, SetNode, TextInput_, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, WanVideoVRAMManagement, easy batchAnything]
problems: []
missing: []
members: [平台全量/VACE14B+step1X自定义视频风格转绘_1923380770398720001.json, 平台全量/【首尾帧+动作迁移】换装变身动效_1976828890830323714.json, 平台全量/换装变身动效+++动作迁移｜FusionX+首尾帧生成视频_1976105825771106306.json, 视频生成/图生视频/换装变身动效 + 动作迁移｜FusionX 首尾帧生成视频_1936038942514794498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_144

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/VACE14B+step1X自定义视频风格转绘_1923380770398720001.json、平台全量/【首尾帧+动作迁移】换装变身动效_1976828890830323714.json、平台全量/换装变身动效+++动作迁移｜FusionX+首尾帧生成视频_1976105825771106306.json、视频生成/图生视频/换装变身动效 + 动作迁移｜FusionX 首尾帧生成视频_1936038942514794498.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MimicMotionGetPoses`
- `SetNode`
- `TextInput_`
- `VHS_LoadVideo`
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
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`
- `easy batchAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `GetImagesFromBatchIndexed` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImageBlur` —— 1/4 个有
- `Int Input [Dream]` —— 1/4 个有
- `InversionDemoLazyIndexSwitch` —— 1/4 个有
- `PixelPerfectResolution` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RunningHub_Step1XEdit` —— 1/4 个有
- `VHS_BatchManager` —— 1/4 个有
- `VHS_GetImageCount` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
