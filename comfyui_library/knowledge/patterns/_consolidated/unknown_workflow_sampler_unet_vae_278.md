---
name: unknown_workflow_sampler_unet_vae_278
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【阡陌】 Teacache 无损加速 flux 文生图_1944714736133132290.json, 图片生成/文生图/【阡陌】FLUX + LORA 中文提示词自动翻译 文生图工作流_1942182398836764674.json, 图片生成/文生图/【阡陌】flux Schnell 文生图工作流_1943252121083146241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_278

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【阡陌】 Teacache 无损加速 flux 文生图_1944714736133132290.json、图片生成/文生图/【阡陌】FLUX + LORA 中文提示词自动翻译 文生图工作流_1942182398836764674.json、图片生成/文生图/【阡陌】flux Schnell 文生图工作流_1943252121083146241.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateCLIPTextEncodeNode` —— 2/3 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `TeaCache` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 20 | 4 - 20 | 3 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 4 - 20，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
