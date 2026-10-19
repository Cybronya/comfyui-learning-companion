---
name: unknown_workflow_sampler_clip_unet_48
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.854333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Simple String]
members: [图片生成/文生图/1975910662452981761.json, 图片生成/文生图/1985963732088041473.json, 图片生成/文生图/FLUX模型基础工作流_1891394911315333122.json, 图片生成/文生图/WaveSpeed FLUX工作流加速神器_1879120968877830146.json, 图片生成/文生图/人物一致性6宫格小红书风格_1894278785376890882.json, 视频生成/图生视频/1879120968877830146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1975910662452981761.json、图片生成/文生图/1985963732088041473.json、图片生成/文生图/FLUX模型基础工作流_1891394911315333122.json、图片生成/文生图/WaveSpeed FLUX工作流加速神器_1879120968877830146.json、图片生成/文生图/人物一致性6宫格小红书风格_1894278785376890882.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ApplyFBCacheOnModel` —— 3/6 个有
- `EnhancedCompileModel` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `ControlNetApplySD3` —— 1/6 个有
- `ControlNetLoader` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `Simple String` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Simple String
