---
name: unknown_workflow_sampler_clip_unet_191
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.901714
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSamplerAdvanced, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, UNETLoader, VAEDecode, VAELoader, easy promptList]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein-9B-True-V2 生图工作流_2038964016755773441.json, 图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json, 图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json, 图片生成/文生图/VividMuse Z-Image MJ风格_2040326843944931330.json, 图片生成/文生图/VividMuse Z-Image MJ风格_2096074367687024642.json, 图片生成/文生图/VividMuse Z-Image-Turbo-PurpleGrainy_2043272930422956033.json, 图片生成/文生图/Z-Image VS  Qwen Image 2512 VS FLUX2. Klein_2020835344152793089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_191

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein-9B-True-V2 生图工作流_2038964016755773441.json、图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json、图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json、图片生成/文生图/VividMuse Z-Image MJ风格_2040326843944931330.json、图片生成/文生图/VividMuse Z-Image MJ风格_2096074367687024642.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/7 个有
- `Seed (rgthree)` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `SigmasPreview` —— 4/7 个有
- `BasicScheduler` —— 3/7 个有
- `CFGGuider` —— 2/7 个有
- `Flux2Scheduler` —— 2/7 个有
- `KSamplerSelect` —— 2/7 个有
- `RandomNoise` —— 2/7 个有
- `SamplerCustomAdvanced` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 86% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 7 | 71% |
| 宽度 | 1536 | 1024 - 1536 | 7 | 85% |
| 高度 | 2048 | 1536 - 2048 | 7 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 86%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，7 个样本，一致性 71%
- 宽度 中位数 1536，观测区间 1024 - 1536，7 个样本，取值集中（一致性 85%）
- 高度 中位数 2048，观测区间 1536 - 2048，7 个样本，取值集中（一致性 88%）
