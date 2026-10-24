---
name: text_to_image_controlnet_sampler_clip_21
type: Text To Image
frequency: 3
level: moderate
coverage: 0.850667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, ModelPatchLoader, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image超写实逼真人物生成_2031760767321640962.json, 图片生成/文生图/动作编辑器应用系列之二——Z Image Turbo_2022827863912751105.json, 图片生成/文生图/节点系列12-Image Color Match节点_2013504175904137217.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/z-image超写实逼真人物生成_2031760767321640962.json、图片生成/文生图/动作编辑器应用系列之二——Z Image Turbo_2022827863912751105.json、图片生成/文生图/节点系列12-Image Color Match节点_2013504175904137217.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 720 - 1280 | 3 | 77% |
| 高度 | 1280 | 720 - 1920 | 3 | 62% |
| 采样步数 | 10 | 8 - 16 | 3 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1088，观测区间 720 - 1280，3 个样本
- 高度 中位数 1280，观测区间 720 - 1920，3 个样本
- 采样步数 中位数 10，观测区间 8 - 16，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
