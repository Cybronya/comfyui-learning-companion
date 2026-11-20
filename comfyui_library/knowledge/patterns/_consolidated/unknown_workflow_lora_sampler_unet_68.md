---
name: unknown_workflow_lora_sampler_unet_68
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8457
common_nodes: [AILab_QwenVL, CLIPLoader, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一键九视图[同人同景同服装]超强有一致性模特套图加强版_2003309725775167489.json, 图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json, 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1986607902217695234.json, 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1997265879790456833.json, 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json, 图片生成/图生图/固定人物Ip多场景生成V2_2004543457458880513.json, 图片生成/图生图/图生图一键九视图[同人同景同服装]超强有一致性模特套图加强版（无水印版）_1985276910106198017.json, 图片生成/图生图/图生图一键九视图[同人同景同服装]超强有一致性模特套图加强版（无水印版）_2066345362234892290.json, 图片生成/图生图/图生图杀马特一键九视图[同人同景同服装]超强有一致性模特套图加强版_1986321370713903106.json, 平台全量/文生IP人物固定场景写真V1.0_1998319708766134274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_68

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/人物一键九视图[同人同景同服装]超强有一致性模特套图加强版_2003309725775167489.json、图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json、图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1986607902217695234.json、图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1997265879790456833.json、图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `CR Text` —— 6/10 个有
- `CR Text Replace` —— 6/10 个有
- `ProcessString` —— 6/10 个有
- `EmptySD3LatentImage` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `GetNode` —— 4/10 个有
- `RH_LLMAPI_NODE` —— 4/10 个有
- `CompressImages` —— 3/10 个有
- `ImageConcanate` —— 3/10 个有
- `ImageFromBatch` —— 3/10 个有
- `LayerUtility: ImageReel` —— 3/10 个有
- `LayerUtility: ImageReelComposit` —— 3/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `KSamplerAdvanced` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta57 | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta57，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
