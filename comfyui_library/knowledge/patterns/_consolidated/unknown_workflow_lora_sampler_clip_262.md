---
name: unknown_workflow_lora_sampler_clip_262
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.879667
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, JjkShowText, JjkText, KSamplerSelect, LoadImage, LoraLoader, MaskToSEGS, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, SEGSPreview, SamplerCustomAdvanced, SaveImage, TextCombinerTwo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/3D卡通可爱古装角色_1909197573905915906.json, 平台全量/PuLID_Flux_ll卡通双人合照_1910623078995456001.json, 音频生成/音频生成/古装人物3D渲染 _ 动漫人物_1933849263581650945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_262

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/3D卡通可爱古装角色_1909197573905915906.json、平台全量/PuLID_Flux_ll卡通双人合照_1910623078995456001.json、音频生成/音频生成/古装人物3D渲染 _ 动漫人物_1933849263581650945.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `JjkShowText`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `MaskToSEGS`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `ApplyTeaCachePatch` —— 1/3 个有
- `CR Image Input Switch` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `FluxForwardOverrider` —— 1/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImageListToBatch+` —— 1/3 个有
- `Int` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `MaskComposite` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SolidMask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.9 - 1 | 3 | 95% |
| LoRA 文本强度 | 0.9 | 0.9 - 1 | 3 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 0.9，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
