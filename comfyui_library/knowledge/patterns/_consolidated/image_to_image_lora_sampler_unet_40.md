---
name: image_to_image_lora_sampler_unet_40
type: Image To Image
frequency: 12
level: strong
coverage: 0.819083
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AA--批量一键出17个角度图-Qwen edit 2511 多角度多镜头+放大 -LORA工具_2010631126053818370.json, 图片生成/图生图/AA--自由选择图片角度-Qwen edit 2511 多角度多镜头+放大_2010621302566031361.json, 图片生成/图生图/DG：可视化的图片换视角+景别（柯基大佬的节点）_2009809256119279618.json, "图片生成/图生图/Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2061263817170051073.json", 图片生成/图生图/Qwen-2511-多角度相机控制_2009953736994594817.json, 图片生成/图生图/Qwen-2511-多角度相机控制_2080264904489132033.json, 图片生成/图生图/丰胸神器 一键变plump! - 千问Qwen2511_2005632117461708801.json, 图片生成/图生图/丰胸神器 一键变plump! - 千问Qwen2511_2030944455557124097.json, 图片生成/图生图/丰胸神器-胸部增大-雯雯的后宫_2075590081682960386.json, 图片生成/图生图/丰胸神器-胸部增强-胸部变大-一键变plump! Qwen2511_2077672131277705217.json, 图片生成/图生图/丰胸神器-胸部增强-胸部变大-一键变plump! Qwen2511_2077925230835748865.json, 图片生成/图生图/自由多角度-rubby_2009805802244149249.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_40

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/AA--批量一键出17个角度图-Qwen edit 2511 多角度多镜头+放大 -LORA工具_2010631126053818370.json、图片生成/图生图/AA--自由选择图片角度-Qwen edit 2511 多角度多镜头+放大_2010621302566031361.json、图片生成/图生图/DG：可视化的图片换视角+景别（柯基大佬的节点）_2009809256119279618.json、图片生成/图生图/Qwen+Edit+2511+镜头多角度控制,一张图片变换多个角度_2061263817170051073.json、图片生成/图生图/Qwen-2511-多角度相机控制_2009953736994594817.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 7/12 个有
- `Image Comparer (rgthree)` —— 7/12 个有
- `QwenMultiangleCameraNode` —— 7/12 个有
- `SeedVR2LoadDiTModel` —— 7/12 个有
- `SeedVR2LoadVAEModel` —— 7/12 个有
- `SeedVR2VideoUpscaler` —— 7/12 个有
- `easy showAnything` —— 7/12 个有
- `easy promptList` —— 6/12 个有
- `Fast Groups Muter (rgthree)` —— 5/12 个有
- `EmptySD3LatentImage` —— 4/12 个有
- `GetNode` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `INTConstant` —— 2/12 个有
- `KepStringList` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
