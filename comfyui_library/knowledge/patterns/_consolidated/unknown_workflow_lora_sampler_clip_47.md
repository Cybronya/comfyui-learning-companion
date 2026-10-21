---
name: unknown_workflow_lora_sampler_clip_47
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.927857
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2039634307186171905.json, 视频生成/文生视频/LTX 2.3 ComfyUI：三阶段 4K 工作流程（修复视频失真）_2038095391647862786.json, 视频生成/文生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2033775150256103426.json, 视频生成/文生视频/LTX2.3 图生_ 文生视频【提示词自动优化】_2033527714837176322.json, 视频生成/文生视频/LTX2.3-图生+文生视频_2034105239082635265.json, 视频生成/文生视频/Ltxv 2.3图生视频更强一致性和动态_2030110680979869697.json, 视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2039634307186171905.json、视频生成/文生视频/LTX 2.3 ComfyUI：三阶段 4K 工作流程（修复视频失真）_2038095391647862786.json、视频生成/文生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2033775150256103426.json、视频生成/文生视频/LTX2.3 图生_ 文生视频【提示词自动优化】_2033527714837176322.json、视频生成/文生视频/LTX2.3-图生+文生视频_2034105239082635265.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleModelLoader` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `CreateVideo` —— 5/7 个有
- `LTXVChunkFeedForward` —— 5/7 个有
- `LTXVLatentUpsampler` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `ModelPatchTorchSettings` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `INTConstant` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `RH_LLMAPI_Pro_Node` —— 3/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `FlashVSR_SM_KSampler` —— 2/7 个有
- `FlashVSR_SM_Model` —— 2/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `Float` —— 1/7 个有
- `GuiderParameters` —— 1/7 个有
- `Image_Resize_longsize` —— 1/7 个有
- `ImpactConditionalBranch` —— 1/7 个有
- `MultimodalGuider` —— 1/7 个有
- `MuyeSizeSelector` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Switch any [Crystools]` —— 1/7 个有
- `image_scale_pixel_v2` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有
- `数学运算_孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |
| 采样步数 | 8.62528e+08 | - | 2 | 83% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8.62528e+08，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.00618e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
