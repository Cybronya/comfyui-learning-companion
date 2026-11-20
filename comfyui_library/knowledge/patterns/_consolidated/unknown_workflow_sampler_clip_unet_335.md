---
name: unknown_workflow_sampler_clip_unet_335
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9175
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, Florence2ModelLoader, Florence2Run, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux1-krea-dev 图生图_1951291484605722625.json, 图片生成/图生图/flux图片高清放大_1902298925074919425.json, 平台全量/flux图片精修_1888104509544267777.json, 平台全量/高清修复_1890045410331832321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_335

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux1-krea-dev 图生图_1951291484605722625.json、图片生成/图生图/flux图片高清放大_1902298925074919425.json、平台全量/flux图片精修_1888104509544267777.json、平台全量/高清修复_1890045410331832321.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
