---
name: text_to_image_lora_sampler_clip_347
type: Text To Image
frequency: 5
level: strong
coverage: 0.808
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Muter (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, XB_BatchImages, easy boolean, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json, 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json, 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_347

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json、图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json、图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XB_BatchImages`
- `easy boolean`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `ImpactConditionalBranch` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `ComfySwitchNodeV2` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Any To String (mtb)` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `SaveImageAdvanced` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
