---
name: unknown_workflow_sampler_unet_vae_93
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.892375
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, Lora Loader Stack (rgthree), Upscale Model Loader, CR Text Concatenate]
members: [图片生成/文生图/1911385397333585922.json, 图片生成/文生图/1911723649815015426.json, 图片生成/文生图/1911771666933055489.json, 图片生成/文生图/1915288629995048961.json, 图片生成/文生图/1938572723696099330.json, 图片生成/文生图/1945170907587596289.json, 图片生成/文生图/1946922717151158273.json, 图片生成/文生图/1949732974748672001.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1911385397333585922.json、图片生成/文生图/1911723649815015426.json、图片生成/文生图/1911771666933055489.json、图片生成/文生图/1915288629995048961.json、图片生成/文生图/1938572723696099330.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/8 个有
- `CLIPTextEncodeFlux` —— 5/8 个有
- `SeargePromptCombiner` —— 4/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `Lora Loader Stack (rgthree)` —— 2/8 个有
- `TeaCache` —— 2/8 个有
- `Upscale Model Loader` —— 2/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `TextInput_` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1024 | 8 | 89% |
| 高度 | 1024 | 1024 - 1536 | 8 | 84% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 6 | 89% |
| LoRA 文本强度 | 1 | 0 - 1 | 6 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1024，8 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 1024 - 1536，8 个样本，取值集中（一致性 84%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，6 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 0 - 1，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、Lora Loader Stack (rgthree)、Upscale Model Loader、CR Text Concatenate
