---
name: text_to_image_face_detailer_lora_sampler
type: Text To Image
frequency: 8
level: strong
coverage: 0.600125
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, FaceDetailer, KSampler, Lora Loader Stack (rgthree), SAMLoader, SaveImage, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy hiresFix]
problems: []
missing: []
members: [图片生成/文生图/CG幻想二次元专属文生图+全节点注释_2039708830812086274.json, 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458.json, 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2049034720654135298.json, 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json, 图片生成/文生图/illustrious动漫专用 光辉模型文生图工作流 面部细化+画质增强_2086320175250501634.json, 图片生成/文生图/illustrious动漫专用文生图 面部细化+画质增强_2039638144642977793.json, 图片生成/文生图/文生图工作流_2086296981193977858.json, 图片生成/文生图/文生图面部细化+四张任选Smooth Workflow v4.0_2041356827237027842.json]
source: knowledge_consolidation
---

# text_to_image_face_detailer_lora_sampler

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/CG幻想二次元专属文生图+全节点注释_2039708830812086274.json、图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458.json、图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2049034720654135298.json、图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json、图片生成/文生图/illustrious动漫专用 光辉模型文生图工作流 面部细化+画质增强_2086320175250501634.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FaceDetailer`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy hiresFix`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `Label (rgthree)` —— 4/8 个有
- `RH_Translator` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 8 | 81% |
| Prompt 约束强度(CFG) | 4 | 3 - 4 | 8 | 88% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1088 | 768 - 1088 | 8 | 86% |
| 高度 | 2080 | 1536 - 2080 | 8 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，8 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 3 - 4，8 个样本，取值集中（一致性 88%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1088，观测区间 768 - 1088，8 个样本，取值集中（一致性 86%）
- 高度 中位数 2080，观测区间 1536 - 2080，8 个样本，取值集中（一致性 88%）
