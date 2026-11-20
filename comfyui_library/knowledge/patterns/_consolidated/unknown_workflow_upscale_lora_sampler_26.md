---
name: unknown_workflow_upscale_lora_sampler_26
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.923125
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RH_Captioner, RandomNoise, SDXLPromptStyler, SamplerCustomAdvanced, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/FLUX IPA+CN 双控制（推荐depth）_1937433850614063106.json, 图片生成/图生图/FLUX Krea + IPAdaper 风格迁移_1951157890688200706.json, 图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json, 图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Redux+Flux风格迁移_1945027298695499777.json, 图片生成/图生图/毛坯房装修迁移（Redux(最强512版)+CN Union Pro双控制（推荐depth）_1937485598129328130.json, 平台全量/老房-毛坯房改造可参考风格图_1945112086164983810.json, 平台全量/老房-毛坯房改造可参考风格图_2031535421020184577.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_26

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX IPA+CN 双控制（推荐depth）_1937433850614063106.json、图片生成/图生图/FLUX Krea + IPAdaper 风格迁移_1951157890688200706.json、图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json、图片生成/图生图/FLUX 双Redux+Flux CN+Wan2.2洗图风格迁移小院改造_1944018116638806018.json、图片生成/图生图/⭐️⭐️⭐️⭐️⭐️——Redux+Flux风格迁移_1945027298695499777.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
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
- `AIO_Preprocessor` —— 6/8 个有
- `ControlNetApplyAdvanced` —— 6/8 个有
- `ControlNetLoader` —— 6/8 个有
- `DF_Get_image_size` —— 6/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImageMirror` —— 6/8 个有
- `ImageResize` —— 6/8 个有
- `SetUnionControlNetType` —— 6/8 个有
- `VAEEncode` —— 6/8 个有
- `GetImageSize+` —— 5/8 个有
- `ModelSamplingFlux` —— 5/8 个有
- `ShowText` —— 5/8 个有
- `StyleModelLoader` —— 5/8 个有
- `CLIPVisionLoader` —— 4/8 个有
- `CombinationText` —— 4/8 个有
- `ReduxAdvanced` —— 4/8 个有
- `ApplyIPAdapterFlux` —— 3/8 个有
- `IPAdapterFluxLoader` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `MirroredImage` —— 3/8 个有
- `DetailDaemonSamplerNode` —— 2/8 个有
- `AdvancedVisionLoader` —— 1/8 个有
- `Anything Everywhere` —— 1/8 个有
- `CFGGuider` —— 1/8 个有
- `CLIPLoader` —— 1/8 个有
- `CLIPVisionEncode` —— 1/8 个有
- `DisableNoise` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `ModelSamplingSD3` —— 1/8 个有
- `SplitSigmas` —— 1/8 个有
- `StyleModelApply` —— 1/8 个有
- `WanVideoNAG` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 8 | 100% |
| 高度 | 1024 | 1024 - 1024 | 8 | 100% |
| ControlNet 权重 | 0.65 | 0.65 - 0.75 | 6 | 94% |
| LoRA 模型强度 | 0.6 | 0 - 0.8 | 8 | 50% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.65，观测区间 0.65 - 0.75，6 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 0.6，观测区间 0 - 0.8，8 个样本，取值分散，一致性仅 50%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
