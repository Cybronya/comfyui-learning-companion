---
name: unknown_workflow_lora_sampler_unet_171
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7465
common_nodes: [Anything Everywhere3, CLIPLoader, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, RHLLMChatNode, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: []
missing: []
members: [图片生成/图生图/Qwen image2.1人物写真套图工作流_2111294327686254593.json, 图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2108914820471939073.json, 图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2114184947660582914.json, 图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2114206742853808130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_171

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1人物写真套图工作流_2111294327686254593.json、图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2108914820471939073.json、图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2114184947660582914.json、图片生成/图生图/Qwenimage2.1漫转真+换头+写真_2114206742853808130.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RHLLMChatNode`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `RH_DLSS5Enhance` —— 1/4 个有
- `VOSR2ModelLoader` —— 1/4 个有
- `VOSR2Upscale` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
