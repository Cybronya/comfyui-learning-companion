---
name: text_to_image_lora_sampler_clip_388
type: Text To Image
frequency: 5
level: moderate
coverage: 0.7434
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenImage_Edit_满血版-8步生图_1958022139515482113.json, 图片生成/图生图/任意角度分镜制作-qwen edit 2511_2010346866856173570.json, 图片生成/图生图/千问双图QwenImage_Edit_2509-8步双图版_1972574913502572546.json, 图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json, 图片生成/图生图/效果图人物改变相机角度，直接拖动改为位置即可_2015794374164094978.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_388

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QwenImage_Edit_满血版-8步生图_1958022139515482113.json、图片生成/图生图/任意角度分镜制作-qwen edit 2511_2010346866856173570.json、图片生成/图生图/千问双图QwenImage_Edit_2509-8步双图版_1972574913502572546.json、图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json、图片生成/图生图/效果图人物改变相机角度，直接拖动改为位置即可_2015794374164094978.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenMultiangleCameraNode` —— 3/5 个有
- `TextEncodeQwenImageEditPlus` —— 3/5 个有
- `easy imageSize` —— 3/5 个有
- `CR Simple Image Compare` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `String Literal` —— 2/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/5 个有
- `CR Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 5 | 65% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1280 | 512 - 1280 | 5 | 61% |
| 高度 | 720 | 512 - 720 | 5 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 512 - 1280，5 个样本
- 高度 中位数 720，观测区间 512 - 720，5 个样本，取值集中（一致性 84%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
