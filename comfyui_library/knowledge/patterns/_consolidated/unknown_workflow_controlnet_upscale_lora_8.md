---
name: unknown_workflow_controlnet_upscale_lora_8
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.853
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, DualCLIPLoader, Fast Groups Muter (rgthree), FluxGuidance, Image Comparer (rgthree), ImageBlend, ImageResize+, ImpactInt, LoadImage, LoraLoader, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed_, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/局部重绘-fill局部重绘封装_2059816583098355714.json, 图片生成/文生图/FLUX 小红书 抖音 快手 批量生成人物风格一致性模特_1902182310718889986.json, 平台全量/FLUX-redux 换装 丨去条纹增加质感【全手工_半自动】_1928277663796838401.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/局部重绘-fill局部重绘封装_2059816583098355714.json、图片生成/文生图/FLUX 小红书 抖音 快手 批量生成人物风格一致性模特_1902182310718889986.json、平台全量/FLUX-redux 换装 丨去条纹增加质感【全手工_半自动】_1928277663796838401.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImageResize+`
- `ImpactInt`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed_`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Batch Size` —— 2/3 个有
- `DifferentialDiffusion` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageToMask` —— 2/3 个有
- `InpaintModelConditioning` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `BaiduTranslateNode` —— 1/3 个有
- `BasicGuider` —— 1/3 个有
- `BasicScheduler` —— 1/3 个有
- `CR Color Panel` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `ImageCrop+` —— 1/3 个有
- `ImageGenResolutionFromImage` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `InpaintCrop` —— 1/3 个有
- `InpaintStitch` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `LayerUtility: ColorImage` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | 0.35 - 0.35 | 3 | 100% |
| LoRA 模型强度 | 0.2 | 0.2 - 0.2 | 3 | 100% |
| LoRA 文本强度 | 0 | 0 - 0 | 3 | 100% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.35，观测区间 0.35 - 0.35，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.2，观测区间 0.2 - 0.2，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
