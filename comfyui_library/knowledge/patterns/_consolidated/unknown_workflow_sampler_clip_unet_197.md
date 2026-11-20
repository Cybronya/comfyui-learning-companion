---
name: unknown_workflow_sampler_clip_unet_197
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.927
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kontext 单图编辑火柴人_1970786088950374402.json, 图片生成/文生图/flux-海报_1914942831851466753.json, 图片生成/文生图/人猫合影_1891781898589384705.json, 图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json, 图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json, 图片生成/文生图/文生图 krea适用于亚马逊_1985963732088041473.json, 图片生成/文生图/最新MagCache加速-Flux文生图_1933315314153365506.json, 图片生成/文生图/美漫手绘故事FLUX + LORA 基础工作流_1955199580277280770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_197

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Kontext 单图编辑火柴人_1970786088950374402.json、图片生成/文生图/flux-海报_1914942831851466753.json、图片生成/文生图/人猫合影_1891781898589384705.json、图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_1966775723971293186.json、图片生成/文生图/企鹅腾讯flux.1-dev-SRPO文生图_2040841926462676993.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 7/8 个有
- `CR SDXL Aspect Ratio` —— 5/8 个有
- `EmptySD3LatentImage` —— 5/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `RH_Translator` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageUpscaleWithModelBatched` —— 1/8 个有
- `MagCache` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `ReferenceLatent` —— 1/8 个有
- `TextInputNode` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
