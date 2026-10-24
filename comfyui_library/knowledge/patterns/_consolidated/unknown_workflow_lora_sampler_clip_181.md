---
name: unknown_workflow_lora_sampler_clip_181
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.377333
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CreateVideo, GetNode, ImageBatch, ImageFromBatch, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PrimitiveInt, SaveVideo, SetNode, UNETLoader, VAEDecode, VAELoader, WanInfiniteTalkToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/凤希AI单数字人无限时长对口型（默认80秒）_2021523374865915905.json, 视频生成/图生视频/InfiniteTalk_图生视频_双人对话-对口型_2019310713029791745.json, 视频生成/图生视频/InfiniteTalk_数字人（单人）_2019342958109134850.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/凤希AI单数字人无限时长对口型（默认80秒）_2021523374865915905.json、视频生成/图生视频/InfiniteTalk_图生视频_双人对话-对口型_2019310713029791745.json、视频生成/图生视频/InfiniteTalk_数字人（单人）_2019342958109134850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：38%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PrimitiveInt`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `AudioConcat` —— 1/3 个有
- `AudioSeparation` —— 1/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy imageScaleDown` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（29/3 个样本）：Steps较低可能导致细节不足
