---
name: unknown_workflow_sampler_clip_unet_378
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.988
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/空白工作流_1951072076297908225.json, 平台全量/Z-Image_turbo工作流_2067072746533777410.json, 平台全量/krea写实_1953305947642990594.json, 平台全量/创意形象_多图参考_脑洞创意_1894577543356284929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_378

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/空白工作流_1951072076297908225.json、平台全量/Z-Image_turbo工作流_2067072746533777410.json、平台全量/krea写实_1953305947642990594.json、平台全量/创意形象_多图参考_脑洞创意_1894577543356284929.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CFGZeroStarAndInit` —— 1/4 个有
- `CLIPLoader` —— 1/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `ReduxAdvanced` —— 1/4 个有
- `StyleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | 20 - 60 | 4 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 29，观测区间 20 - 60，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
