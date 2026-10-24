---
name: text_to_image_sampler_clip_unet_171
type: Text To Image
frequency: 3
level: strong
coverage: 0.855
common_nodes: [CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontxet双图潜空间编辑-dev_1965735074647994369.json, 图片生成/图生图/传图1键去水印_1938807262284861442.json, 图片生成/图生图/好用的kontxet多图参考全家桶-dev开源版_1938867994271666178.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_171

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/kontxet双图潜空间编辑-dev_1965735074647994369.json、图片生成/图生图/传图1键去水印_1938807262284861442.json、图片生成/图生图/好用的kontxet多图参考全家桶-dev开源版_1938867994271666178.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `Get resolution [Crystools]` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 904 | 512 - 1024 | 3 | 73% |
| 高度 | 1024 | 512 - 1200 | 3 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 904，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1200，3 个样本
