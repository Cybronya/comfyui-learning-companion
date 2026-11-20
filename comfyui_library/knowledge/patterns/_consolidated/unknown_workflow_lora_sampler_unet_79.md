---
name: unknown_workflow_lora_sampler_unet_79
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.849111
common_nodes: [CFGNorm, CLIPLoader, CR Text, EmptySD3LatentImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/API-口播稿和拼图-数字人_2066926771995504642.json, 图片生成/图生图/API-纯拼图-数字人custom_2067115245457461249.json, 图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json, 图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json, 图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json, 图片生成/图生图/人物变装 三图参考生图工作流_2038434416120307713.json, 图片生成/文生图/FireRed-Image-Edit 1.1 参考人物生图工作流+全节点注释_2055176231376695297.json, 图片生成/文生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2035665469574750209.json, 数字人/数字人/digital_image.json_2061385489462161410.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/API-口播稿和拼图-数字人_2066926771995504642.json、图片生成/图生图/API-纯拼图-数字人custom_2067115245457461249.json、图片生成/图生图/FireRed-Image-Edit 1.1 三图参考生图工作流_2037737258933030913.json、图片生成/图生图/FireRed-Image-Edit+1.1+参考人物生图工作流+全节点注释_2056552163614216193.json、图片生成/图生图/万象AI_FireRed-Image-Edit 1.1 参考人物生图工作流_2055146636736778242.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
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
- `CLIPTextEncode` —— 6/9 个有
- `PrimitiveInt` —— 6/9 个有
- `GetImageSize` —— 4/9 个有
- `Int` —— 3/9 个有
- `TextEncodeQwenImageEdit` —— 3/9 个有
- `Text _O` —— 2/9 个有
- `easy saveText` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `TextCombinerTwo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 9 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 67% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，9 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 67%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
