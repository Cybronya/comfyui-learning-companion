---
name: unknown_workflow_sampler_clip_unet_168
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.860375
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【老金驿站】Z-anime满血文生图工作流_2046119986116173825.json, 图片生成/文生图/【老金驿站】Z-image高清细节DejpegV2_1997835100480016386.json, 图片生成/文生图/【老金驿站】z-image8步文生图工作流_1994293848790728706.json, 图片生成/文生图/【阡陌】Ovis Image文生图工作流_1999424887913578498.json, 图片生成/文生图/【阡陌】Qwen-Image-2512 + 4步加速lora文生图工作流_2008154394784702466.json, 图片生成/文生图/【阡陌】Z-Image随机多样性增强文生图工作流_2009600567135444994.json, 图片生成/文生图/【阡陌】双截棍Nunchaku Z-Image极速文生图工作流_2011317669181526017.json, 图片生成/文生图/基础案例basic_switch_node+全节点注释_2055478851081383937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_168

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/【老金驿站】Z-anime满血文生图工作流_2046119986116173825.json、图片生成/文生图/【老金驿站】Z-image高清细节DejpegV2_1997835100480016386.json、图片生成/文生图/【老金驿站】z-image8步文生图工作流_1994293848790728706.json、图片生成/文生图/【阡陌】Ovis Image文生图工作流_1999424887913578498.json、图片生成/文生图/【阡陌】Qwen-Image-2512 + 4步加速lora文生图工作流_2008154394784702466.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `ConditioningNoiseInjection` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `MuyeSizeSelector` —— 1/8 个有
- `NunchakuZImageDiTLoader` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 50 | 8 | 2% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 8 | 18% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 50，8 个样本，取值分散，一致性仅 2%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，8 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
