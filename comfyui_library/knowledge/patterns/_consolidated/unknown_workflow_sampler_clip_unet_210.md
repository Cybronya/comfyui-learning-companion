---
name: unknown_workflow_sampler_clip_unet_210
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9515
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/02face-image（th）_2054903846115266562.json, 图片生成/反推提示词/14oldphonerestore_2049045395405283329.json, 图片生成/反推提示词/换脸_2048159102316060674.json, 图片生成/图生图/2026最新FLUX2-Klein 9B版文生图_单图多图编辑工作流_2012390556902625281.json, 图片生成/图生图/Flux2-Klein-9B双图编辑_2013423771364888578.json, 图片生成/图生图/换脸换头 Klein多图编辑 Face and Head Swap_ Klein Multi-Ima_2113063253717897218.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_210

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/02face-image（th）_2054903846115266562.json、图片生成/反推提示词/14oldphonerestore_2049045395405283329.json、图片生成/反推提示词/换脸_2048159102316060674.json、图片生成/图生图/2026最新FLUX2-Klein 9B版文生图_单图多图编辑工作流_2012390556902625281.json、图片生成/图生图/Flux2-Klein-9B双图编辑_2013423771364888578.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `GetImageSize` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `Int` —— 2/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `JWFloat` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
