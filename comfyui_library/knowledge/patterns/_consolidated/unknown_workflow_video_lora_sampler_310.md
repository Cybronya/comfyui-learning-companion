---
name: unknown_workflow_video_lora_sampler_310
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.950111
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, ManualSigmas, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841.json, 平台全量/LTX-2.3视频扩展画幅 (1)_2046181956752252930.json, 平台全量/LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681.json, 平台全量/LTX2.3--视频扩图_2042961910815002625.json, 平台全量/LTX2.3-视频扩图_2042933284837007361.json, 平台全量/LTX2.3视频编辑_2078656946558824450.json, 视频生成/文生视频/01_v2v_Video_Edit_视频编辑_RH_APP_2053497184217247746.json, 视频生成/文生视频/LTX2.3 电影级全向外扩视频工作流_2053375516647931906.json, 视频生成/文生视频/视频扩展3.0｜OmniNFT+Relay+蒸馏1.1｜竖屏扩宽_2058327114209910786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_310

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/LTX-2.3-outpaint-视频外扩-效果惊艳-一手动扩展尺寸_2050489384440483841.json、平台全量/LTX-2.3视频扩展画幅 (1)_2046181956752252930.json、平台全量/LTX2.3 3.5系列套件｜视频画幅智能扩展_2067822318637895681.json、平台全量/LTX2.3--视频扩图_2042961910815002625.json、平台全量/LTX2.3-视频扩图_2042933284837007361.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 8/9 个有
- `Color Correct (mtb)` —— 8/9 个有
- `Int` —— 8/9 个有
- `LTXAVTextEncoderLoader` —— 8/9 个有
- `LTXVAudioVAELoader` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `Switch image [Crystools]` —— 8/9 个有
- `ImageConcanate` —— 7/9 个有
- `ImagePadKJ` —— 6/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `LTXVAudioVAEDecode` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `ResizeImageMaskNode` —— 5/9 个有
- `EmptyImage` —— 4/9 个有
- `GemmaAPITextEncode` —— 4/9 个有
- `GetImageSize+` —— 4/9 个有
- `LTX2SamplingPreviewOverride` —— 4/9 个有
- `PrimitiveString` —— 4/9 个有
- `ResizeAndPadImage` —— 3/9 个有
- `PreviewImage` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `image_scale_pixel_v2` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `ComfyMathExpression` —— 1/9 个有
- `CustomAddLabel` —— 1/9 个有
- `DualCLIPLoader` —— 1/9 个有
- `Float` —— 1/9 个有
- `Float32ColorCorrect` —— 1/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `ShowAnything|Mie` —— 1/9 个有
- `Text` —— 1/9 个有
- `UNETLoader` —— 1/9 个有
- `VAEDecode` —— 1/9 个有
- `VAELoaderKJ` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
