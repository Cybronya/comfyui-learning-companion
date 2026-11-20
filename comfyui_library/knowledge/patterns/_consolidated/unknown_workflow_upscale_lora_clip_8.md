---
name: unknown_workflow_upscale_lora_clip_8
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, DetailerForEachDebug, FaceRestoreCFWithModel, FaceRestoreModelLoader, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, ImpactSegsAndMask, LoadImage, LoraLoader, ReActorFaceSwap, SAMDetectorCombined, SAMLoader, SaveImage, UltralyticsDetectorProvider, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [平台全量/pro换脸_1778250535439228929.json, 平台全量/形象照输出机_1783689001643810818.json, 平台全量/梦宛霖pro换脸_1823405816413073409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/pro换脸_1778250535439228929.json、平台全量/形象照输出机_1783689001643810818.json、平台全量/梦宛霖pro换脸_1823405816413073409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailerForEachDebug`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactSegsAndMask`
- `LoadImage`
- `LoraLoader`
- `ReActorFaceSwap`
- `SAMDetectorCombined`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| LoRA 文本强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
