---
name: text_to_image_lora_sampler_clip_452
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9615
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【批量提示词】LORA模型测试_2067411590521122818.json, 图片生成/文生图/亚洲人脸 脸模005 美女 模特 电商_1935524742722158593.json, 图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json, 图片生成/文生图/文生图_2042149516085825537.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_452

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/【批量提示词】LORA模型测试_2067411590521122818.json、图片生成/文生图/亚洲人脸 脸模005 美女 模特 电商_1935524742722158593.json、图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json、图片生成/文生图/文生图_2042149516085825537.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `FluxGuidance` —— 2/4 个有
- `LoadImage` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `RebatchLatents` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1536 | 4 | 65% |
| 高度 | 1280 | 512 - 1536 | 4 | 63% |
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1536，4 个样本
- 高度 中位数 1280，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
