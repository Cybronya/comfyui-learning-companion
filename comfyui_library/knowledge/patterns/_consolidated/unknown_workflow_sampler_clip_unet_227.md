---
name: unknown_workflow_sampler_clip_unet_227
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.941667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json, 图片生成/文生图/z_image-文生图_2018374992529985537.json, 图片生成/文生图/z_image文生图工作流（内部教学）_2033253705268596738.json, 图片生成/文生图/z_image文生图工作流（真人直播间）_2046779750718377985.json, 图片生成/文生图/zimage 文生图工作流 Z-image_2037728300130377730.json, 图片生成/文生图/zimage+base+文生图+工作流_2074064661959503874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_227

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/qwen2512-qwen-水彩画-文生图工作流_2011342788499087361.json、图片生成/文生图/z_image-文生图_2018374992529985537.json、图片生成/文生图/z_image文生图工作流（内部教学）_2033253705268596738.json、图片生成/文生图/z_image文生图工作流（真人直播间）_2046779750718377985.json、图片生成/文生图/zimage 文生图工作流 Z-image_2037728300130377730.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CR Prompt Text` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `TextConcat` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 12 - 50 | 6 | 46% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4 | 6 | 52% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 12 - 50，6 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
