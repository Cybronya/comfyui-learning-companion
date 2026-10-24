---
name: unknown_workflow_video_lora_sampler_900
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.459
common_nodes: [Anything Everywhere3, AudioEncoderEncode, AudioEncoderLoader, AudioInfo, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, GetNode, ImageBatchOneOrMore, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, ModelSamplingSD3, PrimitiveInt, SetNode, SimpleMath+, ToInt, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/电商数字人 长视频双人图片对口型_2019939783627247617.json, 视频生成/图生视频/电商数字人图片对口型 单人长视频版_2019245927545966594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_900

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/电商数字人 长视频双人图片对口型_2019939783627247617.json、视频生成/图生视频/电商数字人图片对口型 单人长视频版_2019245927545966594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioInfo`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `GetNode`
- `ImageBatchOneOrMore`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `ToInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
