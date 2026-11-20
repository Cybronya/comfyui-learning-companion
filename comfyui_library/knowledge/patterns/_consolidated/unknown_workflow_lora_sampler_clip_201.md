---
name: unknown_workflow_lora_sampler_clip_201
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.868333
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Concatenate, DualCLIPLoader, EmptyImage, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskToSEGS, ModelSamplingFlux, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, SEGSPreview, SamplerCustomAdvanced, SaveImage, TextBox, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/毕业盲盒 _ 创意玩法_1926950324412841985.json, 图片生成/图生图/毛绒玩偶 _ 创意玩法_1927324563615682562.json, 视频生成/图生视频/万物成精，任意产品变成毛绒娃娃特效_1930575698228858881.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/毕业盲盒 _ 创意玩法_1926950324412841985.json、图片生成/图生图/毛绒玩偶 _ 创意玩法_1927324563615682562.json、视频生成/图生视频/万物成精，任意产品变成毛绒娃娃特效_1930575698228858881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `ModelSamplingFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `NunchakuPulidApply` —— 1/3 个有
- `NunchakuPulidLoader` —— 1/3 个有
- `NunchakuTextEncoderLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 504 | 504 - 504 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 504，观测区间 504 - 504，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
