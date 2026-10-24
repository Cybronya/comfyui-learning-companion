---
name: unknown_workflow_lora_sampler_clip_119
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94125
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI素影绘_1924800227784781826.json, 图片生成/图生图/Flux文生图换脸写真 一键生图系列_1907042022929096706.json, 图片生成/文生图/Flux文生图PuLid换脸-双重曝光·黑白艺术海报_1954772987443503106.json, 图片生成/文生图/Flux模型文生图换脸加contral_1913513255921250305.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI素影绘_1924800227784781826.json、图片生成/图生图/Flux文生图换脸写真 一键生图系列_1907042022929096706.json、图片生成/文生图/Flux文生图PuLid换脸-双重曝光·黑白艺术海报_1954772987443503106.json、图片生成/文生图/Flux模型文生图换脸加contral_1913513255921250305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetLoader` —— 2/4 个有
- `LineArtPreprocessor` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `AutoCropFaces` —— 1/4 个有
- `ControlNetApplyAdvanced` —— 1/4 个有
- `ControlNetApplySD3` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/4 个有
- `LayerUtility: TextJoin` —— 1/4 个有
- `PoseNode` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1004 | 896 - 1024 | 4 | 95% |
| 高度 | 1344 | 1152 - 1536 | 4 | 90% |
| ControlNet 权重 | 0.6 | - | 2 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1004，观测区间 896 - 1024，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1344，观测区间 1152 - 1536，4 个样本，取值集中（一致性 90%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
