---
name: unknown_workflow_video_lora_sampler_141
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.946917
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, Float, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, SamplerCustom, SimpleMath+, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2069424373089529858.json, 视频生成/图生视频/2068240964862435329.json, 视频生成/图生视频/2069760326291247105.json, 视频生成/图生视频/2069220320195731457.json, 视频生成/图生视频/2067263836763279362.json, 视频生成/图生视频/2070142023239290882.json, 视频生成/图生视频/2070424027285512193.json, 视频生成/图生视频/LTX2.3-MSR多图像参考数字人(自定义音频)_2086423602479591426.json, 视频生成/图生视频/2072216632251998209.json, 视频生成/图生视频/2055525493520257026.json, 视频生成/图生视频/2070338966414512130.json, 视频生成/文生视频/LTX2.3-MSR 多图参考生成视频_2069948331698249729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_141

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2069424373089529858.json、视频生成/图生视频/2068240964862435329.json、视频生成/图生视频/2069760326291247105.json、视频生成/图生视频/2069220320195731457.json、视频生成/图生视频/2067263836763279362.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Float`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `SamplerCustom`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 5/12 个有
- `LTXVAudioVAEEncode` —— 5/12 个有
- `LoadAudio` —— 5/12 个有
- `LoadAudioUI` —— 5/12 个有
- `PrimitiveBoolean` —— 5/12 个有
- `SetLatentNoiseMask` —— 5/12 个有
- `SolidMask` —— 5/12 个有
- `MathExpression|pysssss` —— 3/12 个有
- `PrimitiveInt` —— 3/12 个有
- `Label (rgthree)` —— 1/12 个有
- `Textbox` —— 1/12 个有
- `llama_cpp_instruct_adv` —— 1/12 个有
- `llama_cpp_model_loader` —— 1/12 个有
- `llama_cpp_parameters` —— 1/12 个有
- `忽略多组孤海` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 12 | 100% |
| 高度 | 50 | 24 - 50 | 12 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，12 个样本，取值集中（一致性 100%）
- 高度 中位数 50，观测区间 24 - 50，12 个样本，取值集中（一致性 85%）
