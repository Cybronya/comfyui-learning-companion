---
name: unknown_workflow_sampler_clip_unet_417
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux全能洗图工作流_1912403868913758209.json, 图片生成/图生图/图生开通图_1907491424999206913.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_417

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux全能洗图工作流_1912403868913758209.json、图片生成/图生图/图生开通图_1907491424999206913.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `Get Image Size` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LatentToWidthHeight` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Seed Everywhere` —— 1/2 个有
- `SplitSigmasDenoise` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
