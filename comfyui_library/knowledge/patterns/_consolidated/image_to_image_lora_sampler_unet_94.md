---
name: image_to_image_lora_sampler_unet_94
type: Image To Image
frequency: 7
level: weak
coverage: 0.893571
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json, 图片生成/图生图/一键换装 女装童装 小红书电商带货_2087841507427573761.json, 图片生成/图生图/千问编辑2511-人物多角度出图_2039933028406923265.json, 图片生成/图生图/千问编辑2511-人物多角度出图_2059908761376083970.json, 图片生成/图生图/图像编辑模型测试-Qwen Image Edit 2511_2110543678782664706.json, 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682.json, 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/一键换衣 OOTD 3.0【 edit 2511 最新版 】_2010296531844337665.json、图片生成/图生图/一键换装 女装童装 小红书电商带货_2087841507427573761.json、图片生成/图生图/千问编辑2511-人物多角度出图_2039933028406923265.json、图片生成/图生图/千问编辑2511-人物多角度出图_2059908761376083970.json、图片生成/图生图/图像编辑模型测试-Qwen Image Edit 2511_2110543678782664706.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `easy int` —— 3/7 个有
- `AddLabel` —— 2/7 个有
- `FluxKontextImageScale` —— 2/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `KOOK_SaveJPGImage` —— 2/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `EmptySD3LatentImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 40 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 40，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
