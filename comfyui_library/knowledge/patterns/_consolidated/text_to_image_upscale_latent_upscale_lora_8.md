---
name: text_to_image_upscale_latent_upscale_lora_8
type: Text To Image
frequency: 7
level: strong
coverage: 0.89
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585.json, 视频生成/图生视频/数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561.json, 视频生成/图生视频/真人短镜头3本地开源免费图生视频生成工作流_2088364240607465474.json, 视频生成/图生视频/真人短镜头3本地开源免费｜图生视频工作流_2088331443171844097.json, 视频生成/图生视频/真人短镜头3高效产出｜本地开源免费图生视频方案_2096209284727140353.json, 视频生成/图生视频/真人短镜头3｜本地免费开源图生视频素材一键生成_2092144230335602689.json, 视频生成/图生视频/真人短镜头生成｜本地开源免费图生视频直出_2092007691907584002.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/提示词反推｜LTX2.5数字人图生视频生成_2089831012640579585.json、视频生成/图生视频/数字Prompt+Relay提示词分段控制｜LTX2.5图生视频工作流_2088361067079618561.json、视频生成/图生视频/真人短镜头3本地开源免费图生视频生成工作流_2088364240607465474.json、视频生成/图生视频/真人短镜头3本地开源免费｜图生视频工作流_2088331443171844097.json、视频生成/图生视频/真人短镜头3高效产出｜本地开源免费图生视频方案_2096209284727140353.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 5/7 个有
- `DualCLIPLoader` —— 5/7 个有
- `EnhancedLoadDiffusionModel` —— 5/7 个有
- `LTXVCropGuides` —— 5/7 个有
- `LTXVEmptyLatentAudio` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `Switch` —— 5/7 个有
- `VAELoaderKJ` —— 5/7 个有
- `easy indexAnything` —— 5/7 个有
- `AudioInfo` —— 2/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `LTXVAudioVAEEncode` —— 2/7 个有
- `LTXVDualCFGGuider` —— 2/7 个有
- `PromptRelaySmartEncode` —— 2/7 个有
- `SetLatentNoiseMask` —— 2/7 个有
- `SolidMask` —— 2/7 个有
- `TrimAudioDuration` —— 2/7 个有
- `PreviewAny` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
