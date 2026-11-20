---
name: image_to_image_sampler_clip_unet_75
type: Image To Image
frequency: 6
level: strong
coverage: 0.939333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SRPO重绘修复工作流——提升细节质感_2073084527190302722.json, 图片生成/图生图/【遇见AI】flux-kontext 单图编辑工作流_2050856923859308546.json, 图片生成/图生图/全能视频S真人前置-素描Kontext_1974104968892387330.json, 图片生成/图生图/图像高清去模糊deblur(Kontext-LORA版)_1943499477413994497.json, 图片生成/图生图/小红书爆款3D emoji小人_1956325155729539073.json, 图片生成/文生图/喜剧复古动漫风格2.0_1942402202403024898.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/SRPO重绘修复工作流——提升细节质感_2073084527190302722.json、图片生成/图生图/【遇见AI】flux-kontext 单图编辑工作流_2050856923859308546.json、图片生成/图生图/全能视频S真人前置-素描Kontext_1974104968892387330.json、图片生成/图生图/图像高清去模糊deblur(Kontext-LORA版)_1943499477413994497.json、图片生成/图生图/小红书爆款3D emoji小人_1956325155729539073.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `RH_Captioner` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `CR Text Replace` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ShowText` —— 2/6 个有
- `Display Any (rgthree)` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `Image Resize To Width` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 0.5 - 1 | 6 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，6 个样本
