---
name: unknown_workflow_sampler_vae_44
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.972125
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/极简——FLUX pulid换脸_1943683612560723970.json, 图片生成/图生图/直播汉服写真_1913521276361633794.json, 图片生成/图生图/角色一致性_1938427878101155842.json, 图片生成/文生图/Flux  dev fp8  PuLID 文生图换脸工作流_2002388093422432257.json, 图片生成/文生图/极简——FLUX pulid换脸_1940416147244167169.json, 平台全量/FLUX+PuLID换脸工作流_1942946766289592322.json, 平台全量/Q 版悟空_1851174621277024257.json, 平台全量/flux_pulid换脸工作流_1898666816447959042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_44

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/极简——FLUX pulid换脸_1943683612560723970.json、图片生成/图生图/直播汉服写真_1913521276361633794.json、图片生成/图生图/角色一致性_1938427878101155842.json、图片生成/文生图/Flux  dev fp8  PuLID 文生图换脸工作流_2002388093422432257.json、图片生成/文生图/极简——FLUX pulid换脸_1940416147244167169.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 7/8 个有
- `EmptySD3LatentImage` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `CLIPTextEncode` —— 5/8 个有
- `FluxGuidance` —— 5/8 个有
- `UnetLoaderGGUF` —— 5/8 个有
- `VAEEncode` —— 4/8 个有
- `CLIPTextEncodeFlux` —— 3/8 个有
- `DualCLIPLoaderGGUF` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `CLIPLoaderGGUF` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `PulidFluxFaceDetector` —— 1/8 个有
- `PulidFluxOptions` —— 1/8 个有
- `RandomPrompt` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1576 | - | 1 | 100% |
| LoRA 模型强度 | 0.9 | 0.8 - 1 | 3 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.8 - 1，3 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
