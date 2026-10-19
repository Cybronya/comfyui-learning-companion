---
name: unknown_workflow_sampler_unet_vae_95
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.745857
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Note Plus (mtb)]
members: [图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json, 图片生成/图生图/2101852516261646337.json, 图片生成/图生图/2101933499191222274.json, 图片生成/图生图/2102150751400316930.json, 图片生成/图生图/2102152565902368769.json, 图片生成/图生图/2102179241923272706.json, 图片生成/文生图/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_95

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json、图片生成/图生图/2101852516261646337.json、图片生成/图生图/2101933499191222274.json、图片生成/图生图/2102150751400316930.json、图片生成/图生图/2102152565902368769.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `Note Plus (mtb)` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `PreviewAny` —— 2/7 个有
- `TextGenerate` —— 2/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `RHLLMChatNode` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有
- `ZNGB_ImageBatchMulti` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 25 | 25 - 50 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)
