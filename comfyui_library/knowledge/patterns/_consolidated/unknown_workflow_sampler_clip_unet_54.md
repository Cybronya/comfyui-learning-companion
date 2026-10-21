---
name: unknown_workflow_sampler_clip_unet_54
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8782
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Beyond Reality Z-image人像写真文生图V1_2003169101386252290.json, 图片生成/文生图/Beyond Reality Z-image超现实人像写真文生图_2004848724062994434.json, 图片生成/文生图/DG_基础Zimage文生图+增强随机性_2011606529237065730.json, 图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json, 图片生成/文生图/Krea2-turbo新模型真实人像_2071435896448184322.json, 图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json, 图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json, 图片生成/文生图/VividMuse Krea2真实人像V1_2071177424569720833.json, 图片生成/文生图/VividMuse Z-Image MJ风格_2096074367687024642.json, 图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Beyond Reality Z-image人像写真文生图V1_2003169101386252290.json、图片生成/文生图/Beyond Reality Z-image超现实人像写真文生图_2004848724062994434.json、图片生成/文生图/DG_基础Zimage文生图+增强随机性_2011606529237065730.json、图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json、图片生成/文生图/Krea2-turbo新模型真实人像_2071435896448184322.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `easy promptList` —— 6/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `LayerUtility: ImageReel` —— 4/10 个有
- `LayerUtility: ImageReelComposit` —— 4/10 个有
- `CR Prompt Text` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `ResolutionSelector` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `BasicScheduler` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SigmasPreview` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1116 | 512 - 1536 | 10 | 63% |
| 高度 | 1800 | 512 - 2048 | 10 | 61% |
| 采样步数 | fixed | - | 10 | 60% |
| Prompt 约束强度(CFG) | 8 | 8 - 15 | 10 | 71% |
| 采样算法 | 1 | 1 - 2 | 10 | 67% |
| 调度器 | euler | - | 10 | 60% |
| 重绘幅度 | simple | - | 10 | 30% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1116，观测区间 512 - 1536，10 个样本
- 高度 中位数 1800，观测区间 512 - 2048，10 个样本
- 采样步数 最常用 fixed，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 15，10 个样本
- 采样算法 中位数 1，观测区间 1 - 2，10 个样本
- 调度器 最常用 euler，10 个样本，一致性 60%
- 重绘幅度 最常用 simple，10 个样本，一致性 30%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
