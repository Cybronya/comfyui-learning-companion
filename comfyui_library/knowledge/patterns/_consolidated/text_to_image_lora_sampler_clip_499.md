---
name: text_to_image_lora_sampler_clip_499
type: Text To Image
frequency: 3
level: strong
coverage: 0.652667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, DapaoMakeImageBatchNode, EmptyLatentImage, ExecutionBlocker, GetNode, ImpactNeg, JjkText, JsonExtractString, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveInt, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330.json, 图片生成/图生图/Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193.json, 图片生成/图生图/提示词强化Qwen Image 2.1文生图图生图处理工具_2102492597783719938.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_499

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image 2.1图像编辑4步加速版，反推提示词图生图高效处理工具_2103938725637091330.json、图片生成/图生图/Qwen image 2.1提示词强化｜反推提示词自动扩写｜文生图效果翻倍_2102233840218632193.json、图片生成/图生图/提示词强化Qwen Image 2.1文生图图生图处理工具_2102492597783719938.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `DapaoMakeImageBatchNode`
- `EmptyLatentImage`
- `ExecutionBlocker`
- `GetNode`
- `ImpactNeg`
- `JjkText`
- `JsonExtractString`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `1hew_SaveTxt` —— 2/3 个有
- `MathExpression_UTK` —— 2/3 个有
- `RHLLMChatNode` —— 2/3 个有
- `CM_BoolToInt` —— 1/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `ImageRGBA2RGB` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有
- `SaveLatent` —— 1/3 个有
- `TextEncodeQwenImage21` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
