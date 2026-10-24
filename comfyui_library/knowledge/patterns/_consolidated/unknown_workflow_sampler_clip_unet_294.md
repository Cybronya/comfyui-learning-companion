---
name: unknown_workflow_sampler_clip_unet_294
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.975
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/星绘-FLUX2-Klein版一键多机位角度调整_2013878236958171138.json, 图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json, 图片生成/图生图/炉石卡通转换_2093517690102181890.json, 图片生成/图生图/电商详情-普通中文版_1988507050411999234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_294

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/星绘-FLUX2-Klein版一键多机位角度调整_2013878236958171138.json、图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json、图片生成/图生图/炉石卡通转换_2093517690102181890.json、图片生成/图生图/电商详情-普通中文版_1988507050411999234.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
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
- `GetImageSize` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `LayerUtility: TextJoin` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/4 个有
- `easy promptList` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
