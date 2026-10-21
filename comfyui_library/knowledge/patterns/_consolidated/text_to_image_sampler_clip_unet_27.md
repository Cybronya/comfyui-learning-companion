---
name: text_to_image_sampler_clip_unet_27
type: Text To Image
frequency: 12
level: moderate
coverage: 0.96725
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Lora Loader Stack (rgthree)]
members: [图片生成/文生图/1985633000824217602.json, 图片生成/文生图/Flux文生图工作流（lora）_2004477668261330945.json, 图片生成/文生图/Flux文生图工作流（lora）_2008357145770729474.json, 图片生成/文生图/Flux文生图工作流（儿童摄影）_1990714650645991425.json, 图片生成/文生图/Flux文生图工作流（带lora版）_2070432527239700481.json, 图片生成/文生图/Flux文生图工作流（带lora版）_2084186114449043458.json, 图片生成/文生图/Flux文生图工作流（萌宠合影）_1990715250611806210.json, 图片生成/文生图/SDXL_Flux文生图基础工作流_2005654993942310913.json, 图片生成/文生图/flux-krea文生图（lora）_2005641568893763586.json, 图片生成/文生图/工作流基础篇-4-Flux文生图工作流-带lora_2012502238333243393.json, 图片生成/文生图/沙雕人物专用工作流_2075022505315749889.json, 图片生成/文生图/沙雕动画人物生成_动画制作专用_2011123524311715841.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1985633000824217602.json、图片生成/文生图/Flux文生图工作流（lora）_2004477668261330945.json、图片生成/文生图/Flux文生图工作流（lora）_2008357145770729474.json、图片生成/文生图/Flux文生图工作流（儿童摄影）_1990714650645991425.json、图片生成/文生图/Flux文生图工作流（带lora版）_2070432527239700481.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 10/12 个有
- `DF_Text_Box` —— 10/12 个有
- `LoraLoader` —— 10/12 个有
- `RH_Translator` —— 4/12 个有
- `CR Text Concatenate` —— 2/12 个有
- `ImpactSwitch` —— 2/12 个有
- `LoadImage` —— 2/12 个有
- `Lora Loader Stack (rgthree)` —— 2/12 个有
- `RH_Captioner` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `CheckpointLoaderSimple` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 10 | 85% |
| LoRA 文本强度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 768 | 720 - 1024 | 12 | 84% |
| 高度 | 1024 | 1024 - 1280 | 12 | 93% |
| 采样步数 | 25 | 25 - 30 | 12 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 12 | 33% |
| 采样算法 | dpmpp_2m | - | 12 | 83% |
| 调度器 | sgm_uniform | - | 12 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，10 个样本，取值集中（一致性 85%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1024，12 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 1024 - 1280，12 个样本，取值集中（一致性 93%）
- 采样步数 中位数 25，观测区间 25 - 30，12 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 dpmpp_2m，12 个样本，一致性 83%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Lora Loader Stack (rgthree)
