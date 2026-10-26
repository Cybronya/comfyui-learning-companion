---
name: text_to_image_lora_sampler_clip_207
type: Text To Image
frequency: 9
level: strong
coverage: 0.875444
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2基础图生图｜通用图像转换高质量生成_2095962002811342850.json, 图片生成/图生图/MiniMax H3全能图像编辑低显存故事板四视图处理工具_2102494252348563457.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2097780554698678273.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098922055084367874.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098980585321623553.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2099656781432709122.json, 图片生成/图生图/minimax H3全能图像编辑｜低显存也能跑的图生图｜改图换景都拿手_2102235515952132097.json, 图片生成/图生图/基础图生图人像写真｜krea2摄影级生成_2095516228675788802.json, 图片生成/图生图/基础图生图稳定出图｜krea2 日常修图必备工作流_2096254734893146113.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_207

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea2基础图生图｜通用图像转换高质量生成_2095962002811342850.json、图片生成/图生图/MiniMax H3全能图像编辑低显存故事板四视图处理工具_2102494252348563457.json、图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2097780554698678273.json、图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098922055084367874.json、图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098980585321623553.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `MultiTextConcatenate` —— 7/9 个有
- `RH_Captioner` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `String Literal` —— 7/9 个有
- `PreviewImage` —— 5/9 个有
- `EmptyImage` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `MiniMaxH3ReferenceToVideo` —— 2/9 个有
- `Text` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
