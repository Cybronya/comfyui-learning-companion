---
name: unknown_workflow_lora_sampler_unet_69
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8745
common_nodes: [CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问人物表情编辑_2026155357369798658.json, 图片生成/图生图/千问编辑手机壳图案_2086993892540506113.json, 图片生成/图生图/平面图转效果图_2004092575822848001.json, 图片生成/图生图/景观设计方案图1210_1998608403167608833.json, 图片生成/图生图/最新qwen image 2511单图编辑工作流x_2013208112680931329.json, 图片生成/图生图/最新qwen image 2511单图编辑工作流x_2070752054544527361.json, 图片生成/图生图/规划用地图生成城市设计方案图v1.0_1985273198331764738.json, 图片生成/图生图/规划用地图生成城市设计方案图v1.0_1986632623231561730.json, 图片生成/图生图/规划用地图生成城市设计方案图v2.0_1986788983076286465.json, 图片生成/图生图/规划用地图生成城市设计方案图v3.0_2008523601170931714.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/千问人物表情编辑_2026155357369798658.json、图片生成/图生图/千问编辑手机壳图案_2086993892540506113.json、图片生成/图生图/平面图转效果图_2004092575822848001.json、图片生成/图生图/景观设计方案图1210_1998608403167608833.json、图片生成/图生图/最新qwen image 2511单图编辑工作流x_2013208112680931329.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 9/10 个有
- `LayerUtility: ImageReelComposit` —— 9/10 个有
- `Text Multiline` —— 9/10 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 7/10 个有
- `EmptyLatentImage` —— 6/10 个有
- `Any Switch (rgthree)` —— 5/10 个有
- `Fast Groups Muter (rgthree)` —— 5/10 个有
- `QwenEditConfigPreparer` —— 3/10 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 3/10 个有
- `PreviewImage` —— 2/10 个有
- `Fast Muter (rgthree)` —— 1/10 个有
- `Int` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `easy promptList` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 10 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 33% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | normal | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1392 | 1200 - 2000 | 6 | 82% |
| 高度 | 1240 | 1200 - 1504 | 6 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，10 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 normal，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1392，观测区间 1200 - 2000，6 个样本，取值集中（一致性 82%）
- 高度 中位数 1240，观测区间 1200 - 1504，6 个样本，取值集中（一致性 92%）
- 高发问题（5/10 个样本）：Steps较低可能导致细节不足
