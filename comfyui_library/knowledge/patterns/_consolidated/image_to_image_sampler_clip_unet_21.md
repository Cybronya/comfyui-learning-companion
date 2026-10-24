---
name: image_to_image_sampler_clip_unet_21
type: Image To Image
frequency: 11
level: moderate
coverage: 0.931182
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein图生图工作流_2061337284183683073.json, 图片生成/图生图/Klein + Zimage图像细化+放大_2093345706391195650.json, 图片生成/图生图/Kook_Flux_Klein_Realphoto 单图编辑_2022704610548391937.json, 图片生成/图生图/【一分钟换脸，要啥自行车】_2081619387710271490.json, 图片生成/图生图/扩图-Kelin 无痕扩图 真实自然_2070011625867927553.json, 图片生成/图生图/扩图-Kelin_2031616716182134786.json, 图片生成/图生图/扩图-Kelin_2033562314321960961.json, 图片生成/图生图/扩图-Klein_2034187314091528194.json, 图片生成/图生图/扩图-Klein_2035293200839090178.json, 图片生成/图生图/扩图-Klein_2039522371379400706.json, 图片生成/图生图/蒜香卡普-Klein-9b_ 扩图-亚秒级无缝扩图_2034222233765289986.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux2-klein图生图工作流_2061337284183683073.json、图片生成/图生图/Klein + Zimage图像细化+放大_2093345706391195650.json、图片生成/图生图/Kook_Flux_Klein_Realphoto 单图编辑_2022704610548391937.json、图片生成/图生图/【一分钟换脸，要啥自行车】_2081619387710271490.json、图片生成/图生图/扩图-Kelin 无痕扩图 真实自然_2070011625867927553.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `ReferenceLatent` —— 9/11 个有
- `EmptyFlux2LatentImage` —— 8/11 个有
- `Image Comparer (rgthree)` —— 8/11 个有
- `FillMaskWithColor` —— 7/11 个有
- `ImagePadForOutpaint` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `ColorMatch` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `RTXVideoSuperResolution` —— 1/11 个有
- `UnetLoaderGGUF` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.3 | 11 | 92% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.2 - 1 | 11 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.3，11 个样本，取值集中（一致性 92%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，11 个样本
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
