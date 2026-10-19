---
name: unknown_workflow_sampler_clip_unet_12
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.763286
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline, easy hiresFix, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1925124635254267905.json, 图片生成/文生图/1925427219194163201.json, 图片生成/文生图/1926115550580338689.json, 图片生成/文生图/1926262954042290178.json, 图片生成/文生图/1926264181538910210.json, 图片生成/文生图/1929399159059595265.json, 图片生成/文生图/1929847965068988417.json, 图片生成/文生图/1930161942738976770.json, 图片生成/文生图/1931186440095641601.json, 图片生成/文生图/1933213412669173762.json, 图片生成/文生图/1933315314153365506.json, 图片生成/文生图/1933821200713830402.json, 图片生成/文生图/1935575269891559426.json, 图片生成/文生图/1955199580277280770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/1925124635254267905.json、图片生成/文生图/1925427219194163201.json、图片生成/文生图/1926115550580338689.json、图片生成/文生图/1926262954042290178.json、图片生成/文生图/1926264181538910210.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 13/14 个有
- `PreviewImage` —— 11/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `JoinStrings` —— 9/14 个有
- `PrimitiveString` —— 9/14 个有
- `Text Multiline` —— 9/14 个有
- `easy hiresFix` —— 9/14 个有
- `CR SDXL Aspect Ratio` —— 2/14 个有
- `MagCache` —— 2/14 个有
- `ImageUpscaleWithModelBatched` —— 1/14 个有
- `TeaCache` —— 1/14 个有
- `UpscaleModelLoader` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy hiresFix、CR SDXL Aspect Ratio
