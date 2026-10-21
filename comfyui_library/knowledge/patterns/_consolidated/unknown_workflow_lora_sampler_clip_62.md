---
name: unknown_workflow_lora_sampler_clip_62
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.874833
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, GetVideoComponents, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, RepeatImageBatch, ResizeImageMaskNode, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2070832295954702337.json, 视频生成/图生视频/2070881520012849153.json, 视频生成/图生视频/2068532278657118210.json, 视频生成/图生视频/2067979933967802369.json, 视频生成/图生视频/2069345362887929858.json, 视频生成/文生视频/【完全不输 MSR】告别崩坏！LTX-2.3 ingredients角色_道具_场景绝对锁定_2070380617480622081.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2070832295954702337.json、视频生成/图生视频/2070881520012849153.json、视频生成/图生视频/2068532278657118210.json、视频生成/图生视频/2067979933967802369.json、视频生成/图生视频/2069345362887929858.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetVideoComponents`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `PreviewAny` —— 4/6 个有
- `JjkText` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `llama_cpp_parameters` —— 2/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageConcatenateMulti_UTK` —— 1/6 个有
- `LTXVImgToVideoInplace` —— 1/6 个有
- `LTXVLatentUpsampler` —— 1/6 个有
- `LatentUpscaleModelLoader` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `StringReplace` —— 1/6 个有
- `TextGenerate` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `VAEDecodeTiled` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 24 | 24 - 24 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，6 个样本，取值集中（一致性 100%）
