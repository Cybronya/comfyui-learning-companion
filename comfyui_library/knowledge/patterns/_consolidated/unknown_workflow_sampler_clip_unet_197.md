---
name: unknown_workflow_sampler_clip_unet_197
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.977667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-turbo与base模型融合文生图_2018686787765407745.json, 图片生成/文生图/Z-image-造相增强随机性-蓝色多脑盒_1999680352287326209.json, 图片生成/文生图/Z-image文生图 -多批次人物一致性_2002833348940709889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_197

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo与base模型融合文生图_2018686787765407745.json、图片生成/文生图/Z-image-造相增强随机性-蓝色多脑盒_1999680352287326209.json、图片生成/文生图/Z-image文生图 -多批次人物一致性_2002833348940709889.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 904 | 720 - 1080 | 3 | 84% |
| 高度 | 1280 | 1280 - 1920 | 3 | 80% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 20 | 3 | 65% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 33% |
| 重绘幅度 | simple | - | 3 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 904，观测区间 720 - 1080，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1280 - 1920，3 个样本
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 20，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 33%
- 重绘幅度 最常用 simple，3 个样本，一致性 33%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
