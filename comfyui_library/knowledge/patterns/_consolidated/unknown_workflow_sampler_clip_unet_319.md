---
name: unknown_workflow_sampler_clip_unet_319
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.982
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/商K一键出图_1973223203931820034.json, 图片生成/文生图/紧身牛仔裤_2053136080395882498.json, 图片生成/文生图/🕵【大炮商K订制】商K一键出图A 🕵_1973209784952467457.json, 图片生成/文生图/🕵【大炮擦边】一见倾心 背影杀🕵_1973180639434420225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_319

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/商K一键出图_1973223203931820034.json、图片生成/文生图/紧身牛仔裤_2053136080395882498.json、图片生成/文生图/🕵【大炮商K订制】商K一键出图A 🕵_1973209784952467457.json、图片生成/文生图/🕵【大炮擦边】一见倾心 背影杀🕵_1973180639434420225.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `ImpactInt` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1920 | 1920 - 1920 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，4 个样本，取值集中（一致性 100%）
