---
name: unknown_workflow_sampler_clip_unet_133
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.901
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image Base 文生图_2016498773949685761.json, 图片生成/文生图/Z-Image-Base-8steps 文生图_2063211651511443458.json, 图片生成/文生图/Z-Image-Base文生图V2（高画质版）_2016193102607818754.json, 图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json, 图片生成/文生图/zimage+base+文生图+工作流_2074064661959503874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image Base 文生图_2016498773949685761.json、图片生成/文生图/Z-Image-Base-8steps 文生图_2063211651511443458.json、图片生成/文生图/Z-Image-Base文生图V2（高画质版）_2016193102607818754.json、图片生成/文生图/Z-Image-Turbo 极致写实文生图工作流_2084326650979905538.json、图片生成/文生图/zimage+base+文生图+工作流_2074064661959503874.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `easy promptLine` —— 2/5 个有
- `MuyeSizeSelector` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `WujiUpscaler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 5 | 52% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 58% |
| 采样算法 | res_multistep | - | 5 | 40% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 最常用 res_multistep，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
