---
name: unknown_workflow_sampler_clip_unet_162
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.8935
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/5 图 18 分钟炼 LoRA，任意场景秒换不换脸_2012576047841157121.json, 图片生成/文生图/ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154.json, 图片生成/文生图/FLUX SRPO真实感文生图_1966782963511930881.json, 图片生成/文生图/FLUX 官方工作流 （教学用）_1955933159051460609.json, 图片生成/文生图/FLUX模型基础工作流_1891394911315333122.json, 图片生成/文生图/Flux+Lora控制角色一致生图-Base_1916028810548936705.json, 图片生成/文生图/人物一致性6宫格小红书风格_1894278785376890882.json, 视频生成/文生视频/古风场景_1930226449242865665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_162

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/5 图 18 分钟炼 LoRA，任意场景秒换不换脸_2012576047841157121.json、图片生成/文生图/ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154.json、图片生成/文生图/FLUX SRPO真实感文生图_1966782963511930881.json、图片生成/文生图/FLUX 官方工作流 （教学用）_1955933159051460609.json、图片生成/文生图/FLUX模型基础工作流_1891394911315333122.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
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
- `DisableNoise` —— 3/8 个有
- `InjectLatentNoise+` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `SplitSigmasDenoise` —— 3/8 个有
- `UltimateSDUpscale` —— 3/8 个有
- `Upscale Model Loader` —— 3/8 个有
- `BetterFilmGrain` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `ApplyFBCacheOnModel` —— 1/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `ExpressionEditor` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `Simple String` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.7 - 0.9 | 3 | 89% |
| LoRA 文本强度 | 0.9 | 0.7 - 0.9 | 3 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.7 - 0.9，3 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，观测区间 0.7 - 0.9，3 个样本，取值集中（一致性 89%）
