---
name: unknown_workflow_sampler_clip_unet_314
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95425
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX-标准文生图（灵魂出窍）_1949732974748672001.json, 图片生成/文生图/Flux完整版文生图-在线生图【中文输入】【SirenYi】_1907048220537544706.json, 图片生成/文生图/Flux文生图快速出图版_1896542920525406210.json, 图片生成/文生图/全能图片G-4o卡通3D盲盒生成器_1911385397333585922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_314

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX-标准文生图（灵魂出窍）_1949732974748672001.json、图片生成/文生图/Flux完整版文生图-在线生图【中文输入】【SirenYi】_1907048220537544706.json、图片生成/文生图/Flux文生图快速出图版_1896542920525406210.json、图片生成/文生图/全能图片G-4o卡通3D盲盒生成器_1911385397333585922.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
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
- `TeaCache` —— 3/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `Lora Loader Stack (rgthree)` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `Upscale Model Loader` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 4 | 88% |
| 高度 | 1280 | 1024 - 1536 | 4 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，4 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 1024 - 1536，4 个样本，取值集中（一致性 80%）
