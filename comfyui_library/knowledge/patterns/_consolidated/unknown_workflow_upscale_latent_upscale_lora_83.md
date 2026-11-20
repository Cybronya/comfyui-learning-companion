---
name: unknown_workflow_upscale_latent_upscale_lora_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9145
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR SDXL Aspect Ratio, CR Text Concatenate, DetailDaemonSamplerNode, DisableNoise, DualCLIPLoader, FL_SDUltimate_Slices, FluxGuidance, Image Comparer (rgthree), InjectLatentNoise+, KSamplerSelect, LatentInterpolate, LatentUpscaleBy, LoadImage, ModelSamplingFlux, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmasDenoise, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy loraStack, easy loraStackApply]
problems: []
missing: []
members: [图片生成/图生图/橙AI_1907001812128505858.json, 平台全量/为720P图生视频准备的遮脸自拍照片_1907473499219193858.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/橙AI_1907001812128505858.json、平台全量/为720P图生视频准备的遮脸自拍照片_1907473499219193858.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Text Concatenate`
- `DetailDaemonSamplerNode`
- `DisableNoise`
- `DualCLIPLoader`
- `FL_SDUltimate_Slices`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InjectLatentNoise+`
- `KSamplerSelect`
- `LatentInterpolate`
- `LatentUpscaleBy`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmasDenoise`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy loraStack`
- `easy loraStackApply`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: TextJoin` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringConstantMultiline` —— 1/2 个有
- `TeaCache` —— 1/2 个有
- `TeaCacheForImgGen` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
