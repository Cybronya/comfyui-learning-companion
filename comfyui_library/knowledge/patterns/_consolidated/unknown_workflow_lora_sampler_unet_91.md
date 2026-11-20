---
name: unknown_workflow_lora_sampler_unet_91
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8715
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit一致性图像编辑_1970030556392136706.json, 图片生成/图生图/Qwen-Edit Anime2RealV1.0_1987069606663753730.json, 图片生成/图生图/qwen_肤质优化_2072599705988722690.json, 图片生成/图生图/动漫转真人_1987102915582169089.json, 图片生成/图生图/千问 基础换装_2064338502980038658.json, 图片生成/图生图/图像迁移(电商专用）-千问多图像编辑-高一致性_1971192596905283586.json, 图片生成/图生图/美女给老头送肉桂-千问Edit2509图像编辑-多图融合_1976569063365283842.json, 图片生成/文生图/千问Edit2511图像编辑-多图融合_2079746757461893122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Edit一致性图像编辑_1970030556392136706.json、图片生成/图生图/Qwen-Edit Anime2RealV1.0_1987069606663753730.json、图片生成/图生图/qwen_肤质优化_2072599705988722690.json、图片生成/图生图/动漫转真人_1987102915582169089.json、图片生成/图生图/千问 基础换装_2064338502980038658.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 7/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `FluxKontextImageScale` —— 4/8 个有
- `ImageConcanate` —— 4/8 个有
- `RH_LLMAPI_NODE` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `AddLabel` —— 2/8 个有
- `CR Prompt Text` —— 2/8 个有
- `EmptyLatentImage` —— 2/8 个有
- `FluxResolutionNode` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 8 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 26% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | beta57 | - | 8 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，8 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 beta57，8 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
