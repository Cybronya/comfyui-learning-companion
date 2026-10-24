---
name: unknown_workflow_video_upscale_latent_upscale_72
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5088
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json, 视频生成/图生视频/LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json, 视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json, 视频生成/图生视频/LTX2.3+首尾帧gguf_2037924833685671937.json, 视频生成/图生视频/人物动作迁移｜参考视频 +人物图像 ｜CN参考Canny + 深度 + 姿态｜LTX2.3_2045081725197357057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_72

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 三图首中尾帧参考_2035556614480076801.json、视频生成/图生视频/LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json、视频生成/图生视频/LTX2.3 双图首尾帧参考_2035556594234167298.json、视频生成/图生视频/LTX2.3+首尾帧gguf_2037924833685671937.json、视频生成/图生视频/人物动作迁移｜参考视频 +人物图像 ｜CN参考Canny + 深度 + 姿态｜LTX2.3_2045081725197357057.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 4/5 个有
- `ComfyMathExpression` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LTXVImgToVideoInplaceKJ` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `CannyEdgePreprocessor` —— 2/5 个有
- `DWPreprocessor` —— 2/5 个有
- `DepthAnythingPreprocessor` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `LTXAddVideoICLoRAGuide` —— 2/5 个有
- `LTXICLoRALoaderModelOnly` —— 2/5 个有
- `LTXVImgToVideoConditionOnly` —— 2/5 个有
- `RH_LLMAPI_Pro_Node` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ImageLoader` —— 1/5 个有
- `JoinStrings` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `MultiplePathsInputPlus` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `SeedGenerator` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `VRAMReserver` —— 1/5 个有
- `VideoLoaderPlus` —— 1/5 个有
- `ttN concat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
