---
name: text_to_image_lora_sampler_clip_540
type: Text To Image
frequency: 3
level: weak
coverage: 0.674333
common_nodes: [AnimaArtistStyleT8, AnimaBoosterLoader, AnimaGelbooruStyleT8, AnimaPromptCombinerT8, AnimaPromptT8, AnimaTeaCache, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, GetNode, INTConstant, KSampler, Load Lora, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetNode, Text Concatenate, VAEDecode, VAELoader, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima动漫-画师文生图_2074170395028185090.json, 图片生成/文生图/Anima动漫-画师文生图_2111630195127046145.json, 图片生成/文生图/Anima画师风格文生图，动漫角色热门IP一键生成_2110782560031830017.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_540

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima动漫-画师文生图_2074170395028185090.json、图片生成/文生图/Anima动漫-画师文生图_2111630195127046145.json、图片生成/文生图/Anima画师风格文生图，动漫角色热门IP一键生成_2110782560031830017.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `AnimaArtistStyleT8`
- `AnimaBoosterLoader`
- `AnimaGelbooruStyleT8`
- `AnimaPromptCombinerT8`
- `AnimaPromptT8`
- `AnimaTeaCache`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `KSampler`
- `Load Lora`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 12 | 3 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1024 | 80 - 1024 | 3 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 12，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
