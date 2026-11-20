---
name: text_to_image_lora_sampler_clip_575
type: Text To Image
frequency: 3
level: strong
coverage: 0.903667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, GODMT_BatchToList, GODMT_SplitString, ImageMergeNode, Int, JjkConcat, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SizeSelector, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy boolean, easy getNode, easy ifElse, easy setNode, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Qwen-Edit-2511一键生成｜人物三视图影视角色资产图_2094728018261536769.json, 数字人/数字人/Qwen-Edit-2511人物三视图影视短剧角色资产图一键生成_2088220739148275714.json, 数字人/数字人/Qwen-Edit-2511角色三视图一键生成｜短剧角色资产图_2094502182212165634.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_575

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/Qwen-Edit-2511一键生成｜人物三视图影视角色资产图_2094728018261536769.json、数字人/数字人/Qwen-Edit-2511人物三视图影视短剧角色资产图一键生成_2088220739148275714.json、数字人/数字人/Qwen-Edit-2511角色三视图一键生成｜短剧角色资产图_2094502182212165634.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `GODMT_BatchToList`
- `GODMT_SplitString`
- `ImageMergeNode`
- `Int`
- `JjkConcat`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SizeSelector`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy boolean`
- `easy getNode`
- `easy ifElse`
- `easy setNode`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（12/3 个样本）：Steps较低可能导致细节不足
