---
name: image_to_image_lora_sampler_vae_14
type: Image To Image
frequency: 8
level: strong
coverage: 0.924375
common_nodes: [CFGNorm, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物多角度一致性，自由旋转 AIO_2009975197419446273.json, 图片生成/图生图/星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482.json, 图片生成/图生图/角色一致性 分镜 模特套图 多视图 qwen_2039201498646716418.json, 平台全量/Qwen-2511-edit自定义镜头转换_2017784759023312897.json, 平台全量/qwenEdit2511控制镜头_2010921569941463042.json, 平台全量/控制多角度视角+打光_2011243606383796226.json, 平台全量/相机多角度，多角度打光angels_2012893013386727425.json, 平台全量/镜头角度切换！最大9视角！_2009661459504041985.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人物多角度一致性，自由旋转 AIO_2009975197419446273.json、图片生成/图生图/星绘一键多机位角度调整（Multi-camera angle adjustment）_2010704541276180482.json、图片生成/图生图/角色一致性 分镜 模特套图 多视图 qwen_2039201498646716418.json、平台全量/Qwen-2511-edit自定义镜头转换_2017784759023312897.json、平台全量/qwenEdit2511控制镜头_2010921569941463042.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `SaveImage` —— 7/8 个有
- `VAELoader` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `UNETLoader` —— 6/8 个有
- `easy promptList` —— 6/8 个有
- `CR Text Concatenate` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `CheckpointLoaderSimple` —— 2/8 个有
- `QwenMultiangleLightningNode` —— 2/8 个有
- `DuckHideNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MakeListNode` —— 1/8 个有
- `PromptSwap` —— 1/8 个有
- `SaveImagePlus` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 8 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，8 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
