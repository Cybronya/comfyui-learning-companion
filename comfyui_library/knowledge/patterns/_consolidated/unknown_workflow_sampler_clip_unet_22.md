---
name: unknown_workflow_sampler_clip_unet_22
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.9318
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-Image SFT 文生图｜4步加速版_2113609550153732098.json, 图片生成/文生图/MOSS-Image SFT 文生图｜4步加速版_2113917931385085953.json, 图片生成/文生图/MOSS文生图-2K极速版-人物更真实_2113908253649362946.json, 图片生成/文生图/MOSS文生图2K极速版!_2112525560906870786.json, 图片生成/文生图/MOSS文生图2K极速版!_2113543303009492994.json, 图片生成/文生图/MOSS文生图2K极速版_2112541313756389378.json, 图片生成/文生图/MOSS文生图2K极速版_2113424816693932034.json, 图片生成/文生图/Moss Image 4步快速文生图_2112395762205290497.json, 图片生成/文生图/Moss Sft Fixed文生图_2112960432251166721.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2112963716441534466.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2112970055196696577.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2112982153691754498.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2112984703698563074.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113137189981868033.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113173523589058562.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113335522285408257.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113531251805220866.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113871067642155010.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113881374963884033.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113922473719844866.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2113951942761340930.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2114394968738586625.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2114397369096822785.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2114582869514481665.json, 图片生成/文生图/文生图  MOSS文生图  2K极速版_2114608957783363586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/MOSS-Image SFT 文生图｜4步加速版_2113609550153732098.json、图片生成/文生图/MOSS-Image SFT 文生图｜4步加速版_2113917931385085953.json、图片生成/文生图/MOSS文生图-2K极速版-人物更真实_2113908253649362946.json、图片生成/文生图/MOSS文生图2K极速版!_2112525560906870786.json、图片生成/文生图/MOSS文生图2K极速版!_2113543303009492994.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 24/25 个有
- `PreviewImage` —— 17/25 个有
- `CR Text` —— 10/25 个有
- `孤海注释` —— 3/25 个有
- `ImpactInt` —— 2/25 个有
- `MuyeTextEditOutput` —— 2/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 25 | 59% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 3 | 25 | 68% |
| 采样算法 | euler | - | 25 | 96% |
| 调度器 | simple | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，25 个样本
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 3，25 个样本
- 采样算法 最常用 euler，25 个样本，一致性 96%
- 调度器 最常用 simple，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（24/25 个样本）：Steps较低可能导致细节不足
