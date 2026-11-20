---
name: text_to_image_sampler_clip_unet_21
type: Text To Image
frequency: 17
level: moderate
coverage: 0.625471
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageScaleBy, JoinStringMulti, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SetNode, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy float, easy positive, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2080636703567597570.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2081017450442870785.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2102718819738406913.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2102724534217564161.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2115768462772625410.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2115793753297477633.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2115995040676929537.json, 图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2116010375887015937.json, 图片生成/图生图/boogu一键动漫转真人｜二次元图生图风格迁移写实出片_2103057704532140033.json, 图片生成/图生图/boogu二次元转真人工作流_2079460366404382722.json, 图片生成/图生图/boogu二次元转真人工作流_2082011876598304770.json, 图片生成/图生图/boogu二次元转真人工作流_2096054197799186433.json, 图片生成/图生图/boogu二次元转真人工作流_2096164094259851265.json, 图片生成/图生图/【击碎次元壁】动漫人物转真人工作流_2116927019513638914.json, 图片生成/图生图/二次元转真人反推提示词图生图｜boogu其它图片处理工作流_2088166802420486146.json, 图片生成/图生图/二次元转真人工作流_2080495779642429441.json, 图片生成/图生图/二次元转真人工作流_2095002756770787329.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2080636703567597570.json、图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2081017450442870785.json、图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2102718819738406913.json、图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2102724534217564161.json、图片生成/图生图/boogu一键二次元动漫转真人图生图工作流_2115768462772625410.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `JoinStringMulti`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy float`
- `easy positive`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/17 个有
- `LoraLoaderModelOnly` —— 2/17 个有
- `solarL_SaveImagesToZip` —— 2/17 个有
- `孤海注释` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 17 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 17 | 20% |
| 采样算法 | euler_ancestral | - | 17 | 88% |
| 调度器 | exponential | - | 17 | 88% |
| 重绘幅度 | 0.8 | 0.8 - 1 | 17 | 92% |
| 宽度 | 512 | 80 - 512 | 17 | 70% |
| 高度 | 512 | 80 - 512 | 17 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 36/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，17 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，17 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler_ancestral，17 个样本，一致性 88%
- 调度器 最常用 exponential，17 个样本，一致性 88%
- 重绘幅度 中位数 0.8，观测区间 0.8 - 1，17 个样本，取值集中（一致性 92%）
- 宽度 中位数 512，观测区间 80 - 512，17 个样本
- 高度 中位数 512，观测区间 80 - 512，17 个样本
- 高发问题（36/17 个样本）：Steps较低可能导致细节不足
