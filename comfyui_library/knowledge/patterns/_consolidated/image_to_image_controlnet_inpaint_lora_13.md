---
name: image_to_image_controlnet_inpaint_lora_13
type: Image To Image
frequency: 3
level: moderate
coverage: 0.734333
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, GetNode, ImagePadForOutpaint, ImpactInt, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/扩图-qwen image_2085083497538080770.json, 图片生成/图生图/扩图-自定义尺寸-qwen image_2001821111258083330.json, 图片生成/图生图/超强扩图+高清修复 Qwen Image InstanX_2080306694537695233.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/扩图-qwen image_2085083497538080770.json、图片生成/图生图/扩图-自定义尺寸-qwen image_2001821111258083330.json、图片生成/图生图/超强扩图+高清修复 Qwen Image InstanX_2080306694537695233.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `GetNode`
- `ImagePadForOutpaint`
- `ImpactInt`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `Int` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `HYPIRAdvancedRestoration` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageAndMaskPreview` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 24 | 3 | 12% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 24，3 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
