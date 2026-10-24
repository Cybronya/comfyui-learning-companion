---
name: unknown_workflow_video_lora_sampler_738
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.438
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, Qwen3_VQA, SetNode, ShowText|pysssss, SomethingToString, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa+SVI2+Pro For循环长视频_2029945689748283393.json, 视频生成/图生视频/Dasiwa+SVI2+Pro长视频（自动提示词）_2029614979116175361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_738

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Dasiwa+SVI2+Pro For循环长视频_2029945689748283393.json、视频生成/图生视频/Dasiwa+SVI2+Pro长视频（自动提示词）_2029614979116175361.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
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
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `ConvertAny2String` —— 1/2 个有
- `Evaluate Integers` —— 1/2 个有
- `GODMT_SplitString` —— 1/2 个有
- `Int` —— 1/2 个有
- `Split String` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy indexAnything` —— 1/2 个有
- `easy string` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
