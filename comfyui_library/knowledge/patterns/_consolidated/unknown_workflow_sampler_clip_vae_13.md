---
name: unknown_workflow_sampler_clip_vae_13
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.930417
common_nodes: [CFGGuider, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein 9B-文生图-测试lora工作流_2046045126165798913.json, 图片生成/图生图/klein 9B-文生图-测试lora工作流_2046055960355016705.json, 图片生成/图生图/klein 9B-测试lora工作流_2042946925502144514.json, 图片生成/图生图/klein 添加真实细节_2027767576952049665.json, 图片生成/图生图/klein(多图编辑)_2016069562856378370.json, 图片生成/图生图/klein+添加真实细节_2042527177735938050.json, 图片生成/图生图/kleinBFS换头，亚洲人也能换_2060971030277087233.json, 图片生成/图生图/klein_9B-文生图-测试lora工作流_2114325174177845249.json, 图片生成/图生图/klein_9B-测试lora工作流_2114322690038390786.json, 图片生成/图生图/klein_KV直出_2022222084566425602.json, 图片生成/图生图/赛博朋克画风_2029859105694814210.json, 图片生成/文生图/klein多图编辑_2017934301005877250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/klein 9B-文生图-测试lora工作流_2046045126165798913.json、图片生成/图生图/klein 9B-文生图-测试lora工作流_2046055960355016705.json、图片生成/图生图/klein 9B-测试lora工作流_2042946925502144514.json、图片生成/图生图/klein 添加真实细节_2027767576952049665.json、图片生成/图生图/klein(多图编辑)_2016069562856378370.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `CLIPLoader` —— 10/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `UNETLoader` —— 10/12 个有
- `GetImageSize` —— 9/12 个有
- `VAEEncode` —— 9/12 个有
- `CR Text` —— 7/12 个有
- `Image Comparer (rgthree)` —— 7/12 个有
- `ImageScaleToTotalPixels` —— 7/12 个有
- `CustomAddLabel` —— 5/12 个有
- `PDImageConcante` —— 5/12 个有
- `PreviewImage` —— 4/12 个有
- `Int` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `ImageResize+` —— 2/12 个有
- `LoadDiffusionModelShared //Inspire` —— 2/12 个有
- `LoadTextEncoderShared //Inspire` —— 2/12 个有
- `PD_ModelLoraLoader` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
