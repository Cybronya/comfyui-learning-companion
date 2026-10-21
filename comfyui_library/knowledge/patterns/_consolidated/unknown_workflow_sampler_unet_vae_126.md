---
name: unknown_workflow_sampler_unet_vae_126
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.782
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, SaveImageAdvanced, Text Multiline, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerMask: SegmentAnythingUltra V2, Text Multiline, RunningHub SeedXPro Translator]
members: [图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json, 图片生成/图生图/2051831969377468417.json, 图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json, 图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json, 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json, 图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2108014065204424705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_126

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json、图片生成/图生图/2051831969377468417.json、图片生成/文生图/千问image2.1文生图 （创意海报 微小字体不崩坏）_2103398353697595393.json、图片生成/文生图/千问image2.1文生图-中文海报-自动扩写提示词-可以抠图_2103050117644378114.json、图片生成/文生图/千问image2.1文生图_创意海报_微小字体不崩坏_2105577600121921537.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenPERewriteT8` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `忽略多组孤海` —— 5/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `QwenImage21Cache` —— 2/6 个有
- `XinbaoImageStandardizer` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `RunningHub SeedXPro Translator` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 25 | 25 - 25 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: SegmentAnythingUltra V2、Text Multiline、RunningHub SeedXPro Translator
