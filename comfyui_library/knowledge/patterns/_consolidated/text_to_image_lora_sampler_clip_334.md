---
name: text_to_image_lora_sampler_clip_334
type: Text To Image
frequency: 6
level: weak
coverage: 0.937333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Layerd智能分层加速版｜一键导出PSD分层文件｜修图后期必备_2112038081107943425.json, 图片生成/图生图/Qwen Image Layered图像智能分层加速版，保存PSD图生图抠图处理工具_2103246417543389186.json, 图片生成/图生图/分层图像加速｜Qwen Image Layerd抠图图生图_2091243031851782146.json, 图片生成/图生图/图生图赛博玄幻湘灵｜中国风动漫女主，一键变身幻想角色_2099929545133608962.json, 图片生成/图生图/梨梨AI拆分PSD｜图片图层分离导出图生图工具_2093137292377546754.json, 图片生成/文生图/Comfyui-HAIGC-PSD 基础流_2007998507042480129.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_334

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image Layerd智能分层加速版｜一键导出PSD分层文件｜修图后期必备_2112038081107943425.json、图片生成/图生图/Qwen Image Layered图像智能分层加速版，保存PSD图生图抠图处理工具_2103246417543389186.json、图片生成/图生图/分层图像加速｜Qwen Image Layerd抠图图生图_2091243031851782146.json、图片生成/图生图/图生图赛博玄幻湘灵｜中国风动漫女主，一键变身幻想角色_2099929545133608962.json、图片生成/图生图/梨梨AI拆分PSD｜图片图层分离导出图生图工具_2093137292377546754.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `LatentCutToBatch` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `solarL_SaveImagesToZip` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `HAIGC_CombineUnits` —— 4/6 个有
- `HAIGC_Layer` —— 4/6 个有
- `HAIGC_SavePSD` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `Int` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `HAIGC_PSD_Background` —— 1/6 个有
- `PromptBatchQueue` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 6 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 2.5 - 4.5 | 6 | 82% |
| 采样算法 | er_sde | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 1024 | 6 | 0% |
| 高度 | 80 | 80 - 1024 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 2.5 - 4.5，6 个样本，取值集中（一致性 82%）
- 采样算法 最常用 er_sde，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 0%
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
