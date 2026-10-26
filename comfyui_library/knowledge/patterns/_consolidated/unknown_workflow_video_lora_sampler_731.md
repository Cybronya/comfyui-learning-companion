---
name: unknown_workflow_video_lora_sampler_731
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.933333
common_nodes: [CLIPVisionLoader, FloatConstant, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PreviewAnimation, PreviewImage, RenderNLFPoses, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1-scail+FOR循环适合小显存配置_2050481432279175169.json, 视频生成/图生视频/▶SCAIL-动作迁移_2011070292294111234.json, 视频生成/图生视频/一键复刻美女小姐姐跳舞SCAILGGUF 低功耗方案动作迁移_2031330145717456898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_731

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.1-scail+FOR循环适合小显存配置_2050481432279175169.json、视频生成/图生视频/▶SCAIL-动作迁移_2011070292294111234.json、视频生成/图生视频/一键复刻美女小姐姐跳舞SCAILGGUF 低功耗方案动作迁移_2031330145717456898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `FloatConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PreviewAnimation`
- `PreviewImage`
- `RenderNLFPoses`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadNLFModel` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `Display Int (rgthree)` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageBatchExtendWithOverlap` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `ImpactCompare` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LoadNLFModel` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
