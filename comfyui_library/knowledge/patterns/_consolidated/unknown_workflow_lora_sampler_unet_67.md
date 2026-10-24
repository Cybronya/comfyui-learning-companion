---
name: unknown_workflow_lora_sampler_unet_67
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.863889
common_nodes: [AILab_QwenVL, CLIPLoader, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一键九视图[同人同景同服装]超强有一致性模特套图加强版_2003309725775167489.json, 图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json, 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1986607902217695234.json, 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1997265879790456833.json, 图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json, 图片生成/图生图/固定人物Ip多场景生成V2_2004543457458880513.json, 图片生成/图生图/图生图一键九视图[同人同景同服装]超强有一致性模特套图加强版（无水印版）_1985276910106198017.json, 图片生成/图生图/图生图一键九视图[同人同景同服装]超强有一致性模特套图加强版（无水印版）_2066345362234892290.json, 图片生成/图生图/图生图杀马特一键九视图[同人同景同服装]超强有一致性模特套图加强版_1986321370713903106.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_67

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/人物一键九视图[同人同景同服装]超强有一致性模特套图加强版_2003309725775167489.json、图片生成/图生图/固定人物IP多场景生成V1.0（IP）_1986353934086373377.json、图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1986607902217695234.json、图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_1997265879790456833.json、图片生成/图生图/固定人物IP多场景生成V2.0（IP打造）人物一致性多图编辑_2018861403326648321.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
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
- `CR Text` —— 5/9 个有
- `CR Text Replace` —— 5/9 个有
- `ProcessString` —— 5/9 个有
- `CR Prompt Text` —— 4/9 个有
- `EmptySD3LatentImage` —— 4/9 个有
- `RH_LLMAPI_NODE` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `CompressImages` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `ImageConcanate` —— 3/9 个有
- `ImageFromBatch` —— 3/9 个有
- `LayerUtility: ImageReel` —— 3/9 个有
- `LayerUtility: ImageReelComposit` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta57 | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta57，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
