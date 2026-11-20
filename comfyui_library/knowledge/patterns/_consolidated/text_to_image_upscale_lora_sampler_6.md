---
name: text_to_image_upscale_lora_sampler_6
type: Text To Image
frequency: 17
level: moderate
coverage: 0.953
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/二次元人物生成_2088191460100362241.json, 图片生成/文生图/二次元真人(男生）_2088399659025911810.json, 图片生成/文生图/二次元真人_2088197741246767105.json, 图片生成/文生图/千问-文生图-高配精细_2097549428528869378.json, 图片生成/文生图/千问优质生图快速工作流_1988895729412354050.json, 图片生成/文生图/千问文生图 高质量 高清晰_2097963267984543745.json, 图片生成/文生图/千问文生图-电商专用_2066788213078978561.json, 图片生成/文生图/千问文生图-电商专用_2108042168052043777.json, 图片生成/文生图/千问文生图-电商专用_2112373154172719105.json, 图片生成/文生图/千问文生图-电商专用_2113920181155225601.json, 图片生成/文生图/千问文生图_高质量_高清晰_2098219987013033986.json, 图片生成/文生图/千问文生图基础款_1985377282284003329.json, 图片生成/文生图/千问文生图电商产品_2090229875432050689.json, 图片生成/文生图/千问超写实文生图（AI仿真人漫剧资产制作）_2021440026743148546.json, 图片生成/文生图/千问（qwen2512最新版）文生图（加速+电影感）_1978855905909444610.json, 图片生成/文生图/文生图-人像生成写实风格_2087860545537011714.json, 图片生成/文生图/文生图-人像生成写实风格_2088186685191450626.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/二次元人物生成_2088191460100362241.json、图片生成/文生图/二次元真人(男生）_2088399659025911810.json、图片生成/文生图/二次元真人_2088197741246767105.json、图片生成/文生图/千问-文生图-高配精细_2097549428528869378.json、图片生成/文生图/千问优质生图快速工作流_1988895729412354050.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 12/17 个有
- `CLIPLoader` —— 12/17 个有
- `PreviewImage` —— 9/17 个有
- `CLIPLoaderGGUF` —— 5/17 个有
- `KOOK_ImageCompression` —— 5/17 个有
- `TextInputBasic` —— 5/17 个有
- `Image Comparer (rgthree)` —— 2/17 个有
- `MuyeTextEditOutput` —— 1/17 个有
- `QwenImageLatentAspectRatio` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1360 | 768 - 2304 | 17 | 66% |
| 高度 | 1024 | 904 - 2048 | 17 | 68% |
| 采样步数 | 8 | 4 - 12 | 17 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 17 | 89% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1360，观测区间 768 - 2304，17 个样本
- 高度 中位数 1024，观测区间 904 - 2048，17 个样本
- 采样步数 中位数 8，观测区间 4 - 12，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，17 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（11/17 个样本）：Steps较低可能导致细节不足
