---
name: unknown_workflow_lora_sampler_unet_104
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.905857
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageResizeKJv2, KSampler, LoraLoaderModelOnly, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit白底图换背景_URL输入_适合API调用_1990309598018064385.json, 图片生成/图生图/QwenEdit白底图生场景_1985929695130726402.json, 图片生成/图生图/QwenEdit白底图生场景_1986276667809288193.json, 图片生成/图生图/Y-Qwen-Image-Edit-2511图像编辑-单图_2003632663460257793.json, 图片生成/图生图/Y-Qwen-Image-Edit-2511图像编辑-多图_2003804106412179457.json, 图片生成/图生图/产品转化白底图自动生成场景 1.0【支持非白底图】_1986063894064091138.json, 图片生成/图生图/电商制作白底图换背景_2002762090655956993.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_104

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/QwenEdit白底图换背景_URL输入_适合API调用_1990309598018064385.json、图片生成/图生图/QwenEdit白底图生场景_1985929695130726402.json、图片生成/图生图/QwenEdit白底图生场景_1986276667809288193.json、图片生成/图生图/Y-Qwen-Image-Edit-2511图像编辑-单图_2003632663460257793.json、图片生成/图生图/Y-Qwen-Image-Edit-2511图像编辑-多图_2003804106412179457.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageResizeKJv2`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 6/7 个有
- `LayerUtility: ImageReelComposit` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `Text Concatenate` —— 5/7 个有
- `easy imageRemBg` —— 5/7 个有
- `ImpactInt` —— 4/7 个有
- `ImpactSwitch` —— 3/7 个有
- `DF_Get_image_size` —— 2/7 个有
- `EmptyLatentImage` —— 2/7 个有
- `SDXL Resolutions (JPS)` —— 2/7 个有
- `FluxKontextImageScale` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LoadImagesFromURL` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 7 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta57 | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，7 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta57，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
