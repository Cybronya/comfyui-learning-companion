---
name: unknown_workflow_lora_sampler_clip_29
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.884571
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, ImageCrop+, SimpleMath+, easy imageSize]
members: [图片生成/文生图/1981992176706035713.json, 图片生成/文生图/1981999558349725697.json, 图片生成/文生图/FLIX文生图｜产品写实 超逼真_1896248747091427329.json, 图片生成/文生图/云朵精灵Zhiban，三视图_1880497654135418881.json, 图片生成/文生图/在线一键生成毛绒玩具卡通形象手稿丨含效果图_1901132060025856001.json, 图片生成/文生图/毛绒奇幻国·Zhiban_1880497829063061506.json, 图片生成/文生图/毛绒奇幻国·Zhiban_1880529226179964930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1981992176706035713.json、图片生成/文生图/1981999558349725697.json、图片生成/文生图/FLIX文生图｜产品写实 超逼真_1896248747091427329.json、图片生成/文生图/云朵精灵Zhiban，三视图_1880497654135418881.json、图片生成/文生图/在线一键生成毛绒玩具卡通形象手稿丨含效果图_1901132060025856001.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/7 个有
- `DetailDaemonSamplerNode` —— 2/7 个有
- `ImageCrop+` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `SeargePromptCombiner` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1664 | 768 - 2000 | 7 | 67% |
| 高度 | 1024 | 1024 - 1280 | 7 | 90% |
| LoRA 模型强度 | 1 | 0.3 - 1 | 7 | 70% |
| LoRA 文本强度 | 1 | 0.65 - 3.5 | 7 | 31% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1664，观测区间 768 - 2000，7 个样本
- 高度 中位数 1024，观测区间 1024 - 1280，7 个样本，取值集中（一致性 90%）
- LoRA 模型强度 中位数 1，观测区间 0.3 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 0.65 - 3.5，7 个样本，取值分散，一致性仅 31%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ImageCrop+、SimpleMath+、easy imageSize
