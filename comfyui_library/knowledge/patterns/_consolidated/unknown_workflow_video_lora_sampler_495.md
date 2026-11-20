---
name: unknown_workflow_video_lora_sampler_495
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5004
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, ComfyMathExpression, ConditioningZeroOut, DiffusionModelLoaderKJ, GetNode, ImageFromBatch, Int, KSamplerAdvanced, LatentCutToBatch, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RebatchImages, ResizeImageMaskNode, SetNode, SkipLayerGuidanceDiTSimple, String, StringConcatenate, TrimAudioDuration, VAEDecode, VAELoader, VHS_VideoCombine, WanDancerEncodeAudio, WanDancerPadKeyframesList, WanDancerVideo, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan-Dancer + Scail2 音乐生成舞蹈邪修版 v1.0 _ 超高质量、极致细节、_2080196477946785794.json, 视频生成/图生视频/Wan-Dancer + Scail2 音生舞工作流邪修版 v1.0 _ 高质量、高动态、人物稳定_2080198878946742274.json, 视频生成/图生视频/Wan-Dancer 工作流_2080118867824824321.json, 视频生成/图生视频/Wan-Dancer 音生舞工作流 v1.1 _ 舞蹈生动 _ 视频效果提升_2078942540585324546.json, 视频生成/图生视频/Wan-Dancer 音生舞蹈工作流_2080192846396739585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_495

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan-Dancer + Scail2 音乐生成舞蹈邪修版 v1.0 _ 超高质量、极致细节、_2080196477946785794.json、视频生成/图生视频/Wan-Dancer + Scail2 音生舞工作流邪修版 v1.0 _ 高质量、高动态、人物稳定_2080198878946742274.json、视频生成/图生视频/Wan-Dancer 工作流_2080118867824824321.json、视频生成/图生视频/Wan-Dancer 音生舞工作流 v1.1 _ 舞蹈生动 _ 视频效果提升_2078942540585324546.json、视频生成/图生视频/Wan-Dancer 音生舞蹈工作流_2080192846396739585.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageFromBatch`
- `Int`
- `KSamplerAdvanced`
- `LatentCutToBatch`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RebatchImages`
- `ResizeImageMaskNode`
- `SetNode`
- `SkipLayerGuidanceDiTSimple`
- `String`
- `StringConcatenate`
- `TrimAudioDuration`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanDancerEncodeAudio`
- `WanDancerPadKeyframesList`
- `WanDancerVideo`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `Label (rgthree)` —— 4/5 个有
- `FlashVSRNode` —— 3/5 个有
- `RTXVideoSuperResolution` —— 3/5 个有
- `SeedVR2LoadDiTModel` —— 3/5 个有
- `SeedVR2LoadVAEModel` —— 3/5 个有
- `SeedVR2VideoUpscaler` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SAM3_VideoTrack` —— 2/5 个有
- `SCAIL2ColoredMask` —— 2/5 个有
- `VAEDecodeTiled` —— 2/5 个有
- `WanContextWindowsManual` —— 2/5 个有
- `WanSCAILToVideo` —— 2/5 个有
- `easy imageRemBg` —— 2/5 个有
- `easy lengthAnything` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 5 | 39% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，5 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
