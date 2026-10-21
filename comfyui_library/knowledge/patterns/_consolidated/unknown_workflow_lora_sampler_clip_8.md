---
name: unknown_workflow_lora_sampler_clip_8
type: Unknown Workflow
frequency: 18
level: weak
coverage: 0.832889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Text Concatenate, Text Multiline]
members: [图片生成/文生图/1988181167390244866.json, 图片生成/文生图/1988450428977373186.json, 图片生成/文生图/Qwen-Image-2512-文生图-提示词优化_2007102360237117441.json, 图片生成/文生图/qwen-image2512q版3d风格_2057869164727062530.json, 图片生成/文生图/qwen2512水墨中式枯笔焦墨勾线插画_2062947076870336513.json, 图片生成/文生图/qwen2512水墨国风_2063805351761367042.json, 图片生成/文生图/qwen2512粗线条水墨_2067961144140197890.json, 图片生成/文生图/qwen2512粗线条水墨_2068857089002393601.json, 图片生成/文生图/qwen2512粗线条水墨_2069676975639326721.json, 图片生成/文生图/qwen2512粗线条水墨_2080477072551665665.json, 图片生成/文生图/qwen2512粗线条水墨_2080481494887391233.json, 图片生成/文生图/qwen2512马克笔插画_2067421994693521410.json, 图片生成/文生图/qwen2512马克笔插画_2069671724421046273.json, 图片生成/文生图/qwen2512马克笔插画_2080470094504873985.json, 图片生成/文生图/qwen2512马克笔插画_2080472510591750146.json, 图片生成/文生图/qwen2512马克笔插画_2081934496953356289.json, 图片生成/文生图/手绘画本_2022488976958951425.json, 视频生成/图生视频/2067062569453576193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/1988181167390244866.json、图片生成/文生图/1988450428977373186.json、图片生成/文生图/Qwen-Image-2512-文生图-提示词优化_2007102360237117441.json、图片生成/文生图/qwen-image2512q版3d风格_2057869164727062530.json、图片生成/文生图/qwen2512水墨中式枯笔焦墨勾线插画_2062947076870336513.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Concatenate` —— 17/18 个有
- `UNETLoader` —— 16/18 个有
- `LatentUpscaleBy` —— 15/18 个有
- `EG_K_LATENT` —— 5/18 个有
- `Int` —— 3/18 个有
- `AILab_QwenVL` —— 2/18 个有
- `UnetLoaderGGUF` —— 2/18 个有
- `easy showAnything` —— 2/18 个有
- `AddLabel` —— 1/18 个有
- `RH_LLMAPI_NODE` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10.5 | 4 - 50 | 18 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 18 | 41% |
| 采样算法 | euler_ancestral | - | 18 | 67% |
| 调度器 | simple | - | 18 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10.5，观测区间 4 - 50，18 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，18 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler_ancestral，18 个样本，一致性 67%
- 调度器 最常用 simple，18 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（9/18 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Concatenate、Text Multiline
