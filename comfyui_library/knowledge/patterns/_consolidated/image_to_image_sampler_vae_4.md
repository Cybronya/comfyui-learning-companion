---
name: image_to_image_sampler_vae_4
type: Image To Image
frequency: 24
level: moderate
coverage: 0.951375
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/双节棍nunchaku Qwen Edit 8步极速图生图_1968520860183212034.json, 图片生成/图生图/双节棍千问图像编辑-qwen-image-edit_1968580136255803393.json, 图片生成/图生图/大斧真人转3D_1972879628723490818.json, 图片生成/图生图/手办_1970355550968049665.json, 图片生成/图生图/插画动漫转真实-Qwen_1968128886720573442.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059974029460725761.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2059977060457734146.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2060179770062761986.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2060283898608832513.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2061056068268158978.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2072383567207944193.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2076638317302607873.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2089411487113764865.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095439305417248770.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095444428671512578.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095449494145028097.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095584894389936129.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095597858056658946.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095599025432125442.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2095605763430510594.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2096642654376386561.json, 图片生成/图生图/真人转动漫  真人转卡通  真人转漫画_2097953971787886594.json, 图片生成/图生图/通义千问图片编辑（qwen-edit）_1958158377425784833.json, 图片生成/图生图/🦖转绘-Qwen-Image_1958477176230277122.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/双节棍nunchaku Qwen Edit 8步极速图生图_1968520860183212034.json、图片生成/图生图/双节棍千问图像编辑-qwen-image-edit_1968580136255803393.json、图片生成/图生图/大斧真人转3D_1972879628723490818.json、图片生成/图生图/手办_1970355550968049665.json、图片生成/图生图/插画动漫转真实-Qwen_1968128886720573442.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 23/24 个有
- `UNETLoader` —— 22/24 个有
- `PIP_图像联结` —— 10/24 个有
- `PreviewImage` —— 10/24 个有
- `ImageScaleToTotalPixels` —— 6/24 个有
- `ImageStitch` —— 4/24 个有
- `ImageAndMaskPreview` —— 2/24 个有
- `ImageConcatMulti` —— 2/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/24 个有
- `NunchakuQwenImageDiTLoader` —— 2/24 个有
- `Text Multiline` —— 2/24 个有
- `RepeatLatentBatch` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 24 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 24 | 56% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，24 个样本
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（20/24 个样本）：Steps较低可能导致细节不足
