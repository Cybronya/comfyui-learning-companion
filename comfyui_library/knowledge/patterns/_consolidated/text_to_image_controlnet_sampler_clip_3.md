---
name: text_to_image_controlnet_sampler_clip_3
type: Text To Image
frequency: 3
level: moderate
coverage: 0.913
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: [CR Text Input Switch, WD14Tagger|pysssss]
members: [图片生成/文生图/1933484061358739458.json, 图片生成/文生图/1935521735636877314.json, 图片生成/文生图/拍同款姿势（文生图）_1846060559706767361.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1933484061358739458.json、图片生成/文生图/1935521735636877314.json、图片生成/文生图/拍同款姿势（文生图）_1846060559706767361.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch` —— 1/3 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/3 个有
- `JWString` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有
- `WD14Tagger|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1024 | 512 - 1536 | 3 | 59% |
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 3 | 88% |
| 采样算法 | dpmpp_2m | - | 3 | 33% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 0.3 - 1 | 3 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1536，3 个样本
- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，3 个样本，取值集中（一致性 88%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 33%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.3 - 1，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Input Switch、WD14Tagger|pysssss
