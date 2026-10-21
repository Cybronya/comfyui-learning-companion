---
name: unknown_workflow_sampler_clip_unet_17
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.915625
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2042489551154847745.json, 视频生成/图生视频/2030260940695932930.json, 视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json, 视频生成/图生视频/2059604648729858049.json, 视频生成/图生视频/2080253203614097410.json, 视频生成/图生视频/2031233763203620866.json, 视频生成/图生视频/2033437706583281665.json, 视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json, 视频生成/图生视频/2029873778003550210.json, 视频生成/图生视频/2029827263906193410.json, 视频生成/图生视频/2029951911398477826.json, 视频生成/图生视频/2062874922061484033.json, 视频生成/图生视频/2065072561171550210.json, 视频生成/图生视频/2081278519476314114.json, 视频生成/图生视频/2060674924032905217.json, 视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2042489551154847745.json、视频生成/图生视频/2030260940695932930.json、视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json、视频生成/图生视频/2059604648729858049.json、视频生成/图生视频/2080253203614097410.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
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
- `llama_cpp_instruct_adv` —— 15/16 个有
- `llama_cpp_model_loader` —— 15/16 个有
- `VHS_VideoCombine` —— 14/16 个有
- `PrimitiveInt` —— 13/16 个有
- `ImageScale` —— 10/16 个有
- `easy cleanGpuUsed` —— 10/16 个有
- `GetNode` —— 7/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/16 个有
- `SetNode` —— 7/16 个有
- `LTXVCropGuides` —— 6/16 个有
- `LTXVLatentUpsampler` —— 6/16 个有
- `LTXVScheduler` —— 6/16 个有
- `LatentUpscaleModelLoader` —— 6/16 个有
- `LoraLoaderModelOnly` —— 6/16 个有
- `ImageScaleBy` —— 4/16 个有
- `ImpactInt` —— 4/16 个有
- `RHHiddenNodes` —— 4/16 个有
- `Anything Everywhere3` —— 3/16 个有
- `CM_IntToFloat` —— 3/16 个有
- `INTConstant` —— 3/16 个有
- `SaveImage` —— 3/16 个有
- `SimpleCalculatorKJ` —— 3/16 个有
- `TT_img_enc_v2` —— 2/16 个有
- `AILab_QwenVL` —— 1/16 个有
- `TT_img_enc` —— 1/16 个有
- `easy promptConcat` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 24 | 24 - 24 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，16 个样本，取值集中（一致性 100%）
