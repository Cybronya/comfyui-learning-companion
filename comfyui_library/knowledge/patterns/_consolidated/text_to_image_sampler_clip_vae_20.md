---
name: text_to_image_sampler_clip_vae_20
type: Text To Image
frequency: 8
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【WS】-文生图j001_1998652096863985666.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）1280_720 V：dxyc2291获取软件_2019545477716381698.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）_2018646916669644802.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）_2038246354245390337.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（竖屏）720_1280 V：dxyc2291获取软件_2019547644695158786.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（竖屏）_2018648567409287169.json, 图片生成/文生图/万象AI+Runninghub文生图工作流（竖屏）_2038253123793326081.json, 图片生成/文生图/文生图工作流（横屏）_2028356992384897025.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_20

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/【WS】-文生图j001_1998652096863985666.json、图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）1280_720 V：dxyc2291获取软件_2019545477716381698.json、图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）_2018646916669644802.json、图片生成/文生图/万象AI+Runninghub文生图工作流（横屏）_2038246354245390337.json、图片生成/文生图/万象AI+Runninghub文生图工作流（竖屏）720_1280 V：dxyc2291获取软件_2019547644695158786.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/8 个有
- `CR Value` —— 1/8 个有
- `PreviewTextNode` —— 1/8 个有
- `ttN concat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1000 | 720 - 1280 | 8 | 72% |
| 高度 | 1000 | 720 - 1280 | 8 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1000，观测区间 720 - 1280，8 个样本
- 高度 中位数 1000，观测区间 720 - 1280，8 个样本
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
