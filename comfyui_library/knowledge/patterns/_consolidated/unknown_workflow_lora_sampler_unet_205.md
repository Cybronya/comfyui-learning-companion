---
name: unknown_workflow_lora_sampler_unet_205
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.858333
common_nodes: [AdaptiveLongestEdge_EditUtils, CFGGuider, CLIPLoader, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2026.04最强换装工作流-bole_2047349240950689794.json, 图片生成/图生图/FK2一致性-批量编辑_2073291622103740418.json, 图片生成/图生图/[Klein] 虚拟试衣与商品局部精准替换 _ 电商换装  _ 图像局部编辑_2063183070840320002.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_205

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2026.04最强换装工作流-bole_2047349240950689794.json、图片生成/图生图/FK2一致性-批量编辑_2073291622103740418.json、图片生成/图生图/[Klein] 虚拟试衣与商品局部精准替换 _ 电商换装  _ 图像局部编辑_2063183070840320002.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AdaptiveLongestEdge_EditUtils`
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Flux2KleinOutputExtractor_EditUtils` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `DapaoImageAspectRatioResizeNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageToURL` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `Qwen3VL_Chat` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy promptList` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
