---
name: unknown_workflow_upscale_lora_sampler_31
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.924167
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RH_Captioner, RandomNoise, SDXLPromptStyler, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/FLUX IPA+CN 双控制（推荐depth）_1937433850614063106.json, 图片生成/图生图/FLUX Krea + IPAdaper 风格迁移_1951157890688200706.json, 图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json, 图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Redux+Flux风格迁移_1945027298695499777.json, 图片生成/图生图/毛坯房装修迁移（Redux(最强512版)+CN Union Pro双控制（推荐depth）_1937485598129328130.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX IPA+CN 双控制（推荐depth）_1937433850614063106.json、图片生成/图生图/FLUX Krea + IPAdaper 风格迁移_1951157890688200706.json、图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json、图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json、图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Redux+Flux风格迁移_1945027298695499777.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SDXLPromptStyler`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/6 个有
- `ControlNetApplyAdvanced` —— 4/6 个有
- `ControlNetLoader` —— 4/6 个有
- `DF_Get_image_size` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageMirror` —— 4/6 个有
- `ImageResize` —— 4/6 个有
- `SetUnionControlNetType` —— 4/6 个有
- `VAEEncode` —— 4/6 个有
- `ApplyIPAdapterFlux` —— 3/6 个有
- `GetImageSize+` —— 3/6 个有
- `IPAdapterFluxLoader` —— 3/6 个有
- `MirroredImage` —— 3/6 个有
- `ModelSamplingFlux` —— 3/6 个有
- `ShowText` —— 3/6 个有
- `StyleModelLoader` —— 3/6 个有
- `CLIPVisionLoader` —— 2/6 个有
- `CombinationText` —— 2/6 个有
- `DetailDaemonSamplerNode` —— 2/6 个有
- `ReduxAdvanced` —— 2/6 个有
- `AdvancedVisionLoader` —— 1/6 个有
- `Anything Everywhere` —— 1/6 个有
- `CFGGuider` —— 1/6 个有
- `CLIPLoader` —— 1/6 个有
- `CLIPVisionEncode` —— 1/6 个有
- `DisableNoise` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `SplitSigmas` —— 1/6 个有
- `StyleModelApply` —— 1/6 个有
- `WanVideoNAG` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| ControlNet 权重 | 0.675 | 0.65 - 0.75 | 4 | 94% |
| LoRA 模型强度 | 0.45 | 0 - 0.8 | 6 | 39% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.675，观测区间 0.65 - 0.75，4 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 0.45，观测区间 0 - 0.8，6 个样本，取值分散，一致性仅 39%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
