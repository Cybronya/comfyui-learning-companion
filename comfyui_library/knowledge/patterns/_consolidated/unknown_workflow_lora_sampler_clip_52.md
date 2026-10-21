---
name: unknown_workflow_lora_sampler_clip_52
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.908167
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Text, ttN concat]
members: [图片生成/文生图/1928999965027155970.json, 图片生成/文生图/1932966165364834305.json, 图片生成/文生图/1933850253839749122.json, 图片生成/文生图/1934978430360592385.json, 图片生成/文生图/1962372606101950465.json, 图片生成/文生图/沙雕动画场景专用工作流_2075008312994787329.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1928999965027155970.json、图片生成/文生图/1932966165364834305.json、图片生成/文生图/1933850253839749122.json、图片生成/文生图/1934978430360592385.json、图片生成/文生图/1962372606101950465.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
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
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `ImageScaleBy` —— 4/6 个有
- `DeepTranslatorTextNode` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `FluxSampler` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `ttN concat` —— 2/6 个有
- `CFGZeroStar` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextInputBasic` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1248 | 1024 - 1344 | 6 | 90% |
| 高度 | 768 | 768 - 1536 | 6 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1248，观测区间 1024 - 1344，6 个样本，取值集中（一致性 90%）
- 高度 中位数 768，观测区间 768 - 1536，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ttN concat
