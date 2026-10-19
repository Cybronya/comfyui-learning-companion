---
name: unknown_workflow_sampler_vae_35
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9
common_nodes: [CLIPLoader, CreateVideo, LoadImage, Lynx_Encode, Lynx_KSampler, Lynx_Model, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: [CR Prompt Text]
members: [视频生成/图生视频/1972855654023143425.json, 视频生成/图生视频/1975547820323246081.json, 视频生成/图生视频/1972500268996882433.json, 视频生成/文生视频/1972855654023143425.json, 视频生成/文生视频/1975547820323246081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_35

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1972855654023143425.json、视频生成/图生视频/1975547820323246081.json、视频生成/图生视频/1972500268996882433.json、视频生成/文生视频/1972855654023143425.json、视频生成/文生视频/1975547820323246081.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoadImage`
- `Lynx_Encode`
- `Lynx_KSampler`
- `Lynx_Model`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 121 | 81 - 121 | 5 | 86% |
| 调度器 | 1 | 1 - 1 | 5 | 100% |
| 重绘幅度 | 2 | 2 - 2 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 121，观测区间 81 - 121，5 个样本，取值集中（一致性 86%）
- 调度器 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 2，观测区间 2 - 2，5 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 2，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
