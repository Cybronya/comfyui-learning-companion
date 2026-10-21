---
name: unknown_workflow_sampler_vae_22
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.972583
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1940292234132766721.json, 图片生成/文生图/1942505597264924674.json, 图片生成/文生图/1942877686643798017.json, 图片生成/文生图/1946106579613609985.json, 图片生成/文生图/1951132199200432130.json, 图片生成/文生图/1951288327628599298.json, 图片生成/文生图/1952013936583495682.json, 图片生成/文生图/1957765376640909314.json, 图片生成/文生图/1964223507485872129.json, 图片生成/文生图/1971036023260123138.json, 图片生成/文生图/Flux1微胖性感美女生成大胸美女图123_2002414890683908097.json, 图片生成/文生图/flux1-dev-fp8与flux1-dev-Q4模型对比_1836327501579841537.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1940292234132766721.json、图片生成/文生图/1942505597264924674.json、图片生成/文生图/1942877686643798017.json、图片生成/文生图/1946106579613609985.json、图片生成/文生图/1951132199200432130.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 11/12 个有
- `UNETLoader` —— 11/12 个有
- `CLIPTextEncode` —— 8/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `FluxGuidance` —— 6/12 个有
- `CLIPTextEncodeFlux` —— 4/12 个有
- `RH_Translator` —— 3/12 个有
- `PreviewImage` —— 2/12 个有
- `UnetLoaderGGUF` —— 2/12 个有
- `DualCLIPLoaderGGUF` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `RandomPrompt` —— 1/12 个有
- `SDXLEmptyLatentSizePicker+` —— 1/12 个有
- `StringFunction|pysssss` —— 1/12 个有
- `TextInput_` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1280 | 11 | 78% |
| 高度 | 1280 | 1 - 1920 | 12 | 44% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1280，11 个样本
- 高度 中位数 1280，观测区间 1 - 1920，12 个样本，取值分散，一致性仅 44%
