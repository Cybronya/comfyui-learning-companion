---
name: text_to_image_lora_sampler_clip_427
type: Text To Image
frequency: 4
level: strong
coverage: 0.85825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图通用转换工作流｜图像再生成高质量处理_2095095993237860353.json, 图片生成/图生图/图生图｜Klein_9B一键溶图，双图融合测试效果实测_2099856179072692225.json, 图片生成/图生图/基础产品展示图生图 商品素材图生成处理工具_2099227769531097089.json, 图片生成/图生图/精修图生图工作流，提升图片细节与质感的专业修图方案_2102889930006548481.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_427

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图生图通用转换工作流｜图像再生成高质量处理_2095095993237860353.json、图片生成/图生图/图生图｜Klein_9B一键溶图，双图融合测试效果实测_2099856179072692225.json、图片生成/图生图/基础产品展示图生图 商品素材图生成处理工具_2099227769531097089.json、图片生成/图生图/精修图生图工作流，提升图片细节与质感的专业修图方案_2102889930006548481.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DisplayImageFromURL` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PainterFluxImageEdit` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
