---
name: unknown_workflow_video_lora_sampler_664
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.60925
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, CheckpointLoaderSimple, DWPreprocessor, DepthCrafter, DownloadAndLoadDepthCrafterModel, FloatToSigmas, ImageConcanate, ImageResize+, ImageToCPU, KSamplerSelect, LTXVAdainLatent, LTXVConditioning, LTXVInContextSampler, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVTiledSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrintSigmas, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, StringToFloatList, VAEDecode, VAEDecodeTiled, VAEEncode, VHS_LoadVideo, VHS_SelectImages, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/LTX-Video-ICLoRA_1944031275911090177.json, 平台全量/LTXV 0.98 IC LORA姿势控制视频生视频V1_1947695587496996866.json, 平台全量/LTXV 0.98 IC LORA深度控制视频生视频V1_1947697975301681153.json, 视频生成/图生视频/LTXV 0.98 IC LORA线稿控制视频生视频V1_1947688689313951745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_664

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/LTX-Video-ICLoRA_1944031275911090177.json、平台全量/LTXV 0.98 IC LORA姿势控制视频生视频V1_1947695587496996866.json、平台全量/LTXV 0.98 IC LORA深度控制视频生视频V1_1947697975301681153.json、视频生成/图生视频/LTXV 0.98 IC LORA线稿控制视频生视频V1_1947688689313951745.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `CheckpointLoaderSimple`
- `DWPreprocessor`
- `DepthCrafter`
- `DownloadAndLoadDepthCrafterModel`
- `FloatToSigmas`
- `ImageConcanate`
- `ImageResize+`
- `ImageToCPU`
- `KSamplerSelect`
- `LTXVAdainLatent`
- `LTXVConditioning`
- `LTXVInContextSampler`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVTiledSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrintSigmas`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `StringToFloatList`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VHS_LoadVideo`
- `VHS_SelectImages`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `RH_Translator` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
