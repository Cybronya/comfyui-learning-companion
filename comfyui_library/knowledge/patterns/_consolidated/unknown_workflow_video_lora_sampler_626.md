---
name: unknown_workflow_video_lora_sampler_626
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.468333
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageColorMatch+, ImageFromBatch, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview, MaskPreview+, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RMBG, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [视频生成/图生视频/1984188715234967554.json, 视频生成/图生视频/1943205882685775873.json, 视频生成/图生视频/1944340195523088386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_626

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1984188715234967554.json、视频生成/图生视频/1943205882685775873.json、视频生成/图生视频/1944340195523088386.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageColorMatch+`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `MaskPreview+`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RMBG`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `TeaCache` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
