---
name: unknown_workflow_sampler_clip_unet_269
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8412
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/多多安全区banner_2079455432715890690.json, 图片生成/图生图/局部重绘-Flux2-klein-模板_2050108664723320834.json, 图片生成/图生图/扩图-Flux2-klein-模板_2050109267771961345.json, 图片生成/图生图/电商一键扩图 flux2 klein_2013426255588237313.json, 图片生成/文生图/一键拍立得+全节点注释_2077751254561943553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_269

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/多多安全区banner_2079455432715890690.json、图片生成/图生图/局部重绘-Flux2-klein-模板_2050108664723320834.json、图片生成/图生图/扩图-Flux2-klein-模板_2050109267771961345.json、图片生成/图生图/电商一键扩图 flux2 klein_2013426255588237313.json、图片生成/文生图/一键拍立得+全节点注释_2077751254561943553.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
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
- `ColorMatch` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `ImagePadForOutpaint` —— 4/5 个有
- `CR Text` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `easy seed` —— 2/5 个有
- `JjkText` —— 1/5 个有
- `LayerUtility: TextJoin` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `图像缩放V2_孤海` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
