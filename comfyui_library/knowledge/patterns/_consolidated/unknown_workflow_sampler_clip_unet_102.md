---
name: unknown_workflow_sampler_clip_unet_102
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.923727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/JoyCaptionOne反推提示词+Qwen生图_1952963427289468930.json, 图片生成/文生图/Qwen 文生图_1955160402595233794.json, 图片生成/文生图/Qwen 文生图工作流--@橘子_SJRJT_1962804112075173889.json, 图片生成/文生图/Qwen-Image ComfyUI原生工作流_2027264283821744129.json, 图片生成/文生图/Qwen-Image-Lightning_1954757119348240386.json, 图片生成/文生图/Qwen_Image_2512_文生图_2038551608694415361.json, 图片生成/文生图/Qwen_Image_2512_文生图_bf16版本_2008392762101604354.json, 图片生成/文生图/Qwen_Image_2512文生图工作流_2063234247065948161.json, 图片生成/文生图/Qwen_Image_2512文生图生成模型工作流_2049713739422769154.json, 图片生成/文生图/Qwen_Image文生图_1955444251107606530.json, 图片生成/文生图/Qwen_image阿里_1952908666094743554.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/JoyCaptionOne反推提示词+Qwen生图_1952963427289468930.json、图片生成/文生图/Qwen 文生图_1955160402595233794.json、图片生成/文生图/Qwen 文生图工作流--@橘子_SJRJT_1962804112075173889.json、图片生成/文生图/Qwen-Image ComfyUI原生工作流_2027264283821744129.json、图片生成/文生图/Qwen-Image-Lightning_1954757119348240386.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `LoadImage` —— 3/11 个有
- `ShowText` —— 2/11 个有
- `Florence2ModelLoader` —— 1/11 个有
- `Florence2Run` —— 1/11 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/11 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/11 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 11 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 35% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，11 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（9/11 个样本）：Steps较低可能导致细节不足
