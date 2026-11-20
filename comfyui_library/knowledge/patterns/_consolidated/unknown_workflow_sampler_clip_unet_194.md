---
name: unknown_workflow_sampler_clip_unet_194
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.876875
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX3文生图_2115074276838699010.json, 图片生成/文生图/Flux3 Klein 提示词增强文生图_2112106153021890562.json, 图片生成/文生图/Flux3 Klein 提示词增强文生图_2113652586107727873.json, 图片生成/文生图/flux3_klien3快速-电商必备文生图_2110994732565483522.json, 图片生成/文生图/flux3_klien3文生图_2110978915194990593.json, 平台全量/FLUX3文生图_2118512875756150786.json, 平台全量/FLUX3文生图_2118883263417774082.json, 平台全量/Flux3 Klein 提示词增强文生图_2117853144616095745.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_194

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/FLUX3文生图_2115074276838699010.json、图片生成/文生图/Flux3 Klein 提示词增强文生图_2112106153021890562.json、图片生成/文生图/Flux3 Klein 提示词增强文生图_2113652586107727873.json、图片生成/文生图/flux3_klien3快速-电商必备文生图_2110994732565483522.json、图片生成/文生图/flux3_klien3文生图_2110978915194990593.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 6/8 个有
- `TextGenerate` —— 6/8 个有
- `EmptyLatentImage` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `EmptyFlux2LatentImage` —— 3/8 个有
- `JjkText` —— 3/8 个有
- `QWEN_TextDisplay` —— 3/8 个有
- `Int` —— 2/8 个有
- `RH_Translator` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
