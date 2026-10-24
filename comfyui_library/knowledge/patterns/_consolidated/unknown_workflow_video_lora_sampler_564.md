---
name: unknown_workflow_video_lora_sampler_564
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.890667
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DisableNoise, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoader, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RH_Captioner, RandomNoise, SDXLPromptStyler, SamplerCustomAdvanced, SaveImage, SeedVR2, SplitSigmas, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/产品展示（人物迁移+场景迁移+产品)_1978473664150704130.json, 图片生成/图生图/产品放到参考场景中（Redux+ 全能图片V1)_1974158869893091330.json, 图片生成/图生图/未来世界概念场景_1954458866765459457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_564

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/产品展示（人物迁移+场景迁移+产品)_1978473664150704130.json、图片生成/图生图/产品放到参考场景中（Redux+ 全能图片V1)_1974158869893091330.json、图片生成/图生图/未来世界概念场景_1954458866765459457.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SDXLPromptStyler`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2`
- `SplitSigmas`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 2/3 个有
- `CombinationText` —— 2/3 个有
- `ConditioningCombine` —— 2/3 个有
- `ConditioningSetAreaStrength` —— 2/3 个有
- `DF_Get_image_size` —— 2/3 个有
- `MirroredImage` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `RH_Nano_Banana_Image2Image` —— 2/3 个有
- `ReduxAdvanced` —— 2/3 个有
- `Text` —— 2/3 个有
- `AdvancedVisionLoader` —— 1/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `Image Blank` —— 1/3 个有
- `ImagePaste` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `SeargePromptCombiner` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `StyleModelApply` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | 0.3 - 0.5 | 3 | 78% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，观测区间 0.3 - 0.5，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
