---
name: text_to_image_lora_sampler_clip_533
type: Text To Image
frequency: 3
level: strong
coverage: 0.802667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商产品展示图生图 商品图编辑处理 多风格素材生成_2099226250886860801.json, 图片生成/图生图/面料材质图生图 纺织面料纹理材质生成工具_2099223212570791937.json, 图片生成/文生图/RH工作流封面生成_2085451153541779457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_533

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电商产品展示图生图 商品图编辑处理 多风格素材生成_2099226250886860801.json、图片生成/图生图/面料材质图生图 纺织面料纹理材质生成工具_2099223212570791937.json、图片生成/文生图/RH工作流封面生成_2085451153541779457.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DisplayImageFromURL` —— 2/3 个有
- `RHLLMChatNode` —— 2/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `JoinStringMulti` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RH_RhartImageG2TextToImage` —— 1/3 个有

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
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
