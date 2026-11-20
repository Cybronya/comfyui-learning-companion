---
name: unknown_workflow_sampler_unet_vae_239
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7315
common_nodes: [CLIPLoader, CR Text, EmptyLatentImage, Fast Groups Muter (rgthree), KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, XB_BatchImages, easy boolean, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2102201438289088513.json, 图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2104057908613967874.json, 图片生成/图生图/Qwen-image2.1文生图+图片编辑_2102309777262075906.json, 图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_239

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2102201438289088513.json、图片生成/图生图/Qwen-image2.1文生_图片编辑多合一_2104057908613967874.json、图片生成/图生图/Qwen-image2.1文生图+图片编辑_2102309777262075906.json、图片生成/文生图/Qwen-image2.1文生图_图片编辑多合一_2101867200528347138.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ComfySwitchNode` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImpactConditionalBranch` —— 3/4 个有
- `Any To String (mtb)` —— 1/4 个有
- `ComfySwitchNodeV2` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 25 - 40 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
