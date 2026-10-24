---
name: unknown_workflow_sampler_vae_52
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.922
common_nodes: [CLIPLoader, CreateVideo, LoadImage, Lynx_Encode, Lynx_KSampler, Lynx_Model, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LYNX字节跳动高保真人脸迁移视频生成_1972500268996882433.json, 视频生成/文生视频/Smthem版Lynx ID特征一致性Full版_1972855654023143425.json, 视频生成/文生视频/Smthem版Lynx ID特征一致性Lite版_1975547820323246081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_52

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LYNX字节跳动高保真人脸迁移视频生成_1972500268996882433.json、视频生成/文生视频/Smthem版Lynx ID特征一致性Full版_1972855654023143425.json、视频生成/文生视频/Smthem版Lynx ID特征一致性Lite版_1975547820323246081.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Prompt Text` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 121 | 81 - 121 | 3 | 82% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | 2 | 2 - 2 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 121，观测区间 81 - 121，3 个样本，取值集中（一致性 82%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 2，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
