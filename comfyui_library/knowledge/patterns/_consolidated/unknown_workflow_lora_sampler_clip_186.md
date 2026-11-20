---
name: unknown_workflow_lora_sampler_clip_186
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8205
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/惠绘_Klein修脸厚涂_橙子（_2024776560175222785.json, 图片生成/图生图/惠绘_橙子一键2d转3dKlein_2049837309243207681.json, 图片生成/图生图/换脸_2071838717576302593.json, 平台全量/👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_186

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/惠绘_Klein修脸厚涂_橙子（_2024776560175222785.json、图片生成/图生图/惠绘_橙子一键2d转3dKlein_2049837309243207681.json、图片生成/图生图/换脸_2071838717576302593.json、平台全量/👽老许Gary：服装替换 V1.1 提示词优化版本丨Flux2-klein 9B_2035606342118936577.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_ImageCompare` —— 2/4 个有
- `AILab_ImageResize` —— 2/4 个有
- `Anything Everywhere3` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Pipe from any [Crystools]` —— 2/4 个有
- `Pipe to/edit any [Crystools]` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `easy float` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有
- `easy int` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `Qwen3VL_Chat` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
