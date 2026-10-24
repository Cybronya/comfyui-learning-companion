---
name: unknown_workflow_sampler_clip_unet_443
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9565
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json, 图片生成/文生图/Shuttle Jaguar 4步快速出图_1940292234132766721.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_443

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FluxKrea - ImageGeneration  文生图工作流_1951504768676122625.json、图片生成/文生图/Shuttle Jaguar 4步快速出图_1940292234132766721.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
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
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Primitive string multiline [Crystools]` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 836 | - | 2 | 92% |
| 高度 | 1024 | - | 2 | 75% |
| LoRA 模型强度 | 0.9 | - | 1 | 100% |
| LoRA 文本强度 | 0.9 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 836，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
