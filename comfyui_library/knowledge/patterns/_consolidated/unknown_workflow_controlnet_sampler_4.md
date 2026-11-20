---
name: unknown_workflow_controlnet_sampler_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CR Image Input Switch, CR Multi-ControlNet Stack, CR Prompt Text, Efficient Loader, KSampler (Efficient), LoadImage, Qr Code (mtb), SaveImage, SeedGenerator]
problems: []
missing: []
members: [平台全量/AI艺术二维码初级版_1905075977725349890.json, 平台全量/AI艺术二维码初级版_1924798371427459074.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/AI艺术二维码初级版_1905075977725349890.json、平台全量/AI艺术二维码初级版_1924798371427459074.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Image Input Switch`
- `CR Multi-ControlNet Stack`
- `CR Prompt Text`
- `Efficient Loader`
- `KSampler (Efficient)`
- `LoadImage`
- `Qr Code (mtb)`
- `SaveImage`
- `SeedGenerator`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
