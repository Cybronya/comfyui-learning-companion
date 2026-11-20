---
name: unknown_workflow_upscale_face_detailer_lora_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.795
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Aspect Ratio SDXL, CR Text, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, FaceDetailer, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PhiPrompt, LoadImage, LoraLoader, RandomNoise, SAMLoader, SUPIR_Upscale, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, StringFunction|pysssss, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/Flux三视图一致性文生图完美反推自动提示词_1910692535243866113.json, 平台全量/Flux三视图一致性文生图完美反推自动提示词_1923287327131824129.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_face_detailer_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux三视图一致性文生图完美反推自动提示词_1910692535243866113.json、平台全量/Flux三视图一致性文生图完美反推自动提示词_1923287327131824129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Aspect Ratio SDXL`
- `CR Text`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceDetailer`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PhiPrompt`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SAMLoader`
- `SUPIR_Upscale`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
