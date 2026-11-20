---
name: unknown_workflow_sampler_unet_vae_249
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6894
common_nodes: [CLIPLoader, EmptyLatentImage, GetNode, KSampler, LoadImage, QwenImage21Cache, SaveImage, SetNode, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json, 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json, 图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json, 图片生成/图生图/啊癫 Qwen Image 2.1多图编辑_2115083447374012418.json, 平台全量/最强换装_2103858547271495681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_249

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json、图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json、图片生成/图生图/【Qwen Image 2.1】图像编辑_2110366155239153666.json、图片生成/图生图/啊癫 Qwen Image 2.1多图编辑_2115083447374012418.json、平台全量/最强换装_2103858547271495681.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 4/5 个有
- `CR Prompt Text` —— 4/5 个有
- `ComfySwitchNode` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `BatchImagesNode` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy setNode` —— 1/5 个有
- `孤海注释` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 50 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 992 - 1600 | 5 | 79% |
| 高度 | 1024 | 1024 - 2400 | 5 | 58% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 50，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 992 - 1600，5 个样本
- 高度 中位数 1024，观测区间 1024 - 2400，5 个样本
