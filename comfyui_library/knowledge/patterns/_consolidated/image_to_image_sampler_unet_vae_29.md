---
name: image_to_image_sampler_unet_vae_29
type: Image To Image
frequency: 8
level: strong
coverage: 0.890875
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI一键换脸-Qwen2511工作流_2094961251532234753.json, 图片生成/图生图/AI修手-Qwen-Edit指令修图工作流_2095002727083495426.json, 图片生成/图生图/AI完美扩图-三档倍率原图零偏移工作流_2096613161687408642.json, 图片生成/图生图/AI无痕改字-图片文字一键替换工作流_2096603998215303170.json, 图片生成/图生图/Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281.json, 图片生成/图生图/全能图片2全能图片编辑-一句话P图工作流_2096603719419912194.json, 图片生成/图生图/全能图片G-Image-2.5图像编辑工作流_2098372807368470529.json, 图片生成/图生图/全能图片G-Image-2全能图片编辑-低价一句话P图工作流_2096603788789510146.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_29

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/AI一键换脸-Qwen2511工作流_2094961251532234753.json、图片生成/图生图/AI修手-Qwen-Edit指令修图工作流_2095002727083495426.json、图片生成/图生图/AI完美扩图-三档倍率原图零偏移工作流_2096613161687408642.json、图片生成/图生图/AI无痕改字-图片文字一键替换工作流_2096603998215303170.json、图片生成/图生图/Qwen Image 3.0图像编辑工作流｜多图融合一句话改图_2103056580613857281.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/8 个有
- `ComfyMathExpression` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `ImagePadForOutpaint` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 24 - 24 | 6 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 24 - 24，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
