---
name: unknown_workflow_sampler_clip_unet_206
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8775
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX风格迁移，IPadapter_1913766205277306882.json, 图片生成/图生图/Flux Kcontext dev基础工作流_1906247837728821249.json, 图片生成/图生图/Flux Kontext Inpaint_Borges_1970488705611952129.json, 图片生成/图生图/Flux Kontext SingalImage_单图参考_Borges_1970488640340193281.json, 图片生成/图生图/Kontext 人物一致性参考_1970750953735528450.json, 图片生成/图生图/Kontext 单图编辑_1970750981891911681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_206

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX风格迁移，IPadapter_1913766205277306882.json、图片生成/图生图/Flux Kcontext dev基础工作流_1906247837728821249.json、图片生成/图生图/Flux Kontext Inpaint_Borges_1970488705611952129.json、图片生成/图生图/Flux Kontext SingalImage_单图参考_Borges_1970488640340193281.json、图片生成/图生图/Kontext 人物一致性参考_1970750953735528450.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `VAEEncode` —— 5/6 个有
- `EmptyLatentImage` —— 4/6 个有
- `LoadImageFromUrl` —— 4/6 个有
- `Note Plus (mtb)` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `GetImageSize+` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `ApplyIPAdapterFlux` —— 1/6 个有
- `IPAdapterFluxLoader` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `Kontext Inpainting Conditioning` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `ModelSamplingFlux` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `ResizeMask` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1248 | 4 | 91% |
| 高度 | 1024 | 832 - 1536 | 4 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1248，4 个样本，取值集中（一致性 91%）
- 高度 中位数 1024，观测区间 832 - 1536，4 个样本
