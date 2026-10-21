---
name: unknown_workflow_lora_sampler_clip_103
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.835
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [ttN concat, easy seed]
members: [图片生成/文生图/1920133263510142977.json, 图片生成/文生图/1936219766145323010.json, 图片生成/文生图/【一键运行】二次元性感美少女_2018845332670521345.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1920133263510142977.json、图片生成/文生图/1936219766145323010.json、图片生成/文生图/【一键运行】二次元性感美少女_2018845332670521345.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy seed` —— 2/3 个有
- `Bjornulf_ShowStringText` —— 1/3 个有
- `EG_FX_BDAPI` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ttN concat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：ttN concat、easy seed
