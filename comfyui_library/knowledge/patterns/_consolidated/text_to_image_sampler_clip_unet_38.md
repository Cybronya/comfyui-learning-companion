---
name: text_to_image_sampler_clip_unet_38
type: Text To Image
frequency: 14
level: moderate
coverage: 0.752071
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Moss-image Base文生图_2116371868184825858.json, 图片生成/文生图/Moss-image_Base文生图_2116673819573309441.json, 图片生成/文生图/Moss文生图 角色设计 三视图_2115304039620636674.json, 图片生成/文生图/Moss文生图 角色设计 三视图_2115703070192660482.json, 图片生成/文生图/Moss文生图+8步加速_2112030480005689345.json, 图片生成/文生图/Moss文生图+8步加速_2114886860421029890.json, 图片生成/文生图/Moss文生图_角色设计_三视图_2115643527953739778.json, 图片生成/文生图/image_krea2_turbo_t2i_2072904099296800770.json, 图片生成/文生图/image_krea2_turbo_t2i_2079183226878382082.json, 图片生成/文生图/image_krea2_turbo_t2i_2099207878002429953.json, 图片生成/文生图/image_krea2_turbo文生图_2074494308316700673.json, 图片生成/文生图/krea-2-turbo 文生图_1903742090277195777.json, 图片生成/文生图/krea-2-turbo开源版-文生图_2117074124618162177.json, 图片生成/文生图/krea2-t2i_2101830220889288705.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Moss-image Base文生图_2116371868184825858.json、图片生成/文生图/Moss-image_Base文生图_2116673819573309441.json、图片生成/文生图/Moss文生图 角色设计 三视图_2115304039620636674.json、图片生成/文生图/Moss文生图 角色设计 三视图_2115703070192660482.json、图片生成/文生图/Moss文生图+8步加速_2112030480005689345.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextGenerate` —— 12/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `ResolutionSelector` —— 8/14 个有
- `ComfySwitchNode` —— 7/14 个有
- `ConditioningZeroOut` —— 7/14 个有
- `PreviewAny` —— 7/14 个有
- `PrimitiveBoolean` —— 7/14 个有
- `StringConcatenate` —— 7/14 个有
- `PreviewImage` —— 5/14 个有
- `SkipLayerGuidanceDiTSimple` —— 5/14 个有
- `PrimitiveInt` —— 2/14 个有
- `ConditioningKrea2Rebalance` —— 1/14 个有
- `CustomCombo` —— 1/14 个有
- `RegexExtract` —— 1/14 个有
- `StringReplace` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 14 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 14 | 46% |
| 采样算法 | er_sde | - | 14 | 50% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 960 - 2048 | 14 | 75% |
| 高度 | 1024 | 1024 - 2048 | 14 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，14 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，14 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 er_sde，14 个样本，一致性 50%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 960 - 2048，14 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，14 个样本
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足
