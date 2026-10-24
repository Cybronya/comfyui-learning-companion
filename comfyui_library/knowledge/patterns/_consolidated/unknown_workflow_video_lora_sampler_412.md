---
name: unknown_workflow_video_lora_sampler_412
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9482
common_nodes: [AudioSeparation, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE&InfiniteTalk-首尾帧+对口型_1958191030833201153.json, 视频生成/图生视频/VACE&MultiTalk-首尾帧+对口型_1942474167965126658.json, 视频生成/图生视频/子易奇谭V1.0_1955552816828858370.json, 视频生成/图生视频/子易奇谭V1.0仅首帧_1951123683320471554.json, 视频生成/图生视频/百变唱跳星-首尾帧+对口型【翻唱版】+动作迁移_1949260320406216705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_412

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/VACE&InfiniteTalk-首尾帧+对口型_1958191030833201153.json、视频生成/图生视频/VACE&MultiTalk-首尾帧+对口型_1942474167965126658.json、视频生成/图生视频/子易奇谭V1.0_1955552816828858370.json、视频生成/图生视频/子易奇谭V1.0仅首帧_1951123683320471554.json、视频生成/图生视频/百变唱跳星-首尾帧+对口型【翻唱版】+动作迁移_1949260320406216705.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Audio Duration (mtb)` —— 3/5 个有
- `AudioCrop` —— 2/5 个有
- `FaceRestoreCFWithModel` —— 2/5 个有
- `FaceRestoreModelLoader` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `ReActorFaceSwap` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `StringToInt` —— 2/5 个有
- `AudioCombine` —— 1/5 个有
- `MimicMotionGetPoses` —— 1/5 个有
- `SeedVCRun` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
