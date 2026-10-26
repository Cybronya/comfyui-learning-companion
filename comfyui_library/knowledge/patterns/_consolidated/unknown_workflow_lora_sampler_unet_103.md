---
name: unknown_workflow_lora_sampler_unet_103
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.812143
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Eidt-2511-遮罩定位精准重绘工作流_2005991188308119553.json, 图片生成/图生图/Qwen-Eidt-2511-遮罩精细化改图零偏移工作流_2003746502742843393.json, 图片生成/图生图/Qwen-Eidt-2511遮罩精准重绘_2012062229088182274.json, 图片生成/图生图/Qwen2511 局部改图_2016674287960199170.json, 图片生成/图生图/QwenEdit2511单角色提升一致性Lora_2010970305585483777.json, 图片生成/图生图/WH-AI-Studio-Qwen-Eidt-2511局部重绘_2015620805454991362.json, 图片生成/文生图/Qwen-Eidt-2511零偏移遮罩双图局部重绘_2009941483956215810.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_103

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Eidt-2511-遮罩定位精准重绘工作流_2005991188308119553.json、图片生成/图生图/Qwen-Eidt-2511-遮罩精细化改图零偏移工作流_2003746502742843393.json、图片生成/图生图/Qwen-Eidt-2511遮罩精准重绘_2012062229088182274.json、图片生成/图生图/Qwen2511 局部改图_2016674287960199170.json、图片生成/图生图/QwenEdit2511单角色提升一致性Lora_2010970305585483777.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintCrop` —— 6/7 个有
- `InpaintStitch` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `ImageAndMaskPreview` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `LayerUtility: ImageReel` —— 3/7 个有
- `LayerUtility: ImageReelComposit` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `GetImage` —— 1/7 个有
- `LayerMask: MaskPreview` —— 1/7 个有
- `LayerUtility: SaveImagePlus` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `QwenEditAdaptiveLongestEdge` —— 1/7 个有
- `Text Multiline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
