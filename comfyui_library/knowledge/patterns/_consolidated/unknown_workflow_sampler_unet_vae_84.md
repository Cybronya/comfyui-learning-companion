---
name: unknown_workflow_sampler_unet_vae_84
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.958556
common_nodes: [EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1957280959416692738.json, 图片生成/文生图/1959355153205899265.json, 图片生成/文生图/1960596890238746626.json, 图片生成/文生图/1986700537984921601.json, 图片生成/文生图/1987149238826151938.json, 图片生成/文生图/1987158769756999681.json, 图片生成/文生图/1987323968367603713.json, 图片生成/文生图/【阡陌】Z-Image随机多样性增强文生图工作流_2009600567135444994.json, 图片生成/文生图/【阡陌】双截棍Nunchaku Z-Image极速文生图工作流_2011317669181526017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_84

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1957280959416692738.json、图片生成/文生图/1959355153205899265.json、图片生成/文生图/1960596890238746626.json、图片生成/文生图/1986700537984921601.json、图片生成/文生图/1987149238826151938.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `CLIPLoader` —— 6/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `ModelSamplingAuraFlow` —— 6/9 个有
- `DualCLIPLoader` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `CLIPTextEncodeFlux` —— 2/9 个有
- `ConditioningNoiseInjection` —— 2/9 个有
- `AILab_QwenVL` —— 1/9 个有
- `FusionText` —— 1/9 个有
- `MuyeSizeSelector` —— 1/9 个有
- `NunchakuZImageDiTLoader` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `ZML_TextInput` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 30 | 9 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 30，9 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
