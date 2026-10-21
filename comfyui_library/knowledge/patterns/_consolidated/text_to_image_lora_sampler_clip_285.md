---
name: text_to_image_lora_sampler_clip_285
type: Text To Image
frequency: 3
level: strong
coverage: 0.737667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Muter (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, XB_BatchImages, easy boolean, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [Any To String (mtb), CR Text, easy boolean, easy cleanGpuUsed]
members: [图片生成/图生图/2102551057128845314.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_285

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2102551057128845314.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImpactConditionalBranch` —— 2/3 个有
- `Any To String (mtb)` —— 1/3 个有
- `ComfySwitchNodeV2` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Any To String (mtb)、CR Text、easy boolean、easy cleanGpuUsed
