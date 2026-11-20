---
name: unknown_workflow_inpaint_sampler_clip_12
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.909571
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ACE++一致性人物生成_1911028207112417282.json, 图片生成/图生图/Fill One - reward扩图工作流_2101586412402466817.json, 图片生成/图生图/Fill-OneReward局部重绘_1966039985273171969.json, 图片生成/图生图/Fill-OneReward扩图工作流_1966111199823826945.json, 图片生成/图生图/Fill-OneReward物体擦除工作流_1966081797090086914.json, 图片生成/图生图/OneReward 局部重绘_1967635377592950785.json, 图片生成/图生图/OneReward 物体擦除_1967620723143577601.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/ACE++一致性人物生成_1911028207112417282.json、图片生成/图生图/Fill One - reward扩图工作流_2101586412402466817.json、图片生成/图生图/Fill-OneReward局部重绘_1966039985273171969.json、图片生成/图生图/Fill-OneReward扩图工作流_1966111199823826945.json、图片生成/图生图/Fill-OneReward物体擦除工作流_1966081797090086914.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 6/7 个有
- `ImageAndMaskPreview` —— 5/7 个有
- `LayerUtility: ImageReel` —— 5/7 个有
- `LayerUtility: ImageReelComposit` —— 5/7 个有
- `RH_Translator` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `ImagePadForOutpaint` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `EnhancedLoadDiffusionModel` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `LayerMask: MaskGrow` —— 1/7 个有
- `LayerUtility: CropByMask V3` —— 1/7 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/7 个有
- `LayerUtility: RestoreCropBox` —— 1/7 个有
- `easy imageSizeByLongerSide` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
