---
name: text_to_image_controlnet_inpaint_lora_5
type: Text To Image
frequency: 3
level: strong
coverage: 0.806667
common_nodes: [ApplyInstantID, BboxDetectorSEGS, CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ControlNetLoader, CropFace, DifferentialDiffusion, EmptyLatentImage, FastFilmGrain, GetNode, ImpactInt, ImpactSwitch, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JjkText, KSampler, LoadImage, LoraLoader, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SAMDetectorCombined, SAMLoader, SaveImage, Seed (rgthree), SetNode, TextCombinerSix, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy clearCacheAll, easy imageBatchToImageList, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/生成图片更加真实_1979360264481050626.json, 图片生成/文生图/wan视频模型生成图片更加真实（大炮打蚊子系列一）_1945428725083119618.json, 图片生成/文生图/🐝【真实摄影】亚洲审美超强真实感脱离AI工作流🐝_1944992587074953218.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/生成图片更加真实_1979360264481050626.json、图片生成/文生图/wan视频模型生成图片更加真实（大炮打蚊子系列一）_1945428725083119618.json、图片生成/文生图/🐝【真实摄影】亚洲审美超强真实感脱离AI工作流🐝_1944992587074953218.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyInstantID`
- `BboxDetectorSEGS`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `CropFace`
- `DifferentialDiffusion`
- `EmptyLatentImage`
- `FastFilmGrain`
- `GetNode`
- `ImpactInt`
- `ImpactSwitch`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SAMDetectorCombined`
- `SAMLoader`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `TextCombinerSix`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy clearCacheAll`
- `easy imageBatchToImageList`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1216 | 1216 - 1216 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，观测区间 1216 - 1216，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
