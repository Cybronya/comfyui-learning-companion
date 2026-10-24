---
name: unknown_workflow_lora_sampler_unet_72
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.835
common_nodes: [CFGNorm, CLIPLoader, CR Text, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/API-口播稿和拼图-数字人_2066926771995504642.json, 图片生成/图生图/API-纯拼图-数字人custom_2067115245457461249.json, 图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json, 图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json, 图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json, 图片生成/图生图/人物变装 三图参考生图工作流_2038434416120307713.json, 图片生成/文生图/FireRed-Image-Edit 1.1 参考人物生图工作流+全节点注释_2055176231376695297.json, 图片生成/文生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_72

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/API-口播稿和拼图-数字人_2066926771995504642.json、图片生成/图生图/API-纯拼图-数字人custom_2067115245457461249.json、图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json、图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json、图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/8 个有
- `PrimitiveInt` —— 6/8 个有
- `GetImageSize` —— 4/8 个有
- `Int` —— 2/8 个有
- `TextEncodeQwenImageEdit` —— 2/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `Text _O` —— 1/8 个有
- `easy saveText` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 8 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 75% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，8 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 75%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
