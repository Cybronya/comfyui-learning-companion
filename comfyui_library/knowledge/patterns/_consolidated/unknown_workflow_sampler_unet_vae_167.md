---
name: unknown_workflow_sampler_unet_vae_167
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.7315
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, MiniMaxH3ImageConditioning, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/KOOK-Minimax-H3-image-尘星_2121117996713332737.json, 平台全量/MiniMax-H3-Image-文生图-6步_2120340135966498817.json, 平台全量/Minimax H3 Image 文生图高质量（Kook 尘星）_2121125165458350082.json, 平台全量/Minimax-H3 官方文生图_2120284554522091521.json, 平台全量/Minimax-h3-mage-文生图_2120325207587115009.json, 平台全量/minimaxh3 文生图_2120339642829598722.json, 视频生成/视频生视频/H3 Image｜6步16图参考编辑_2120807220840591361.json, 视频生成/视频生视频/H3 Image｜6步单图编辑_2120806758502453249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_167

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/KOOK-Minimax-H3-image-尘星_2121117996713332737.json、平台全量/MiniMax-H3-Image-文生图-6步_2120340135966498817.json、平台全量/Minimax H3 Image 文生图高质量（Kook 尘星）_2121125165458350082.json、平台全量/Minimax-H3 官方文生图_2120284554522091521.json、平台全量/Minimax-h3-mage-文生图_2120325207587115009.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `MiniMaxH3ImageConditioning`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `TextGenerateV2` —— 6/8 个有
- `JsonExtractString` —— 5/8 个有
- `PreviewAny` —— 5/8 个有
- `StringReplace` —— 5/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `GetImageSize` —— 2/8 个有
- `ImageCompare` —— 2/8 个有
- `KOOK_SaveJPGImage` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `ResizeImageMaskNode` —— 2/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
