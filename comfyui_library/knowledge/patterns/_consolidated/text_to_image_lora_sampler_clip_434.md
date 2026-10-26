---
name: text_to_image_lora_sampler_clip_434
type: Text To Image
frequency: 4
level: strong
coverage: 0.826
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResizeImageMaskNode, ResolutionSelector, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634.json, 图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2103968730760962050.json, 图片生成/文生图/短剧角色资产批量生成｜角色图一键量产短剧制作利器_2113543227218415618.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_434

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 W版部位变大｜图生图局部调整随心改_2111777238613061634.json、图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json、图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2103968730760962050.json、图片生成/文生图/短剧角色资产批量生成｜角色图一键量产短剧制作利器_2113543227218415618.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Comfyui_Image_Proportional_Scaling` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `XB_BatchImages` —— 1/4 个有
- `easy promptLine` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（11/4 个样本）：Steps较低可能导致细节不足
