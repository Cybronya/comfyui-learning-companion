---
name: unknown_workflow_sampler_unet_vae_181
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.592
common_nodes: [CLIPLoader, CR Text, EmptyLatentImage, Fast Groups Muter (rgthree), KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, XB_BatchImages, easy boolean, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: [CR Text, easy boolean, easy cleanGpuUsed]
members: [图片生成/图生图/2102201438289088513.json, 图片生成/图生图/2102309777262075906.json, 图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2102201438289088513.json、图片生成/图生图/2102309777262075906.json、图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XB_BatchImages`
- `easy boolean`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImpactConditionalBranch` —— 2/3 个有
- `Any To String (mtb)` —— 1/3 个有
- `ComfySwitchNodeV2` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 40 | 3 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy boolean、easy cleanGpuUsed
