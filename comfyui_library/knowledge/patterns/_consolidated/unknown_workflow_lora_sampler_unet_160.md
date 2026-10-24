---
name: unknown_workflow_lora_sampler_unet_160
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.75225
common_nodes: [CLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-EDIT-过人脸_2046465672477155329.json, 图片生成/图生图/FireRed-Image-Edit-角色视图排版_2046480664115027969.json, 图片生成/图生图/即梦真人画风图片处理_2047285042627485698.json, 图片生成/图生图/第一步：智能服装提取 (Outfit Transfer)_1990304299924246530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_160

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-EDIT-过人脸_2046465672477155329.json、图片生成/图生图/FireRed-Image-Edit-角色视图排版_2046480664115027969.json、图片生成/图生图/即梦真人画风图片处理_2047285042627485698.json、图片生成/图生图/第一步：智能服装提取 (Outfit Transfer)_1990304299924246530.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `CustomAddLabel` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 1.5 | 4 | 84% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1500 | 1024 - 1920 | 4 | 71% |
| 高度 | 1080 | 1024 - 1920 | 4 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 1.5，4 个样本，取值集中（一致性 84%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1500，观测区间 1024 - 1920，4 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，4 个样本
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
