---
name: unknown_workflow_video_lora_sampler_781
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.736
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, LayerMask: MaskGrow, LayerUtility: PurgeVRAM, MathExpression|pysssss, PreviewAnimation, PreviewImage, RHHiddenNodes, RMBG, SetNode, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1970359648316497921.json, 视频生成/图生视频/1967851309351206913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_781

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1970359648316497921.json、视频生成/图生视频/1967851309351206913.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerMask: MaskGrow`
- `LayerUtility: PurgeVRAM`
- `MathExpression|pysssss`
- `PreviewAnimation`
- `PreviewImage`
- `RHHiddenNodes`
- `RMBG`
- `SetNode`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | beta57 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
