---
name: unknown_workflow_video_lora_sampler_469
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8874
common_nodes: [Audio Duration (mtb), AudioConcat, AudioCrop, AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageFromBatch, Int, KSamplerAdvanced, LatentComposite, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, PreviewAudio, PrimitiveInt, Seed Generator, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/商用级 数字人 完全体 infinitetalk_2042956099917193218.json, 数字人/数字人/商用级-完全体infinitetalk_2042050654834794498.json, 数字人/数字人/数字人音乐MV商用级-完全体infinitetalk(神棍大佬）_2042239902800154625.json, 数字人/数字人/魔改-官流infinitetalk-wan2.2_2018585403422416898.json, 视频生成/图生视频/完全体infinitetalk(转自神棍大佬）大幅度解决了循环和长视频的问题_2044311378168647682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_469

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/商用级 数字人 完全体 infinitetalk_2042956099917193218.json、数字人/数字人/商用级-完全体infinitetalk_2042050654834794498.json、数字人/数字人/数字人音乐MV商用级-完全体infinitetalk(神棍大佬）_2042239902800154625.json、数字人/数字人/魔改-官流infinitetalk-wan2.2_2018585403422416898.json、视频生成/图生视频/完全体infinitetalk(转自神棍大佬）大幅度解决了循环和长视频的问题_2044311378168647682.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioConcat`
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageFromBatch`
- `Int`
- `KSamplerAdvanced`
- `LatentComposite`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `PreviewAudio`
- `PrimitiveInt`
- `Seed Generator`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ImageBatchExtendWithOverlap` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `WanImageToVideoSVIPro` —— 4/5 个有
- `easy getNode` —— 4/5 个有
- `easy promptLine` —— 4/5 个有
- `easy setNode` —— 4/5 个有
- `CLIPVisionEncode` —— 1/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageBatch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 5 | 86% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，5 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
