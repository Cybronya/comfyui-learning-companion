---
name: text_to_image_sampler_clip_unet_88
type: Text To Image
frequency: 7
level: strong
coverage: 0.865143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682.json, 图片生成/图生图/Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522.json, 图片生成/图生图/Qwen-image-edit-plus-2509-单图编辑_1991506158217338882.json, 图片生成/图生图/Qwen-image-edit-plus-2509-更改色调_1973677046226358273.json, 图片生成/图生图/Qwen-image-edit-plus-2509_1971563492245499905.json, 图片生成/图生图/qwen_image_多图合一-图片编辑_1970819754611118082.json, 图片生成/文生图/Qwen-image-edit-2059图像编辑_1973209775687208961.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit-plus-2509-lora-文生图工作流-触发词：maozhan_1979394793413447682.json、图片生成/图生图/Qwen-image-edit-plus-2509-lora-毛毡效果V2.0-图生图-触发词：maozhan_1995315430677995522.json、图片生成/图生图/Qwen-image-edit-plus-2509-单图编辑_1991506158217338882.json、图片生成/图生图/Qwen-image-edit-plus-2509-更改色调_1973677046226358273.json、图片生成/图生图/Qwen-image-edit-plus-2509_1971563492245499905.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/7 个有
- `AIO_Preprocessor` —— 3/7 个有
- `ImageStitch` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Int` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1864 | 768 - 1920 | 7 | 69% |
| 高度 | 1280 | 1024 - 1920 | 7 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1864，观测区间 768 - 1920，7 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，7 个样本
