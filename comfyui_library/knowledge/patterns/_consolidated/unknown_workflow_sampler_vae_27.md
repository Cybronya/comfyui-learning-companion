---
name: unknown_workflow_sampler_vae_27
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.952
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen千问2509 多图编辑  加速版（4步）_1997547051980361729.json, 图片生成/图生图/qwen千问2509 多图编辑_1997529016326361089.json, 图片生成/图生图/qwen图生图  洗图  重绘 局部修改_2046419289288216577.json, 图片生成/图生图/产品展示 产品替换 图生图 多图编辑_2044376198586834945.json, 图片生成/图生图/产品展示 多图编辑 多图融合  图生图_2044421173475287041.json, 图片生成/图生图/产品展示 多图融合 多图编辑_2044376805544566785.json, 图片生成/图生图/产品替换 产品展示 电商 双图融合 多图编辑 多图融合  图生图_2045403356130189314.json, 图片生成/图生图/产品替换 产品展示_2045428594398208002.json, 图片生成/图生图/产品替换 双图融合 多图编辑 多图融合  图生图_2045390109431832578.json, 图片生成/图生图/人物角色-全视角参考视图_2040802253094785026.json, 图片生成/图生图/全视图 _ 角色一致性_1991419477451624450.json, 图片生成/图生图/全视图 _ 角色一致性_2007004747022213121.json, 平台全量/全视图 _ 角色一致性_1870371208901599234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_27

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/qwen千问2509 多图编辑  加速版（4步）_1997547051980361729.json、图片生成/图生图/qwen千问2509 多图编辑_1997529016326361089.json、图片生成/图生图/qwen图生图  洗图  重绘 局部修改_2046419289288216577.json、图片生成/图生图/产品展示 产品替换 图生图 多图编辑_2044376198586834945.json、图片生成/图生图/产品展示 多图编辑 多图融合  图生图_2044421173475287041.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `PreviewImage` —— 7/13 个有
- `Anything Everywhere` —— 4/13 个有
- `Anything Everywhere3` —— 4/13 个有
- `ConstrainImage|pysssss` —— 4/13 个有
- `ImageResize+` —— 2/13 个有
- `MuyeTextEditOutput` —— 1/13 个有
- `NunchakuQwenImageDiTLoader` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 960 - 1024 | 13 | 97% |
| 高度 | 1536 | 1248 - 1536 | 13 | 91% |
| 采样步数 | 8 | 4 - 20 | 13 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 13 | 64% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 60/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 960 - 1024，13 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1248 - 1536，13 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，观测区间 4 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（60/13 个样本）：Steps较低可能导致细节不足
