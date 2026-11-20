---
name: text_to_image_sampler_clip_unet_36
type: Text To Image
frequency: 14
level: moderate
coverage: 0.982214
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux文生图工作流_1985633000824217602.json, 图片生成/文生图/Flux文生图工作流（lora）_2004477668261330945.json, 图片生成/文生图/Flux文生图工作流（lora）_2008357145770729474.json, 图片生成/文生图/Flux文生图工作流（lora）_2050168363120381954.json, 图片生成/文生图/Flux文生图工作流（儿童摄影）_1984195134919163905.json, 图片生成/文生图/Flux文生图工作流（儿童摄影）_1990714650645991425.json, 图片生成/文生图/Flux文生图工作流（奇幻背景生成）_1984613779646398466.json, 图片生成/文生图/Flux文生图工作流（带lora版）_2070432527239700481.json, 图片生成/文生图/Flux文生图工作流（带lora版）_2084186114449043458.json, 图片生成/文生图/Flux文生图工作流（萌宠合影）_1984209491019317249.json, 图片生成/文生图/Flux文生图工作流（萌宠合影）_1990715250611806210.json, 图片生成/文生图/SDXL_Flux文生图基础工作流_2005654993942310913.json, 图片生成/文生图/flux-krea文生图（lora）_2005641568893763586.json, 图片生成/文生图/工作流基础篇-4-Flux文生图工作流-带lora_2012502238333243393.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Flux文生图工作流_1985633000824217602.json、图片生成/文生图/Flux文生图工作流（lora）_2004477668261330945.json、图片生成/文生图/Flux文生图工作流（lora）_2008357145770729474.json、图片生成/文生图/Flux文生图工作流（lora）_2050168363120381954.json、图片生成/文生图/Flux文生图工作流（儿童摄影）_1984195134919163905.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 12/14 个有
- `DF_Text_Box` —— 12/14 个有
- `LoraLoader` —— 12/14 个有
- `Image Comparer (rgthree)` —— 3/14 个有
- `Lora Loader Stack (rgthree)` —— 2/14 个有
- `RH_Translator` —— 2/14 个有
- `CheckpointLoaderSimple` —— 1/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 12 | 83% |
| LoRA 文本强度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 960 | 720 - 1024 | 14 | 87% |
| 高度 | 1024 | 1024 - 1536 | 14 | 87% |
| 采样步数 | 25 | 25 - 30 | 14 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 14 | 34% |
| 采样算法 | dpmpp_2m | - | 14 | 100% |
| 调度器 | sgm_uniform | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，12 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 960，观测区间 720 - 1024，14 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1536，14 个样本，取值集中（一致性 87%）
- 采样步数 中位数 25，观测区间 25 - 30，14 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 dpmpp_2m，14 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
