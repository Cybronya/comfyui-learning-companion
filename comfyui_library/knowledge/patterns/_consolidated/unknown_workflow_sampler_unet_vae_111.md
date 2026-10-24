---
name: unknown_workflow_sampler_unet_vae_111
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.819889
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Q版3D女孩生成器_1977989588658651138.json, 图片生成/文生图/incontext-controlnet-home_1914936305506287617.json, 图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json, 图片生成/文生图/incontextlora-人物肖像_1915236159570509826.json, 图片生成/文生图/一致性美女小红书网图神器｜Flux_1909542088999116801.json, 图片生成/文生图/一键微电影分镜-flux完全人物一致+自动裁剪-三分镜_1911275546050002945.json, 图片生成/文生图/国漫美女生成器_1965956635371941889.json, 图片生成/文生图/国漫美女生成器_2059552047061626882.json, 图片生成/文生图/赤木晴子生成工作流_1923305531946299393.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_111

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Q版3D女孩生成器_1977989588658651138.json、图片生成/文生图/incontext-controlnet-home_1914936305506287617.json、图片生成/文生图/incontextlora-filmstoryboard_1915225224143372289.json、图片生成/文生图/incontextlora-人物肖像_1915236159570509826.json、图片生成/文生图/一致性美女小红书网图神器｜Flux_1909542088999116801.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `ModelSamplingFlux` —— 8/9 个有
- `LoraLoader` —— 7/9 个有
- `CLIPTextEncode` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `CLIPTextEncodeFlux` —— 4/9 个有
- `FluxGuidance` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `PrimitiveInt` —— 2/9 个有
- `easy int` —— 2/9 个有
- `EmptyLatentImage` —— 1/9 个有
- `ImageCrop+` —— 1/9 个有
- `ImpactInt` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 7 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，7 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
