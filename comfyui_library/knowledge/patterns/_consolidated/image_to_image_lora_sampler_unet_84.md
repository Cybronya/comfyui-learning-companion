---
name: image_to_image_lora_sampler_unet_84
type: Image To Image
frequency: 9
level: strong
coverage: 0.831556
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json, 图片生成/文生图/面料印花提取工作流｜Qwen Image Edit+花纹LoRA，去褶皱去背景全注释+全节点注释_2060980136811520002.json, 平台全量/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2052200249728487425.json, 平台全量/Qwen Multiangle 多角度一致性分镜工作流_2010573008347340801.json, 平台全量/Qwen2511 自由调节摄影机 多角度可视化控制   图像多角度编辑+SeedVR2 高清放大_2014544416677044226.json, 平台全量/多角度摄像控制（96种机位选择）+直观便捷操作【2026-1-12】_2010569306987302913.json, 平台全量/空间_2011261744601108481.json, 数字人/数字人/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2042627893414596610.json, 数字人/数字人/多角度摄像控制（96种机位选择）+直观便捷操作_2056928106224644097.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/千问qwen 双图图片编辑，换服装、模特、背景...+全节点注释_2085905889881583617.json、图片生成/文生图/面料印花提取工作流｜Qwen Image Edit+花纹LoRA，去褶皱去背景全注释+全节点注释_2060980136811520002.json、平台全量/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2052200249728487425.json、平台全量/Qwen Multiangle 多角度一致性分镜工作流_2010573008347340801.json、平台全量/Qwen2511 自由调节摄影机 多角度可视化控制   图像多角度编辑+SeedVR2 高清放大_2014544416677044226.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 8/9 个有
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `QwenMultiangleCameraNode` —— 7/9 个有
- `EmptySD3LatentImage` —— 5/9 个有
- `Int` —— 5/9 个有
- `KepStringList` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `Text Concatenate` —— 3/9 个有
- `easy string` —— 3/9 个有
- `PreviewAny` —— 2/9 个有
- `TextEncodeQwenImageEdit` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `Float` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `TextInput_` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 9 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
