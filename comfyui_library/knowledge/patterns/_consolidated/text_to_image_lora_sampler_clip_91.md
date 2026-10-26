---
name: text_to_image_lora_sampler_clip_91
type: Text To Image
frequency: 14
level: weak
coverage: 0.9105
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen t2m_2040622346905587714.json, 图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json, 图片生成/文生图/krea2-turbo极简极速文生图｜小说配图专用 文生图秒出插画_2104056464099864578.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2097777800206970882.json, 图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2101478583771422722.json, 图片生成/文生图/丰盈美女人像写真生成｜文生图高质量出图工作流_2094542170748448770.json, 图片生成/文生图/冷冬圣诞夜漫画风出图｜动漫角色分镜文生图_2096901929984151554.json, 图片生成/文生图/动漫二次元风格文生图｜创意插画一键生成工具_2101181321061167106.json, 图片生成/文生图/动漫女孩文生图工作流｜动漫角色插画配图｜小说插图轻松出图_2101862601419481090.json, 图片生成/文生图/小说配图极速直出 krea2 turbo极简文生图工作流_2104314139870060545.json, 图片生成/文生图/文生图基础流｜krea2文生图图生图双模式_2089846295853879298.json, 图片生成/文生图/极速版Krea2 Trubo文生图｜美商极高V2版 美感直接拉满_2105551057450524673.json, 图片生成/文生图/精致漫画风文生图工作流｜动漫角色封面插图｜叙事感拉满出片_2101869067136233474.json, 图片生成/文生图/视频跟练｜文生图打造跟练画面素材，健身舞蹈教学好帮手_2107363684484993025.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Qwen t2m_2040622346905587714.json、图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json、图片生成/文生图/krea2-turbo极简极速文生图｜小说配图专用 文生图秒出插画_2104056464099864578.json、图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2097777800206970882.json、图片生成/文生图/krea2基础文生图工作流｜物品摄影人像写真生成_2101478583771422722.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 13/14 个有
- `JjkText` —— 12/14 个有
- `solarL_SaveImagesToZip` —— 12/14 个有
- `孤海注释` —— 12/14 个有
- `ConditioningZeroOut` —— 9/14 个有
- `CheckpointLoaderSimple` —— 6/14 个有
- `Fast Groups Bypasser (rgthree)` —— 5/14 个有
- `Seed (rgthree)` —— 3/14 个有
- `ResolutionSelector` —— 1/14 个有
- `TT_img_enc` —— 1/14 个有
- `VRAM_Debug` —— 1/14 个有
- `easy imageSwitch` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1280 | 14 | 0% |
| 高度 | 80 | 80 - 1920 | 14 | 0% |
| 采样步数 | 4 | 4 - 6 | 14 | 87% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 14 | 69% |
| 采样算法 | er_sde | - | 14 | 86% |
| 调度器 | beta | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1280，14 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，14 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 6，14 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，14 个样本
- 采样算法 最常用 er_sde，14 个样本，一致性 86%
- 调度器 最常用 beta，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（18/14 个样本）：Steps较低可能导致细节不足
