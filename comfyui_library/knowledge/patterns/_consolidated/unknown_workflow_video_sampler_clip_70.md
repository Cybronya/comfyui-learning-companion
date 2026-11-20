---
name: unknown_workflow_video_sampler_clip_70
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.621111
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json, 视频生成/图生视频/Dasiwa V2 ltx2.3 I2V_2058155153185918978.json, 视频生成/图生视频/LTX2-3-文生-图生视频（极大概率去台词，强一致性修订版V4）_2030557129664372738.json, 视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json, 视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json, 视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json, 视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json, 视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json, 视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json、视频生成/图生视频/Dasiwa V2 ltx2.3 I2V_2058155153185918978.json、视频生成/图生视频/LTX2-3-文生-图生视频（极大概率去台词，强一致性修订版V4）_2030557129664372738.json、视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json、视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `ComfyMathExpression` —— 8/9 个有
- `LTX2_NAG` —— 8/9 个有
- `LTXVCropGuides` —— 8/9 个有
- `LTXVLatentUpsampler` —— 8/9 个有
- `LatentUpscaleModelLoader` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `easy cleanGpuUsed` —— 8/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `Anything Everywhere` —— 6/9 个有
- `GetNode` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `MathExpression|pysssss` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `llama_cpp_instruct_adv` —— 6/9 个有
- `llama_cpp_model_loader` —— 6/9 个有
- `LTXVImgToVideoInplaceKJ` —— 4/9 个有
- `ResizeImagesByLongerEdge` —— 3/9 个有
- `WujiCleaner` —— 3/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `RH_LLMAPI_Pro_Node` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `ImageScale` —— 1/9 个有
- `LTXVScheduler` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `ResizeImageMaskNode` —— 1/9 个有
- `Text Concatenate` —— 1/9 个有
- `easy ifElse` —— 1/9 个有
- `easy mathString` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 24 - 44 | 9 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 44，9 个样本
