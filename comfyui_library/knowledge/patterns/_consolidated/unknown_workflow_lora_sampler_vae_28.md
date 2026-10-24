---
name: unknown_workflow_lora_sampler_vae_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9345
common_nodes: [AddLabel, BasicGuider, BasicScheduler, Create Grid Image from Batch, ImpactMakeImageList, Int, JoinStrings, KSamplerSelect, Lora Loader, RandomNoise, ReActorImageDublicator, SamplerCustomAdvanced, SaveImage, String, VAEDecode, easy anythingIndexSwitch, easy convertAnything, easy imageListToImageBatch, easy rangeFloat, easy rangeInt]
problems: []
missing: []
members: [图片生成/文生图/在线测试 FluxD  lora test_1956993926366420994.json, 图片生成/文生图/在线测试用SDXL  lora test_1956993471274782722.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/在线测试 FluxD  lora test_1956993926366420994.json、图片生成/文生图/在线测试用SDXL  lora test_1956993471274782722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `BasicGuider`
- `BasicScheduler`
- `Create Grid Image from Batch`
- `ImpactMakeImageList`
- `Int`
- `JoinStrings`
- `KSamplerSelect`
- `Lora Loader`
- `RandomNoise`
- `ReActorImageDublicator`
- `SamplerCustomAdvanced`
- `SaveImage`
- `String`
- `VAEDecode`
- `easy anythingIndexSwitch`
- `easy convertAnything`
- `easy imageListToImageBatch`
- `easy rangeFloat`
- `easy rangeInt`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `Efficient Loader` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
