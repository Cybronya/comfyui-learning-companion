---
name: unknown_workflow_lora_sampler_unet_107
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.819833
common_nodes: [Any Switch (rgthree), CLIPLoader, ConditioningZeroOut, Fast Groups Muter (rgthree), FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-Edit——支持多图编辑_2026634164103028738.json, 图片生成/图生图/Jojo—qwen_image_dit_2511-单图、双图、三图自定义工作流_2003723593496338433.json, 图片生成/图生图/Qwen_image_edit_2511-单图、双图、三图自定义工作流（优化版）_2004164393304760321.json, 图片生成/图生图/平面图转效果图_2004092575822848001.json, 图片生成/图生图/景观设计方案图1210_1998608403167608833.json, 图片生成/图生图/规划用地图生成城市设计方案图v3.0_2008523601170931714.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_107

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit——支持多图编辑_2026634164103028738.json、图片生成/图生图/Jojo—qwen_image_dit_2511-单图、双图、三图自定义工作流_2003723593496338433.json、图片生成/图生图/Qwen_image_edit_2511-单图、双图、三图自定义工作流（优化版）_2004164393304760321.json、图片生成/图生图/平面图转效果图_2004092575822848001.json、图片生成/图生图/景观设计方案图1210_1998608403167608833.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/6 个有
- `LayerUtility: ImageReel` —— 4/6 个有
- `LayerUtility: ImageReelComposit` —— 4/6 个有
- `Anything Everywhere3` —— 3/6 个有
- `CR SDXL Aspect Ratio` —— 3/6 个有
- `CropWithPadInfo` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `QwenEditOutputExtractor` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `easy int` —— 3/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/6 个有
- `Int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 2000 | 4 | 27% |
| 高度 | 512 | 512 - 1200 | 4 | 56% |
| 采样步数 | 10 | 8 - 30 | 6 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 34% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 2000，4 个样本，取值分散，一致性仅 27%
- 高度 中位数 512，观测区间 512 - 1200，4 个样本
- 采样步数 中位数 10，观测区间 8 - 30，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
