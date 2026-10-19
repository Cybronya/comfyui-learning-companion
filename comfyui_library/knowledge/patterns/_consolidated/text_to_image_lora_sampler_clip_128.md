---
name: text_to_image_lora_sampler_clip_128
type: Text To Image
frequency: 7
level: strong
coverage: 0.668286
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy seed]
members: [图片生成/图生图/2102591631139622913.json, 图片生成/文生图/Qwen Image 2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2102888298095140865.json, 图片生成/文生图/Qwen Image 2.1图像编辑工作流，图生图处理高质量方案_2105774125573828610.json, 图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json, 视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json, 视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json, 视频生成/图生视频/Qwen_Image_2.1故事分镜参考图生成，支持九宫格六宫格四宫格三种模式_2106549378277273601.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102591631139622913.json、图片生成/文生图/Qwen Image 2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2102888298095140865.json、图片生成/文生图/Qwen Image 2.1图像编辑工作流，图生图处理高质量方案_2105774125573828610.json、图片生成/文生图/Qwen image 2.1图像编辑加文生图 二合一工作流_2105110276558381057.json、视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `PreviewAny` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `easy seed` —— 5/7 个有
- `孤海注释` —— 5/7 个有
- `BatchImagesNode` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `TextGenerateLTX2Prompt` —— 4/7 个有
- `EmptyImage` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `RHLLMChatNode` —— 3/7 个有
- `StringConcatenate` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy seed
