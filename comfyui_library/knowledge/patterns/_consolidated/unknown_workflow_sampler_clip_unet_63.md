---
name: unknown_workflow_sampler_clip_unet_63
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.866
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json, 图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json, 图片生成/文生图/FLUX2 Klein 9B Consistency 一致性工作流_2073316611037163521.json, 图片生成/文生图/FLUX2 Klein 9B Image Edit_2073301759640035330.json, 图片生成/文生图/Flux2 Klein 图像编辑4B版V1_2012131213674287106.json, 图片生成/文生图/Flux2 Klein 图像编辑_2070333019503808513.json, 图片生成/文生图/klein多图编辑_2017934301005877250.json, 图片生成/文生图/一键拍立得+全节点注释_2077751254561943553.json, 图片生成/文生图/去除图像AI感 去油腻质感，增加细节纹理，防止僵尸脸_2093538755654275073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json、图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json、图片生成/文生图/FLUX2 Klein 9B Consistency 一致性工作流_2073316611037163521.json、图片生成/文生图/FLUX2 Klein 9B Image Edit_2073301759640035330.json、图片生成/文生图/Flux2 Klein 图像编辑4B版V1_2012131213674287106.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 8/9 个有
- `GetImageSize` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `CR Text` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `ImageConcanate` —— 2/9 个有
- `ImageResize+` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `ColorMatch` —— 1/9 个有
- `DetailDaemonSamplerNode` —— 1/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `ImageSharpen` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/9 个有
- `easy float` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
