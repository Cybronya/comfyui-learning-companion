---
name: unknown_workflow_sampler_clip_unet_88
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.977727
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux文生图（自动润色提示词）_1937568663094628354.json, 图片生成/文生图/Flux版IP三视图角色生成_1923645200881602562.json, 图片生成/文生图/Flux版IP三视图角色生成_1991794796115210242.json, 图片生成/文生图/Flux版_IP三视图角色一致性生成_1923655528982245378.json, 图片生成/文生图/IP三视图角色生成工作流_1929042246597820418.json, 图片生成/文生图/flux1-krea-dev 文生图_1951288327628599298.json, 图片生成/文生图/flux双lora批量出图_1900015521121579010.json, 图片生成/文生图/flux底膜双lora批量工作流5通道_1902172176840335361.json, 图片生成/文生图/flux文生图基础工作流+双lora_1887374428500549633.json, 图片生成/文生图/flux文生图多通道测试lora_1905507891238080513.json, 图片生成/文生图/最强文生图 flux krea 加强人物真实感_1952013936583495682.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Flux文生图（自动润色提示词）_1937568663094628354.json、图片生成/文生图/Flux版IP三视图角色生成_1923645200881602562.json、图片生成/文生图/Flux版IP三视图角色生成_1991794796115210242.json、图片生成/文生图/Flux版_IP三视图角色一致性生成_1923655528982245378.json、图片生成/文生图/IP三视图角色生成工作流_1929042246597820418.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 8/11 个有
- `CR Text` —— 3/11 个有
- `CR Text Concatenate` —— 3/11 个有
- `PMRF` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `FluxGuidance` —— 2/11 个有
- `Bjornulf_ShowStringText` —— 1/11 个有
- `RH_LLMAPI_NODE` —— 1/11 个有
- `TeaCache` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1200 | 512 - 1920 | 11 | 68% |
| 高度 | 1080 | 512 - 2560 | 11 | 60% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 8 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1200，观测区间 512 - 1920，11 个样本
- 高度 中位数 1080，观测区间 512 - 2560，11 个样本
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，8 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
