---
name: unknown_workflow_video_lora_sampler_826
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.751
common_nodes: [ADE_AnimateDiffSamplingSettings, ADE_ApplyAnimateDiffModelSimple, ADE_LoadAnimateDiffModel, ADE_StandardStaticContextOptions, ADE_UseEvolvedSampling, CLIPSetLastLayer, CM_FloatToInt, CM_IntToFloat, CheckpointLoaderSimpleWithNoiseSelect, ControlNextDiffusersScheduler, DownloadAndLoadMimicMotionModel, GetImageSizeAndCount, GetNode, ImageScale, ImageSharpen, KSamplerPipe //Inspire, LoadImage, LoraLoaderModelOnly, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, RIFE VFI, ReActorFaceSwap, SetNode, ToBasicPipe, VAEDecode, VAEEncode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, smZ CLIPTextEncode]
problems: []
missing: []
members: [平台全量/照片跳舞 _ 视频生视频  lora控制+换脸_1884609806248955906.json, 视频生成/图生视频/一键美女视频跳舞机V8带人脸替换_1894249128619323393.json, 视频生成/图生视频/超清模特_跳舞工作流。1k画质。_1905666716616019969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_826

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/照片跳舞 _ 视频生视频  lora控制+换脸_1884609806248955906.json、视频生成/图生视频/一键美女视频跳舞机V8带人脸替换_1894249128619323393.json、视频生成/图生视频/超清模特_跳舞工作流。1k画质。_1905666716616019969.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `ADE_AnimateDiffSamplingSettings`
- `ADE_ApplyAnimateDiffModelSimple`
- `ADE_LoadAnimateDiffModel`
- `ADE_StandardStaticContextOptions`
- `ADE_UseEvolvedSampling`
- `CLIPSetLastLayer`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CheckpointLoaderSimpleWithNoiseSelect`
- `ControlNextDiffusersScheduler`
- `DownloadAndLoadMimicMotionModel`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageScale`
- `ImageSharpen`
- `KSamplerPipe //Inspire`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MimicMotionDecode`
- `MimicMotionGetPoses`
- `MimicMotionSampler`
- `RIFE VFI`
- `ReActorFaceSwap`
- `SetNode`
- `ToBasicPipe`
- `VAEDecode`
- `VAEEncode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `smZ CLIPTextEncode`

**可变部分**（部分 workflow 才有）：
- `DiffusersScheduler` —— 2/3 个有
- `ReActorLoadFaceModel` —— 2/3 个有
- `Any To String (mtb)` —— 1/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `FaceAnalysisModels` —— 1/3 个有
- `FaceSegmentation` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageCrop+` —— 1/3 个有
- `Int` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ReActorBuildFaceModel` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | ddim | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.26 | 0.2 - 0.26 | 3 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 ddim，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.26，观测区间 0.2 - 0.26，3 个样本，取值集中（一致性 88%）
