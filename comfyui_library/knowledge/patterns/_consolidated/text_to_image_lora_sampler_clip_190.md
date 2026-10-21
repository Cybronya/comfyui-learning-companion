---
name: text_to_image_lora_sampler_clip_190
type: Text To Image
frequency: 6
level: strong
coverage: 0.8565
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, CR Prompt Text, easy int]
members: [图片生成/图生图/2102137579343794177.json, 图片生成/图生图/2102151973511454722.json, 图片生成/图生图/2102164933382332417.json, 图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json, 图片生成/文生图/H3人物三视图和场景图生成优化版V3工具_2100664259473657857.json, 图片生成/文生图/全能图片全能图片G2.5文生图与图生图 角色一致性高质量创作_2098123716503891970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_190

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102137579343794177.json、图片生成/图生图/2102151973511454722.json、图片生成/图生图/2102164933382332417.json、图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json、图片生成/文生图/H3人物三视图和场景图生成优化版V3工具_2100664259473657857.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/6 个有
- `RH_RhartImageG25SunburstImageToImage` —— 4/6 个有
- `RH_RhartImageG2ImageToImage` —— 4/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `KOOK_SaveJPGImage` —— 2/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、CR Prompt Text、easy int
