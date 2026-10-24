---
name: unknown_workflow_lora_sampler_unet_14
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.911083
common_nodes: [CFGNorm, CLIPLoader, CR Text, CR Text Replace, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3月固定人物IP多场景生成（IP打造）人物一致性多图编辑_2036989882937122818.json, 图片生成/图生图/ComfyUI图生图神级工作流｜人脸不变，一键自动换衣+换背景_2041457441367400450.json, 图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json, 图片生成/图生图/FireRed-Image-Edit 小红书 一键套图 九宫格_2036051449859280898.json, 图片生成/图生图/FireRed-Image-Edit 小红书一键套图 模特套图_2037760135145201666.json, 图片生成/图生图/FireRed-Image-Edit 小红书专用  小红书大模型 一键套图 网红感_2038118562136596482.json, 图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图-V3_2045152020759318530.json, 图片生成/图生图/FireRed-Image-Edit-1.1-小红书一键套图-模特套图_2042238014172172289.json, 图片生成/图生图/FireRed-Image-edit1.1电商模特出图_2031377996577251330.json, 图片生成/图生图/Qwen 多分镜多角度生成图片_2032477079954006017.json, 图片生成/图生图/一秒写真-人物多场景_2052908771151753218.json, 图片生成/图生图/一键买家秀_朋友圈_微博图，一张场景图AI多个姿态_2032867458738036737.json, 图片生成/图生图/一键套图  FireRed-Image-Edit 小红书专用  网红感 图生图_2041825511285985282.json, 图片生成/图生图/一键套图  FireRed-Image-Edit 小红书专用  网红感 图生图_2042526164039770114.json, 图片生成/图生图/一键套图  图生图 FireRed-Image-Edit 小红书专用  网红感_2042417087305490434.json, 图片生成/图生图/一键套图  图生图 FireRed-Image-Edit 小红书专用  网红感_2042825994603601922.json, 图片生成/图生图/一键套图  图生图 FireRed-Image-Edit 小红书专用  网红感_2042917048216457217.json, 图片生成/图生图/一键套图 9张不同模特姿势 图生图_2058599468710326273.json, 图片生成/图生图/一键套图 9张不同模特姿势 图生图_2059514134651297793.json, 图片生成/图生图/一键套图 9张不同模特姿势 图生图_2059913694108278786.json, 图片生成/图生图/一键姿势生成器   角色姿势  人物动作_2047595020592615425.json, 图片生成/图生图/一键摄影照（自动提示词）_2059009844501368833.json, 图片生成/图生图/一键生成专属写真照人物多场景写真生成器_2052620280123670530.json, 图片生成/图生图/一键生成专属写真照人物多场景写真生成器_2053355060582723585.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_14

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/3月固定人物IP多场景生成（IP打造）人物一致性多图编辑_2036989882937122818.json、图片生成/图生图/ComfyUI图生图神级工作流｜人脸不变，一键自动换衣+换背景_2041457441367400450.json、图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json、图片生成/图生图/FireRed-Image-Edit 小红书 一键套图 九宫格_2036051449859280898.json、图片生成/图生图/FireRed-Image-Edit 小红书一键套图 模特套图_2037760135145201666.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `CR Text Replace`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 23/24 个有
- `GetImageSize` —— 21/24 个有
- `JDCN_StringToList` —— 21/24 个有
- `PreviewImage` —— 14/24 个有
- `AutoCropFaces` —— 3/24 个有
- `CustomAddLabel` —— 3/24 个有
- `MemoryCleaner` —— 3/24 个有
- `PrimitiveInt` —— 3/24 个有
- `easy promptLine` —— 3/24 个有
- `Int` —— 2/24 个有
- `GetNode` —— 1/24 个有
- `JWInteger` —— 1/24 个有
- `MultiTextConcatenate` —— 1/24 个有
- `RH_Utils` —— 1/24 个有
- `SetNode` —— 1/24 个有
- `Text` —— 1/24 个有
- `easy textIndexSwitch` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 24 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 75% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，24 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 75%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：Steps较低可能导致细节不足
