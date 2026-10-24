---
name: unknown_workflow_lora_sampler_unet_22
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.641
common_nodes: [Anything Everywhere3, CFGNorm, CLIPLoader, CR Text, GetNode, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, RH_LLMAPI_NODE, SaveImage, SetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2053434132474150914.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2054157894966366210.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2073017193691963394.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2077016584656343041.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2083919554585128961.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2101264219399344129.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111789094073360385.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111795349353488385.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2046960867496960002.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2056914263595376641.json, 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2057278935905431553.json, 图片生成/图生图/h3分镜图FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程去水印_2086670579725324289.json, 图片生成/图生图/一键分镜工作流V2（支持动漫和真人）_2031222012189872129.json, 图片生成/图生图/一键分镜工作流V2（支持动漫和真人）_2073952433583255554.json, 图片生成/图生图/圣诞气氛一键达_1995787953970483202.json, 图片生成/图生图/换装-圣诞氛围冬季换装_1996749447172431874.json, 图片生成/图生图/超好用🔥单图一键生成专业影视分镜与关键帧全流程提示词 新_2052579231091175425.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_22

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit 1.1 上传图片一键分镜_2033173454689669122.json、图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2053434132474150914.json、图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2054157894966366210.json、图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2073017193691963394.json、图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2077016584656343041.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 18 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `GetNode`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 14/18 个有
- `MultiTextConcatenate` —— 14/18 个有
- `ttN concat` —— 14/18 个有
- `JjkText` —— 13/18 个有
- `easy showAnything` —— 13/18 个有
- `llama_cpp_instruct_adv` —— 13/18 个有
- `llama_cpp_model_loader` —— 13/18 个有
- `llama_cpp_parameters` —— 13/18 个有
- `Text` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 18 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，18 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
