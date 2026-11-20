---
name: unknown_workflow_inpaint_sampler_unet_6
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936
common_nodes: [CLIPLoader, Image Comparer (rgthree), InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561.json, 图片生成/图生图/Qwen_Rapid_局部重绘_2017588748258643969.json, 图片生成/图生图/蒙版重绘贴图替换（双图）_2024117929792507906.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561.json、图片生成/图生图/Qwen_Rapid_局部重绘_2017588748258643969.json、图片生成/图生图/蒙版重绘贴图替换（双图）_2024117929792507906.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MaskBlur+` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `TextEncodeQwenImage21` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
