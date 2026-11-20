---
name: image_to_image_lora_sampler_unet_122
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9764
common_nodes: [ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F1 图像修复 图生图 细节修复 CN产品控制_1927603483548225538.json, 图片生成/图生图/F1图像控制 CN产品控制 背景生成 产品迁移_1927164669704962049.json, 图片生成/图生图/FLUX洗图V1.0_1914702912063270913.json, 图片生成/图生图/Flux.1Krea图生图+线稿控制_1951798915828011009.json, 图片生成/图生图/LABUBU图生图线稿控制_1936654629663051778.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/F1 图像修复 图生图 细节修复 CN产品控制_1927603483548225538.json、图片生成/图生图/F1图像控制 CN产品控制 背景生成 产品迁移_1927164669704962049.json、图片生成/图生图/FLUX洗图V1.0_1914702912063270913.json、图片生成/图生图/Flux.1Krea图生图+线稿控制_1951798915828011009.json、图片生成/图生图/LABUBU图生图线稿控制_1936654629663051778.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/5 个有
- `ControlNetApplyAdvanced` —— 4/5 个有
- `ControlNetLoader` —— 4/5 个有
- `CLIPTextEncodeFlux` —— 3/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `ImageCompositeMasked` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `ClipInterrogator` —— 1/5 个有
- `WD14Tagger|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.85 | 0.7 - 1 | 4 | 82% |
| 采样步数 | 23 | 20 - 30 | 5 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 33% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 0.55 | 0.46 - 1 | 5 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.85，观测区间 0.7 - 1，4 个样本，取值集中（一致性 82%）
- 采样步数 中位数 23，观测区间 20 - 30，5 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 0.55，观测区间 0.46 - 1，5 个样本
