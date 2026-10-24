---
name: unknown_workflow_sampler_clip_unet_33
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.83095
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json, 视频生成/图生视频/LTX2.3-图生视频 人物一致性大概率字幕去除增强版x3长视频生成短剧漫剧视频无限生成_2030260940695932930.json, 视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json, 视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2059604648729858049.json, 视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json, 视频生成/图生视频/LTX2.3-图生视频 高清极速优化增强版 长视频_2031233763203620866.json, 视频生成/图生视频/LTX2.3-图生视频-AIGC大赏_2033437706583281665.json, 视频生成/图生视频/LTX2.3-图生视频-去台词文字去字幕中文提示词声音配音视频图生视频_2029912263112531970.json, 视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版V2）_2029873778003550210.json, 视频生成/图生视频/LTX2.3-图生视频（大概率去台词文字修订版）_2029827263906193410.json, 视频生成/图生视频/LTX2.3-图生视频（强一致性，高概率去台词修订版V3）_2029951911398477826.json, 视频生成/图生视频/LTX2.3视频无限生成 人物一致性_2062874922061484033.json, 视频生成/图生视频/LTX2.3视频无限生成 人物一致性_2065072561171550210.json, 视频生成/图生视频/LTX2.3视频无限生成 人物一致性图生视频_2081278519476314114.json, 视频生成/图生视频/短视频无限生成+人物一致性（LTX2.3）_2060674924032905217.json, 视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json, 视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json, 视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json, 视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json, 视频生成/文生视频/声色俱全！LTX2.3-图生视频-匹配原图比例-高质量音视频！自定义Lora_2031651024238288898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-VBVR逻辑优化-图生视频-AIGC大赏_2042489551154847745.json、视频生成/图生视频/LTX2.3-图生视频 人物一致性大概率字幕去除增强版x3长视频生成短剧漫剧视频无限生成_2030260940695932930.json、视频生成/图生视频/LTX2.3-图生视频 人物一致性字幕去除增强版x3长视频生成短剧视频无限生成_2030069604189474818.json、视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2059604648729858049.json、视频生成/图生视频/LTX2.3-图生视频 字幕去除增强版 人物一致性长视频生成短剧视频无限生成_2080253203614097410.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 19/20 个有
- `llama_cpp_model_loader` —— 19/20 个有
- `VHS_VideoCombine` —— 18/20 个有
- `PrimitiveInt` —— 17/20 个有
- `GetImageSize` —— 16/20 个有
- `ResizeImagesByLongerEdge` —— 16/20 个有
- `easy cleanGpuUsed` —— 14/20 个有
- `GetNode` —— 11/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/20 个有
- `SetNode` —— 11/20 个有
- `ImageScale` —— 10/20 个有
- `LTXVCropGuides` —— 10/20 个有
- `LTXVLatentUpsampler` —— 10/20 个有
- `LatentUpscaleModelLoader` —— 10/20 个有
- `LTXVScheduler` —— 6/20 个有
- `LoraLoaderModelOnly` —— 6/20 个有
- `Anything Everywhere` —— 4/20 个有
- `ComfyMathExpression` —— 4/20 个有
- `ImageScaleBy` —— 4/20 个有
- `ImpactInt` —— 4/20 个有
- `LTX2_NAG` —— 4/20 个有
- `MathExpression|pysssss` —— 4/20 个有
- `PrimitiveBoolean` —— 4/20 个有
- `RHHiddenNodes` —— 4/20 个有
- `Anything Everywhere3` —— 3/20 个有
- `CM_IntToFloat` —— 3/20 个有
- `INTConstant` —— 3/20 个有
- `SaveImage` —— 3/20 个有
- `SimpleCalculatorKJ` —— 3/20 个有
- `WujiCleaner` —— 3/20 个有
- `LTXVImgToVideoInplaceKJ` —— 2/20 个有
- `TT_img_enc_v2` —— 2/20 个有
- `easy imageConcat` —— 2/20 个有
- `AILab_QwenVL` —— 1/20 个有
- `TT_img_enc` —— 1/20 个有
- `easy promptConcat` —— 1/20 个有
- `孤海注释` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 20 | 100% |
| 高度 | 24 | 24 - 25 | 20 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，20 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 25，20 个样本，取值集中（一致性 98%）
