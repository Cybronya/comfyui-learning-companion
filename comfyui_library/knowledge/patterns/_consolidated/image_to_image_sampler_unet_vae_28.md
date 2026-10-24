---
name: image_to_image_sampler_unet_vae_28
type: Image To Image
frequency: 8
level: weak
coverage: 0.898375
common_nodes: [CLIPLoader, CR Prompt Text, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/00_人物持物融合_单道具_20步_2101706068576530433.json, 图片生成/图生图/00_人物持物融合_单道具_4步_2101706038402707458.json, 图片生成/图生图/00_人物持物融合_双道具_20步_2101706122561413121.json, 图片生成/图生图/00_人物持物融合_双道具_4步_2101706099593400322.json, 图片生成/图生图/01_人物入景首帧_1至5人_2101611485456850946.json, 图片生成/图生图/01_人物入景首帧_1至5人_双人同轮融合优化版_2102593466231508993.json, 图片生成/图生图/01_人物入景首帧_1至5人_数值修复版_2102410325357318146.json, 图片生成/图生图/2511+调整任意角度（柯基大佬版）简化版-jbp_2009986941873295361.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_28

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/00_人物持物融合_单道具_20步_2101706068576530433.json、图片生成/图生图/00_人物持物融合_单道具_4步_2101706038402707458.json、图片生成/图生图/00_人物持物融合_双道具_20步_2101706122561413121.json、图片生成/图生图/00_人物持物融合_双道具_4步_2101706099593400322.json、图片生成/图生图/01_人物入景首帧_1至5人_2101611485456850946.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `CFGNorm` —— 5/8 个有
- `ImageCompositeMasked` —— 3/8 个有
- `ImpactInt` —— 3/8 个有
- `ImpactSwitch` —— 3/8 个有
- `ImpactConvertDataType` —— 2/8 个有
- `ImpactFloat` —— 2/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `QwenMultiangleCameraNode` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy promptConcat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 8 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 26% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，8 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（18/8 个样本）：Steps较低可能导致细节不足
