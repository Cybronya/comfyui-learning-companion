---
name: image_to_image_lora_sampler_unet_37
type: Image To Image
frequency: 13
level: moderate
coverage: 0.969692
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen万能图片编辑图生图全能图片V1平替_2005434060799442945.json, 图片生成/图生图/三张图就编辑 ICEdit_LoRA_2015404467323146242.json, 图片生成/图生图/主体抠图与黑白蒙版生成_2052234697593368577.json, 图片生成/图生图/主体抠图与黑白蒙版生成_2061622051689033729.json, 图片生成/图生图/产品摄影背景迁移 qwen_image_edit_2511_2015810728174821378.json, 图片生成/图生图/人物镜头多角度展示_2007372715937767425.json, 图片生成/图生图/人物镜头多角度工作流_1995473495901581313.json, 图片生成/图生图/千问-3D转绘_1995785923046543362.json, 图片生成/图生图/千问2509-人物镜头多角度展示_1994932012010102785.json, 图片生成/图生图/千问2509-人物镜头多角度展示_1998321817486000129.json, 图片生成/图生图/千问2509模型人物多镜头多角度展现_1995297236168978434.json, 图片生成/图生图/最强-人物不变+多角度写真生成【Qwen2511+lora】_2010916855375994882.json, 图片生成/图生图/超牛的一致性人物多角度展示流！_1995001388340064257.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/qwen万能图片编辑图生图全能图片V1平替_2005434060799442945.json、图片生成/图生图/三张图就编辑 ICEdit_LoRA_2015404467323146242.json、图片生成/图生图/主体抠图与黑白蒙版生成_2052234697593368577.json、图片生成/图生图/主体抠图与黑白蒙版生成_2061622051689033729.json、图片生成/图生图/产品摄影背景迁移 qwen_image_edit_2511_2015810728174821378.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 12/13 个有
- `ModelSamplingAuraFlow` —— 12/13 个有
- `Text Multiline` —— 9/13 个有
- `ImageScaleToTotalPixels` —— 8/13 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 7/13 个有
- `easy promptLine` —— 7/13 个有
- `FluxKontextImageScale` —— 4/13 个有
- `Image Comparer (rgthree)` —— 4/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `DuckHideNode` —— 1/13 个有
- `ImageListToImageBatch` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `YANC.MultilineString` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 13 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 13 | 56% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，13 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（11/13 个样本）：Steps较低可能导致细节不足
