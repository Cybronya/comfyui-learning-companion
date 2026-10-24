---
name: text_to_image_sampler_clip_unet_27
type: Text To Image
frequency: 15
level: moderate
coverage: 0.962333
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux文生图工作流_1985633000824217602.json, 图片生成/文生图/Flux文生图工作流（lora）_2004477668261330945.json, 图片生成/文生图/Flux文生图工作流（lora）_2008357145770729474.json, 图片生成/文生图/Flux文生图工作流（lora）_2050168363120381954.json, 图片生成/文生图/Flux文生图工作流（儿童摄影）_1984195134919163905.json, 图片生成/文生图/Flux文生图工作流（儿童摄影）_1990714650645991425.json, 图片生成/文生图/Flux文生图工作流（奇幻背景生成）_1984613779646398466.json, 图片生成/文生图/Flux文生图工作流（带lora版）_2070432527239700481.json, 图片生成/文生图/Flux文生图工作流（萌宠合影）_1984209491019317249.json, 图片生成/文生图/Flux文生图工作流（萌宠合影）_1990715250611806210.json, 图片生成/文生图/SDXL_Flux文生图基础工作流_2005654993942310913.json, 图片生成/文生图/flux-krea文生图（lora）_2005641568893763586.json, 图片生成/文生图/工作流基础篇-4-Flux文生图工作流-带lora_2012502238333243393.json, 图片生成/文生图/沙雕人物专用工作流_2075022505315749889.json, 图片生成/文生图/沙雕动画人物生成_动画制作专用_2011123524311715841.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Flux文生图工作流_1985633000824217602.json、图片生成/文生图/Flux文生图工作流（lora）_2004477668261330945.json、图片生成/文生图/Flux文生图工作流（lora）_2008357145770729474.json、图片生成/文生图/Flux文生图工作流（lora）_2050168363120381954.json、图片生成/文生图/Flux文生图工作流（儿童摄影）_1984195134919163905.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 14/15 个有
- `CLIPTextEncodeFlux` —— 13/15 个有
- `DF_Text_Box` —— 13/15 个有
- `RH_Translator` —— 4/15 个有
- `Image Comparer (rgthree)` —— 3/15 个有
- `CR Text Concatenate` —— 2/15 个有
- `ImpactSwitch` —— 2/15 个有
- `LoadImage` —— 2/15 个有
- `Lora Loader Stack (rgthree)` —— 2/15 个有
- `RH_Captioner` —— 2/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `CheckpointLoaderSimple` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 14 | 84% |
| LoRA 文本强度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 896 | 720 - 1024 | 15 | 85% |
| 高度 | 1024 | 1024 - 1536 | 15 | 87% |
| 采样步数 | 25 | 25 - 30 | 15 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 15 | 34% |
| 采样算法 | dpmpp_2m | - | 15 | 87% |
| 调度器 | sgm_uniform | - | 15 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，14 个样本，取值集中（一致性 84%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 720 - 1024，15 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1536，15 个样本，取值集中（一致性 87%）
- 采样步数 中位数 25，观测区间 25 - 30，15 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，15 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 dpmpp_2m，15 个样本，一致性 87%
- 调度器 最常用 sgm_uniform，15 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
