---
name: unknown_workflow_video_lora_sampler_954
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7165
common_nodes: [ADE_AnimateDiffSamplingSettings, ADE_ApplyAnimateDiffModelSimple, ADE_LoadAnimateDiffModel, ADE_StandardStaticContextOptions, ADE_UseEvolvedSampling, CLIPSetLastLayer, CM_FloatToInt, CM_IntToFloat, CheckpointLoaderSimpleWithNoiseSelect, ControlNextDiffusersScheduler, DownloadAndLoadMimicMotionModel, GetImageSizeAndCount, GetNode, ImageScale, ImageSharpen, KSamplerPipe //Inspire, LoadImage, LoraLoaderModelOnly, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, RIFE VFI, ReActorFaceSwap, SetNode, ToBasicPipe, VAEDecode, VAEEncode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed, smZ CLIPTextEncode]
problems: []
missing: []
members: [视频生成/图生视频/一键美女视频跳舞机V8带人脸替换_1894249128619323393.json, 视频生成/图生视频/超清模特_跳舞工作流。1k画质。_1905666716616019969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_954

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/一键美女视频跳舞机V8带人脸替换_1894249128619323393.json、视频生成/图生视频/超清模特_跳舞工作流。1k画质。_1905666716616019969.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
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
- `Any To String (mtb)` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `DiffusersScheduler` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceSegmentation` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `Int` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ReActorBuildFaceModel` —— 1/2 个有
- `ReActorLoadFaceModel` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | ddim | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.23 | - | 2 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 ddim，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.23，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
