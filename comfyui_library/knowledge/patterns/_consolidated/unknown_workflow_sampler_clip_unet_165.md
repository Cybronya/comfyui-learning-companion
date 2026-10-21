---
name: unknown_workflow_sampler_clip_unet_165
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.80075
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2图像修复_2064329697353359361.json, 图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json, 图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json, 图片生成/文生图/反差人设-剧场后台花絮_1999861137980223490.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/flux2图像修复_2064329697353359361.json、图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json、图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json、图片生成/文生图/反差人设-剧场后台花絮_1999861137980223490.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
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
- `EmptyFlux2LatentImage` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PiDTextPrompt` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `image_scale_pixel_v2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
