---
name: image_to_image_sampler_clip_unet_41
type: Image To Image
frequency: 9
level: moderate
coverage: 0.818333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 洗图流_1993520238505426945.json, 图片生成/图生图/Flux2图生图洗图_1993506160825352194.json, 图片生成/图生图/Flux2洗图工作流_1993561388627017729.json, 图片生成/图生图/Z-Image 图生图细节增强版_2015750867261071362.json, 图片生成/图生图/Z-Image图生图（细节增强版）_2020347508572037121.json, 图片生成/图生图/Z-image 超真实感 洗图_1993895502299283457.json, 图片生成/图生图/Z-image-turbo 图生图 洗图 ai变真人_1982650838457958402.json, 图片生成/图生图/Z-image图生图最强图生图洗图新玩法_1993890648885575682.json, 图片生成/图生图/全能图片2.0+Z-Image图生图（细节增强版）_2033800127114125314.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2 洗图流_1993520238505426945.json、图片生成/图生图/Flux2图生图洗图_1993506160825352194.json、图片生成/图生图/Flux2洗图工作流_1993561388627017729.json、图片生成/图生图/Z-Image 图生图细节增强版_2015750867261071362.json、图片生成/图生图/Z-Image图生图（细节增强版）_2020347508572037121.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `CR Text` —— 5/9 个有
- `DownloadAndLoadFlorence2Model` —— 2/9 个有
- `Florence2Run` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `FluxGuidance` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 9 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 72% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 0.4 | 0.2 - 0.55 | 9 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 0.4，观测区间 0.2 - 0.55，9 个样本
