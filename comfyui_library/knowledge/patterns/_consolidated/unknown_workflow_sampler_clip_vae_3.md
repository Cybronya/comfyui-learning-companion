---
name: unknown_workflow_sampler_clip_vae_3
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.838143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2-Klein-9B-base-Q8(mac m芯片本地可用)-基础文生图_2056983301881155585.json, 图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json, 图片生成/文生图/FLUX新王炸 Klein 文生图急速10秒出图_2016041654972583938.json, 图片生成/文生图/Flux-2-Klein-4B （文生图）_2011880923473645570.json, 图片生成/文生图/Flux-Klein-9b文生图_2078378043567075329.json, 图片生成/文生图/Flux2 Klein-文生图 加速版10秒出图_2012172099653214210.json, 图片生成/文生图/Flux2-Klein文生图_2012285704222543873.json, 图片生成/文生图/Flux2-klein-9b-fp8 基础文生图_2016379670488424449.json, 图片生成/文生图/Flux2-klein-9b-fp8 文生图_2013086202567598081.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2013502856430620674.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2084470823594848258.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2084518939031326721.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2084529249729474562.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2085253506654621698.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2085255233579601922.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2087429216940937218.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2087708601073881089.json, 图片生成/文生图/Flux2.Klein文生图基础款_2013133525679087617.json, 图片生成/文生图/Flux2.Klein文生图基础款（单图生成）_2039547259301400577.json, 图片生成/文生图/Klein-t2i_2073767273445289985.json, 图片生成/文生图/Klein4B文生图(又快又好)_2036253514183221249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/FLUX2-Klein-9B-base-Q8(mac m芯片本地可用)-基础文生图_2056983301881155585.json、图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json、图片生成/文生图/FLUX新王炸 Klein 文生图急速10秒出图_2016041654972583938.json、图片生成/文生图/Flux-2-Klein-4B （文生图）_2011880923473645570.json、图片生成/文生图/Flux-Klein-9b文生图_2078378043567075329.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 21 个 workflow 都包含：
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
- `UNETLoader` —— 20/21 个有
- `PrimitiveStringMultiline` —— 18/21 个有
- `ConditioningZeroOut` —— 16/21 个有
- `PrimitiveInt` —— 16/21 个有
- `easy int` —— 4/21 个有
- `Seed (rgthree)` —— 3/21 个有
- `AddLabel` —— 2/21 个有
- `LoraLoaderModelOnly` —— 2/21 个有
- `CR Text Concatenate` —— 1/21 个有
- `GGUFLoaderKJ` —— 1/21 个有
- `LoadImage` —— 1/21 个有
- `PrimitiveBoolean` —— 1/21 个有
- `ResolutionSelector` —— 1/21 个有
- `easy ifElse` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
