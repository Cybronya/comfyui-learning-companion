---
name: unknown_workflow_upscale_latent_upscale_lora_11
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.874737
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json, 图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json, 平台全量/LTX 图片转视频_2059204262760112129.json, 平台全量/LTX 快速文生视频_2059204248012943361.json, 数字人/数字人/最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306.json, 数字人/数字人/最新LTX2.3首尾帧视频工作流 V3.0_2034864223569842177.json, 视频生成/图生视频/KK图生视频工作流_2079742870340325377.json, 视频生成/图生视频/LTX2.3 --首尾帧双图生视频--全自动提示词--自由控制尾帧位置--超高出片率_2035325472770367490.json, 视频生成/图生视频/LTX2.3 -首尾帧双图生视频-长镜头一镜到底-提示词高遵从-直出1K_2057749829224329218.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版「Supermate」_2047731840944967682.json, 视频生成/图生视频/LTX2.3 全自动提示词--首中尾帧三图生视频_2035325465820405761.json, 视频生成/图生视频/LTX2.3-五图生视频10秒电商展示变装-全自动提示词_2051490555791720450.json, 视频生成/图生视频/LTX2.3-五图生视频15秒电商展示变装-全自动提示词_2051660543777361922.json, 视频生成/图生视频/LTX2.3首尾帧双图生视频-单镜头自动提示词版本_2051217425542201345.json, 视频生成/图生视频/LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json, 视频生成/图生视频/万象AI真人短剧专用图生视频工作流（LTX2.3自动提示词优化版自动横屏竖屏自动时长）_2040620367496089602.json, 视频生成/图生视频/全能图片G 2.0+LTX2.3文生图首尾帧生视频&自动提示词版本_2051654152509501441.json, 视频生成/图生视频/图生视频一镜到底_已修复_2078421854469050370.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json、图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json、平台全量/LTX 图片转视频_2059204262760112129.json、平台全量/LTX 快速文生视频_2059204248012943361.json、数字人/数字人/最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 19 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 18/19 个有
- `LoadImage` —— 17/19 个有
- `easy showAnything` —— 17/19 个有
- `LTXVPreprocess` —— 16/19 个有
- `RH_LLMAPI_Pro_Node` —— 16/19 个有
- `ResizeImagesByLongerEdge` —— 15/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/19 个有
- `LTXVImgToVideoInplaceKJ` —— 12/19 个有
- `FloatConstant` —— 11/19 个有
- `PrimitiveStringMultiline` —— 11/19 个有
- `SimpleMath+` —— 11/19 个有
- `LTXVChunkFeedForward` —— 10/19 个有
- `ModelPatchTorchSettings` —— 10/19 个有
- `PathchSageAttentionKJ` —— 10/19 个有
- `PreviewAny` —— 9/19 个有
- `TextGenerateLTX2Prompt` —— 9/19 个有
- `CR Prompt Text` —— 8/19 个有
- `ResizeImageMaskNode` —— 8/19 个有
- `DualCLIPLoader` —— 7/19 个有
- `PrimitiveBoolean` —— 7/19 个有
- `CR Text` —— 5/19 个有
- `Int` —— 5/19 个有
- `easy int` —— 5/19 个有
- `CR Integer To String` —— 4/19 个有
- `GetAudioDurationFromAudio` —— 4/19 个有
- `LoadAudio` —— 4/19 个有
- `MathExpression|pysssss` —— 4/19 个有
- `RH_LLMAPI_NODE` —— 4/19 个有
- `easy promptReplace` —— 4/19 个有
- `ComfySwitchNode` —— 2/19 个有
- `LoraLoader` —— 2/19 个有
- `PreviewImage` —— 2/19 个有
- `ResizeAndPadImage` —— 2/19 个有
- `CR Text Concatenate` —— 1/19 个有
- `EmptyImage` —— 1/19 个有
- `ImageResize+` —— 1/19 个有
- `RH_RhartImageG2TextToImage` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 19 | 100% |
| 高度 | 25 | 25 - 25 | 19 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，19 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，19 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
