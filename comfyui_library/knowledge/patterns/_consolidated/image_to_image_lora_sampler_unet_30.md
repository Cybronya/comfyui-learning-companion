---
name: image_to_image_lora_sampler_unet_30
type: Image To Image
frequency: 14
level: moderate
coverage: 0.885714
common_nodes: [CLIPLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449.json, 图片生成/图生图/Krea 2.0 风格重塑神器！内置 397+ 预设，一张图一键变大片_2104038615826395137.json, 图片生成/图生图/Krea2 Edit 单图编辑_2085625746910965761.json, 图片生成/图生图/Krea2 单图像编辑（保持人物一致性）_2084627099599597569.json, 图片生成/图生图/Krea2 单图编辑 保持人物一致性_2084779099117154305.json, 图片生成/图生图/Krea2 照片风格转换流｜内置397种风格_2103306485861281793.json, 图片生成/图生图/Krea2_照片风格转换流｜内置397种风格_2108735472326500354.json, 图片生成/图生图/Krea2_照片风格转换流｜内置397种风格_2110182995679338497.json, 图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085010240629723138.json, 图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085181759821537282.json, 图片生成/图生图/Krea_2_Identity_Edit_V1.2单图编辑替换衣服·替换发型·替换背景_2085205841640251394.json, 图片生成/图生图/krea2-edit-单图编辑_2076126181744799746.json, 图片生成/图生图/krea2-identity-edit 双图编辑（替换服装，替换背景）_2080923117085609986.json, 图片生成/图生图/krea2-identity-edit 双图编辑（替换服装，替换背景）_2081678351055540225.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_30

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Krea 2 Identity Edit V1.2单图编辑（替换衣服·替换发型·替换背景）_2080992938896744449.json、图片生成/图生图/Krea 2.0 风格重塑神器！内置 397+ 预设，一张图一键变大片_2104038615826395137.json、图片生成/图生图/Krea2 Edit 单图编辑_2085625746910965761.json、图片生成/图生图/Krea2 单图像编辑（保持人物一致性）_2084627099599597569.json、图片生成/图生图/Krea2 单图编辑 保持人物一致性_2084779099117154305.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 10/14 个有
- `FluxKontextImageScale` —— 6/14 个有
- `Image Comparer (rgthree)` —— 6/14 个有
- `ImpactInt` —— 5/14 个有
- `CR Prompt Text` —— 4/14 个有
- `EmptyLatentImage` —— 4/14 个有
- `easy stylesSelector` —— 4/14 个有
- `孤海注释` —— 4/14 个有
- `Int` —— 2/14 个有
- `PreviewImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 11 | 14 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 768 | 512 - 1024 | 4 | 67% |
| 高度 | 1024 | 512 - 1536 | 4 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 11，14 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1024，4 个样本
- 高度 中位数 1024，观测区间 512 - 1536，4 个样本
