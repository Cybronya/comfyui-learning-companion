---
name: unknown_workflow_sampler_unet_vae_263
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8288
common_nodes: [CLIPLoader, EmptyLatentImage, KSamplerSelect, ManualSigmas, ResolutionSelector, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json, 图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json, 图片生成/文生图/Qwen_Image_2.1_Turbo_官方8步_文生图_2109357397138567170.json, 图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json, 平台全量/Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_263

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 turbo文生图 画质优化LoRA_2112091031368978433.json、图片生成/文生图/Qwen image 2.1 turbo文生图_2109555458041270273.json、图片生成/文生图/Qwen_Image_2.1_Turbo_官方8步_文生图_2109357397138567170.json、图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json、平台全量/Qwen Image 2.1 Turbo 文生图｜降饱和 LoRA_2119864233625210881.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `ResolutionSelector`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/5 个有
- `TextGenerateLTX2Prompt` —— 4/5 个有
- `SaveImageAdvanced` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `JjkText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
