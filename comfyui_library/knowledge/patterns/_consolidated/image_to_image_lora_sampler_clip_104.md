---
name: image_to_image_lora_sampler_clip_104
type: Image To Image
frequency: 4
level: moderate
coverage: 0.769
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json, 图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json, 图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json, 平台全量/人物姿态迁移qwen版_1957991475625734146.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-lmage-CN 深度_线稿_软边缘_姿态等多种控制_Diffsynth_lora版_1962447068671381506.json、图片生成/文生图/controlnet—千问教学工作流_1994239870906417154.json、图片生成/文生图/qwen-毛坯房一键精装图_1994410356925665282.json、平台全量/人物姿态迁移qwen版_1957991475625734146.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `DWPreprocessor` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `SetUnionControlNetType` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Conditioning Input Switch` —— 1/4 个有
- `CR Image Input Switch (4 way)` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 20 | 4 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.8 | 0.75 - 1.8 | 3 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 20，4 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.75 - 1.8，3 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
