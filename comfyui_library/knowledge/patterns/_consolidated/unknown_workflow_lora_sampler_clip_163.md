---
name: unknown_workflow_lora_sampler_clip_163
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7454
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, ImagePadForOutpaint, ImageResize+, ImageToMask, KSampler, LoraLoader, MaskToImage, ModelSamplingSD3, PrimitiveInt, RepeatImageBatch, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideoFFmpeg, VHS_VideoInfoSource, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/手动扩展视频_1992876192525250562.json, 平台全量/横屏转竖屏_1992866249956978689.json, 平台全量/横屏转竖屏_2005640430085697537.json, 平台全量/竖屏转横屏_1992866985059086338.json, 平台全量/竖屏转横屏_2008191607199240193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/手动扩展视频_1992876192525250562.json、平台全量/横屏转竖屏_1992866249956978689.json、平台全量/横屏转竖屏_2005640430085697537.json、平台全量/竖屏转横屏_1992866985059086338.json、平台全量/竖屏转横屏_2008191607199240193.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `ImagePadForOutpaint`
- `ImageResize+`
- `ImageToMask`
- `KSampler`
- `LoraLoader`
- `MaskToImage`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `RepeatImageBatch`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoInfoSource`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `DisplayAny` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `TrimVideoLatent` —— 3/5 个有
- `Display Any (rgthree)` —— 2/5 个有
- `Display Int (rgthree)` —— 2/5 个有
- `easy compare` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.2 - 1 | 5 | 62% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 8 | 4 - 8 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.2 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
