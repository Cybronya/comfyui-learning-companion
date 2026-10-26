---
name: unknown_workflow_lora_sampler_clip_179
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.724667
common_nodes: [Any Switch (rgthree), ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FaceAnalysisModels, FaceBoundingBox, Fast Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageScaleBy, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, Mute / Bypass Repeater (rgthree), PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed Everywhere, ShowText|pysssss, SplitSigmasDenoise, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/FLUX+超逼真!+网红制造-高清放大+洗图+换脸+自定义相似度重绘_1896044072568225793.json, 图片生成/图生图/Pulid2 超高清换脸_1914636840983560194.json, 图片生成/图生图/Pulid2超高清换脸_1918115409055121409.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_179

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX+超逼真!+网红制造-高清放大+洗图+换脸+自定义相似度重绘_1896044072568225793.json、图片生成/图生图/Pulid2 超高清换脸_1914636840983560194.json、图片生成/图生图/Pulid2超高清换脸_1918115409055121409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `Fast Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `ShowText|pysssss`
- `SplitSigmasDenoise`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LayerColor: Brightness & Contrast` —— 2/3 个有
- `LayerFilter: FilmV2` —— 2/3 个有
- `LayerMask: PersonMaskUltra V2` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `SUPIR_Upscale` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `Tensor Batch to Image` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | sgm_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
