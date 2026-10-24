---
name: unknown_workflow_lora_sampler_clip_175
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.667333
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GetNode, GrowMaskWithBlur, INTConstant, ImageResize+, KSamplerSelect, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoader, MaskPreview+, ModelSamplingFlux, PreviewImage, PulidEvaClipLoader, PulidFluxModelLoader, PulidInsightFaceLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/pulid+Joy2反推提示词  保留人脸 风格迁移_1916495327514529793.json, 图片生成/图生图/人物换脸+风格特征 PULID联合 REDUX_1917530774286045185.json, 图片生成/图生图/学习必看  Redux+pulid  换脸 风格特征迁移_1916819520000819202.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/pulid+Joy2反推提示词  保留人脸 风格迁移_1916495327514529793.json、图片生成/图生图/人物换脸+风格特征 PULID联合 REDUX_1917530774286045185.json、图片生成/图生图/学习必看  Redux+pulid  换脸 风格特征迁移_1916819520000819202.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResize+`
- `KSamplerSelect`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidInsightFaceLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `StyleModelApply` —— 2/3 个有
- `StyleModelLoader` —— 2/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
