---
name: unknown_workflow_controlnet_upscale_lora_5
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.751667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ConcatText_Zho, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, Efficient Loader, FreeU_V2, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, Image Comparer (rgthree), Image Overlay, ImageResize+, ImageResizeKJ, ImageUpscaleWithModel, ImpactSwitch, InvertMask, KSampler (Efficient), KSamplerSelect, LayerMask: MaskPreview, LineArtPreprocessor, LoadImage, LoraLoader, MaskBlur+, MiDaS-DepthMapPreprocessor, ModelSamplingFlux, PortraitMaster_中文版, PreviewImage, RandomNoise, SAMLoader, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, ShowText|pysssss, SubtractMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [图片生成/图生图/03-sd1.5_Flux产品图换模特工作流_1902374480709103617.json, 平台全量/AI电商产品模特替换_1838041421566865409.json, 平台全量/电商换脸_1933046460533407745.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/03-sd1.5_Flux产品图换模特工作流_1902374480709103617.json、平台全量/AI电商产品模特替换_1838041421566865409.json、平台全量/电商换脸_1933046460533407745.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConcatText_Zho`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `Efficient Loader`
- `FreeU_V2`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `ImpactSwitch`
- `InvertMask`
- `KSampler (Efficient)`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `MaskBlur+`
- `MiDaS-DepthMapPreprocessor`
- `ModelSamplingFlux`
- `PortraitMaster_中文版`
- `PreviewImage`
- `RandomNoise`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SubtractMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `WD14Tagger|pysssss` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `Molmo7BDbnb` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
