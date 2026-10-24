---
name: unknown_workflow_video_lora_sampler_390
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8314
common_nodes: [CLIPLoader, CLIPTextEncode, CR Integer To String, CR String To Number, CR Text, EmptySD3LatentImage, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, RHHiddenNodes, ReadExcelData, ShowText|pysssss, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy forLoopEnd, easy forLoopStart, easy mathInt, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/动漫短剧全自动工作流V4.1_1966707230915670018.json, 视频生成/文生视频/wanduDMDJV1.0_1967613409602801666.json, 视频生成/文生视频/动漫短剧 全自动工作流 可指定分镜个数 上手简单效果好_2004470132204335105.json, 视频生成/文生视频/动漫短剧 全自动工作流 可指定分镜个数 上手简单效果好_2008541055511175170.json, 视频生成/文生视频/动漫短剧全自动工作流V4.1_2067305785524318209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_390

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/动漫短剧全自动工作流V4.1_1966707230915670018.json、视频生成/文生视频/wanduDMDJV1.0_1967613409602801666.json、视频生成/文生视频/动漫短剧 全自动工作流 可指定分镜个数 上手简单效果好_2004470132204335105.json、视频生成/文生视频/动漫短剧 全自动工作流 可指定分镜个数 上手简单效果好_2008541055511175170.json、视频生成/文生视频/动漫短剧全自动工作流V4.1_2067305785524318209.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Integer To String`
- `CR String To Number`
- `CR Text`
- `EmptySD3LatentImage`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `RHHiddenNodes`
- `ReadExcelData`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 4/5 个有
- `LoadImage` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 0 | 0 - 0 | 5 | 100% |
| 调度器 | lcm | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0，观测区间 0 - 0，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
