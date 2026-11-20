---
name: unknown_workflow_sampler_clip_unet_347
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8155
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/高频噪点修复_2108555371207020545.json, 图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json, 图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json, 视频生成/图生视频/高频噪点修复_2114194025107513346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_347

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/高频噪点修复_2108555371207020545.json、图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json、图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json、视频生成/图生视频/高频噪点修复_2114194025107513346.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `EmptyFlux2LatentImage` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有
- `SplitSigmasDenoise` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `TextInput_` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
