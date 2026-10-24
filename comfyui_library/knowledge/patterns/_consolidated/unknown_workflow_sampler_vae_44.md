---
name: unknown_workflow_sampler_vae_44
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8435
common_nodes: [ConditioningZeroOut, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型-多图模式_1975849919569375233.json, 图片生成/图生图/Qwen-Image-Edit-2509：告别 “崩图”！人物身份稳、多图融得顺_1970737870178820098.json, 图片生成/图生图/Qwen-Image-Edit_2509单图融合编辑【Nunchaku版】_1971933422384050178.json, 图片生成/图生图/nunchaku-qwen-edit-2509_1972268680992256001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_44

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型-多图模式_1975849919569375233.json、图片生成/图生图/Qwen-Image-Edit-2509：告别 “崩图”！人物身份稳、多图融得顺_1970737870178820098.json、图片生成/图生图/Qwen-Image-Edit_2509单图融合编辑【Nunchaku版】_1971933422384050178.json、图片生成/图生图/nunchaku-qwen-edit-2509_1972268680992256001.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `ConditioningZeroOut`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `easy imageConcat` —— 3/4 个有
- `NunchakuQwenImageDiTLoader` —— 2/4 个有
- `OpenposePreprocessor` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CFGZeroStar` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 4 | 69% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
