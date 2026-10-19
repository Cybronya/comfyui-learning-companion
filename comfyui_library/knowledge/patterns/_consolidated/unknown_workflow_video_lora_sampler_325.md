---
name: unknown_workflow_video_lora_sampler_325
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.863857
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageBatch, ImageFromBatch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2075127473318227970.json, 视频生成/图生视频/2021783792129675265.json, 视频生成/图生视频/2046426953556692994.json, 视频生成/图生视频/2046186407764434945.json, 视频生成/图生视频/2019714364567199745.json, 视频生成/图生视频/2019764021985021953.json, 视频生成/文生视频/数字人对口型官版自循环版+3分钟高速平衡优化_2054151517233532929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_325

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2075127473318227970.json、视频生成/图生视频/2021783792129675265.json、视频生成/图生视频/2046426953556692994.json、视频生成/图生视频/2046186407764434945.json、视频生成/图生视频/2019714364567199745.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AudioInfo` —— 6/7 个有
- `AudioTrim` —— 6/7 个有
- `Evaluate Integers` —— 6/7 个有
- `PreviewAudio` —— 6/7 个有
- `easy mathInt` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `JWFloat` —— 3/7 个有
- `PurgeVRAM_UTK` —— 3/7 个有
- `Apply Whisper` —— 2/7 个有
- `CR Text Replace` —— 2/7 个有
- `Fast Bypasser (rgthree)` —— 2/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/7 个有
- `Qwen3TTSModelLoader` —— 2/7 个有
- `Qwen3TTSVoiceClone` —— 2/7 个有
- `Qwen3_VQA` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `Text` —— 2/7 个有
- `TextConcatenate` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `AudioCropProcessUTK` —— 1/7 个有
- `Float` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SimpleCalculatorKJ` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 4 | 7 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 4，7 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
