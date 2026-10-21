---
name: unknown_workflow_sampler_clip_unet_69
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.846889
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2文生图1.0_1998240533703196674.json, 图片生成/文生图/【GUGU】FLUX2.0文生图_1993486400035160066.json, 图片生成/文生图/【老金驿站】FLUX2-dev文生图工作流_1993506834367660033.json, 图片生成/文生图/【遇见AI】FLUX2-klein-4b，文生图_2012008988237373441.json, 图片生成/文生图/【遇见AI】FLUX2-klein-9b，文生图_2012015997716271105.json, 图片生成/文生图/【遇见AI】FLUX2-klein-base-4b，文生图_2012011674202546178.json, 图片生成/文生图/【遇见AI】FLUX2-klein-base-9b，文生图_2012019877464248321.json, 图片生成/文生图/【遇见AI】FLUX2基础文生图_1993593869338165249.json, 视频生成/图生视频/MiniMax_H3_通用导演台_图生配音视频_2086025061747748866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/flux2文生图1.0_1998240533703196674.json、图片生成/文生图/【GUGU】FLUX2.0文生图_1993486400035160066.json、图片生成/文生图/【老金驿站】FLUX2-dev文生图工作流_1993506834367660033.json、图片生成/文生图/【遇见AI】FLUX2-klein-4b，文生图_2012008988237373441.json、图片生成/文生图/【遇见AI】FLUX2-klein-9b，文生图_2012015997716271105.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/9 个有
- `CR Seed` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `CreateVideo` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `MiniMaxH3Director` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `SaveVideo` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
