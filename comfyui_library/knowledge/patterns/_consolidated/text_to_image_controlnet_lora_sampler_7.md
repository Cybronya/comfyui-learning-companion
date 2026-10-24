---
name: text_to_image_controlnet_lora_sampler_7
type: Text To Image
frequency: 4
level: strong
coverage: 0.80075
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPTextEncodeFlux, ControlNetApplySD3, ControlNetLoaderAdvanced, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoadImage, LoraLoader, PreviewImage, RH_Translator, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX ControlNet 图生图_1955522992438743042.json, 图片生成/文生图/FLUX 文生图 + ControlNet + 支持中文输入_1942963980317188098.json, 图片生成/文生图/FLUX 文生图 + ControlNet + 支持中文输入_1981592219788427265.json, 图片生成/文生图/FLUX 文生图 + ControlNet + 支持中文输入_2045775166080290818.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX ControlNet 图生图_1955522992438743042.json、图片生成/文生图/FLUX 文生图 + ControlNet + 支持中文输入_1942963980317188098.json、图片生成/文生图/FLUX 文生图 + ControlNet + 支持中文输入_1981592219788427265.json、图片生成/文生图/FLUX 文生图 + ControlNet + 支持中文输入_2045775166080290818.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
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
- `BasicGuider` —— 3/4 个有
- `BasicScheduler` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `RandomNoise` —— 3/4 个有
- `RepeatLatentBatch` —— 3/4 个有
- `SamplerCustomAdvanced` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 928 | 4 | 91% |
| 高度 | 1024 | 1024 - 1232 | 4 | 92% |
| ControlNet 权重 | 0.65 | 0.65 - 0.65 | 4 | 100% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.6 | 0.6 - 1 | 4 | 75% |
| LoRA 文本强度 | 0.6 | 0.6 - 1 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 928，4 个样本，取值集中（一致性 91%）
- 高度 中位数 1024，观测区间 1024 - 1232，4 个样本，取值集中（一致性 92%）
- ControlNet 权重 中位数 0.65，观测区间 0.65 - 0.65，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 1，4 个样本
- LoRA 文本强度 中位数 0.6，观测区间 0.6 - 1，4 个样本
