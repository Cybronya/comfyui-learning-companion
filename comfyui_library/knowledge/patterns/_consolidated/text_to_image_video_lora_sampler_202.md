---
name: text_to_image_video_lora_sampler_202
type: Text To Image
frequency: 2
level: weak
coverage: 0.527
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveStringMultiline, SaveImage, SetNode, SimpleMath+, TextEncodeQwenImageEditPlus, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy convertAnything, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/整合aio和next-scene，生图生视频手动档_1978029679443595266.json, 视频生成/文生视频/整合aio和next-scene，生图生视频自动挡_1978029698238263298.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_202

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/整合aio和next-scene，生图生视频手动档_1978029679443595266.json、视频生成/文生视频/整合aio和next-scene，生图生视频自动挡_1978029698238263298.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CR Integer To String` —— 1/2 个有
- `CR String To Number` —— 1/2 个有
- `Evaluate Strings` —— 1/2 个有
- `ImpactStringSelector` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `VHS_SelectImages` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy mathInt` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
