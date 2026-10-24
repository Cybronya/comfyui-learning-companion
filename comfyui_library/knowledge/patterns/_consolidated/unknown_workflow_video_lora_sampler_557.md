---
name: unknown_workflow_video_lora_sampler_557
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.787
common_nodes: [CLIPLoader, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PainterPrompt, PainterSequentialF2V, PathchSageAttentionKJ, PrimitiveInt, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy promptList]
problems: []
missing: []
members: [图片生成/图生图/26.2.14绘画小子节点-首尾帧FOR循环长视频生成_2022611248910700545.json, 视频生成/图生视频/首尾帧for循环长视频生成-附视频分段提示词_2022953132912807937.json, 视频生成/图生视频/🐳首尾帧FOR循环长视频生成🐳_2022491815936532481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_557

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/26.2.14绘画小子节点-首尾帧FOR循环长视频生成_2022611248910700545.json、视频生成/图生视频/首尾帧for循环长视频生成-附视频分段提示词_2022953132912807937.json、视频生成/图生视频/🐳首尾帧FOR循环长视频生成🐳_2022491815936532481.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PainterPrompt`
- `PainterSequentialF2V`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
