---
name: unknown_workflow_video_lora_sampler_562
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.634667
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, FloatToSigmas, ImageResizeKJ, KSamplerSelect, LTXVConditioning, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVLoopingSampler, LTXVTiledVAEDecode, LoraLoaderModelOnly, MultiPromptProvider, PrimitiveInt, PrintSigmas, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, StringToFloatList, VAEEncode, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/ltx-0.9.8-长视频生成_1947543467977232385.json, 视频生成/图生视频/LTXV 0.98 提示词调度（多组）图生视频V1（支持60秒）_1947704155776397313.json, 视频生成/图生视频/LTXV 0.98 深度视频转绘长视频V1_1947715360633040897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_562

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/ltx-0.9.8-长视频生成_1947543467977232385.json、视频生成/图生视频/LTXV 0.98 提示词调度（多组）图生视频V1（支持60秒）_1947704155776397313.json、视频生成/图生视频/LTXV 0.98 深度视频转绘长视频V1_1947715360633040897.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `FloatToSigmas`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVLoopingSampler`
- `LTXVTiledVAEDecode`
- `LoraLoaderModelOnly`
- `MultiPromptProvider`
- `PrimitiveInt`
- `PrintSigmas`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `StringToFloatList`
- `VAEEncode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LTXVFilmGrain` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
