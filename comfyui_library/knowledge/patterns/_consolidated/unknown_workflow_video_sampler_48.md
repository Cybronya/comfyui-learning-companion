---
name: unknown_workflow_video_sampler_48
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.578
common_nodes: [CR Set Value On Boolean, Display Any (rgthree), EmptyImage, Evaluate Integers, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageSizeAndCount, GetNode, ImageBatch, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, ImpactSwitch, Int, Manual XY Entry Info, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy compare, easy forLoopEnd, easy forLoopStart, easy mathInt]
problems: []
missing: []
members: [平台全量/FlashVSR长视频分段放大(SM版本)_1982346588683149313.json, 平台全量/FlashVSR长视频循环放大(SM版本)_1991794768929976322.json, 平台全量/Flash循环放大_1989297153782804482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_48

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/FlashVSR长视频分段放大(SM版本)_1982346588683149313.json、平台全量/FlashVSR长视频循环放大(SM版本)_1991794768929976322.json、平台全量/Flash循环放大_1989297153782804482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Set Value On Boolean`
- `Display Any (rgthree)`
- `EmptyImage`
- `Evaluate Integers`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatch`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `Manual XY Entry Info`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `LoadWanVideoT5TextEncoder` —— 2/3 个有
- `VHS_VideoInfoLoaded` —— 2/3 个有
- `WanVideoExtraModelSelect` —— 2/3 个有
- `WanVideoFlashVSRDecoderLoader` —— 2/3 个有
- `WanVideoModelLoader` —— 2/3 个有
- `WanVideoTextEncode` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.02839e+09 | 1.99564e+08 - 2.14159e+09 | 3 | 39% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 2.02839e+09，观测区间 1.99564e+08 - 2.14159e+09，3 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.14159e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
