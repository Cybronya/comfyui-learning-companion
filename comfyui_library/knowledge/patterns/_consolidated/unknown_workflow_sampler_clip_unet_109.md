---
name: unknown_workflow_sampler_clip_unet_109
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9565
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Label (rgthree)]
members: [图片生成/文生图/1926971761274093569.json, 图片生成/文生图/1929042246597820418.json, 图片生成/文生图/1929761113691340801.json, 图片生成/文生图/1937568663094628354.json, 图片生成/文生图/1943614394796568578.json, 图片生成/文生图/1948667723191595009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1926971761274093569.json、图片生成/文生图/1929042246597820418.json、图片生成/文生图/1929761113691340801.json、图片生成/文生图/1937568663094628354.json、图片生成/文生图/1943614394796568578.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoraLoader` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `Bjornulf_ShowStringText` —— 1/6 个有
- `DetailDaemonSamplerNode` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PatchModelAddDownscale` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `ShowText` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 5 | 78% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 964 | 768 - 1920 | 6 | 65% |
| 高度 | 1292 | 1024 - 2048 | 6 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 964，观测区间 768 - 1920，6 个样本
- 高度 中位数 1292，观测区间 1024 - 2048，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
