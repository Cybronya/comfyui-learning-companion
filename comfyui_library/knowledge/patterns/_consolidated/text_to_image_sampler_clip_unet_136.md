---
name: text_to_image_sampler_clip_unet_136
type: Text To Image
frequency: 6
level: weak
coverage: 0.859833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/沙雕场景-四视图-klein_2084085233376382977.json, 图片生成/文生图/法式复古风格的美女_2114250444477394946.json, 图片生成/文生图/电商一键生成模特 Z-Image_2012713566901637122.json, 图片生成/文生图/电商文生图 krea2_2079494663781834754.json, 图片生成/文生图/百度大模型 文生图ERNIE-image-turbo 人物一致性 自然真实_2044640662099857410.json, 图片生成/文生图/百度大模型ERNIE-image-turbo-文生图  人物一致性 自然真实_2044656791585296386.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/沙雕场景-四视图-klein_2084085233376382977.json、图片生成/文生图/法式复古风格的美女_2114250444477394946.json、图片生成/文生图/电商一键生成模特 Z-Image_2012713566901637122.json、图片生成/文生图/电商文生图 krea2_2079494663781834754.json、图片生成/文生图/百度大模型 文生图ERNIE-image-turbo 人物一致性 自然真实_2044640662099857410.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `JjkText` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `CR Prompt List` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 1472 | 720 - 2048 | 6 | 58% |
| 高度 | 1180 | 1024 - 2048 | 6 | 73% |
| 采样步数 | 8 | 2 - 20 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 0.2 - 1 | 6 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1472，观测区间 720 - 2048，6 个样本
- 高度 中位数 1180，观测区间 1024 - 2048，6 个样本
- 采样步数 中位数 8，观测区间 2 - 20，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
