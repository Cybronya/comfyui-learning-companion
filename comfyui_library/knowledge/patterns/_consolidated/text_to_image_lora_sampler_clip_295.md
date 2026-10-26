---
name: text_to_image_lora_sampler_clip_295
type: Text To Image
frequency: 7
level: strong
coverage: 0.877286
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json, 图片生成/图生图/qwen image 2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102232264989036546.json, 图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json, 图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json, 图片生成/图生图/qwen2.1移除rgba通道 透明背景图处理_2104688268930535425.json, 图片生成/文生图/Qwen Image 2.1 ControlNet工作流，精准控制改图文生图图生图方案_2106521489427222529.json, 图片生成/文生图/qwen_image_21_controlnet可控生成｜文生图图生图精准控制_2106248623163011074.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_295

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen2.1图像编辑PE增强版，已清理think的图生图处理工作流_2103888095346257922.json、图片生成/图生图/qwen image 2.1编辑工作流｜文生图图生图双支持｜日常改图必备款_2102232264989036546.json、图片生成/图生图/qwen2.1图像编辑 局部修改指令式操作_2104648645625860097.json、图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json、图片生成/图生图/qwen2.1移除rgba通道 透明背景图处理_2104688268930535425.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `StringConstantMultiline` —— 6/7 个有
- `StringFunction|pysssss` —— 6/7 个有
- `StringReplace` —— 6/7 个有
- `TextGenerate` —— 6/7 个有
- `easy seed` —— 6/7 个有
- `FluxKontextImageScale` —— 5/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `ModelPatchLoader` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `ZImageFunControlnet` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `TextGenerateLTX2Prompt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
