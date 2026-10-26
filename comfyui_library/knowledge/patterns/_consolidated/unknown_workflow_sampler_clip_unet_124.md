---
name: unknown_workflow_sampler_clip_unet_124
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9274
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【老金驿站】Z-anime满血文生图工作流_2046119986116173825.json, 图片生成/文生图/【老金驿站】Z-image高清细节DejpegV2_1997835100480016386.json, 图片生成/文生图/【老金驿站】z-image8步文生图工作流_1994293848790728706.json, 图片生成/文生图/【阡陌】Ovis Image文生图工作流_1999424887913578498.json, 图片生成/文生图/一键生成可爱的小仙女_2029386005651922945.json, 图片生成/文生图/亚秒级生成！Zimage超快图片生成器官方工作流_2038610580453466113.json, 图片生成/文生图/千问QWEN IMAGE极速文生图_2006405852235833345.json, 图片生成/文生图/千问文生图（中文海报直出）_1962714914005626881.json, 图片生成/文生图/常用_图片_qwen2512文生图_2037710756266905602.json, 图片生成/文生图/文生图-qwen_image_2512-模板_2090689557934206978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/【老金驿站】Z-anime满血文生图工作流_2046119986116173825.json、图片生成/文生图/【老金驿站】Z-image高清细节DejpegV2_1997835100480016386.json、图片生成/文生图/【老金驿站】z-image8步文生图工作流_1994293848790728706.json、图片生成/文生图/【阡陌】Ovis Image文生图工作流_1999424887913578498.json、图片生成/文生图/一键生成可爱的小仙女_2029386005651922945.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `CLIPLoaderGGUF` —— 2/10 个有
- `FluxResolutionNode` —— 2/10 个有
- `CFGNorm` —— 1/10 个有
- `CompressImages` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 2 - 50 | 10 | 7% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 10 | 23% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 2 - 50，10 个样本，取值分散，一致性仅 7%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，10 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
