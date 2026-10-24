---
name: text_to_image_sampler_clip_unet_113
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9215
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-kera文生图基础工作流_1951153128769040386.json, 图片生成/文生图/FLUX-新_1981699548944965633.json, 图片生成/文生图/Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513.json, 图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json, 图片生成/文生图/Flux.1-Krea-Dev文生图_1951218791621570562.json, 图片生成/文生图/Flux.1Krea文生图_1951794471434399745.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/FLUX-kera文生图基础工作流_1951153128769040386.json、图片生成/文生图/FLUX-新_1981699548944965633.json、图片生成/文生图/Flux.1 Krea Dev：文生图王者，独特美学，细节拉满！去除AI感_真实感摄影_1951065960218304513.json、图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json、图片生成/文生图/Flux.1-Krea-Dev文生图_1951218791621570562.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

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
- `ConditioningZeroOut` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `Text Multiline` —— 4/6 个有
- `easy showAnything` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `ApplyFBCacheAndSkipBlocks` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1080 | 6 | 79% |
| 高度 | 1280 | 768 - 1920 | 6 | 66% |
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 6 | 68% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1080，6 个样本
- 高度 中位数 1280，观测区间 768 - 1920，6 个样本
- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
