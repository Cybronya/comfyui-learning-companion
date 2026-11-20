---
name: unknown_workflow_video_sampler_clip_51
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.918091
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json, 视频生成/图生视频/Dasiwa V2 ltx2.3 I2V_2058155153185918978.json, 视频生成/图生视频/LTX2-3-文生-图生视频（极大概率去台词，强一致性修订版V4）_2030557129664372738.json, 视频生成/图生视频/LTX2.3 完美人物一致性_2064713194668650497.json, 视频生成/图生视频/LTX2.3 自用优化版 I2V_2063969422162882561.json, 视频生成/图生视频/LTX2.3-图生视频 人物一致性大概率字幕去除增强版x3长视频生成短剧漫剧视频无限生成_2030260940695932930.json, 视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json, 视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2059604648729858049.json, 视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json, 视频生成/图生视频/LTX2.3-图生视频 高清极速优化增强版 长视频_2031233763203620866.json, 视频生成/图生视频/LTX2_3-图生视频 (V5版，切镜人物保持相对一致)_2037403697717714946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/LTX2.3-图生视频工业版_2030090763832401922.json、视频生成/图生视频/Dasiwa V2 ltx2.3 I2V_2058155153185918978.json、视频生成/图生视频/LTX2-3-文生-图生视频（极大概率去台词，强一致性修订版V4）_2030557129664372738.json、视频生成/图生视频/LTX2.3 完美人物一致性_2064713194668650497.json、视频生成/图生视频/LTX2.3 自用优化版 I2V_2063969422162882561.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/11 个有
- `ShowText|pysssss` —— 7/11 个有
- `easy cleanGpuUsed` —— 7/11 个有
- `llama_cpp_instruct_adv` —— 7/11 个有
- `llama_cpp_model_loader` —— 7/11 个有
- `GetImageSize` —— 6/11 个有
- `ImageScale` —— 6/11 个有
- `ComfyMathExpression` —— 5/11 个有
- `LTXVCropGuides` —— 5/11 个有
- `LTXVLatentUpsampler` —— 5/11 个有
- `LatentUpscaleModelLoader` —— 5/11 个有
- `PrimitiveStringMultiline` —— 5/11 个有
- `LTX2_NAG` —— 4/11 个有
- `LayerUtility: PurgeVRAM` —— 3/11 个有
- `INTConstant` —— 2/11 个有
- `LTXTiledSampler` —— 2/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `PromptRelayEncode` —— 2/11 个有
- `ResizeImageMaskNode` —— 2/11 个有
- `easy ifElse` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `LTXAddVideoICLoRAGuideAdvanced` —— 1/11 个有
- `LTXICLoRALoaderModelOnly` —— 1/11 个有
- `LTXVScheduler` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `Text Concatenate` —— 1/11 个有
- `easy mathString` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 24 | 24 - 44 | 11 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 44，11 个样本
