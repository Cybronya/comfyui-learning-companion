---
name: text_to_image_sampler_clip_unet_87
type: Text To Image
frequency: 8
level: weak
coverage: 0.938375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SuperZimage图片处理（4K文生图）_2041019748875509762.json, 图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json, "图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json", "图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json", 图片生成/文生图/Z image 文生图_1993886895799205889.json, 图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json, 图片生成/文生图/Z-Image-Turbo写真｜一键蜂腰身材曲线自定义调整_2101548693785759746.json, 图片生成/文生图/动漫生图｜Anima base v1官方文生图直出_2089769718608650241.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/SuperZimage图片处理（4K文生图）_2041019748875509762.json、图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json、图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json、图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json、图片生成/文生图/Z image 文生图_1993886895799205889.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `ModelSamplingAuraFlow` —— 3/8 个有
- `Int` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `solarL_SaveImagesToZip` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `AddLabel` —— 1/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `DyPE_FLUX` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `Textbox` —— 1/8 个有
- `easy globalSeed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 15 | 6 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 24% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1052 | 80 - 4096 | 8 | 0% |
| 高度 | 1472 | 80 - 2160 | 8 | 31% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 15，6 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 80 - 4096，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 1472，观测区间 80 - 2160，8 个样本，取值分散，一致性仅 31%
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
