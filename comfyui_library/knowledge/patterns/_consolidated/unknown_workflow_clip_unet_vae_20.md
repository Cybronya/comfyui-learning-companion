---
name: unknown_workflow_clip_unet_vae_20
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/百度Ernie极速5步文生图_2045655487722561537.json, 图片生成/文生图/百度Ernie极速5步文生图_2045870550827933697.json, 图片生成/文生图/空白工作流_2033896316320882689.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/百度Ernie极速5步文生图_2045655487722561537.json、图片生成/文生图/百度Ernie极速5步文生图_2045870550827933697.json、图片生成/文生图/空白工作流_2033896316320882689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `VRAMReserver` —— 2/3 个有
- `KSampler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 3 | 49% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | er_sde | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，3 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 er_sde，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
