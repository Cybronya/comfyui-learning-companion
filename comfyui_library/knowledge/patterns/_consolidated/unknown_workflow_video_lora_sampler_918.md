---
name: unknown_workflow_video_lora_sampler_918
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.933
common_nodes: [Audio Duration (mtb), AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/子易奇谭V1.0_1955552816828858370.json, 视频生成/图生视频/子易奇谭V1.0仅首帧_1951123683320471554.json, 视频生成/图生视频/百变唱跳星-首尾帧+对口型【翻唱版】+动作迁移_1949260320406216705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_918

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/子易奇谭V1.0_1955552816828858370.json、视频生成/图生视频/子易奇谭V1.0仅首帧_1951123683320471554.json、视频生成/图生视频/百变唱跳星-首尾帧+对口型【翻唱版】+动作迁移_1949260320406216705.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `Int`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
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

**可变部分**（部分 workflow 才有）：
- `FaceRestoreCFWithModel` —— 2/3 个有
- `FaceRestoreModelLoader` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ReActorFaceSwap` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `AudioCombine` —— 1/3 个有
- `MimicMotionGetPoses` —— 1/3 个有
- `SeedVCRun` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
