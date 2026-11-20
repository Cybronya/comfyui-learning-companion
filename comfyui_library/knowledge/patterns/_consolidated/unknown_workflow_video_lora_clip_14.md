---
name: unknown_workflow_video_lora_clip_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8385
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, IntToText, JWInteger, JWStringConcat, JjkText, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, PrimitiveStringMultiline, RHBatchImages:, RHUploadZip, SimpleMath+, Text Load Line From File, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy boolean, easy forLoopEnd, easy forLoopStart, easy ifElse, easy imageCount, easy mathInt, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.1 flf2v 两图首尾帧循环_2011044989047939074.json, 视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.1 flf2v 两图首尾帧循环_2011044989047939074.json、视频生成/文生视频/Wan2.2-3图首尾帧循环_2007695996830097409.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `IntToText`
- `JWInteger`
- `JWStringConcat`
- `JjkText`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RHBatchImages:`
- `RHUploadZip`
- `SimpleMath+`
- `Text Load Line From File`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy boolean`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy imageCount`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `Compare` —— 1/2 个有
- `HunyuanVideoFoley` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWImageExtractFromBatch` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RHExtractImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `TrimVideoLatent` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfoSource` —— 1/2 个有
- `WanAdvancedI2V` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `easy compare` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
