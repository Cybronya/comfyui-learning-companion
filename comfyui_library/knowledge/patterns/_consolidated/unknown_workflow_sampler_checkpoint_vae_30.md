---
name: unknown_workflow_sampler_checkpoint_vae_30
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8985
common_nodes: [CR Text, CheckpointLoaderSimple, EmptyLatentImage, Fast Bypasser (rgthree), ImageConcanate, ImageConcatMulti, ImageScaleToTotalPixels, ImpactSwitch, KSampler, LoadImage, ModelSamplingAuraFlow, Mute / Bypass Repeater (rgthree), SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Remix-AIO-批图_2045570507235397633.json, 图片生成/图生图/🥯千问Edit-Rapid-AIO-v5 金总补习班优化版🥯_1979349762338099202.json, 平台全量/全能图片V1 大香蕉平替千问Edit-Rapid-AIO-v5 图片编辑流_1986213318979440641.json, 平台全量/超稳定 超快 的服装替换+融合 可本地部署_1987751918837673986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Remix-AIO-批图_2045570507235397633.json、图片生成/图生图/🥯千问Edit-Rapid-AIO-v5 金总补习班优化版🥯_1979349762338099202.json、平台全量/全能图片V1 大香蕉平替千问Edit-Rapid-AIO-v5 图片编辑流_1986213318979440641.json、平台全量/超稳定 超快 的服装替换+融合 可本地部署_1987751918837673986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `Mute / Bypass Repeater (rgthree)`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `DF_Float` —— 1/4 个有
- `HAIGC_LoadImagesFromZip` —— 1/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `easy imageScaleDownBy` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 796 | 512 - 1080 | 4 | 64% |
| 高度 | 976 | 512 - 1440 | 4 | 52% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 796，观测区间 512 - 1080，4 个样本
- 高度 中位数 976，观测区间 512 - 1440，4 个样本
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
