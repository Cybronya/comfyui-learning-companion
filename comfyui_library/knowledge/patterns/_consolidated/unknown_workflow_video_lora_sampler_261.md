---
name: unknown_workflow_video_lora_sampler_261
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.851875
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioInfo, AudioTrim, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Evaluate Integers, ImageBatch, ImageFromBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy int, easy mathInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2025770017006030849.json, 视频生成/图生视频/2019621453360013313.json, 视频生成/图生视频/2056921656811147266.json, 视频生成/图生视频/2024713111399309314.json, 视频生成/图生视频/2019616198597550082.json, 视频生成/图生视频/2019582542961188866.json, 视频生成/图生视频/2018961391968849921.json, 视频生成/图生视频/2019080494813552642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_261

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2025770017006030849.json、视频生成/图生视频/2019621453360013313.json、视频生成/图生视频/2056921656811147266.json、视频生成/图生视频/2024713111399309314.json、视频生成/图生视频/2019616198597550082.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioInfo`
- `AudioTrim`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Evaluate Integers`
- `ImageBatch`
- `ImageFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 6/8 个有
- `PreviewAudio` —— 6/8 个有
- `Text Multiline` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `Fast Bypasser (rgthree)` —— 4/8 个有
- `Mute / Bypass Repeater (rgthree)` —— 4/8 个有
- `RHHiddenNodes` —— 3/8 个有
- `BasicScheduler` —— 2/8 个有
- `CFGGuider` —— 2/8 个有
- `GetImageSize` —— 2/8 个有
- `ImageBatchMulti` —— 2/8 个有
- `JWFloat` —— 2/8 个有
- `KSamplerSelect` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `RandomNoise` —— 2/8 个有
- `SamplerCustomAdvanced` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `BatchCount+` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `Image Batch` —— 1/8 个有
- `ImpactStringSelector` —— 1/8 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `ProcessString` —— 1/8 个有
- `PurgeVRAM_UTK` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy convertAnything` —— 1/8 个有
- `easy ifElse` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 4 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 4，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足
