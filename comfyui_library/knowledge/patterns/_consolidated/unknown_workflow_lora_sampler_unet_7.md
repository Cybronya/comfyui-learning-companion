---
name: unknown_workflow_lora_sampler_unet_7
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.88225
common_nodes: [CFGNorm, CLIPLoader, CR Text, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, RH_LLMAPI_NODE, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text]
members: [图片生成/图生图/2100881020475240450.json, 图片生成/图生图/2102079328715628545.json, 图片生成/图生图/2102095048337879041.json, 图片生成/图生图/2102284370366259202.json, 图片生成/图生图/2102291103130152961.json, 图片生成/图生图/2102301014081753090.json, 图片生成/图生图/2102436707214909442.json, 图片生成/图生图/2102445394839031809.json, 图片生成/文生图/分镜套图  角色融合_2086992639202775042.json, 数字人/数字人/分镜 自动分镜  短剧分镜 漫剧分镜_优化版本_2095891748332597250.json, 视频生成/图生视频/2067686821718482945.json, 视频生成/图生视频/2065728809785188353.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2100881020475240450.json、图片生成/图生图/2102079328715628545.json、图片生成/图生图/2102095048337879041.json、图片生成/图生图/2102284370366259202.json、图片生成/图生图/2102291103130152961.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 11/12 个有
- `SeedVR2LoadDiTModel` —— 1/12 个有
- `SeedVR2LoadVAEModel` —— 1/12 个有
- `SeedVR2VideoUpscaler` —— 1/12 个有
- `easy imageBatchToImageList` —— 1/12 个有
- `easy imageListToImageBatch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
