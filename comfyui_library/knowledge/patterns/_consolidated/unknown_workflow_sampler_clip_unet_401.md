---
name: unknown_workflow_sampler_clip_unet_401
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.920333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/klein-9B 文生图_2058031589531148289.json, 图片生成/文生图/扎染-小帽子lora测l试_2062536155131895810.json, 图片生成/文生图/珠宝文生效果图_2102930912613847041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_401

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/klein-9B 文生图_2058031589531148289.json、图片生成/文生图/扎染-小帽子lora测l试_2062536155131895810.json、图片生成/文生图/珠宝文生效果图_2102930912613847041.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Primitive string multiline [Crystools]` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
