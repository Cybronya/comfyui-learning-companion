---
name: unknown_workflow_sampler_unet_vae_52
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.924786
common_nodes: [CLIPLoader, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（qwen版clip）_2012417850039869441.json, 图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（条件串联）_2012413491184930818.json, 图片生成/图生图/【遇见AI】FLUX2-klein-base-4b，图像编辑_2012012542809350145.json, 图片生成/图生图/【遇见AI】FLUX2-klein-base-9b，图像编辑_2012020744510775298.json, 图片生成/图生图/【遇见AI】FLUX2多图参考_1993593282003402754.json, 图片生成/图生图/【遇见AI】texture2albedo-v2光影移除lora，基于klein9b模型_2071132171263369217.json, 图片生成/图生图/一键人像转3D建模_2031914265522737154.json, 图片生成/图生图/一键去万物工作流Seg3+Klein_2031956746331230209.json, 图片生成/图生图/交换角色位置_2042497890186170370.json, 图片生成/图生图/添加真实感细节 _ flux 2_1962490094668132354.json, 图片生成/文生图/Flux2-Turbo加速生图_2005931616717467650.json, 图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json, 图片生成/文生图/动作编辑器应用系列之一__FLUX-2-klein-9b_文生图_2022474573257641985.json, 图片生成/文生图/图1给姿势，图2给脸｜Flux Klein 双图融合工作流【全节点注释】_2070728938242011138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_52

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（qwen版clip）_2012417850039869441.json、图片生成/图生图/【遇见AI】FLUX2-klein-9b，多图参考（条件串联）_2012413491184930818.json、图片生成/图生图/【遇见AI】FLUX2-klein-base-4b，图像编辑_2012012542809350145.json、图片生成/图生图/【遇见AI】FLUX2-klein-base-9b，图像编辑_2012020744510775298.json、图片生成/图生图/【遇见AI】FLUX2多图参考_1993593282003402754.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
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
- `CLIPTextEncode` —— 13/14 个有
- `ReferenceLatent` —— 13/14 个有
- `BasicGuider` —— 11/14 个有
- `EmptyFlux2LatentImage` —— 9/14 个有
- `FluxGuidance` —— 9/14 个有
- `ImageScaleToTotalPixels` —— 9/14 个有
- `LoraLoaderModelOnly` —— 9/14 个有
- `GetImageSize` —— 6/14 个有
- `CFGGuider` —— 3/14 个有
- `ImpactImageInfo` —— 3/14 个有
- `AIO_Preprocessor` —— 2/14 个有
- `ConditioningZeroOut` —— 2/14 个有
- `GetImageSizeAndCount` —— 2/14 个有
- `Image Comparer (rgthree)` —— 2/14 个有
- `VRAMReserver` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `TextEncodeQwenImageEditPlus` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
