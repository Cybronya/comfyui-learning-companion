---
name: unknown_workflow_sampler_clip_unet_6
type: Unknown Workflow
frequency: 31
level: strong
coverage: 0.842516
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json, 图片生成/文生图/FLUX klein 4B 文生图_2013180405410697218.json, 图片生成/文生图/FLUX klein 9B 文生图_2013484429548724225.json, 图片生成/文生图/FLUX-Klein-文生图-10秒急速出图_2012122075317669889.json, 图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json, 图片生成/文生图/FLUX.2 klein 蒸馏版文生图_2012457929915502594.json, 图片生成/文生图/FLUX2 klein-9B 【文生图】_2013859086563024897.json, 图片生成/文生图/FLUX2 klein-9B 文生图_2013123316474716162.json, 图片生成/文生图/FLUX2Klein 文生图 flux克莱因文生图Basic Text-to-lmage_2015976117517164545.json, 图片生成/文生图/FLUX新王炸 Klein 文生图急速10秒出图_2016041654972583938.json, 图片生成/文生图/Flux-Klein-9b文生图_2078378043567075329.json, 图片生成/文生图/Flux.2-Klein 文生图_2012020733546860545.json, 图片生成/文生图/Flux2 Klein 文生图_2012770598530846721.json, 图片生成/文生图/Flux2 Klein-文生图 加速版10秒出图_2012172099653214210.json, 图片生成/文生图/Flux2-Klein文生图_2012285704222543873.json, 图片生成/文生图/Flux2-klein-9b-fp8 基础文生图_2016379670488424449.json, 图片生成/文生图/Flux2-klein-9b-fp8 文生图_2013086202567598081.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2013502856430620674.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2084470823594848258.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2084518939031326721.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2084529249729474562.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2085253506654621698.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2085255233579601922.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2087429216940937218.json, 图片生成/文生图/Flux2-klein-9b-fp8 未来感卡通风格_2087708601073881089.json, 图片生成/文生图/Flux2-klein-base-9b-fp8 文生图_2013133653185929218.json, 图片生成/文生图/Flux2.Klein文生图基础款_2013133525679087617.json, 图片生成/文生图/Klein-t2i_2073767273445289985.json, 图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json, 图片生成/文生图/flux klein9B 工作流 浮云1.19_2013089641938817026.json, 图片生成/文生图/😶_🌫️FLUX新王炸 Klein 文生图急速10秒出图😶_🌫️_2012094524113297409.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（图片生成/文生图/F.2-klein-9B+LoRA文生图工作流_2013075554722914305.json、图片生成/文生图/FLUX klein 4B 文生图_2013180405410697218.json、图片生成/文生图/FLUX klein 9B 文生图_2013484429548724225.json、图片生成/文生图/FLUX-Klein-文生图-10秒急速出图_2012122075317669889.json、图片生成/文生图/FLUX.2 klein base 版文生图_2012463751529762817.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 31 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 26/31 个有
- `PrimitiveInt` —— 24/31 个有
- `ConditioningZeroOut` —— 19/31 个有
- `Seed (rgthree)` —— 5/31 个有
- `easy int` —— 5/31 个有
- `AddLabel` —— 4/31 个有
- `LoraLoader` —— 2/31 个有
- `LoraLoaderModelOnly` —— 2/31 个有
- `ImageConcatMulti` —— 1/31 个有
- `Int` —— 1/31 个有
- `Note Plus (mtb)` —— 1/31 个有
- `ResolutionSelector` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.5 | - | 2 | 100% |
| LoRA 文本强度 | 1.41 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1.41，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
