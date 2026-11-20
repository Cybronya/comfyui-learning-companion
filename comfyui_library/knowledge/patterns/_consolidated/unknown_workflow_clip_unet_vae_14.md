---
name: unknown_workflow_clip_unet_vae_14
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.96
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/百度Ernie极速5步文生图_2045655487722561537.json, 图片生成/文生图/百度Ernie极速5步文生图_2045870550827933697.json, 图片生成/文生图/空白工作流_2033896316320882689.json, 平台全量/ERNIE-Image-Turbo开源版-文生图_2117127200074977281.json, 数字人/数字人/FLUX2文生图工作流_2039267124157358081.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/百度Ernie极速5步文生图_2045655487722561537.json、图片生成/文生图/百度Ernie极速5步文生图_2045870550827933697.json、图片生成/文生图/空白工作流_2033896316320882689.json、平台全量/ERNIE-Image-Turbo开源版-文生图_2117127200074977281.json、数字人/数字人/FLUX2文生图工作流_2039267124157358081.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `KSampler` —— 3/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `VRAMReserver` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 20 | 3 | 63% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 5 | 38% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，5 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
