---
name: unknown_workflow_video_sampler_clip_130
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.933
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json, 视频生成/文生视频/图+文生视频 -WanImageToVideo_1986023978202529793.json, 视频生成/文生视频/图生视频  (分段生成一20S长视频)_1985046868029837313.json, 视频生成/文生视频/图生视频  (支持AI自动生成剧本)_1983914577035493377.json, 视频生成/文生视频/图生视频 (支持AI自动手动生成短视频剧本)_1985873348330696706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/wan2.2-图生视频-20秒长视频_1985192415910838274.json、视频生成/文生视频/图+文生视频 -WanImageToVideo_1986023978202529793.json、视频生成/文生视频/图生视频  (分段生成一20S长视频)_1985046868029837313.json、视频生成/文生视频/图生视频  (支持AI自动生成剧本)_1983914577035493377.json、视频生成/文生视频/图生视频 (支持AI自动手动生成短视频剧本)_1985873348330696706.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 4/5 个有
- `CLIPVisionLoader` —— 4/5 个有
- `CR Text` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `Int` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `easy batchAnything` —— 2/5 个有
- `easy textSwitch` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `CR Upscale Image` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ttN concat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
