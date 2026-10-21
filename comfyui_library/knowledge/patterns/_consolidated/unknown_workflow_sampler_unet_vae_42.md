---
name: unknown_workflow_sampler_unet_vae_42
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.757
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenPERewriteT8, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, easy cleanGpuUsed, CR Prompt Text]
members: [图片生成/图生图/2102719060134940673.json, 图片生成/图生图/2102935036923310081.json, 图片生成/图生图/2102952588135194626.json, 图片生成/图生图/2103026012618584066.json, 图片生成/图生图/2103518802859352065.json, 图片生成/图生图/2105844300620853250.json, 图片生成/图生图/2106042591421747201.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图2609_2106042102424629249.json, 图片生成/文生图/Qwen Image 2.1 PE 文生图_2102653627042189314.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（优化版）_2103650787716059138.json, 图片生成/文生图/（稳定加速版+Tao）Qwen+Image+2.1+PE+文生图（图生图编辑版）_2103658795657424897.json, 图片生成/文生图/（稳定加速版）Qwen Image 2.1 PE 文生图_2102956400250023938.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_42

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2102719060134940673.json、图片生成/图生图/2102935036923310081.json、图片生成/图生图/2102952588135194626.json、图片生成/图生图/2103026012618584066.json、图片生成/图生图/2103518802859352065.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenPERewriteT8`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 11/12 个有
- `QwenImage21Cache` —— 10/12 个有
- `ResolutionSelector` —— 10/12 个有
- `LoadImage` —— 8/12 个有
- `ColorMatch` —— 2/12 个有
- `GrowMaskWithBlur` —— 2/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `LayerUtility: CropByMask V2` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `LayerUtility: ImageScaleRestore V2` —— 2/12 个有
- `LayerUtility: RestoreCropBox` —— 2/12 个有
- `AIO_Preprocessor` —— 1/12 个有
- `ConcatTextOfUtils` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |
| 采样步数 | 40 | 4 - 40 | 12 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 4 - 40，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: CropByMask V2、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: ImageScaleRestore V2、LayerUtility: RestoreCropBox、easy cleanGpuUsed
