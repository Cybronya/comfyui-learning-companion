---
name: unknown_workflow_sampler_clip_unet_87
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.892818
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Beyond Reality Z-image人像写真文生图V1_2003169101386252290.json, 图片生成/文生图/Beyond Reality Z-image超现实人像写真文生图_2004848724062994434.json, 图片生成/文生图/DG_基础Zimage文生图+增强随机性_2011606529237065730.json, 图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json, 图片生成/文生图/Krea2-turbo新模型真实人像_2071435896448184322.json, 图片生成/文生图/VividMuse Krea2真实人像V1_2071177424569720833.json, 图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json, 图片生成/文生图/VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257.json, 图片生成/文生图/VividMuse Z-Image家族模型大对比(2)_2034289450481623041.json, 图片生成/文生图/VividMuse Z-Image家族模型大对比_2021580062834827265.json, 图片生成/文生图/Z-Image-turbo Qwen3 4B Engineer V4和Flow-DPO比对_2028451786385793026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Beyond Reality Z-image人像写真文生图V1_2003169101386252290.json、图片生成/文生图/Beyond Reality Z-image超现实人像写真文生图_2004848724062994434.json、图片生成/文生图/DG_基础Zimage文生图+增强随机性_2011606529237065730.json、图片生成/文生图/Krea2 动画人物文生图_2090097765106933761.json、图片生成/文生图/Krea2-turbo新模型真实人像_2071435896448184322.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `easy promptList` —— 7/11 个有
- `LayerUtility: ImageReel` —— 4/11 个有
- `LayerUtility: ImageReelComposit` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `Seed (rgthree)` —— 4/11 个有
- `DF_Text_Box` —— 3/11 个有
- `PrimitiveInt` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `GetNode` —— 2/11 个有
- `ResolutionSelector` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `CLIPLoaderGGUF` —— 1/11 个有
- `CheckpointLoaderSimple` —— 1/11 个有
- `Saturation` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 512 - 1536 | 11 | 63% |
| 高度 | 1920 | 512 - 2048 | 11 | 63% |
| 采样步数 | fixed | - | 11 | 55% |
| Prompt 约束强度(CFG) | 8 | 8 - 15 | 11 | 72% |
| 采样算法 | 1 | 1 - 2 | 11 | 67% |
| 调度器 | euler | - | 11 | 55% |
| 重绘幅度 | simple | - | 11 | 45% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 512 - 1536，11 个样本
- 高度 中位数 1920，观测区间 512 - 2048，11 个样本
- 采样步数 最常用 fixed，11 个样本，一致性 55%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 15，11 个样本
- 采样算法 中位数 1，观测区间 1 - 2，11 个样本
- 调度器 最常用 euler，11 个样本，一致性 55%
- 重绘幅度 最常用 simple，11 个样本，一致性 45%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
