---
name: text_to_image_sampler_clip_unet_74
type: Text To Image
frequency: 9
level: weak
coverage: 0.875444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json, 图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json, 图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json, 图片生成/文生图/Krea2-文生图+自动扩写提示词_2068202850336985089.json, 图片生成/文生图/Krea2美人极速版，支持反推。_2092435948138221569.json, 图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json, 图片生成/文生图/Z-Anime-自动提示词二次元动漫生成_2049497102346100738.json, 图片生成/文生图/krea2+Afterlight+最强文生图(媲美MJ)_2082826253823995905.json, 图片生成/文生图/z image海报设计，主图设计_2038970982379032577.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Anima -aesthetic-v1.1-自动优化提示词-动漫文生图_2078551646241648642.json、图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json、图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json、图片生成/文生图/Krea2-文生图+自动扩写提示词_2068202850336985089.json、图片生成/文生图/Krea2美人极速版，支持反推。_2092435948138221569.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 8/9 个有
- `llama_cpp_model_loader` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `llama_cpp_parameters` —— 3/9 个有
- `LoadImage` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 40 | 9 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 18% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | beta | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 768 | 720 - 1440 | 9 | 74% |
| 高度 | 1280 | 1024 - 1920 | 9 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 40，9 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 beta，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1440，9 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，9 个样本
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
