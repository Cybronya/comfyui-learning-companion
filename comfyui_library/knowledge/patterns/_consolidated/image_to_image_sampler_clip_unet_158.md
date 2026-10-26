---
name: image_to_image_sampler_clip_unet_158
type: Image To Image
frequency: 3
level: strong
coverage: 0.966667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/换装-Kontext-白底图穿衣上身走秀_1955854421794193409.json, 数字人/数字人/【服饰提取】人物模特服装衣物精确提取_1944933239409795073.json, 视频生成/图生视频/FLUX kontext 开源模型 工作流_1937024075837640705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_158

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/换装-Kontext-白底图穿衣上身走秀_1955854421794193409.json、数字人/数字人/【服饰提取】人物模特服装衣物精确提取_1944933239409795073.json、视频生成/图生视频/FLUX kontext 开源模型 工作流_1937024075837640705.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `PromptComposerMerge` —— 1/3 个有
- `easy imageCount` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
