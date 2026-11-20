---
name: unknown_workflow_sampler_clip_unet_260
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.823167
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, KSamplerSelect, LayerUtility: TextJoin, LoadImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键生成新年头像_1892845550293979138.json, 图片生成/图生图/宫崎骏吉卜力 Ghibli_1910150250202628098.json, 图片生成/图生图/生成专属 JelleyCat 毛绒玩具 一键生图系列_1908158686215155713.json, 图片生成/文生图/地标冰箱贴+全节点注释_2055980297757437953.json, 图片生成/文生图/宠物冰箱贴+全节点注释_2054823619720687618.json, 平台全量/定制人像专属冰箱贴_1909502444630646786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_260

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键生成新年头像_1892845550293979138.json、图片生成/图生图/宫崎骏吉卜力 Ghibli_1910150250202628098.json、图片生成/图生图/生成专属 JelleyCat 毛绒玩具 一键生图系列_1908158686215155713.json、图片生成/文生图/地标冰箱贴+全节点注释_2055980297757437953.json、图片生成/文生图/宠物冰箱贴+全节点注释_2054823619720687618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `KSamplerSelect`
- `LayerUtility: TextJoin`
- `LoadImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `LoraLoader` —— 5/6 个有
- `MaskToSEGS` —— 5/6 个有
- `ModelSamplingFlux` —— 5/6 个有
- `SDXLAspectRatioSelector` —— 5/6 个有
- `SEGSPreview` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `ConstrainImage|pysssss` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `RH_Captioner` —— 3/6 个有
- `LoadImageFromUrl` —— 2/6 个有
- `Text _O` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `JWStringMultiline` —— 1/6 个有
- `Joy_caption` —— 1/6 个有
- `Joy_caption_load` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `SaveImageAndMetadata_` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 768 - 832 | 6 | 97% |
| 高度 | 1216 | 1024 - 1216 | 6 | 94% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 768 - 832，6 个样本，取值集中（一致性 97%）
- 高度 中位数 1216，观测区间 1024 - 1216，6 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
