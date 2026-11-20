---
name: unknown_workflow_lora_sampler_unet_18
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.87095
common_nodes: [CLIPLoader, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed模特写真套图一致性工作流_2032310944155570178.json, 图片生成/图生图/IP打造多场景生成V2.0_2031530143709143042.json, 图片生成/图生图/Qwen-Edit-2509人物固定多场景生成_1991136693919264769.json, 图片生成/图生图/Qwen-美女一键写真大片_2042090297726869505.json, 图片生成/图生图/Qwen2509人物固定多场景生成_1995445677461266433.json, 图片生成/图生图/qwen-image_qwen_模特套图_分镜头_九宫格套图_2032013275688345602.json, 图片生成/图生图/人物一致性-生成多场景_2012765654553731073.json, 图片生成/图生图/人物一致性-生成多场景（Qwen-人物IP打造）_1990331943755673602.json, 图片生成/图生图/人物一致性-生成多场景（Qwen-人物IP打造）_1995512081849966594.json, 图片生成/图生图/人物一键极致写真两种方案_1996923193854201857.json, 图片生成/图生图/人物不变 多张生成 不同背景姿势服饰V3.0_2032109068378185729.json, 图片生成/图生图/固定人物IP 多张多场景生成V3.0（IP打造）_2031743464865533954.json, 图片生成/图生图/女模特多场景摆拍（Qwen-人物IP打造）_1991886389321027585.json, 图片生成/图生图/模特套图 出图质量高 简单上手_2031725899757916162.json, 图片生成/图生图/模特套图工作流V2(升级可本地部署）_1982986515359891457.json, 图片生成/图生图/模特套图工作流V2(升级可本地部署）_2039503858971451394.json, 图片生成/图生图/模特套图工作流V2(升级可本地部署）_2046107754628128770.json, 图片生成/图生图/模特套图工作流V3(大幅度提升人物一致性和指令遵循）_1983376779484274690.json, 图片生成/图生图/模特套图工作流V4(提升姿态幅度及差异化）_1985516927198109698.json, 图片生成/图生图/自动换背景-姿势服饰-人物不变_2032280897092849666.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_18

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/FireRed模特写真套图一致性工作流_2032310944155570178.json、图片生成/图生图/IP打造多场景生成V2.0_2031530143709143042.json、图片生成/图生图/Qwen-Edit-2509人物固定多场景生成_1991136693919264769.json、图片生成/图生图/Qwen-美女一键写真大片_2042090297726869505.json、图片生成/图生图/Qwen2509人物固定多场景生成_1995445677461266433.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 18/20 个有
- `AILab_QwenVL` —— 16/20 个有
- `CR Text` —— 16/20 个有
- `EmptySD3LatentImage` —— 15/20 个有
- `ProcessString` —— 15/20 个有
- `CR Text Replace` —— 14/20 个有
- `TextEncodeQwenImageEdit` —— 14/20 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 14/20 个有
- `Fast Groups Bypasser (rgthree)` —— 6/20 个有
- `GetImageSize` —— 6/20 个有
- `TextEncodeQwenImageEditPlus` —— 6/20 个有
- `Anything Everywhere` —— 4/20 个有
- `MuyeTextEditOutput` —— 1/20 个有
- `Qwen3VL_Chat` —— 1/20 个有
- `RH_Nano_Banana2_Image2Image` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 20 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 90% |
| 调度器 | kl_optimal | - | 20 | 35% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 90%
- 调度器 最常用 kl_optimal，20 个样本，一致性 35%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（25/20 个样本）：Steps较低可能导致细节不足
