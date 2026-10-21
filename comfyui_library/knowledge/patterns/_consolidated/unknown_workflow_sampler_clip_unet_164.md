---
name: unknown_workflow_sampler_clip_unet_164
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.93675
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/boogu turbo文生图加速版工作流（附提示词工程）_2067891090774126594.json, 图片生成/文生图/danotebook-ernie-image-turbo_2062464622694854657.json, 图片生成/文生图/flux.2-klein文生图_2077238073297031169.json, 图片生成/文生图/flux2-Klein-自动文生图（4B）_2012021202050617346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/boogu turbo文生图加速版工作流（附提示词工程）_2067891090774126594.json、图片生成/文生图/danotebook-ernie-image-turbo_2062464622694854657.json、图片生成/文生图/flux.2-klein文生图_2077238073297031169.json、图片生成/文生图/flux2-Klein-自动文生图（4B）_2012021202050617346.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `ResolutionMaster` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 8 | 4 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
