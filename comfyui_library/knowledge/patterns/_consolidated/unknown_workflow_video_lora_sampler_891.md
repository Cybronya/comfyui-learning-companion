---
name: unknown_workflow_video_lora_sampler_891
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.597
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Ceil, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, SetNode, SimpleMath+, SimpleMathInt+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VantageWanBlockSwap, WanAnimateToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy int, easy lengthAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2029880214125289473.json, 视频生成/图生视频/2029920731403915266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_891

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2029880214125289473.json、视频生成/图生视频/2029920731403915266.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Ceil`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `SimpleMathInt+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VantageWanBlockSwap`
- `WanAnimateToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy lengthAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
