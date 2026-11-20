---
name: text_to_image_lora_sampler_clip_330
type: Text To Image
frequency: 6
level: strong
coverage: 0.7485
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json, 图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json, 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json, 图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json, 图片生成/文生图/Qwen Image 2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2102900918982369281.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_330

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1文生图图片编辑多合一处理工具_2102551057128845314.json、图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json、图片生成/图生图/Qwen_Image_2.1文生图与图片编辑合一，电商产品图生图多场景适用_2105519436647190529.json、图片生成/图生图/Qwen_Image_2.1文生图与图片编辑多合一，产品精修场景融合风格迁移全覆盖_2104735854735482881.json、图片生成/文生图/Qwen Image 2.1文生图与图片编辑合一，电商产品图生图多场景适用_2102855288981377025.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Fast Groups Muter (rgthree)` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `XB_BatchImages` —— 5/6 个有
- `easy boolean` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `ComfySwitchNode` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `ImpactConditionalBranch` —— 3/6 个有
- `ComfySwitchNodeV2` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `SaveImageAdvanced` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `Any To String (mtb)` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
