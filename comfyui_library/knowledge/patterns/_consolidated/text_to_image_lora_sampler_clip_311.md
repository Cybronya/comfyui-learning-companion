---
name: text_to_image_lora_sampler_clip_311
type: Text To Image
frequency: 3
level: strong
coverage: 0.948667
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【批量提示词】LORA模型测试_2067411590521122818.json, 图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json, 图片生成/文生图/文生图_2042149516085825537.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_311

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【批量提示词】LORA模型测试_2067411590521122818.json、图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json、图片生成/文生图/文生图_2042149516085825537.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 2/3 个有
- `FluxGuidance` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RebatchLatents` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1536 | 3 | 80% |
| 高度 | 1536 | 1024 - 1536 | 3 | 82% |
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1536，3 个样本
- 高度 中位数 1536，观测区间 1024 - 1536，3 个样本，取值集中（一致性 82%）
- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
