---
name: unknown_workflow_lora_sampler_clip_263
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.597333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ColorMatchV2, ConditioningZeroOut, Flux2Scheduler, FluxKVCache, GetNode, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SamplerCustom, SaveImage, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/4K_8K 是玄学还是科学？_2065990016148529154.json, 平台全量/Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545.json, 平台全量/油光终结者：AI 皮肤修复_2065978929348960257.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_263

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/4K_8K 是玄学还是科学？_2065990016148529154.json、平台全量/Flux.2-Klein-9B-KV 最终篇：标准图像编辑工作流（SOP）_2070446133947756545.json、平台全量/油光终结者：AI 皮肤修复_2065978929348960257.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `FluxKVCache`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `TextBoxConcatenate` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
