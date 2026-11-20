---
name: unknown_workflow_lora_sampler_unet_30
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.893882
common_nodes: [CLIPLoader, CR Text, CR Text Replace, EmptySD3LatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最美文生图_2056557138692104194.json, 图片生成/图生图/模特套图工作流2026年3月_2034618803618844674.json, 图片生成/图生图/模特套图工作流V5_2030891757851910146.json, 图片生成/图生图/真人写真套图v1.0_2049333924999991298.json, 图片生成/图生图/美少女合集文生图_2056898268851953665.json, 图片生成/图生图/超好用🔥小红书一键套图-模特套图-多视角-多角度效果嘎嘎好_2046884202188115969.json, 图片生成/图生图/超清！QWEN 2511 EDIT qwen3.5vl 一键套图 9张不同模特姿势 图生图，巨好用！_2101517590890893314.json, 图片生成/图生图/超清！一键套图 9张不同模特姿势 图生图，巨好用！_2059921087705735170.json, 图片生成/图生图/🦄FireRed模特套图🎯天下无腰_2034663152297709569.json, 图片生成/文生图/Z+Image：极致写实图像 抖音小红书洗 风格迷人美学文生图_2047194111127588865.json, 图片生成/文生图/ZB文生图自动优化260406_2041135448864595970.json, 图片生成/文生图/ZIB-piaopiao-2605121822_2054132741498777601.json, 图片生成/文生图/ZT文生图自动优化260406_2041140677815308289.json, 图片生成/文生图/图生图 模特套图 一键套图 小红书 FireRed-Image-Edit_2044271313870659585.json, 平台全量/分镜多角度一致性_2044324991772135425.json, 平台全量/模特套图生成 人物更一致 场景更多样 构图更美观 照片更真实_2038433379640676354.json, 视频生成/图生视频/固定人物IP多场景生成V3.0（IP打造）人物一致性多图编辑_2041990716972343297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_30

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/最美文生图_2056557138692104194.json、图片生成/图生图/模特套图工作流2026年3月_2034618803618844674.json、图片生成/图生图/模特套图工作流V5_2030891757851910146.json、图片生成/图生图/真人写真套图v1.0_2049333924999991298.json、图片生成/图生图/美少女合集文生图_2056898268851953665.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 11/17 个有
- `GetImageSize` —— 11/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/17 个有
- `LoadImage` —— 11/17 个有
- `TextEncodeQwenImageEditPlus` —— 11/17 个有
- `Fast Groups Bypasser (rgthree)` —— 7/17 个有
- `CLIPTextEncode` —— 6/17 个有
- `llama_cpp_clean_states` —— 6/17 个有
- `PreviewImage` —— 5/17 个有
- `MemoryCleaner` —— 4/17 个有
- `GetNode` —— 1/17 个有
- `RH_Nano_Banana2_Image2Image` —— 1/17 个有
- `RH_RhartImageG2ImageToImage` —— 1/17 个有
- `SetNode` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 9 | 17 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler_ancestral | - | 17 | 53% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 9，17 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，17 个样本，一致性 53%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（23/17 个样本）：Steps较低可能导致细节不足
