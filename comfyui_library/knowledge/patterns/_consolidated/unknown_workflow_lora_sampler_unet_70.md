---
name: unknown_workflow_lora_sampler_unet_70
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.937
common_nodes: [CLIPLoader, CR Text, CR Text Concatenate, EmptyLatentImage, GetTextFromJson, KSampler, LoadImage, LoadJsonFromText, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_Captioner_Pro, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptList, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2509服装+人脸=模特穿搭套图  林耀2.24_2026191549901574145.json, 图片生成/图生图/提示词行（json格式） 浮云 12.15_2000576227083776002.json, 图片生成/图生图/服装+人脸+文本控制=模特穿搭套图_2013986414349787137.json, 图片生成/图生图/服装+人脸=模特穿搭套图_1999796216533745666.json, 图片生成/图生图/服装+人脸=模特穿搭套图_2002580893992665090.json, 图片生成/图生图/服装+人脸=模特穿搭套图_2009412482535792641.json, 图片生成/图生图/白底服装+人脸=模特穿搭图_2000402760468135938.json, 图片生成/图生图/🍿Qwen2511模特穿搭+场景 四连随心换🍿_2004466267748794369.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_70

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/2509服装+人脸=模特穿搭套图  林耀2.24_2026191549901574145.json、图片生成/图生图/提示词行（json格式） 浮云 12.15_2000576227083776002.json、图片生成/图生图/服装+人脸+文本控制=模特穿搭套图_2013986414349787137.json、图片生成/图生图/服装+人脸=模特穿搭套图_1999796216533745666.json、图片生成/图生图/服装+人脸=模特穿搭套图_2002580893992665090.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `GetTextFromJson`
- `KSampler`
- `LoadImage`
- `LoadJsonFromText`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_Captioner_Pro`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptList`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 7/8 个有
- `ImageFromBatch` —— 7/8 个有
- `easy imageListToImageBatch` —— 7/8 个有
- `CR Text Replace` —— 4/8 个有
- `PreviewImage` —— 2/8 个有
- `DapaoImageLayoutNode` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `ImageListToBatch+` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 8 | 71% |
| 高度 | 1536 | 1536 - 3056 | 8 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1536，观测区间 1536 - 3056，8 个样本
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
