---
name: unknown_workflow_lora_sampler_unet_62
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.908667
common_nodes: [CFGNorm, CLIPLoader, CR Text, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/32nineimage_2049742594141327361.json, 图片生成/图生图/12分镜 自动分镜_2082124227095912450.json, 图片生成/图生图/3月固定人物IP多场景生成（IP打造）人物一致性多图编辑_2036989882937122818.json, 图片生成/图生图/ComfyUI图生图神级工作流｜人脸不变，一键自动换衣+换背景_2041457441367400450.json, 图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2104790428624183297.json, 图片生成/图生图/FireRed-Image-Edit 小红书 一键套图 九宫格_2036051449859280898.json, 图片生成/图生图/FireRed-Image-Edit 小红书一键套图 模特套图_2037760135145201666.json, 图片生成/图生图/FireRed-Image-Edit 小红书专用  小红书大模型 一键套图 网红感_2038118562136596482.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_62

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/32nineimage_2049742594141327361.json、图片生成/图生图/12分镜 自动分镜_2082124227095912450.json、图片生成/图生图/3月固定人物IP多场景生成（IP打造）人物一致性多图编辑_2036989882937122818.json、图片生成/图生图/ComfyUI图生图神级工作流｜人脸不变，一键自动换衣+换背景_2041457441367400450.json、图片生成/图生图/FireRed-Image-Edit 1.1 上传人物图片一键套图_2033189810042576897.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `llama_cpp_instruct_adv` —— 8/9 个有
- `llama_cpp_model_loader` —— 8/9 个有
- `llama_cpp_parameters` —— 8/9 个有
- `EmptySD3LatentImage` —— 7/9 个有
- `GetImageSize` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `MemoryCleaner` —— 2/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/9 个有
- `BatchImagesNode` —— 1/9 个有
- `CustomAddLabel` —— 1/9 个有
- `CustomCombo` —— 1/9 个有
- `Int2String` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `Text Find and Replace` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 9 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 78% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，9 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 78%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
