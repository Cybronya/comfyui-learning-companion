---
name: text_to_image_lora_sampler_clip_229
type: Text To Image
frequency: 8
level: strong
coverage: 0.890625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image turbo洗图利器｜图生图效果出众又快又好_2101526094900981762.json, 图片生成/图生图/Z-Image图生图洗图｜旧图重绘翻新画质直出更耐看_2112891527868542978.json, 图片生成/图生图/aesthetic-v1.1局部重绘｜Anima动漫图生图编辑_2093831024676524033.json, 图片生成/图生图/aesthetic-v1.1局部重绘｜Anima图生图一键处理_2094040960849244161.json, 图片生成/图生图/动漫局部重绘+图像反推｜Anima图生图工作流_2094039635407237121.json, 图片生成/图生图/动漫局部重绘图像反推｜Anima图生图编辑_2093826830473195522.json, 图片生成/图生图/动漫局部重绘工作流｜Anima图生图一键精修处理_2094008235165577217.json, 图片生成/图生图/动漫局部重绘｜Anima图生图编辑一键修改_2093771756107550722.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_229

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-Image turbo洗图利器｜图生图效果出众又快又好_2101526094900981762.json、图片生成/图生图/Z-Image图生图洗图｜旧图重绘翻新画质直出更耐看_2112891527868542978.json、图片生成/图生图/aesthetic-v1.1局部重绘｜Anima动漫图生图编辑_2093831024676524033.json、图片生成/图生图/aesthetic-v1.1局部重绘｜Anima图生图一键处理_2094040960849244161.json、图片生成/图生图/动漫局部重绘+图像反推｜Anima图生图工作流_2094039635407237121.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `AnimaLLLiteApply` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ModelPatchLoader` —— 6/8 个有
- `SetLatentNoiseMask` —— 6/8 个有
- `Mask Fill Holes` —— 4/8 个有
- `MaskFillHoles` —— 2/8 个有
- `ToriiGateT8_GroundingBuilder` —— 2/8 个有
- `ToriiGateT8_LlamaCppVisionGenerate` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `RepeatLatentBatch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（16/8 个样本）：Steps较低可能导致细节不足
