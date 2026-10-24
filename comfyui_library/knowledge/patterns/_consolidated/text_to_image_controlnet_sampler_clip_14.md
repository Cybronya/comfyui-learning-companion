---
name: text_to_image_controlnet_sampler_clip_14
type: Text To Image
frequency: 4
level: moderate
coverage: 0.92875
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/实景真人转二次元动漫风格_2007784967413178369.json, 图片生成/文生图/ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137.json, 图片生成/文生图/ComfyUi-深度控制生图工作流_1935521735636877314.json, 图片生成/文生图/一键古画变真人 工作流V1_1933484061358739458.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/实景真人转二次元动漫风格_2007784967413178369.json、图片生成/文生图/ComfyUI官方示例9：深度控制ControlNet工作流 _ ComfyUI从入门到精通_1932442202058715137.json、图片生成/文生图/ComfyUi-深度控制生图工作流_1935521735636877314.json、图片生成/文生图/一键古画变真人 工作流V1_1933484061358739458.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WD14Tagger|pysssss` —— 2/4 个有
- `CR Text Input Switch` —— 1/4 个有
- `CannyEdgePreprocessor` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `JWString` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | 0.3 - 1 | 4 | 56% |
| 采样步数 | 20.5 | 20 - 30 | 4 | 82% |
| Prompt 约束强度(CFG) | 6.5 | 4 - 7 | 4 | 80% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 904 - 1024 | 4 | 95% |
| 高度 | 1024 | 600 - 1536 | 4 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.75，观测区间 0.3 - 1，4 个样本
- 采样步数 中位数 20.5，观测区间 20 - 30，4 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 4 - 7，4 个样本
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 904 - 1024，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1024，观测区间 600 - 1536，4 个样本
