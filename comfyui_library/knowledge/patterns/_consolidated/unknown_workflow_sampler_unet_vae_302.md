---
name: unknown_workflow_sampler_unet_vae_302
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9375
common_nodes: [CreateVideo, GetVideoComponents, KSampler, LoadVideo, RelayVSRConditioning, SaveVideo, UNETLoader, VAELoader, VSRDecode]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/Relay VSR-视频高清放大_2119239757669691393.json, 平台全量/Relay VSR放大_2111016859377168386.json, 平台全量/Relay VSR视频极速高清放大_2120019680332181505.json, 平台全量/RelayVSR 视频超分放大_2121147686937260033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_302

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Relay VSR-视频高清放大_2119239757669691393.json、平台全量/Relay VSR放大_2111016859377168386.json、平台全量/Relay VSR视频极速高清放大_2120019680332181505.json、平台全量/RelayVSR 视频超分放大_2121147686937260033.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateVideo`
- `GetVideoComponents`
- `KSampler`
- `LoadVideo`
- `RelayVSRConditioning`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `VSRDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
