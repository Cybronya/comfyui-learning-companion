---
name: image_to_image_sampler_clip_unet_38
type: Image To Image
frequency: 11
level: moderate
coverage: 0.83
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 洗图流_1993520238505426945.json, 图片生成/图生图/Flux2图生图洗图_1993506160825352194.json, 图片生成/图生图/Flux2洗图工作流_1993561388627017729.json, 图片生成/图生图/Z-Image 图生图细节增强版_2015750867261071362.json, 图片生成/图生图/Z-Image-De洗图图生图_1997877980846260226.json, 图片生成/图生图/Z-Image图生图（细节增强版）_2020347508572037121.json, 图片生成/图生图/Z-image 超真实感 洗图_1993895502299283457.json, 图片生成/图生图/Z-image+千问VL反推图生图洗图增强真实感_1993893012516306946.json, 图片生成/图生图/Z-image图生图最强图生图洗图新玩法_1993890648885575682.json, 图片生成/图生图/Z-image图生图洗图_2015740669658144770.json, 图片生成/图生图/Z-image图生图洗图增加真实感_1996559760713457666.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux2 洗图流_1993520238505426945.json、图片生成/图生图/Flux2图生图洗图_1993506160825352194.json、图片生成/图生图/Flux2洗图工作流_1993561388627017729.json、图片生成/图生图/Z-Image 图生图细节增强版_2015750867261071362.json、图片生成/图生图/Z-Image-De洗图图生图_1997877980846260226.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
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
- `PrimitiveInt` —— 10/11 个有
- `CR Text` —— 5/11 个有
- `Image Comparer (rgthree)` —— 5/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `AILab_QwenVL` —— 3/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `DownloadAndLoadFlorence2Model` —— 2/11 个有
- `Florence2Run` —— 2/11 个有
- `FluxGuidance` —— 1/11 个有
- `LayerUtility: TextJoin` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `ModelSamplingAuraFlow` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `RH_Captioner` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 20 | 11 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 11 | 74% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 0.4 | 0.2 - 0.75 | 11 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 0.4，观测区间 0.2 - 0.75，11 个样本
