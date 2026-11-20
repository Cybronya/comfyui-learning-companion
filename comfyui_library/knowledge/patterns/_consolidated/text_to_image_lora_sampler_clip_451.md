---
name: text_to_image_lora_sampler_clip_451
type: Text To Image
frequency: 4
level: weak
coverage: 0.62
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键生成多镜头多角度出图 多视角场景图生图工具_2099226620409237505.json, 图片生成/图生图/动漫转真人高还原工作流，CG幻想风格图生图写实化处理方案_2103525035259547649.json, 图片生成/文生图/Qwen_Image_Edit图像编辑模型｜文生图图生图 编辑能力很能打_2105555719201320962.json, 图片生成/文生图/任意多角度，可单选多选-Rubby_1996846983686103041.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_451

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键生成多镜头多角度出图 多视角场景图生图工具_2099226620409237505.json、图片生成/图生图/动漫转真人高还原工作流，CG幻想风格图生图写实化处理方案_2103525035259547649.json、图片生成/文生图/Qwen_Image_Edit图像编辑模型｜文生图图生图 编辑能力很能打_2105555719201320962.json、图片生成/文生图/任意多角度，可单选多选-Rubby_1996846983686103041.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
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
- `GetNode` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 4 | 13% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 8 | 4 | 72% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，4 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 8，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高发问题（28/4 个样本）：Steps较低可能导致细节不足
