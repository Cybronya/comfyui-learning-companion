---
name: unknown_workflow_lora_sampler_unet_93
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.883375
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402.json, 图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642.json, 图片生成/图生图/gen全能视频Si-参照主体+自动多角度生成_1988507274354278402.json, 图片生成/图生图/开源顶级电商详情页批量设计工作流_2072278687252303873.json, 图片生成/图生图/电商详情页批量直出图Qwen2511满血版_2114641512159072258.json, 图片生成/图生图/电商详情页批量直出图（Qwen2511满血版）_2056729840673447937.json, 图片生成/图生图/高质量电商产品详情页批量设计工作流_2096089277015871490.json, 图片生成/文生图/电商详情页批量直出（Qwen2511满血版）_2084590694081056769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1977738722605158402.json、图片生成/图生图/QwenEdit Next Scane场景一致性lora批量跑图_1978060571725680642.json、图片生成/图生图/gen全能视频Si-参照主体+自动多角度生成_1988507274354278402.json、图片生成/图生图/开源顶级电商详情页批量设计工作流_2072278687252303873.json、图片生成/图生图/电商详情页批量直出图Qwen2511满血版_2114641512159072258.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 7/8 个有
- `ProcessString` —— 6/8 个有
- `ShowText|pysssss` —— 6/8 个有
- `FluxKontextImageScale` —— 5/8 个有
- `RH_LLMAPI_Pro_Node` —— 5/8 个有
- `SaveText|pysssss` —— 5/8 个有
- `ShowText` —— 5/8 个有
- `Text` —— 5/8 个有
- `easy promptConcat` —— 5/8 个有
- `EmptyLatentImage` —— 3/8 个有
- `RH_Captioner` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
