---
name: unknown_workflow_video_lora_sampler_390
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8535
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, PathchSageAttentionKJ, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/InfiniteTalk数字人官方版_2019292524422107137.json, 视频生成/图生视频/infinitalk无限时长数字人_2075127473318227970.json, 视频生成/图生视频/新InfiniteTalk-Comfyui官方魔改多图无限长视频数字人_2021783792129675265.json, 视频生成/图生视频/目前最强InfiniteTalk 官版自循环版  林耀2.6_2019714364567199745.json, 视频生成/图生视频/长视频画音同步InfiniteTalk-数字人官版自循环版（高质量）_2019764021985021953.json, 视频生成/文生视频/数字人对口型官版自循环版+3分钟高速平衡优化_2054151517233532929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_390

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/InfiniteTalk数字人官方版_2019292524422107137.json、视频生成/图生视频/infinitalk无限时长数字人_2075127473318227970.json、视频生成/图生视频/新InfiniteTalk-Comfyui官方魔改多图无限长视频数字人_2021783792129675265.json、视频生成/图生视频/目前最强InfiniteTalk 官版自循环版  林耀2.6_2019714364567199745.json、视频生成/图生视频/长视频画音同步InfiniteTalk-数字人官版自循环版（高质量）_2019764021985021953.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `PathchSageAttentionKJ`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 5/6 个有
- `ImageFromBatch` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `PreviewAudio` —— 5/6 个有
- `easy forLoopEnd` —— 5/6 个有
- `easy forLoopStart` —— 5/6 个有
- `AudioInfo` —— 4/6 个有
- `AudioTrim` —— 4/6 个有
- `Evaluate Integers` —— 4/6 个有
- `easy mathInt` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `Fast Bypasser (rgthree)` —— 3/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/6 个有
- `AudioCrop` —— 1/6 个有
- `AudioCropProcessUTK` —— 1/6 个有
- `Float` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `JWFloat` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PurgeVRAM_UTK` —— 1/6 个有
- `SimpleCalculatorKJ` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 4 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 4，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
