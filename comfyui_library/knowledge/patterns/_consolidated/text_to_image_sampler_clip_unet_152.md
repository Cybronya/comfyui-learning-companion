---
name: text_to_image_sampler_clip_unet_152
type: Text To Image
frequency: 5
level: weak
coverage: 0.9096
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全自动krea2文生图_2070721265224216578.json, 图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json, 图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json, 图片生成/文生图/自动多风格文生图｜krea2+Qwen3.5一键直出_2093466592263888897.json, 视频生成/图生视频/krea2+Qwen3.5-自动多风格文生图 (1)_2085254333008007169.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/全自动krea2文生图_2070721265224216578.json、图片生成/文生图/多风格文生图｜krea2+Qwen3.5自动生成_2089836661319487489.json、图片生成/文生图/多风格自动文生图｜Qwen3.5+krea2风格轮换生成_2093467909044658177.json、图片生成/文生图/自动多风格文生图｜krea2+Qwen3.5一键直出_2093466592263888897.json、视频生成/图生视频/krea2+Qwen3.5-自动多风格文生图 (1)_2085254333008007169.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `孤海注释` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 5 | 16% |
| 高度 | 80 | 80 - 512 | 5 | 16% |
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 45% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 高度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
