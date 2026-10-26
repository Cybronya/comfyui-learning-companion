---
name: unknown_workflow_sampler_clip_unet_236
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.867833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Base 文生图_2016498773949685761.json, 图片生成/文生图/Z-Image-Base-8steps 文生图_2063211651511443458.json, 图片生成/文生图/Z-Image-Base文生图V2（高画质版）_2016193102607818754.json, 图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json, 图片生成/文生图/Z-Image-Turbo批量文生图_1993884946834145281.json, 图片生成/文生图/千问文生图-海报制造机器_1954172979645181954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_236

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image Base 文生图_2016498773949685761.json、图片生成/文生图/Z-Image-Base-8steps 文生图_2063211651511443458.json、图片生成/文生图/Z-Image-Base文生图V2（高画质版）_2016193102607818754.json、图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json、图片生成/文生图/Z-Image-Turbo批量文生图_1993884946834145281.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `PreviewImage` —— 3/6 个有
- `easy promptLine` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `MuyeSizeSelector` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `WujiUpscaler` —— 1/6 个有
- `easy hiresFix` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21 | 8 - 50 | 6 | 39% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 4 | 6 | 49% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 21，观测区间 8 - 50，6 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 4，6 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
