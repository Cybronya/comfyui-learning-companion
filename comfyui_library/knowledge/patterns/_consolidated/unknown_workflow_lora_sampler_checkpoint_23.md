---
name: unknown_workflow_lora_sampler_checkpoint_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [CheckpointLoaderSimple, DuckHideNode, GetImageSizeAndCount, LoadImage, LoraLoaderModelOnly, QwenImageIntegratedKSampler, SaveImage, Text]
problems: []
missing: []
members: [图片生成/文生图/本子上色_2036085822201536514.json, 图片生成/文生图/本子上色_2038220913065336833.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/本子上色_2036085822201536514.json、图片生成/文生图/本子上色_2038220913065336833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `DuckHideNode`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `Text`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 29% |
| 采样算法 | 1472 | - | 2 | 100% |
| 调度器 | 1104 | - | 2 | 100% |
| 重绘幅度 | 3.49409e+14 | - | 2 | 39% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 29%
- 采样算法 中位数 1472，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1104，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 3.49409e+14，样本不足，未给区间，2 个样本，取值分散，一致性仅 39%
- 风险：重绘幅度 观测到 5.64061e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
