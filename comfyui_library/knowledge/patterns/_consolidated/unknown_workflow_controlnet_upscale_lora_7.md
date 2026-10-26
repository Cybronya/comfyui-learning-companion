---
name: unknown_workflow_controlnet_upscale_lora_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.888
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Latent Batch Size, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, DualCLIPLoader, Fast Groups Muter (rgthree), FluxGuidance, Image Comparer (rgthree), ImageBlend, ImageResize+, ImpactInt, LoadImage, LoraLoader, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed_, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/局部重绘-fill局部重绘封装_2059816583098355714.json, 图片生成/文生图/FLUX 小红书 抖音 快手 批量生成人物风格一致性模特_1902182310718889986.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/局部重绘-fill局部重绘封装_2059816583098355714.json、图片生成/文生图/FLUX 小红书 抖音 快手 批量生成人物风格一致性模特_1902182310718889986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
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
- `ArgosTranslateTextNode` —— 1/2 个有
- `BaiduTranslateNode` —— 1/2 个有
- `BasicGuider` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `CR Color Panel` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageGenResolutionFromImage` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | - | 2 | 100% |
| LoRA 模型强度 | 0.2 | - | 2 | 100% |
| LoRA 文本强度 | 0 | - | 2 | 100% |
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
