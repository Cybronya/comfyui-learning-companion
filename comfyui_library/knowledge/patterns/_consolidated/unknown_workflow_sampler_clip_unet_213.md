---
name: unknown_workflow_sampler_clip_unet_213
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.952333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyHunyuanLatentVideo, KSamplerAdvanced, MathExpression|pysssss, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1950032228946501633.json, 视频生成/文生视频/1949846570944651266.json, 视频生成/文生视频/1949986877459881985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_213

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1950032228946501633.json、视频生成/文生视频/1949846570944651266.json、视频生成/文生视频/1949986877459881985.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `DF_Integer` —— 1/3 个有
- `JjkText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 3 | 100% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
