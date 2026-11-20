---
name: text_to_image_controlnet_sampler_clip_10
type: Text To Image
frequency: 5
level: strong
coverage: 1
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/19.tonnie-SD1.5老照片修复_1997627618528833537.json, 图片生成/图生图/SD1.5控制图片_2000762731127074817.json, 图片生成/图生图/绘画风格转换（水彩）_1977998649215123457.json, 图片生成/图生图/绘画风格转换（综合 油画）_2033381081344380929.json, 图片生成/图生图/绘画风格转换（综合 油画）_2113174659905703938.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/19.tonnie-SD1.5老照片修复_1997627618528833537.json、图片生成/图生图/SD1.5控制图片_2000762731127074817.json、图片生成/图生图/绘画风格转换（水彩）_1977998649215123457.json、图片生成/图生图/绘画风格转换（综合 油画）_2033381081344380929.json、图片生成/图生图/绘画风格转换（综合 油画）_2113174659905703938.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
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
- `IPAdapterUnifiedLoader` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `IPAdapterMS` —— 3/5 个有
- `ImageResizeKJ` —— 3/5 个有
- `StringFunction|pysssss` —— 3/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `IPAdapterFaceID` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 1 | 5 | 82% |
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |
| 采样步数 | 17 | 17 - 20 | 5 | 92% |
| Prompt 约束强度(CFG) | 6.21 | 6.21 - 8 | 5 | 87% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 1，5 个样本，取值集中（一致性 82%）
- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 17，观测区间 17 - 20，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 6.21，观测区间 6.21 - 8，5 个样本，取值集中（一致性 87%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
