---
name: unknown_workflow_lora_sampler_clip_92
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.947333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2073397315003572225.json, 视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json, 视频生成/文生视频/1949875835437236226.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2073397315003572225.json、视频生成/文生视频/wan2.2文生视频4steps加速官方版_2028309492064063490.json、视频生成/文生视频/1949875835437236226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `CM_IntToNumber` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `Number Multiple Of` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `WanFunInpaintToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 3 | 65% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
