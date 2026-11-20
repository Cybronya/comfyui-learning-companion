---
name: text_to_image_lora_sampler_clip_136
type: Text To Image
frequency: 12
level: moderate
coverage: 0.818083
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["平台全量/MJ？,krea2+moss_2117207337055375361.json", 平台全量/Moss文生图 角色设计 三视图_2117297242745950209.json, 平台全量/Moss文生图 角色设计 三视图_2117842762069532674.json, 平台全量/Moss文生图 角色设计 三视图_2119006944097816578.json, 平台全量/Moss文生图 角色设计 三视图_2119145229000470529.json, 平台全量/Moss文生图 角色设计 三视图_2119515693031976962.json, 平台全量/Moss文生图 角色设计 三视图_2119674331734298625.json, 平台全量/Moss文生图 角色设计 三视图_2120025361957343233.json, 平台全量/Moss文生图 角色设计 三视图_2120039769072816130.json, 平台全量/Moss文生图 角色设计 三视图_2120050705338814466.json, 平台全量/Moss文生图 角色设计 三视图_2121130556594417666.json, 平台全量/Moss文生图+8步加速，保存latten_2117605662011256834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/MJ？,krea2+moss_2117207337055375361.json、平台全量/Moss文生图 角色设计 三视图_2117297242745950209.json、平台全量/Moss文生图 角色设计 三视图_2117842762069532674.json、平台全量/Moss文生图 角色设计 三视图_2119006944097816578.json、平台全量/Moss文生图 角色设计 三视图_2119145229000470529.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextGenerate` —— 11/12 个有
- `PreviewImage` —— 9/12 个有
- `ConditioningZeroOut` —— 1/12 个有
- `ImageScaleBy` —— 1/12 个有
- `ResolutionSelector` —— 1/12 个有
- `SaveLatent` —— 1/12 个有
- `VAEEncode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 960 - 1056 | 12 | 97% |
| 高度 | 1280 | 1024 - 1408 | 12 | 94% |
| 采样步数 | 8 | 8 - 25 | 12 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 63% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 0.35 - 1 | 12 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 960，观测区间 960 - 1056，12 个样本，取值集中（一致性 97%）
- 高度 中位数 1280，观测区间 1024 - 1408，12 个样本，取值集中（一致性 94%）
- 采样步数 中位数 8，观测区间 8 - 25，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，12 个样本，取值集中（一致性 81%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
