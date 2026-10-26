---
name: image_to_image_lora_sampler_unet_84
type: Image To Image
frequency: 7
level: strong
coverage: 0.737286
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AA--批量一键出17个角度图-Qwen edit 2511 多角度多镜头+放大 -LORA工具_2010631126053818370.json, 图片生成/图生图/AA--自由选择图片角度-Qwen edit 2511 多角度多镜头+放大_2010621302566031361.json, 图片生成/图生图/DG：可视化的图片换视角+景别（柯基大佬的节点）_2009809256119279618.json, "图片生成/图生图/Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2061263817170051073.json", 图片生成/图生图/Qwen-2511-多角度相机控制_2009953736994594817.json, 图片生成/图生图/Qwen-2511-多角度相机控制_2080264904489132033.json, 图片生成/图生图/Qwen_Flux _ 一键多角度控制 可自动 可手动 精准构图_2057547027516579841.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/AA--批量一键出17个角度图-Qwen edit 2511 多角度多镜头+放大 -LORA工具_2010631126053818370.json、图片生成/图生图/AA--自由选择图片角度-Qwen edit 2511 多角度多镜头+放大_2010621302566031361.json、图片生成/图生图/DG：可视化的图片换视角+景别（柯基大佬的节点）_2009809256119279618.json、图片生成/图生图/Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2061263817170051073.json、图片生成/图生图/Qwen-2511-多角度相机控制_2009953736994594817.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `easy promptList` —— 5/7 个有
- `EmptySD3LatentImage` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `KepStringList` —— 2/7 个有
- `SeedVR2LoadDiTModel` —— 2/7 个有
- `SeedVR2LoadVAEModel` —— 2/7 个有
- `SeedVR2VideoUpscaler` —— 2/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 7 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
