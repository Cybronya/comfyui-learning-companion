---
name: unknown_workflow_sampler_clip_unet_163
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.840125
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2 巨构文生图_2091510907372396546.json, 图片生成/文生图/Krea2文生图-美感画质V2_2100973649820999682.json, 图片生成/文生图/Krea2美感画质双提升V2_2097626860837494785.json, 图片生成/文生图/Krea2美感画质双提升V2_2098923708609032194.json, 图片生成/文生图/Krea2美感画质双提升_2093345673189089282.json, 图片生成/文生图/krea2横_2091833320878469121.json, 图片生成/文生图/krea2竖_2092094811011641346.json, 图片生成/文生图/东方美学制作流_2100541472004198401.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_163

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Krea2 巨构文生图_2091510907372396546.json、图片生成/文生图/Krea2文生图-美感画质V2_2100973649820999682.json、图片生成/文生图/Krea2美感画质双提升V2_2097626860837494785.json、图片生成/文生图/Krea2美感画质双提升V2_2098923708609032194.json、图片生成/文生图/Krea2美感画质双提升_2093345673189089282.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `ConditioningKrea2Rebalance` —— 6/8 个有
- `Lora Loader Stack (rgthree)` —— 6/8 个有
- `LatentUpscaleBy` —— 3/8 个有
- `PrimitiveFloat` —— 3/8 个有
- `EmptyImage` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 1024 - 1920 | 8 | 73% |
| 高度 | 1920 | 736 - 1920 | 8 | 69% |
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 10 | 8 | 95% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1088，观测区间 1024 - 1920，8 个样本
- 高度 中位数 1920，观测区间 736 - 1920，8 个样本
- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 10，8 个样本，取值集中（一致性 95%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
