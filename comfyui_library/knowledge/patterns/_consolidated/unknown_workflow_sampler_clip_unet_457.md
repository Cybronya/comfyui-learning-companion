---
name: unknown_workflow_sampler_clip_unet_457
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9545
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ernic-image+Z-image双采样文生图_2045479604814618626.json, 图片生成/文生图/人像写真(文生图)- Beyond Reality Z-image_2003840206602182657.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_457

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Ernic-image+Z-image双采样文生图_2045479604814618626.json、图片生成/文生图/人像写真(文生图)- Beyond Reality Z-image_2003840206602182657.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 900 | - | 2 | 80% |
| 高度 | 1420 | - | 2 | 90% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 12.5 | - | 2 | 80% |
| 采样算法 | 1.5 | - | 2 | 67% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 900，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 1420，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1.5，样本不足，未给区间，2 个样本
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
