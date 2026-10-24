---
name: unknown_workflow_sampler_unet_vae_269
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.895
common_nodes: [ConditioningZeroOut, DualCLIPLoader, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json, 图片生成/文生图/JoyCaption_Beta-one 最强图像反推神器_1948653855824326658.json, 图片生成/文生图/flux krea 加 joy caption 3_1951269472583798786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_269

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json、图片生成/文生图/JoyCaption_Beta-one 最强图像反推神器_1948653855824326658.json、图片生成/文生图/flux krea 加 joy caption 3_1951269472583798786.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `SDXL Empty Latent Image (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 28 | 3 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 28，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
