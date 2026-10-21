---
name: unknown_workflow_sampler_clip_vae_9
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.964667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FluxGuidance, InjectLatentNoise+, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmasDenoise, VAEDecode, VAELoader]
problems: []
missing: [InjectLatentNoise+, Upscale Model Loader]
members: [图片生成/文生图/1916028810548936705.json, 图片生成/文生图/5 图 18 分钟炼 LoRA，任意场景秒换不换脸_2012576047841157121.json, 图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json, 图片生成/文生图/抖音网红脸cos敖闰_1892232669667745794.json, 图片生成/文生图/抖音美女跳舞图片环节_1867930205196271617.json, 图片生成/文生图/炉鼎之家-文生图_1889684383299788802.json, 图片生成/文生图/颜值网红美女工作流_1896063182081490945.json, 视频生成/图生视频/1932281057691729921.json, 视频生成/文生视频/1930226449242865665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1916028810548936705.json、图片生成/文生图/5 图 18 分钟炼 LoRA，任意场景秒换不换脸_2012576047841157121.json、图片生成/文生图/F.1 - 极致逼真文生图（噪声注入）_2007506616567992322.json、图片生成/文生图/抖音网红脸cos敖闰_1892232669667745794.json、图片生成/文生图/抖音美女跳舞图片环节_1867930205196271617.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FluxGuidance`
- `InjectLatentNoise+`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmasDenoise`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `LatentUpscaleBy` —— 5/9 个有
- `CR Aspect Ratio` —— 4/9 个有
- `EmptySD3LatentImage` —— 3/9 个有
- `LoraLoader` —— 3/9 个有
- `UltimateSDUpscale` —— 3/9 个有
- `Upscale Model Loader` —— 3/9 个有
- `BetterFilmGrain` —— 2/9 个有
- `CheckpointLoaderSimple` —— 2/9 个有
- `EmptyLatentImage` —— 2/9 个有
- `ImageSmartSharpen+` —— 2/9 个有
- `LatentInterpolate` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `ExpressionEditor` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `Simple String` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.7 - 0.9 | 3 | 89% |
| LoRA 文本强度 | 0.9 | 0.7 - 0.9 | 3 | 89% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1760 | - | 2 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.7 - 0.9，3 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，观测区间 0.7 - 0.9，3 个样本，取值集中（一致性 89%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1760，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 这些节点还没有知识卡，系统对它们的理解有限：InjectLatentNoise+、Upscale Model Loader
