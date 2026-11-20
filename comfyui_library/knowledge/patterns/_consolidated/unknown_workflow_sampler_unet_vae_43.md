---
name: unknown_workflow_sampler_unet_vae_43
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.944059
common_nodes: [CLIPLoader, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（qwen版clip）_2012417850039869441.json, 图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（条件串联）_2012413491184930818.json, 图片生成/图生图/【遇见AI】FLUX2-klein-base-4b，图像编辑_2012012542809350145.json, 图片生成/图生图/【遇见AI】FLUX2-klein-base-9b，图像编辑_2012020744510775298.json, 图片生成/图生图/【遇见AI】FLUX2多图参考_1993593282003402754.json, 图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json, 图片生成/图生图/【阡陌】FLUX-2-Klein 9B base版单图编辑工作流_2016508238623154177.json, 图片生成/图生图/一次出图100张 海量图生图 多角度 保持人物一致 Flux2 Klein 9B Klein  一图_2027279328433676290.json, 图片生成/图生图/一键高品质产品精修Klein_2014308186299310082.json, 图片生成/图生图/万物迁移工作流_2036348251548426241.json, "平台全量/Flux-2-Klein-9B 图片增加真实感,真实摄影质感，干净皮肤，增加真实细节，清晰去AI油腻_2021450229274382338.json", 平台全量/Flux2 Klein 9B Klein 海量 一图生多图 保持人物一致 多角度_2017795358658662401.json, 平台全量/Klein 渲染现实_1890339748198653953.json, 平台全量/写实渲染 优化皮肤细节 高清放大 增加细节 去除AI塑料感 Flux2 Klein_2022499898502942722.json, 平台全量/增强真实感、皮肤毛孔细节｜Flux2 Klein_2026625608498810881.json, 平台全量/多角度 保持人物一致 Flux2 Klein 9B Klein 海量图生图 一图生多图_2026093486969200641.json, 平台全量/海量图生图 多角度生图 保持人物一致 Flux2 Klein 9B Klein  一图生多图海量图生_2027922013146320898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_43

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（qwen版clip）_2012417850039869441.json、图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（条件串联）_2012413491184930818.json、图片生成/图生图/【遇见AI】FLUX2-klein-base-4b，图像编辑_2012012542809350145.json、图片生成/图生图/【遇见AI】FLUX2-klein-base-9b，图像编辑_2012020744510775298.json、图片生成/图生图/【遇见AI】FLUX2多图参考_1993593282003402754.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 17 个 workflow 都包含：
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
- `CLIPTextEncode` —— 16/17 个有
- `ReferenceLatent` —— 16/17 个有
- `ImageScaleToTotalPixels` —— 12/17 个有
- `CFGGuider` —— 11/17 个有
- `EmptyFlux2LatentImage` —— 11/17 个有
- `Image Comparer (rgthree)` —— 11/17 个有
- `ConditioningZeroOut` —— 10/17 个有
- `GetImageSize` —— 10/17 个有
- `BasicGuider` —— 6/17 个有
- `FluxGuidance` —— 6/17 个有
- `LoraLoaderModelOnly` —— 6/17 个有
- `CR Prompt List` —— 4/17 个有
- `easy promptLine` —— 4/17 个有
- `ImpactImageInfo` —— 3/17 个有
- `GetImageSizeAndCount` —— 2/17 个有
- `ColorMatch` —— 1/17 个有
- `TextEncodeQwenImageEditPlus` —— 1/17 个有
- `easy imageSize` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
