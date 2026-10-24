---
name: unknown_workflow_sampler_clip_unet_416
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.93
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, Florence2Run, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux1-krea-dev 图生图_1951291484605722625.json, 图片生成/图生图/flux图片高清放大_1902298925074919425.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_416

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux1-krea-dev 图生图_1951291484605722625.json、图片生成/图生图/flux图片高清放大_1902298925074919425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
