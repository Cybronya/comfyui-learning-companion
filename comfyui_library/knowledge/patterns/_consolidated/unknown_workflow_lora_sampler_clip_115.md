---
name: unknown_workflow_lora_sampler_clip_115
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.6615
common_nodes: [AILab_ImageResize, Anything Everywhere3, CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetNode, ImageStitch, Int, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewAny, Qwen3VL_Chat, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键提取服装白底图 Flux2-klein 9B模型_2103447528330055682.json, 图片生成/图生图/服装完美正面提取加大_自选出图丨Flux2-klein 9B_2033617434636197889.json, 图片生成/图生图/服装模特图高清提取服装3D平面图平铺图生图_2066190874966581250.json, 平台全量/👽老许Gary： 单图编辑-服装提取丨Flux2-klein 9B_2033490098733457410.json, 平台全量/👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850.json, 平台全量/👽老许Gary：Flux2-klein 9B 基础三图编辑_2033449904412041217.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键提取服装白底图 Flux2-klein 9B模型_2103447528330055682.json、图片生成/图生图/服装完美正面提取加大_自选出图丨Flux2-klein 9B_2033617434636197889.json、图片生成/图生图/服装模特图高清提取服装3D平面图平铺图生图_2066190874966581250.json、平台全量/👽老许Gary： 单图编辑-服装提取丨Flux2-klein 9B_2033490098733457410.json、平台全量/👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B👽老许Gary： 服装立体化-单图编辑丨Flux2-klein 9B_2034197723368398850.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_ImageResize`
- `Anything Everywhere3`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetNode`
- `ImageStitch`
- `Int`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `Qwen3VL_Chat`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `GetImageSize+` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `QwenMultiangleCameraNode` —— 3/6 个有
- `TextInputNode` —— 3/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `TT_img_enc` —— 1/6 个有
- `TT_img_enc_v2` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `ZML_SwitchOutput` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy promptLine` —— 1/6 个有
- `text_mul_Join` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
