---
name: unknown_workflow_video_lora_sampler_311
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.948333
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, Color Correct (mtb), EmptyLTXVLatentVideo, GetImageSize, ImagePadKJ, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, Switch image [Crystools], VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/Ltx 2.3 视频外扩画面_2048613599265955841.json, 平台全量/ltx2.3视频-前端版-视频扩展画面_2051828139629785090.json, 平台全量/ltx23视频外绘_2042562672696233986.json, 平台全量/电商15秒视频扩图 保持人物一致性 Ltx2.3_2042877538057330690.json, 平台全量/视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482.json, 平台全量/超好用的视频扩图  视频编辑 LTX 2.3_2042820578607894529.json, 平台全量/长视频扩图｜上下左右｜超无感融合（如：给视频 上下左右加宽）LTX 2.3_2044805974556413954.json, 数字人/数字人/无痕视频扩图 视频编辑 LTX2.3_2042587548962263042.json, 数字人/数字人/视频扩图  视频编辑 LTX 2.3_2042574837587120129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_311

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Ltx 2.3 视频外扩画面_2048613599265955841.json、平台全量/ltx2.3视频-前端版-视频扩展画面_2051828139629785090.json、平台全量/ltx23视频外绘_2042562672696233986.json、平台全量/电商15秒视频扩图 保持人物一致性 Ltx2.3_2042877538057330690.json、平台全量/视频外扩-LTX-2.3-22b-IC-LoRA-Outpaint_2043273379469332482.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `Color Correct (mtb)`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImagePadKJ`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Switch image [Crystools]`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 8/9 个有
- `LTX2SamplingPreviewOverride` —— 8/9 个有
- `ResizeImageMaskNode` —— 8/9 个有
- `LTXICLoRALoaderModelOnly` —— 7/9 个有
- `ImageConcanate` —— 5/9 个有
- `Text` —— 3/9 个有
- `ImageScaleBy` —— 2/9 个有
- `Int` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `ImageScaleToTotalPixelsX` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `LTXVAudioVAEDecode` —— 1/9 个有
- `LTXVChunkFeedForward` —— 1/9 个有
- `ModelPatchTorchSettings` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SelectImages` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `ycImageCropBatchApply` —— 1/9 个有
- `ycImageCropInteractive` —— 1/9 个有

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
