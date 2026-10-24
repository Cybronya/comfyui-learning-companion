---
name: image_to_image_lora_sampler_unet_81
type: Image To Image
frequency: 8
level: moderate
coverage: 0.91275
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit-图生图工作流_2095499580333973505.json, 图片生成/图生图/QwenEdit2511图片编辑 多角度生成工作流-B站UP主@好奇漫步_2065257036354506754.json, 图片生成/图生图/Qwen_360° 视图 多视角工作流_1993279358852939777.json, 图片生成/图生图/Qwen_人物_物品_产品 多视图 一键生成工作流_1993649585836982273.json, 图片生成/图生图/qwen_image_edit  _ 精准镜头控制器 _ 模特套图_2037780822270418946.json, 图片生成/图生图/qwen_image_edit 精准镜头控制器  模特套图 商品套图_2034504749021663233.json, 图片生成/图生图/qwen_image_edit 精准镜头视角控制器  模特套图 商品套图_2037729340846252034.json, 图片生成/图生图/【阡陌】Qwen-Eidt-2511可视化视角控制生成工作流_2011005734066069506.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_81

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QwenEdit-图生图工作流_2095499580333973505.json、图片生成/图生图/QwenEdit2511图片编辑 多角度生成工作流-B站UP主@好奇漫步_2065257036354506754.json、图片生成/图生图/Qwen_360° 视图 多视角工作流_1993279358852939777.json、图片生成/图生图/Qwen_人物_物品_产品 多视图 一键生成工作流_1993649585836982273.json、图片生成/图生图/qwen_image_edit  _ 精准镜头控制器 _ 模特套图_2037780822270418946.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `FluxKontextMultiReferenceLatentMethod` —— 6/8 个有
- `QwenMultiangleCameraNode` —— 5/8 个有
- `easy promptList` —— 5/8 个有
- `easy showAnything` —— 4/8 个有
- `ImageUpscaleWithModel` —— 3/8 个有
- `UpscaleModelLoader` —— 3/8 个有
- `CameraControlPromptNode` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `FluxKontextImageScale` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `VAEEncodeTiled` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 8 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 8 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，8 个样本
- 高发问题（25/8 个样本）：Steps较低可能导致细节不足
