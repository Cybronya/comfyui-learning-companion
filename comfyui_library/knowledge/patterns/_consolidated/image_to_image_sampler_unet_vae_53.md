---
name: image_to_image_sampler_unet_vae_53
type: Image To Image
frequency: 5
level: strong
coverage: 0.927
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-Edit-2511一致性人物多角度-专门支持横向图片_2016856646928044033.json, 平台全量/Qwen一致性人物多角度_2015394863084212226.json, 平台全量/人物一致性-多图裂变-百变女友_2001882128629526529.json, 平台全量/人物服装拆解_2008516959490547714.json, 平台全量/人物服装拆解_2008531755271200770.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-Edit-2511一致性人物多角度-专门支持横向图片_2016856646928044033.json、平台全量/Qwen一致性人物多角度_2015394863084212226.json、平台全量/人物一致性-多图裂变-百变女友_2001882128629526529.json、平台全量/人物服装拆解_2008516959490547714.json、平台全量/人物服装拆解_2008531755271200770.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `Text` —— 2/5 个有
- `图像缩放范围孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（33/5 个样本）：Steps较低可能导致细节不足
