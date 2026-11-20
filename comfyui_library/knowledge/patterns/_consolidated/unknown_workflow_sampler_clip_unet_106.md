---
name: unknown_workflow_sampler_clip_unet_106
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.902727
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json, 视频生成/图生视频/LTX2.3-图生视频-AIGC大赏_2033437706583281665.json, 视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json, 视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json, 视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版）_2029827263906193410.json, 视频生成/图生视频/LTX2.3-图生视频（强一致性，高概率去台词修订版V3）_2029951911398477826.json, 视频生成/图生视频/LTX2.3视频无限生成 人物一致性_2062874922061484033.json, 视频生成/图生视频/LTX2.3视频无限生成 人物一致性_2065072561171550210.json, 视频生成/图生视频/LTX2.3视频无限生成 人物一致性图生视频_2081278519476314114.json, 视频生成/图生视频/短视频无限生成+人物一致性（LTX2.3）_2060674924032905217.json, 视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_106

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json、视频生成/图生视频/LTX2.3-图生视频-AIGC大赏_2033437706583281665.json、视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json、视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json、视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版）_2029827263906193410.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
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
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 10/11 个有
- `llama_cpp_model_loader` —— 10/11 个有
- `VHS_VideoCombine` —— 9/11 个有
- `PrimitiveInt` —— 8/11 个有
- `GetNode` —— 7/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `LTXVCropGuides` —— 6/11 个有
- `LTXVLatentUpsampler` —— 6/11 个有
- `LTXVScheduler` —— 6/11 个有
- `LatentUpscaleModelLoader` —— 6/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `ImageScale` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `ImageScaleBy` —— 4/11 个有
- `ImpactInt` —— 4/11 个有
- `RHHiddenNodes` —— 4/11 个有
- `Anything Everywhere3` —— 3/11 个有
- `CM_IntToFloat` —— 3/11 个有
- `INTConstant` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `SimpleCalculatorKJ` —— 3/11 个有
- `TT_img_enc_v2` —— 2/11 个有
- `AILab_QwenVL` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有
- `easy promptConcat` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 24 | 24 - 24 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，11 个样本，取值集中（一致性 100%）
