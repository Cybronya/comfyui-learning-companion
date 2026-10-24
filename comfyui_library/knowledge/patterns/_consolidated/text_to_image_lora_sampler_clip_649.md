---
name: text_to_image_lora_sampler_clip_649
type: Text To Image
frequency: 2
level: weak
coverage: 0.8165
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, DapaoRandomPromptLineExtractNode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, RH_LLMAPI_NODE, SaveImage, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906.json, 图片生成/文生图/网恋照片-全是美女-批量出_2024483802432675841.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_649

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图写实国漫3D风手动+API随机提示词.千问Qwen_2009092152491515906.json、图片生成/文生图/网恋照片-全是美女-批量出_2024483802432675841.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DapaoRandomPromptLineExtractNode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1444 | - | 2 | 63% |
| 高度 | 1196 | - | 2 | 93% |
| 采样步数 | 19.5 | - | 2 | 46% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1444，样本不足，未给区间，2 个样本
- 高度 中位数 1196，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样步数 中位数 19.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
