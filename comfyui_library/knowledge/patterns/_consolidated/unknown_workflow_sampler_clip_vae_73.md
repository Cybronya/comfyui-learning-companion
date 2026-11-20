---
name: unknown_workflow_sampler_clip_vae_73
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.971
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json, 图片生成/文生图/Shuttle Jaguar 4步快速出图_1940292234132766721.json, 图片生成/文生图/超高清  文生卡通图_1907499231920156674.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_73

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json、图片生成/文生图/Shuttle Jaguar 4步快速出图_1940292234132766721.json、图片生成/文生图/超高清  文生卡通图_1907499231920156674.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 1/3 个有
- `LatentToWidthHeight` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `Primitive string multiline [Crystools]` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 904 | 768 - 1024 | 3 | 88% |
| 高度 | 1024 | 768 - 1280 | 3 | 80% |
| LoRA 模型强度 | 0.9 | - | 1 | 100% |
| LoRA 文本强度 | 0.9 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 904，观测区间 768 - 1024，3 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 768 - 1280，3 个样本
