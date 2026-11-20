---
name: unknown_workflow_sampler_clip_unet_221
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9185
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KLEIN 深度控制_2030614146588352514.json, 图片生成/图生图/Klein -通道主图2_2041417376184410114.json, 图片生成/图生图/Klein -通道主图3_2041804986694242306.json, 图片生成/图生图/Klein单图编辑_2014887219860869122.json, 图片生成/图生图/WH-AI-Studio超强FLUX2-Klein单图语义修改器_2053315100181835777.json, 图片生成/图生图/WH-AI-Studio（超强FLUX2-Klein单图语义修改器）_2026674751833378817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_221

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/KLEIN 深度控制_2030614146588352514.json、图片生成/图生图/Klein -通道主图2_2041417376184410114.json、图片生成/图生图/Klein -通道主图3_2041804986694242306.json、图片生成/图生图/Klein单图编辑_2014887219860869122.json、图片生成/图生图/WH-AI-Studio超强FLUX2-Klein单图语义修改器_2053315100181835777.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Int` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `DuckHideNode` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `ImageConcanate` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `MultiTextConcatenate` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
