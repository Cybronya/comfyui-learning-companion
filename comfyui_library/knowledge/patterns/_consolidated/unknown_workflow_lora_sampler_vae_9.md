---
name: unknown_workflow_lora_sampler_vae_9
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.774286
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/19号特工：FireRed图片编辑+换装_2091071826360365057.json, 图片生成/图生图/FireRedImageEdit1.1换衣换装模特服装展示_2062092204809744386.json, 图片生成/图生图/FireRedImageEdit一键换衣换装换衣电商服装_2060740654908665857.json, 图片生成/图生图/LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098.json, 图片生成/图生图/Qwen-Edit-2511-单图_多图编辑合集-迅风幻影_2073780548887207937.json, 图片生成/图生图/QwenEdit2511单图_多图编辑_换装_姿势参考合集_2003774347670110209.json, 图片生成/图生图/QwenEdit2511单图编辑_2031737656530440193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/19号特工：FireRed图片编辑+换装_2091071826360365057.json、图片生成/图生图/FireRedImageEdit1.1换衣换装模特服装展示_2062092204809744386.json、图片生成/图生图/FireRedImageEdit一键换衣换装换衣电商服装_2060740654908665857.json、图片生成/图生图/LH-DMT版本-2.生图片类-041.QwenEdit2511单图编辑+双图互动_2016524689539076098.json、图片生成/图生图/Qwen-Edit-2511-单图_多图编辑合集-迅风幻影_2073780548887207937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `DWPreprocessor` —— 3/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `Lora Loader Stack (rgthree)` —— 1/7 个有
- `ResolutionPicker` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
