---
name: unknown_workflow_lora_sampler_clip_123
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7898
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CreateVideo, ImageBatch, ImageFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PrimitiveInt, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/InfiniteTalk_数字人_单人_多图_无限时长_2019505709020352513.json, 数字人/数字人/InfiniteTalk_数字人_单人_无限时长_2019517637587374082.json, 数字人/数字人/infinitetalk官方版单人for循环工作流 长视频不崩坏 自用保存_2026702408734220289.json, 数字人/数字人/infinitetalk官方版单人for循环工作流 长视频不崩坏_2020177369331404801.json, 视频生成/图生视频/infinitetalk官方版单人Loop循环流_2073310072448577538.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/InfiniteTalk_数字人_单人_多图_无限时长_2019505709020352513.json、数字人/数字人/InfiniteTalk_数字人_单人_无限时长_2019517637587374082.json、数字人/数字人/infinitetalk官方版单人for循环工作流 长视频不崩坏 自用保存_2026702408734220289.json、数字人/数字人/infinitetalk官方版单人for循环工作流 长视频不崩坏_2020177369331404801.json、视频生成/图生视频/infinitetalk官方版单人Loop循环流_2073310072448577538.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CreateVideo`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PrimitiveInt`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 4/5 个有
- `Audio Duration (mtb)` —— 3/5 个有
- `SimpleCalculatorKJ` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `AudioInfo` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `easy int` —— 2/5 个有
- `AudioCrop` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `Music_AudioTrimmer` —— 1/5 个有
- `VHS_LoadAudioUpload` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
