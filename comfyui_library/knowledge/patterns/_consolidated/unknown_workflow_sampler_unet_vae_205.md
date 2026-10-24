---
name: unknown_workflow_sampler_unet_vae_205
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.981
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/极简——FLUX pulid换脸_1943683612560723970.json, 图片生成/图生图/直播汉服写真_1913521276361633794.json, 图片生成/图生图/角色一致性_1938427878101155842.json, 图片生成/文生图/Flux  dev fp8  PuLID 文生图换脸工作流_2002388093422432257.json, 图片生成/文生图/极简——FLUX pulid换脸_1940416147244167169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_205

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/极简——FLUX pulid换脸_1943683612560723970.json、图片生成/图生图/直播汉服写真_1913521276361633794.json、图片生成/图生图/角色一致性_1938427878101155842.json、图片生成/文生图/Flux  dev fp8  PuLID 文生图换脸工作流_2002388093422432257.json、图片生成/文生图/极简——FLUX pulid换脸_1940416147244167169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `CLIPTextEncodeFlux` —— 3/5 个有
- `CLIPLoaderGGUF` —— 2/5 个有
- `CLIPTextEncode` —— 2/5 个有
- `FluxGuidance` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PulidFluxFaceDetector` —— 1/5 个有
- `PulidFluxOptions` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1576 | - | 1 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
