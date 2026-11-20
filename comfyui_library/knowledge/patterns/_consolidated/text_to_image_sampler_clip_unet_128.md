---
name: text_to_image_sampler_clip_unet_128
type: Text To Image
frequency: 6
level: strong
coverage: 0.948333
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/中文输入自动扩写flux文生图基础工作流-_1892792029888614402.json, 图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json, 图片生成/文生图/文生图_2042149516085825537.json, 图片生成/文生图/文生图kontext_1950688204880039937.json, 图片生成/文生图/模特选妃 2.0_1921302462970658818.json, 图片生成/文生图/简约风格婚礼留影区设计V1_1904463583671980033.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/中文输入自动扩写flux文生图基础工作流-_1892792029888614402.json、图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json、图片生成/文生图/文生图_2042149516085825537.json、图片生成/文生图/文生图kontext_1950688204880039937.json、图片生成/文生图/模特选妃 2.0_1921302462970658818.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `DifferentialDiffusion` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `PreviewTextNode` —— 1/6 个有
- `RH_OneShot_Prompter` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 6 | 88% |
| 高度 | 1408 | 768 - 1536 | 6 | 77% |
| 采样步数 | 20 | 20 - 26 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，6 个样本，取值集中（一致性 88%）
- 高度 中位数 1408，观测区间 768 - 1536，6 个样本
- 采样步数 中位数 20，观测区间 20 - 26，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
