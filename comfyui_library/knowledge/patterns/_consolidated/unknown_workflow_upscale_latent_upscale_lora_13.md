---
name: unknown_workflow_upscale_latent_upscale_lora_13
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.848143
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 首尾帧_2031685383376867330.json, 视频生成/图生视频/LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json, 视频生成/图生视频/LTX 2.3图生视频_文生视频工作流_2030540846281527298.json, 视频生成/图生视频/LTX 2.3图生视频高清增强版_2075950096994361345.json, 视频生成/图生视频/LTX2.3 多图参考_2031341831253925890.json, 视频生成/图生视频/LTX2.3 多图参考_2032121353918226434.json, 视频生成/图生视频/LTX2.3-首尾多帧视频生成_2031368415541202945.json, 视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032374429937836033.json, 视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032414154048413698.json, 视频生成/图生视频/LTX2.3_首尾帧 视频工作流_2033429258751709185.json, 视频生成/图生视频/LTX2.3真人短剧_2033403811573800961.json, 视频生成/图生视频/ltx2.3图生视频_2037154084020559874.json, 视频生成/图生视频/ltx2.3首尾帧过度_2037180362916368386.json, 视频生成/图生视频/音画同步图生视频高清版_2081658308183814145.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 首尾帧_2031685383376867330.json、视频生成/图生视频/LTX 2.3 首尾帧生成视频-调用版_2031928343846723586.json、视频生成/图生视频/LTX 2.3图生视频_文生视频工作流_2030540846281527298.json、视频生成/图生视频/LTX 2.3图生视频高清增强版_2075950096994361345.json、视频生成/图生视频/LTX2.3 多图参考_2031341831253925890.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 13/14 个有
- `PrimitiveInt` —— 11/14 个有
- `Int` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/14 个有
- `ResizeImagesByLongerEdge` —— 9/14 个有
- `LTXVImgToVideoInplaceKJ` —— 8/14 个有
- `SimpleMath+` —— 7/14 个有
- `PrimitiveBoolean` —— 6/14 个有
- `ResizeImageMaskNode` —— 6/14 个有
- `easy showAnything` —— 6/14 个有
- `ImageResizeKJv2` —— 5/14 个有
- `LayerUtility: PurgeVRAM V2` —— 5/14 个有
- `RH_LLMAPI_Pro_Node` —— 5/14 个有
- `LTX2_NAG` —— 4/14 个有
- `Float` —— 3/14 个有
- `LTXVFirstLastFrameControl_TTP` —— 3/14 个有
- `MathExpression|pysssss` —— 3/14 个有
- `ShowText|pysssss` —— 3/14 个有
- `LTXTiledSampler` —— 2/14 个有
- `LTXVLatentUpsamplerTiled` —— 2/14 个有
- `LTXVMiddleFrame_TTP` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `TextConcat` —— 2/14 个有
- `ToString` —— 2/14 个有
- `easy mathInt` —— 2/14 个有
- `llama_cpp_instruct_adv` —— 2/14 个有
- `llama_cpp_model_loader` —— 2/14 个有
- `llama_cpp_parameters` —— 2/14 个有
- `PreviewImage` —— 1/14 个有
- `Text` —— 1/14 个有
- `easy imageConcat` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
