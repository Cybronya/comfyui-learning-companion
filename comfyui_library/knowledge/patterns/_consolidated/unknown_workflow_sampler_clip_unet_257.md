---
name: unknown_workflow_sampler_clip_unet_257
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.949667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, ManualSigmas, RandomNoise, ReferenceMultiLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux_klien3图像编辑_2110985829039558657.json, 图片生成/图生图/（4图 可以上满4张最少可以上传1张）Flux3多图编辑加速版_2111603711633092609.json, 图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json, 图片生成/文生图/Flux3&多图编辑-加速版_2111293209782603777.json, 图片生成/文生图/flux_klien3单图-快速图像编辑_2110999906369490946.json, 视频生成/图生视频/Flux3加速版多图编辑V1_2110847111846780929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_257

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/flux_klien3图像编辑_2110985829039558657.json、图片生成/图生图/（4图 可以上满4张最少可以上传1张）Flux3多图编辑加速版_2111603711633092609.json、图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json、图片生成/文生图/Flux3&多图编辑-加速版_2111293209782603777.json、图片生成/文生图/flux_klien3单图-快速图像编辑_2110999906369490946.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ReferenceMultiLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `孤海注释` —— 2/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `Text` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
