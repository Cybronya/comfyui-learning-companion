---
name: unknown_workflow_sampler_clip_unet_131
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.951889
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2_klein_image_edit_单图_2017799165614497794.json, 图片生成/图生图/Flux2_klein_image_edit_双图_2018351257873813506.json, 图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json, 图片生成/图生图/Klein9b-BFS-换脸_2034835916870656002.json, 图片生成/图生图/Klein9b-BFS最强换脸 V2版相似度99% 谁用谁知道（记得看说明文件）_2029587665544286209.json, 图片生成/图生图/更用好的换脸工作流 DarkBeast（黑兽）风格-Klein9b-BFS_2039134741198282753.json, 图片生成/图生图/最强换面流-Klein9b-BFS_2029175273211564034.json, 图片生成/图生图/贼好用的换脸-Klein9b-BFS_2087457438445424641.json, 图片生成/文生图/人像换脸丨Flux2-Klein 9B丨面部发型替换_2105644038434152450.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_131

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2_klein_image_edit_单图_2017799165614497794.json、图片生成/图生图/Flux2_klein_image_edit_双图_2018351257873813506.json、图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json、图片生成/图生图/Klein9b-BFS-换脸_2034835916870656002.json、图片生成/图生图/Klein9b-BFS最强换脸 V2版相似度99% 谁用谁知道（记得看说明文件）_2029587665544286209.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `ReferenceLatent` —— 8/9 个有
- `VAEEncode` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `Seed (rgthree)` —— 7/9 个有
- `LayerUtility: PurgeVRAM V2` —— 6/9 个有
- `Number to Float` —— 2/9 个有
- `Text Dictionary Get` —— 2/9 个有
- `Text Dictionary New` —— 2/9 个有
- `Text to Number` —— 2/9 个有
- `InpaintStitchImproved` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Manual XY Entry Info` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
