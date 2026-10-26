---
name: unknown_workflow_sampler_unet_vae_96
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9575
common_nodes: [CLIPLoader, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（qwen版clip）_2012417850039869441.json, 图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（条件串联）_2012413491184930818.json, 图片生成/图生图/【遇见AI】FLUX2-klein-base-4b，图像编辑_2012012542809350145.json, 图片生成/图生图/【遇见AI】FLUX2-klein-base-9b，图像编辑_2012020744510775298.json, 图片生成/图生图/【遇见AI】FLUX2多图参考_1993593282003402754.json, 图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json, 图片生成/图生图/【阡陌】FLUX-2-Klein 9B base版单图编辑工作流_2016508238623154177.json, 图片生成/图生图/一次出图100张 海量图生图 多角度 保持人物一致 Flux2 Klein 9B Klein  一图_2027279328433676290.json, 图片生成/图生图/一键高品质产品精修Klein_2014308186299310082.json, 图片生成/图生图/万物迁移工作流_2036348251548426241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_96

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（qwen版clip）_2012417850039869441.json、图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（条件串联）_2012413491184930818.json、图片生成/图生图/【遇见AI】FLUX2-klein-base-4b，图像编辑_2012012542809350145.json、图片生成/图生图/【遇见AI】FLUX2-klein-base-9b，图像编辑_2012020744510775298.json、图片生成/图生图/【遇见AI】FLUX2多图参考_1993593282003402754.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/10 个有
- `ReferenceLatent` —— 9/10 个有
- `BasicGuider` —— 6/10 个有
- `FluxGuidance` —— 6/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `CFGGuider` —— 4/10 个有
- `EmptyFlux2LatentImage` —— 4/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `GetImageSize` —— 3/10 个有
- `ImpactImageInfo` —— 3/10 个有
- `GetImageSizeAndCount` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `CR Prompt List` —— 1/10 个有
- `ColorMatch` —— 1/10 个有
- `TextEncodeQwenImageEditPlus` —— 1/10 个有
- `easy imageSize` —— 1/10 个有
- `easy promptLine` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
