---
name: unknown_workflow_video_lora_sampler_219
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.390889
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, GetNode, INTConstant, ImageBatch, ImageFromBatch, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingSD3, PreviewAudio, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2019318204899794946.json, 视频生成/图生视频/2018199752789204993.json, 视频生成/图生视频/2018680802581684225.json, 视频生成/图生视频/2018684694845460482.json, 视频生成/图生视频/2027300224661721090.json, 视频生成/图生视频/2025036533815844865.json, 视频生成/图生视频/2020782430164094977.json, 视频生成/图生视频/2018872300161998849.json, 视频生成/图生视频/2018523773288321026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_219

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2019318204899794946.json、视频生成/图生视频/2018199752789204993.json、视频生成/图生视频/2018680802581684225.json、视频生成/图生视频/2018684694845460482.json、视频生成/图生视频/2027300224661721090.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：39%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `GetNode`
- `INTConstant`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PreviewAudio`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `Compare` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Int` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `LongTextToList` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `VRGDG_AudioCropTime` —— 1/9 个有
- `easy forLoopEnd` —— 1/9 个有
- `easy forLoopStart` —— 1/9 个有
- `easy ifElse` —— 1/9 个有
- `easy indexAnything` —— 1/9 个有
- `ttN float` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 53/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（53/9 个样本）：Steps较低可能导致细节不足
