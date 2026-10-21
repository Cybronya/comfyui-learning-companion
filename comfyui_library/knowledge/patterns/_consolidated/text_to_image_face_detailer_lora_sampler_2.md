---
name: text_to_image_face_detailer_lora_sampler_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.611
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, FaceDetailer, GetNode, KSampler, Lora Loader Stack (rgthree), SAMLoader, SaveImage, SetNode, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy hiresFix]
problems: []
missing: []
members: [图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json, 图片生成/文生图/illustrious动漫专用 光辉模型文生图工作流 面部细化+画质增强_2086320175250501634.json, 图片生成/文生图/文生图工作流_2086296981193977858.json]
source: knowledge_consolidation
---

# text_to_image_face_detailer_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json、图片生成/文生图/illustrious动漫专用 光辉模型文生图工作流 面部细化+画质增强_2086320175250501634.json、图片生成/文生图/文生图工作流_2086296981193977858.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FaceDetailer`
- `GetNode`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `SAMLoader`
- `SaveImage`
- `SetNode`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy hiresFix`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 3 | 3 - 4 | 3 | 86% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 768 - 1088 | 3 | 83% |
| 高度 | 1536 | 1536 - 2080 | 3 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 4，3 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1088，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1536 - 2080，3 个样本，取值集中（一致性 85%）
