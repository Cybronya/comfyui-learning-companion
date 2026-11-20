---
name: unknown_workflow_sampler_clip_vae_17
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8274
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2-Klein-9B-base-Q8(mac m芯片本地可用)-基础文生图_2056983301881155585.json, 图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json, 图片生成/文生图/FLUX新王炸 Klein 文生图急速10秒出图_2016041654972583938.json, 图片生成/文生图/Flux-2-Klein-4B （文生图）_2011880923473645570.json, 图片生成/文生图/Flux-Klein-9b文生图_2078378043567075329.json, 图片生成/文生图/Flux2 Klein-文生图 加速版10秒出图_2012172099653214210.json, 图片生成/文生图/Flux2-Klein文生图+图生图_2012291526050717697.json, 图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json, 图片生成/文生图/二次元老婆秒变真人！ComfyUI动漫转写实，脸不变质感拉满_2059589704609255426.json, 图片生成/文生图/产品抠图透明背景精修版+全节点注释_2090760561532424194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_17

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/FLUX2-Klein-9B-base-Q8(mac m芯片本地可用)-基础文生图_2056983301881155585.json、图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json、图片生成/文生图/FLUX新王炸 Klein 文生图急速10秒出图_2016041654972583938.json、图片生成/文生图/Flux-2-Klein-4B （文生图）_2011880923473645570.json、图片生成/文生图/Flux-Klein-9b文生图_2078378043567075329.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 9/10 个有
- `LoadImage` —— 5/10 个有
- `easy int` —— 5/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `PrimitiveInt` —— 4/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `ReferenceLatent` —— 4/10 个有
- `Seed (rgthree)` —— 4/10 个有
- `VAEEncode` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `GGUFLoaderKJ` —— 1/10 个有
- `ImageSmartSharpen+` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `LayerMask: BiRefNetUltra` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
