---
name: text_to_image_lora_sampler_clip_197
type: Text To Image
frequency: 9
level: strong
coverage: 0.882222
common_nodes: [CLIPLoader, CLIPTextEncode, CM_FloatToInt, CM_FloatUnaryOperation, CM_IntToFloat, CR Prompt Text, EmptyLatentImage, FL_ImageBatchToGrid, FluxKontextMultiReferenceLatentMethod, GetImageSizeAndCount, ImageListToBatch+, Int, JWIntegerToString, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, ProcessString, Qwen3_VQA_Plus, RH_LLMAPI_NODE, SaveImage, StringFunction|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy saveText, easy seed, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit NextScene｜图生图多分镜自动生成 8步写实写真_2097535884341112834.json, 图片生成/图生图/Qwen-Edit-NextScene-2511｜多分镜自动图生图8步一致性出图_2092615856743342081.json, 图片生成/图生图/Qwen-Edit-NextScene2511｜图生图多分镜自动8步_2107675125259792386.json, 图片生成/图生图/Qwen-Edit多分镜图生图｜NextScene 2511八步自动分镜_2099917725115179009.json, 图片生成/图生图/图生图加多分镜自动Qwen Edit NextScene 2511 8步工作流，角色一致性图生图_2107928830039117826.json, 图片生成/图生图/图生图加多分镜自动Qwen Edit NextScene 2511 8步工作流，角色一致性图生图_2107963550802210817.json, 图片生成/图生图/多分镜自动出图｜Qwen-Edit NextScene 2511八步，角色一致性_2099881138817949697.json, 图片生成/图生图/多分镜自动图生图｜Qwen-Edit-NextScene-2511-8步生成_2095101182455934978.json, 图片生成/图生图/多分镜自动生成｜Qwen Edit NextScene 2511图生图8步一致性出图_2090876709213138946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit NextScene｜图生图多分镜自动生成 8步写实写真_2097535884341112834.json、图片生成/图生图/Qwen-Edit-NextScene-2511｜多分镜自动图生图8步一致性出图_2092615856743342081.json、图片生成/图生图/Qwen-Edit-NextScene2511｜图生图多分镜自动8步_2107675125259792386.json、图片生成/图生图/Qwen-Edit多分镜图生图｜NextScene 2511八步自动分镜_2099917725115179009.json、图片生成/图生图/图生图加多分镜自动Qwen Edit NextScene 2511 8步工作流，角色一致性图生图_2107928830039117826.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_FloatUnaryOperation`
- `CM_IntToFloat`
- `CR Prompt Text`
- `EmptyLatentImage`
- `FL_ImageBatchToGrid`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSizeAndCount`
- `ImageListToBatch+`
- `Int`
- `JWIntegerToString`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ProcessString`
- `Qwen3_VQA_Plus`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `StringFunction|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy saveText`
- `easy seed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（18/9 个样本）：Steps较低可能导致细节不足
