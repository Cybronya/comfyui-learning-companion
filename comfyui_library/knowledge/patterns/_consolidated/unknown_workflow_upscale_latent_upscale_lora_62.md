---
name: unknown_workflow_upscale_latent_upscale_lora_62
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9715
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, CreateVideo, EmptyImage, FluxResolutionNode, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXDirector, LTXDirectorGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, VAEDecodeTiled, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353.json, 视频生成/文生视频/LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001.json, 视频生成/文生视频/LTX2.3 分镜导演视频｜角色、动作、场景一体化控制_2061524156398788609.json, 视频生成/文生视频/导演综合流3.0｜OmniNFT+Relay+蒸馏1.1｜短片双人首尾帧_2057744531994537985.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_62

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 3.5套件｜分镜别乱·六宫格故事板导演台_2068718977450340353.json、视频生成/文生视频/LTX2.3 3.5套件｜角色别散·分镜导演角色动作场景控制_2068718478793728001.json、视频生成/文生视频/LTX2.3 分镜导演视频｜角色、动作、场景一体化控制_2061524156398788609.json、视频生成/文生视频/导演综合流3.0｜OmniNFT+Relay+蒸馏1.1｜短片双人首尾帧_2057744531994537985.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `FluxResolutionNode`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAEDecodeTiled`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `STGGuiderAdvanced` —— 3/4 个有
- `Sigmas Easing` —— 3/4 个有
- `ImageFromBatch` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `CS-LTXGridDirector` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `Image To Mask` —— 1/4 个有
- `LTX2SamplingPreviewOverride` —— 1/4 个有
- `LTXAddVideoICLoRAGuide` —— 1/4 个有
- `LTXVImgToVideoConditionOnly` —— 1/4 个有
- `LTXVPreprocess` —— 1/4 个有
- `LayerUtility: ColorImage` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `RepeatImageBatch` —— 1/4 个有
- `VAEEncodeForInpaint` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `easy imageCount` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
