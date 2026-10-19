---
name: text_to_image_video_lora_sampler_136
type: Text To Image
frequency: 4
level: strong
coverage: 0.44375
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveStringMultiline, SaveImage, SetNode, SimpleMath+, TextEncodeQwenImageEditPlus, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy convertAnything, easy int]
problems: [Steps较低可能导致细节不足]
missing: [SimpleMath+, easy convertAnything, easy int, CR Integer To String, CR String To Number, Evaluate Strings, Text Multiline, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy mathInt]
members: [图片生成/文生图/1978029679443595266.json, 视频生成/图生视频/1978029679443595266.json, 视频生成/图生视频/1978029698238263298.json, 视频生成/文生视频/1978029698238263298.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_136

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1978029679443595266.json、视频生成/图生视频/1978029679443595266.json、视频生成/图生视频/1978029698238263298.json、视频生成/文生视频/1978029698238263298.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy convertAnything`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Integer To String` —— 2/4 个有
- `CR String To Number` —— 2/4 个有
- `Evaluate Strings` —— 2/4 个有
- `ImpactStringSelector` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VHS_SelectImages` —— 2/4 个有
- `easy batchAnything` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `easy mathInt` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1920 | 1920 - 1920 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+、easy convertAnything、easy int、CR Integer To String、CR String To Number
