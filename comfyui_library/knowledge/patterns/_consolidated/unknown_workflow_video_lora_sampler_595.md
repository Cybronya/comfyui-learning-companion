---
name: unknown_workflow_video_lora_sampler_595
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.448
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, Qwen3_VQA, SetNode, ShowText|pysssss, SomethingToString, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/2029945689748283393.json, 视频生成/图生视频/2029614979116175361.json, 视频生成/图生视频/2006611754909962242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_595

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2029945689748283393.json、视频生成/图生视频/2029614979116175361.json、视频生成/图生视频/2006611754909962242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `SetNode`
- `ShowText|pysssss`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `Split String` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Replace` —— 1/3 个有
- `ConvertAny2String` —— 1/3 个有
- `Evaluate Integers` —— 1/3 个有
- `GODMT_SplitString` —— 1/3 个有
- `Int` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy indexAnything` —— 1/3 个有
- `easy string` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 3 | 86% |
| 采样算法 | 1 | 1 - 2.5 | 3 | 53% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 2.5，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
