---
name: unknown_workflow_video_lora_sampler_876
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4875
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SetNode, Text Load Line From File, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [视频生成/图生视频/SVI 2.0Pro 一键生成长视频！_2008875910526668802.json, 视频生成/文生视频/大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_876

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SVI 2.0Pro 一键生成长视频！_2008875910526668802.json、视频生成/文生视频/大凯辰光_SVI_2.0_Pro 长视频优化工作流-For循环+旅行提示词高级版_2006383252696735745.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SetNode`
- `Text Load Line From File`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoNAG` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy isNone` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
