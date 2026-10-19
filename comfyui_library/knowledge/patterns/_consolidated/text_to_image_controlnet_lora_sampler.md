---
name: text_to_image_controlnet_lora_sampler
type: Text To Image
frequency: 3
level: strong
coverage: 0.802667
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPTextEncodeFlux, ControlNetApplySD3, ControlNetLoaderAdvanced, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoadImage, LoraLoader, PreviewImage, RH_Translator, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1942963980317188098.json, 图片生成/文生图/1955522992438743042.json, 图片生成/文生图/1981592219788427265.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1942963980317188098.json、图片生成/文生图/1955522992438743042.json、图片生成/文生图/1981592219788427265.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ControlNetApplySD3`
- `ControlNetLoaderAdvanced`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `RepeatLatentBatch` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 928 | 3 | 91% |
| 高度 | 1024 | 1024 - 1232 | 3 | 91% |
| ControlNet 权重 | 0.65 | 0.65 - 0.65 | 3 | 100% |
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 3 | 74% |
| LoRA 文本强度 | 0.6 | 0.6 - 1 | 3 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 928，3 个样本，取值集中（一致性 91%）
- 高度 中位数 1024，观测区间 1024 - 1232，3 个样本，取值集中（一致性 91%）
- ControlNet 权重 中位数 0.65，观测区间 0.65 - 0.65，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 0.6，观测区间 0.6 - 1，3 个样本
